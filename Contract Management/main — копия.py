import datetime
import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import re

class MainForm:
    def __init__(self, master):
        self.master = master

        self.search_frame = tk.Frame(self.master)
        self.frame = tk.Frame(self.master)
        self.menu_frame = tk.LabelFrame(self.master)
        self.status_groupby = 0

        self.table = Table(self.frame)

        self.search_label = tk.Label(self.search_frame, text="Поиск по", )

        self.search_combobox = ttk.Combobox(self.search_frame, values=columns)
        self.search_combobox.current(0)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_button = tk.Button(self.search_frame, width=4, height=1, text="Поиск", command=self.search)
        self.default_button = tk.Button(self.search_frame, width=4, height=1, text="Сброс", command=self.reset)

        self.hierarchical_button = tk.Button(self.search_frame, width=4, height=1, text="Ок",
                                             command=self.groupBy_window)
        self.hierarchical_combobox = ttk.Combobox(self.search_frame, values=columns)
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
        list_names_columns_info = ["info.id", "date", "number", "subject", "costing", "end_date", "name", "payment",
                                   "contr_time", "approval", "status", "note", "additional"]
        column_table = list_names_columns_info[self.search_combobox.current()]

        request = (
            f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note,info.additional "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)"
            f"WHERE {column_table} LIKE \"%{self.search_entry.get()}%\"")

        if self.status_groupby:
            self.table.table.destroy()
            self.table = GroupBy(self.frame, self.hierarchical_combobox)
            self.groupBy(request)
            self.table.table.heading('#0', text=columns[self.hierarchical_combobox.current()], anchor=tk.W)
        else:
            for record in self.table.table.get_children():
                self.table.table.delete(record)
            my_cursor.execute(request)
        self.indicator_for_mainform()

    def indicator_for_mainform(self):
        for row in my_cursor:
            date, days, option = row[1], row[8].split()[0], row[8].split()[1][0]
            date = datetime.datetime.strptime("-".join(str(date).split(".")[::-1]), '%Y-%m-%d').date()
            if (datetime.date.today()+datetime.timedelta(days=7) >= Table.indentification_type_of_days(self.table,date, days, option)) and (row[10] != "исполнено"):
                self.table.table.insert("", 'end', values=row, tags=("yellow",))
            else:
                self.table.table.insert("", 'end', values=row)
        self.table.table.pack(expand=True, fill=tk.BOTH)
        self.table.table.tag_configure("yellow", background="yellow")

    def reset(self):
        self.reset_for_groupBy()
        for record in self.table.table.get_children():
            self.table.table.delete(record)
        my_cursor.execute(f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note,info.additional "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        self.indicator_for_mainform()
        self.search_combobox.current(0)
        self.search_entry.delete(0, "end")
        self.status_groupby = 0
        Table.default_selected_row(self.table)

    def add_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddingForm(self.newWindow, self.table)
        Table.default_selected_row(self.table)
        self.indicator_for_mainform()

    def edit_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Edit_row(self.newWindow, self.table)
        Table.default_selected_row(self.table)
        self.indicator_for_mainform()

    def groupBy_window(self):
        #
        self.table.table.destroy()
        self.table = GroupBy(self.frame, self.hierarchical_combobox)
        request = (f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note,info.additional "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        self.groupBy(request)
        self.table.table.heading('#0', text=columns[self.hierarchical_combobox.current()], anchor=tk.W)

    def groupBy(self,request):
        #done - work but not clear
        i, n, index = 0, 0, 0
        self.status_groupby = 1
        my_cursor.execute(request)
        list_repeats,dict_repeats = [],{}

        for row in my_cursor:
            for column in columns:
                if column == columns[self.hierarchical_combobox.current()]:
                    list_repeats.append(row[columns.index(column)])

        for first_columns in set(list_repeats):
            dict_repeats[first_columns] = 0
            self.table.table.insert("", tk.END, text=first_columns, iid=str(i), open=False)
            i+=1

        my_cursor.execute(request)

        for row in my_cursor:

            for column in columns:
                if column == columns[self.hierarchical_combobox.current()]:
                    date, days, option = row[1], row[8].split()[0], row[8].split()[1][0]
                    #if (datetime.date.today() + datetime.timedelta(days=7) >= Table.indentification_type_of_days(self.table, date,days,option)) and (row[10] != "исполнено"):
                    self.table.table.insert("", tk.END, text=row[columns.index(column)],tags=("yellow",), iid=str(i), open=False)
                    #else: self.table.table.insert("", tk.END, text=row[columns.index(column)], iid=str(i), open=False)
                    self.table.table.move(str(i), str(list(set(list_repeats)).index(row[columns.index(column)])),dict_repeats[row[columns.index(column)]])
                    dict_repeats[row[columns.index(column)]]+=1
                    i += 1

        my_cursor.execute(request)
        n = len(set(list_repeats))
        for row in my_cursor:
            for column in columns:
                if column != columns[self.hierarchical_combobox.current()]:
                    self.table.table.insert("", tk.END, text=column+": "+str(row[columns.index(column)]), iid=str(i), open=False)
                    self.table.table.move(str(i), str(n), index)
                    i += 1
                    index += 1
            n += 1
            index = 0
        self.table.table.pack(fill="both", expand=True)

    def reset_for_groupBy(self):
        self.table.table.destroy()
        self.table = Table(self.frame)

    def delete(self):
        selected_id = list(self.table.table.item(self.table.table.selection()[0]).values())[2][0]
        if selected_id:
            x = selected_id
            sql = '''DELETE FROM contract.info WHERE info.id = %s;'''
            my_cursor.execute(sql, (x,))
            my_connect.commit()

            for record in self.table.table.get_children():
                self.table.table.delete(record)

            my_cursor.execute(f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note,info.additional "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
            self.indicator_for_mainform()

class Table:
    def __init__(self, master):
        self.master = master
        self.table = ttk.Treeview(self.master,columns=columns)

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
        my_cursor.execute(f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note,info.additional "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        for row in my_cursor:
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
        # done
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(self.table.set(child, col), child) for child in self.table.get_children('')]
        # if the data to be sorted is numeric change to float
        if self.isfloat(data[0][0]):
            data = self.change_numeric_sortby(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            self.table.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
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
        my_cursor.execute(f"SELECT info.id, date_format(info.date, '%d.%m.%Y') as date, info.number, info.subject, info.costing, "
            f"date_format(info.end_date, '%d.%m.%Y') as end_date, employee_name.name, "
            f"info.payment, info.contr_time, date_format(info.approval, '%d.%m.%Y') as approval, info.status,info.note,info.additional "
            f"FROM contract.info INNER JOIN contract.employee_name ON (info.id_executiver=employee_name.id)")
        for row in my_cursor:
            date,days,option = row[1],row[8].split()[0],row[8].split()[1][0]
            date = datetime.datetime.strptime("-".join(str(date).split(".")[::-1]), '%Y-%m-%d').date()
            if (datetime.date.today()+datetime.timedelta(days=7) >= self.indentification_type_of_days(date,days,option)) and (row[10]!="исполнено"):
                self.table.insert("", 'end', values=row, tags=("yellow",))
            else:
                self.table.insert("", 'end', values=row)
        self.table.pack(expand=True, fill=tk.BOTH)
        self.table.tag_configure("yellow",background="yellow")

    def indentification_type_of_days(self,date,days,option):
        if option in ["б", "р"]:
            return self.date_by_adding_business_days(date, int(days))
        else:
            return self.date_by_adding_business_days(date, int(days))

    def date_by_adding_business_days(self,from_date, add_days):
        business_days_to_add = add_days
        current_date = from_date
        while business_days_to_add > 0:
            current_date += datetime.timedelta(days=1)
            weekday = current_date.weekday()
            if weekday >= 5:  # sunday = 6
                continue
            business_days_to_add -= 1
        return current_date

    def date_by_adding_calendar_days(self,from_date, add_days):
        business_days_to_add = add_days
        current_date = from_date
        while business_days_to_add > 0:
            current_date += datetime.timedelta(days=1)
            business_days_to_add -= 1
        return current_date

class AddingForm:
    def __init__(self, master, table):
        self.master = master
        self.master.resizable(width=False, height=False)
        self.table = table
        self.text_size_height = 1

        self.main_frame = tk.Frame(self.master)
        self.frame_labels1 = tk.Frame(self.main_frame)

        self.main_frame.pack(fill="both")
        self.frame_labels1.pack(fill="both")

        self.label_executiver = tk.Label(self.frame_labels1, text="Ответственное лицо", anchor="w")
        self.label_end_date = tk.Label(self.frame_labels1, text="Дата окончания", anchor="w")
        self.label_costing = tk.Label(self.frame_labels1, text="Стоимость", anchor="w")
        self.label_subject = tk.Label(self.frame_labels1, text="Предмет", anchor="w")
        self.label_number = tk.Label(self.frame_labels1, text="Номер", anchor="w")
        self.label_date = tk.Label(self.frame_labels1, text="Дата", anchor="w")
        self.label_id = tk.Label(self.frame_labels1, text="Id", anchor="w")

        self.label_executiver.grid(row=6, column=0)
        self.label_end_date.grid(row=5, column=0)
        self.label_costing.grid(row=4, column=0)
        self.label_subject.grid(row=3, column=0)
        self.label_number.grid(row=2, column=0)
        self.label_date.grid(row=1, column=0)
        self.label_id.grid(row=0, column=0)

        self.entry_id = tk.Text(self.frame_labels1, width=30, height=1, background="gainsboro")
        self.entry_date = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_number = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_subject = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_costing = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_end_date = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_executiver = tk.Text(self.frame_labels1, width=30, height=1)

        self.entry_id.grid(row=0, column=1)
        self.entry_date.grid(row=1, column=1)
        self.entry_number.grid(row=2, column=1)
        self.entry_subject.grid(row=3, column=1)
        self.entry_costing.grid(row=4, column=1)
        self.entry_end_date.grid(row=5, column=1)
        self.entry_executiver.grid(row=6, column=1)

        self.button_adding_executiver = tk.Button(self.frame_labels1, text="+", width=1, command=self.option_db_or_excel)
        self.button_adding_executiver.grid(row=6, column=1,sticky="e")

        self.label_additional = tk.Label(self.frame_labels1, text="Доп. соглашение", anchor="w")
        self.label_note = tk.Label(self.frame_labels1, text="Примечание", anchor="w")
        self.label_status = tk.Label(self.frame_labels1, text="Статус", anchor="w")
        self.label_approval = tk.Label(self.frame_labels1, text="Дата согласования", anchor="w")
        self.label_contr_time = tk.Label(self.frame_labels1, text="Сроки исполнения", anchor="w")
        self.label_payment = tk.Label(self.frame_labels1, text="Порядок оплаты", anchor="w")

        self.label_additional.grid(row=5, column=2)
        self.label_note.grid(row=4, column=2)
        self.label_status.grid(row=3, column=2)
        self.label_approval.grid(row=2, column=2)
        self.label_contr_time.grid(row=1, column=2)
        self.label_payment.grid(row=0, column=2)

        self.entry_payment = tk.Text(self.frame_labels1, width=30, height=4)
        self.entry_contr_time = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_approval = tk.Text(self.frame_labels1, width=30, height=1)
        self.combobox_status = ttk.Combobox(self.frame_labels1, width=37, values=("исполнено", "не исполнено"))
        self.entry_note = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_additional = tk.Text(self.frame_labels1, width=30, height=1)

        self.entry_payment.grid(row=0, column=3, padx=5, pady=2)
        self.entry_contr_time.grid(row=1, column=3, padx=5, pady=2)
        self.entry_approval.grid(row=2, column=3, padx=5, pady=2)
        self.combobox_status.grid(row=3, column=3, padx=5, pady=2)
        self.entry_note.grid(row=4, column=3, padx=5, pady=2)
        self.entry_additional.grid(row=5, column=3, padx=5, pady=2)

        self.quitButton = tk.Button(self.frame_labels1, text='Выйти', width=15, command=self.close_windows)
        self.addButton = tk.Button(self.frame_labels1, text="Добавить", width=25, command=self.add_row)
        self.quitButton.grid(row=7, column=1, padx=5, pady=10)
        self.addButton.grid(row=7, column=2, padx=5, pady=10)

        self.list_widgets = [self.entry_id, self.entry_date, self.entry_number, self.entry_subject, self.entry_costing,
                             self.entry_end_date, self.entry_payment, self.entry_contr_time,
                             self.entry_approval, self.entry_note, self.entry_additional]
        self.last_added_id()
        self.entry_id.configure(state='disabled')
        self.entry_executiver.configure(state='disabled')

    def option_db_or_excel(self):
        self.Window_options = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_options)
        self.main_frame_executiver.pack(fill="both")

        self.button_from_database = tk.Button(self.main_frame_executiver,text="С базы данных",width=40,command=self.get_executiver_from_db)
        self.button_from_excel = tk.Button(self.main_frame_executiver, text="С excel",width=40,command=self.get_executiver_from_excel)

        self.button_from_database.grid(column=0,row=0,pady=5,padx=10)
        self.button_from_excel.grid(column=0,row=1,pady=5,padx=10)

    def get_executiver_from_db(self):
        self.Window_options.destroy()
        self.Window_executiver_from_db = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_executiver_from_db)
        self.main_frame_executiver.pack(fill="both")

        self.label_executiver = tk.Label(self.main_frame_executiver, text="C базы данных", width=15, )
        self.combobox_executiver = ttk.Combobox(self.main_frame_executiver, width=40,values=self.get_list_names_db())
        self.combobox_executiver.bind('<KeyRelease>', self.check_input)
        self.button_executiver = tk.Button(self.main_frame_executiver, text="Ок", width=20,command=self.insert_name_from_db)

        self.label_executiver.grid(column=0, row=0, sticky="w", )
        self.combobox_executiver.grid(column=0, row=1, padx=10)
        self.button_executiver.grid(column=1, row=1, padx=10, pady=5)

    def get_executiver_from_excel(self):
        self.Window_options.destroy()
        self.Window_executiver_from_excel = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_executiver_from_excel)
        self.main_frame_executiver.pack(fill="both")

        self.label_executiver = tk.Label(self.main_frame_executiver, text="C excel", width=15, )
        self.combobox_executiver = ttk.Combobox(self.main_frame_executiver, width=40,values=self.get_list_names_excel())
        self.combobox_executiver.bind('<KeyRelease>', self.check_input)
        self.button_executiver = tk.Button(self.main_frame_executiver, text="Ок", width=20,command=self.insert_name_from_excel)

        self.label_executiver.grid(column=0, row=0, sticky="w", )
        self.combobox_executiver.grid(column=0, row=1, padx=10)
        self.button_executiver.grid(column=1, row=1, padx=10, pady=5)

    def get_list_names_db(self):
        my_cursor.execute("select name from contract.employee_name")
        list_names = [name[0] for name in my_cursor]
        return list_names

    def get_list_names_excel(self):
        list_names = pd.read_excel("Executivers.xlsx",sheet_name='Лист1').values.tolist()
        list_names = [name[0] for name in list_names]
        return list_names

    def insert_name_from_db(self):
        self.entry_executiver.configure(state='normal')
        self.entry_executiver.delete('1.0', 'end')
        self.entry_executiver.insert("end",self.combobox_executiver['values'][self.combobox_executiver.current()])
        self.entry_executiver.configure(state='disabled')
        self.Window_executiver_from_db.destroy()

    def insert_name_from_excel(self):
        self.entry_executiver.configure(state='normal')
        self.entry_executiver.delete('1.0', 'end')
        self.entry_executiver.insert("end",self.combobox_executiver['values'][self.combobox_executiver.current()])
        self.entry_executiver.configure(state='disabled')
        self.Window_executiver_from_excel.destroy()

    def check_input(self,event):
        value = event.widget.get()
        list_names = self.get_list_names_db()
        if value == '':
            self.combobox_executiver['values'] = list_names
        else:
            data = []
            for item in list_names:
                if value.lower() in item.lower():
                    data.append(item)
            self.combobox_executiver['values'] = data

    def last_added_id(self):
        self.last_id = 0
        my_cursor.execute("SELECT MAX( id ) FROM contract.info;")
        for i in my_cursor:
            self.last_id = i[0] + 1
        self.entry_id.insert("end", self.last_id)

    def add_row(self):
        # done
        list_status = ["исполнено", "не исполнено"]

        row = list()
        for text in self.list_widgets:
            row.append(text.get("1.0", 'end-1c'))
        row.insert(6,self.get_list_names_db().index(self.entry_executiver.get("1.0", 'end-1c'))+1)
        row.insert(10, list_status[self.combobox_status.current()])
        sql = ("INSERT INTO info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
        my_cursor.execute(sql, tuple(row))
        my_connect.commit()

        for record in self.table.table.get_children():
            self.table.table.delete(record)

        Table.insert_data_from_dbf(self.table)
        Table.create_indicator_by_date(self.table)

        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

class Edit_row():
    def __init__(self, master, table):
        self.master = master
        self.table = table
        self.row = self.table.table.focus()
        self.list_data_selected_row = list(self.table.table.item(self.row).values())[2]

        self.main_frame = tk.Frame(self.master)

        self.frame_labels1 = tk.Frame(self.main_frame)

        self.main_frame.pack(fill="both")
        self.frame_labels1.pack(fill="both")


        self.label_executiver = tk.Label(self.frame_labels1, text="Ответственное лицо", anchor="w")
        self.label_end_date = tk.Label(self.frame_labels1, text="Дата окончания", anchor="w")
        self.label_costing = tk.Label(self.frame_labels1, text="Стоимость", anchor="w")
        self.label_subject = tk.Label(self.frame_labels1, text="Предмет", anchor="w")
        self.label_number = tk.Label(self.frame_labels1, text="Номер", anchor="w")
        self.label_date = tk.Label(self.frame_labels1, text="Дата", anchor="w")
        self.label_id = tk.Label(self.frame_labels1, text="Id", anchor="w")

        self.label_executiver.grid(row=6, column=0)
        self.label_end_date.grid(row=5, column=0)
        self.label_costing.grid(row=4, column=0)
        self.label_subject.grid(row=3, column=0)
        self.label_number.grid(row=2, column=0)
        self.label_date.grid(row=1, column=0)
        self.label_id.grid(row=0, column=0)

        self.entry_id = tk.Text(self.frame_labels1, width=30, height=1, background="gainsboro")
        self.entry_date = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_number = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_subject = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_costing = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_end_date = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_executiver = tk.Text(self.frame_labels1, width=30, height=1)

        self.entry_id.grid(row=0, column=1)
        self.entry_date.grid(row=1, column=1)
        self.entry_number.grid(row=2, column=1)
        self.entry_subject.grid(row=3, column=1)
        self.entry_costing.grid(row=4, column=1)
        self.entry_end_date.grid(row=5, column=1)
        self.entry_executiver.grid(row=6, column=1)

        self.button_adding_executiver = tk.Button(self.frame_labels1, text="+", width=1,
                                                  command=self.option_db_or_excel)
        self.button_adding_executiver.grid(row=6, column=1, sticky="e")

        self.label_additional = tk.Label(self.frame_labels1, text="Доп. соглашение", anchor="w")
        self.label_note = tk.Label(self.frame_labels1, text="Примечание", anchor="w")
        self.label_status = tk.Label(self.frame_labels1, text="Статус", anchor="w")
        self.label_approval = tk.Label(self.frame_labels1, text="Дата согласования", anchor="w")
        self.label_contr_time = tk.Label(self.frame_labels1, text="Сроки исполнения", anchor="w")
        self.label_payment = tk.Label(self.frame_labels1, text="Порядок оплаты", anchor="w")

        self.label_additional.grid(row=5, column=2)
        self.label_note.grid(row=4, column=2)
        self.label_status.grid(row=3, column=2)
        self.label_approval.grid(row=2, column=2)
        self.label_contr_time.grid(row=1, column=2)
        self.label_payment.grid(row=0, column=2)

        self.entry_payment = tk.Text(self.frame_labels1, width=30, height=4)
        self.entry_contr_time = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_approval = tk.Text(self.frame_labels1, width=30, height=1)
        self.combobox_status = ttk.Combobox(self.frame_labels1, width=37, values=("исполнено", "не исполнено"))
        self.entry_note = tk.Text(self.frame_labels1, width=30, height=1)
        self.entry_additional = tk.Text(self.frame_labels1, width=30, height=1)

        self.entry_payment.grid(row=0, column=3, padx=5, pady=2)
        self.entry_contr_time.grid(row=1, column=3, padx=5, pady=2)
        self.entry_approval.grid(row=2, column=3, padx=5, pady=2)
        self.combobox_status.grid(row=3, column=3, padx=5, pady=2)
        self.entry_note.grid(row=4, column=3, padx=5, pady=2)
        self.entry_additional.grid(row=5, column=3, padx=5, pady=2)

        self.list_widgets = [self.entry_id, self.entry_date, self.entry_number, self.entry_subject, self.entry_costing,
                             self.entry_end_date, self.entry_executiver, self.entry_payment, self.entry_contr_time,
                             self.entry_approval, self.combobox_status, self.entry_note, self.entry_additional]

        self.get_data_from_selected_row()
        self.entry_id.configure(state='disabled')
        self.entry_executiver.configure(state='disabled')

        self.quitButton = tk.Button(self.frame_labels1, text='Выйти', width=15, command=self.close_windows)
        self.addButton = tk.Button(self.frame_labels1, text="Изменить", width=25, command=self.edit)
        self.quitButton.grid(row=7, column=1, padx=5, pady=10)
        self.addButton.grid(row=7, column=2, padx=5, pady=10)


    def option_db_or_excel(self):
        self.Window_options = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_options)
        self.main_frame_executiver.pack(fill="both")

        self.button_from_database = tk.Button(self.main_frame_executiver,text="С базы данных",width=40,command=self.get_executiver_from_db)
        self.button_from_excel = tk.Button(self.main_frame_executiver, text="С excel",width=40,command=self.get_executiver_from_excel)

        self.button_from_database.grid(column=0,row=0,pady=5,padx=10)
        self.button_from_excel.grid(column=0,row=1,pady=5,padx=10)

    def get_executiver_from_db(self):
        self.Window_options.destroy()
        self.Window_executiver_from_db = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_executiver_from_db)
        self.main_frame_executiver.pack(fill="both")

        self.label_executiver = tk.Label(self.main_frame_executiver, text="C базы данных", width=15, )
        self.combobox_executiver = ttk.Combobox(self.main_frame_executiver, width=40,values=self.get_list_names_db())
        self.combobox_executiver.bind('<KeyRelease>', self.check_input)
        self.button_executiver = tk.Button(self.main_frame_executiver, text="Ок", width=20,command=self.insert_name_from_db)

        self.label_executiver.grid(column=0, row=0, sticky="w", )
        self.combobox_executiver.grid(column=0, row=1, padx=10)
        self.button_executiver.grid(column=1, row=1, padx=10, pady=5)

    def get_executiver_from_excel(self):
        self.Window_options.destroy()
        self.Window_executiver_from_excel = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_executiver_from_excel)
        self.main_frame_executiver.pack(fill="both")

        self.label_executiver = tk.Label(self.main_frame_executiver, text="C excel", width=15, )
        self.combobox_executiver = ttk.Combobox(self.main_frame_executiver, width=40,values=self.get_list_names_excel())
        self.combobox_executiver.bind('<KeyRelease>', self.check_input)
        self.button_executiver = tk.Button(self.main_frame_executiver, text="Ок", width=20,command=self.insert_name_from_excel)

        self.label_executiver.grid(column=0, row=0, sticky="w", )
        self.combobox_executiver.grid(column=0, row=1, padx=10)
        self.button_executiver.grid(column=1, row=1, padx=10, pady=5)

    def get_list_names_db(self):
        my_cursor.execute("select name from contract.employee_name")
        list_names = [name[0] for name in my_cursor]
        return list_names

    def get_list_names_excel(self):
        list_names = pd.read_excel("Executivers.xlsx",sheet_name='Лист1').values.tolist()
        list_names = [name[0] for name in list_names]
        return list_names

    def insert_name_from_db(self):
        self.entry_executiver.configure(state='normal')
        self.entry_executiver.delete('1.0', 'end')
        self.entry_executiver.insert("end",self.combobox_executiver['values'][self.combobox_executiver.current()])
        self.entry_executiver.configure(state='disabled')
        self.Window_executiver_from_db.destroy()

    def insert_name_from_excel(self):
        self.entry_executiver.configure(state='normal')
        self.entry_executiver.delete('1.0', 'end')
        self.entry_executiver.insert("end",self.combobox_executiver['values'][self.combobox_executiver.current()])
        self.entry_executiver.configure(state='disabled')
        self.Window_executiver_from_excel.destroy()

    def check_input(self,event):
        value = event.widget.get()
        list_names = self.get_list_names_db()
        if value == '':
            self.combobox_executiver['values'] = list_names
        else:
            data = []
            for item in list_names:
                if value.lower() in item.lower():
                    data.append(item)
            self.combobox_executiver['values'] = data

    def get_data_from_selected_row(self):
        for i in range(len(self.list_widgets)):
            self.list_widgets[i].insert("end", self.list_data_selected_row[i])

    def close_windows(self):
        self.master.destroy()

    def edit(self):
        # done
        self.list_widgets = [self.entry_id, self.entry_date, self.entry_number, self.entry_subject, self.entry_costing,
                             self.entry_end_date, self.entry_payment, self.entry_contr_time,
                             self.entry_approval, self.entry_note, self.entry_additional]

        list_status = ["исполнено", "не исполнено"]

        row = list()
        for text in self.list_widgets:
            row.append(text.get("1.0", 'end-1c'))
        row.insert(6,self.get_list_names_db().index(self.entry_executiver.get("1.0", 'end-1c'))+1)
        row.insert(10, list_status[self.combobox_status.current()])

        my_cursor.execute("""
           UPDATE info,employee_name
           SET info.id=%s, date=%s, number=%s, subject=%s, costing=%s, end_date=%s, id_executiver=%s,payment=%s,
            contr_time=%s, approval=%s, status=%s, note=%s, additional=%s
           WHERE info.id=%s
        """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12],
              row[0]))

        my_connect.commit()

        for record in self.table.table.get_children():
            self.table.table.delete(record)

        Table.insert_data_from_dbf(self.table)
        Table.create_indicator_by_date(self.table)
        Table.default_selected_row(self.table)
        self.master.destroy()


