import datetime
import tkinter as tk
import tkinter.ttk as ttk

columns = ["Id", "Дата", "№", "Предмет", "Стоимость", "Дата окончания действия договора", "Ответственное лицо",
           "Порядок оплаты", "Срок исполнения", "Дата согласования", "Статус исполнения", "Примечание"]

class Table:
    def __init__(self, master, my_connect,my_cursor):
        self.master = master
        self.table = ttk.Treeview(self.master, columns=columns)

        self.my_connect = my_connect
        self.my_cursor = my_cursor
        self.create_table_columns()
        self.insert_data_from_dbf()
        self.create_y_scrollbar()
        self.create_x_scrollbar()
        self.create_indicator_by_date()
        self.default_selected_row()

    def default_selected_row(self):
        # done
        self.table.focus_set()
        children = self.table.get_children()
        if children:
            self.table.focus(children[0])
            self.table.selection_set(children[0])

    def insert_data_from_dbf(self):
        # done
        self.my_cursor.execute(
            f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        for row in self.my_cursor:
            self.table.insert("", "end", values=row)
        self.table.pack(fill="both", expand=True)

    def create_table_columns(self):
        # done
        self.table["column"] = columns
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column, command=lambda c=column: self.sortby_column(self.table, c, 0))

    def create_y_scrollbar(self):
        # done
        self.y_scrollbar = ttk.Scrollbar(self.table, orient="vertical", command=self.table.yview)
        self.y_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.y_scrollbar.set)

    def create_x_scrollbar(self):
        # done
        self.x_scrollbar = ttk.Scrollbar(self.table, orient="horizontal", command=self.table.xview)
        self.x_scrollbar.pack(side="bottom", fill="x")
        self.table.configure(xscrollcommand=self.x_scrollbar.set)

    def sortby_column(self, table, col, descending):
        """sort tree contents when a column header is clicked on"""
        data = [(self.table.set(child, col), child) for child in self.table.get_children('')]
        if self.isfloat(data[0][0]):
            data = self.change_numeric_sortby(data)
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            self.table.move(item[1], '', ix)
        self.table.heading(col, command=lambda col=col: self.sortby_column(self.table, col, int(not descending)))

    def change_numeric_sortby(self, data):
        # done
        new_data = list()
        for string_number in range(len(data)):
            new_data.append((float(data[string_number][0]), data[string_number][1]))
        return new_data

    def isfloat(self, num):
        # done
        try:
            float(num)
            return True
        except ValueError:
            return False

    def create_indicator_by_date(self):
        for record in self.table.get_children():
            self.table.delete(record)
        self.my_cursor.execute(
            f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        for row in self.my_cursor:
            date, days, option = row[1], row[8].split()[0], row[8].split()[1][0]
            date = datetime.datetime.strptime("-".join(str(date).split(".")[::-1]), '%Y-%m-%d').date()
            if (datetime.date.today() + datetime.timedelta(days=7) >= self.indentification_type_of_days(date, days,
                                                                                                        option)) and (
                    row[10] != "исполнено"):
                self.table.insert("", 'end', values=row, tags=("yellow",))
            else:
                self.table.insert("", 'end', values=row)
        self.table.pack(expand=True, fill=tk.BOTH)
        self.table.tag_configure("yellow", background="yellow")

    def indentification_type_of_days(self, date, days, option):
        if option in ["б", "р"]:
            return self.date_by_adding_business_days(date, int(days))
        else:
            return self.date_by_adding_business_days(date, int(days))

    def date_by_adding_business_days(self, from_date, add_days):
        business_days_to_add = add_days
        current_date = from_date
        while business_days_to_add > 0:
            current_date += datetime.timedelta(days=1)
            weekday = current_date.weekday()
            if weekday >= 5:  # sunday = 6
                continue
            business_days_to_add -= 1
        return current_date

    def date_by_adding_calendar_days(self, from_date, add_days):
        business_days_to_add = add_days
        current_date = from_date
        while business_days_to_add > 0:
            current_date += datetime.timedelta(days=1)
            business_days_to_add -= 1
        return current_date