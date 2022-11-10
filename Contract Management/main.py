import datetime
import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk
import AddingForm
import EditRow
import GroupBy
import Table

class MainForm:
    def __init__(self, master):
        self.master = master

        self.my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mghfghmghfgh4573434",
            database="contract",
        )
        self.my_cursor = self.my_connect.cursor()

        self.search_frame = tk.Frame(self.master)
        self.frame = tk.Frame(self.master)
        self.menu_frame = tk.LabelFrame(self.master)
        self.status_groupby = 0

        self.table = Table.Table(self.frame,self.my_connect,self.my_cursor)

        self.search_label = tk.Label(self.search_frame, text="Поиск по", )

        self.search_combobox = ttk.Combobox(self.search_frame, values=columns)
        self.search_combobox.current(0)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_button = tk.Button(self.search_frame, width=4, height=1, text="Поиск", command=self.search)
        self.default_button = tk.Button(self.search_frame, width=4, height=1, text="Сброс", command=self.reset)

        self.hierarchical_button = tk.Button(self.search_frame, width=4, height=1, text="Ок",
                                             command=self.groupBy_window)
        self.hierarchical_combobox = ttk.Combobox(self.search_frame, values=columns)
        self.hierarchical_combobox.current(0)
        self.hierarchical_label = tk.Label(self.search_frame, text="Группировка по", )

        self.Addbutton = tk.Button(self.menu_frame, text='Добавить', width=25, command=self.add_window)
        self.Editbutton = tk.Button(self.menu_frame, text='Изменить', width=25, command=self.edit_window)
        self.DeleteButton = tk.Button(self.menu_frame, text='Удалить', width=25, command=self.delete)

        self.search_frame.pack(fill="both")
        self.frame.pack(fill="both", expand=True)
        self.menu_frame.pack()

        self.default_button.pack(side="right", padx=5, pady=3)
        self.search_button.pack(side="right", padx=5, pady=3)
        self.search_entry.pack(side="right", padx=7, pady=3)
        self.search_combobox.pack(side="right", padx=7, pady=3)
        self.search_label.pack(side="right", padx=7, pady=3)
        self.hierarchical_button.pack(side="right", padx=7, pady=3)
        self.hierarchical_combobox.pack(side="right", padx=7, pady=3)
        self.hierarchical_label.pack(side="right", padx=7, pady=3)

        self.Addbutton.pack(side="left")
        self.Editbutton.pack(side="left")
        self.DeleteButton.pack(side="left")

    def search(self):
        ''' Search row in database by item '''

        list_names_columns_info = ["info.id", "date", "number", "subject", "costing", "end_date", "name", "payment",
                                   "contr_time", "approval", "status", "note"]
        column_table = list_names_columns_info[self.search_combobox.current()]

        request = (
            f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)"
            f"WHERE {column_table} LIKE \"%{self.search_entry.get()}%\"")

        if self.status_groupby:
            self.table.table.destroy()
            self.table = GroupBy.GroupBy(self.frame, self.hierarchical_combobox)
            self.groupBy(request)
            self.table.table.heading('#0', text=columns[self.hierarchical_combobox.current()], anchor=tk.W)
        else:
            for record in self.table.table.get_children():
                self.table.table.delete(record)
            self.my_cursor.execute(request)
        self.indicator_for_mainform()

    def indicator_for_mainform(self):
        ''' Create yellow indicator in Table'''
        for row in self.my_cursor:
            date, days, option = row[1], row[8].split()[0], row[8].split()[1][0]
            date = datetime.datetime.strptime("-".join(str(date).split(".")[::-1]), '%Y-%m-%d').date()
            if (datetime.date.today() + datetime.timedelta(days=7) >= Table.Table.indentification_type_of_days(self.table,
                                                                                                         date, days,
                                                                                                         option)) and (
                    row[10] != "исполнено"):
                self.table.table.insert("", 'end', values=row, tags=("yellow",))
            else:
                self.table.table.insert("", 'end', values=row)
        self.table.table.pack(expand=True, fill=tk.BOTH)
        self.table.table.tag_configure("yellow", background="yellow")

    def reset(self):
        ''' Reset all rows in Table.table '''
        self.reset_for_groupBy()
        for record in self.table.table.get_children():
            self.table.table.delete(record)
        self.my_cursor.execute(
            f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        self.indicator_for_mainform()
        self.search_combobox.current(0)
        self.search_entry.delete(0, "end")
        self.status_groupby = 0
        Table.Table.default_selected_row(self.table)

    def add_window(self):
        ''' Add new row in Table.table '''
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddingForm.AddingForm(self.newWindow, self.table,self.my_connect,self.my_cursor)
        Table.Table.default_selected_row(self.table)

    def edit_window(self):
        ''' Edit row in Table.table '''
        self.newWindow = tk.Toplevel(self.master)
        self.app = EditRow.Edit_row(self.newWindow, self.table,self.my_connect,self.my_cursor)
        Table.Table.default_selected_row(self.table)

    def groupBy_window(self):
        self.table.table.destroy()
        self.table = GroupBy.GroupBy(self.frame, self.hierarchical_combobox)
        request = (
            f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        self.groupBy(request)
        self.table.table.heading('#0', text=columns[self.hierarchical_combobox.current()], anchor=tk.W)

    def groupBy(self, request):
        ''' Groups all records in tables according to a selected parameter  '''
        i, n, index = 0, 0, 0
        self.status_groupby = 1
        self.my_cursor.execute(request)
        list_repeats, dict_repeats = [], {}

        for row in self.my_cursor:
            for column in columns:
                if column == columns[self.hierarchical_combobox.current()]:
                    list_repeats.append(row[columns.index(column)])

        for first_columns in set(list_repeats):
            dict_repeats[first_columns] = 0
            self.table.table.insert("", tk.END, text=first_columns, iid=str(i), open=False)
            i += 1

        self.my_cursor.execute(request)

        for row in self.my_cursor:

            for column in columns:
                if column == columns[self.hierarchical_combobox.current()]:
                    date, days, option = row[1], row[8].split()[0], row[8].split()[1][0]
                    # if (datetime.date.today() + datetime.timedelta(days=7) >= Table.indentification_type_of_days(self.table, date,days,option)) and (row[10] != "исполнено"):
                    self.table.table.insert("", tk.END, text=row[columns.index(column)], tags=("yellow",), iid=str(i),
                                            open=False)
                    # else: self.table.table.insert("", tk.END, text=row[columns.index(column)], iid=str(i), open=False)
                    self.table.table.move(str(i), str(list(set(list_repeats)).index(row[columns.index(column)])),
                                          dict_repeats[row[columns.index(column)]])
                    dict_repeats[row[columns.index(column)]] += 1
                    i += 1

        self.my_cursor.execute(request)
        n = len(set(list_repeats))
        for row in self.my_cursor:
            for column in columns:
                if column != columns[self.hierarchical_combobox.current()]:
                    self.table.table.insert("", tk.END, text=column + ": " + str(row[columns.index(column)]),
                                            iid=str(i), open=False)
                    self.table.table.move(str(i), str(n), index)
                    i += 1
                    index += 1
            n += 1
            index = 0
        self.table.table.pack(fill="both", expand=True)

    def reset_for_groupBy(self):
        """Reset all records in tables for group"""
        self.table.table.destroy()
        self.table = Table.Table(self.frame,self.my_connect,self.my_cursor)

    def delete(self):
        selected_id = list(self.table.table.item(self.table.table.selection()[0]).values())[2][0]
        if selected_id:
            x = selected_id
            sql = '''DELETE FROM contract.info WHERE info.id = %s;'''
            self.my_cursor.execute(sql, (x,))
            self.my_connect.commit()

            for record in self.table.table.get_children():
                self.table.table.delete(record)
            self.my_cursor.execute(
                f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
                f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
                f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note "
                f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
            self.indicator_for_mainform()

def main():
    root.title('Contract app')
    root.geometry('1440x960')

    app = MainForm(root)
    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas()

    columns = ["Id", "Дата", "№", "Предмет", "Стоимость", "Дата окончания действия договора", "Ответственное лицо",
               "Порядок оплаты", "Срок исполнения", "Дата согласования", "Статус исполнения", "Примечание"]
    counter_id = 0

    main()