class BaseForam():


class GroupBy:
    def __init__(self, master, hierarchical_combobox):
        self.master = master
        self.table = ttk.Treeview(self.master)
        self.hierarchical_combobox = hierarchical_combobox
        self.table.heading('#0', text=columns[self.hierarchical_combobox.current()], anchor=tk.W)

        self.create_y_scrollbar()

    def create_y_scrollbar(self):
        self.y_scrollbar = ttk.Scrollbar(self.table, orient="vertical", command=self.table.yview)
        self.y_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.y_scrollbar.set)



def main():
    root.title('Contract app')
    root.geometry('1440x960')
    app = MainForm(root)
    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas()

    my_connect = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mghfghmghfgh4573434",
        database="contract",
    )
    my_cursor = my_connect.cursor()

    def reset_id_increment(my_cursor):

        my_cursor.execute('''SET @num := 0;
                    UPDATE your_table SET id = @num := (@num+1);
                    ALTER TABLE your_table AUTO_INCREMENT =1;''')

#         '''SET @num := 0;
# UPDATE contract.info SET info.id = @num := (@num+1);
# ALTER TABLE contract.info AUTO_INCREMENT =1;'''


    columns = ["Id", "Дата", "№", "Предмет", "Стоимость", "Дата окончания действия договора", "Ответственное лицо",
               "Порядок оплаты", "Срок исполнения", "Дата согласования", "Статус исполнения", "Примечание",
               "Дополнительное соглашение"]
    counter_id = 0
    main()
