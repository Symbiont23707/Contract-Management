import datetime
import CheckFormatData
import Table
import tkinter as tk
import tkinter.ttk as ttk
import GetNameExecutiver
import gallery



class Edit_row():
    def __init__(self, master, table,my_connect,my_cursor):
        self.master = master
        self.my_connect = my_connect
        self.my_cursor = my_cursor
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
                                                  command=self.get_name_executive)
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
        self.entry_additional = tk.Button(self.frame_labels1,text="Прикрепить",width=30, height=1,command=self.add_image)

        self.entry_payment.grid(row=0, column=3, padx=5, pady=2)
        self.entry_contr_time.grid(row=1, column=3, padx=5, pady=2)
        self.entry_approval.grid(row=2, column=3, padx=5, pady=2)
        self.combobox_status.grid(row=3, column=3, padx=5, pady=2)
        self.entry_note.grid(row=4, column=3, padx=5, pady=2)
        self.entry_additional.grid(row=5, column=3, padx=5, pady=2)

        self.list_widgets = [self.entry_id, self.entry_date, self.entry_number, self.entry_subject, self.entry_costing,
                             self.entry_end_date, self.entry_executiver, self.entry_payment, self.entry_contr_time,
                             self.entry_approval, self.combobox_status, self.entry_note]

        self.get_data_from_selected_row()
        self.entry_id.configure(state='disabled')
        self.entry_executiver.configure(state='disabled')

        self.quitButton = tk.Button(self.frame_labels1, text='Выйти', width=15, command=self.close_windows)
        self.addButton = tk.Button(self.frame_labels1, text="Изменить", width=25, command=self.edit)
        self.quitButton.grid(row=7, column=1, padx=5, pady=10)
        self.addButton.grid(row=7, column=2, padx=5, pady=10)

        for entry in [self.entry_id,self.entry_date, self.entry_number, self.entry_subject, self.entry_costing,self.entry_end_date,
                             self.entry_executiver,self.entry_payment, self.entry_contr_time,self.entry_approval, self.entry_note]:
            entry.event_add('<<Paste>>', '<Control-v>')

    def add_image(self):
        window = tk.Toplevel(self.master)
        self.my_cursor.execute(f"Select image,name,pure_path from contract.additional where (id_info = {self.entry_id.get('1.0', 'end-1c')})")
        list_image = [list(row) for row in self.my_cursor]

        self.app_gallery = gallery.Gallery(window,self.ok_button_command,list_image)

    def ok_button_command(self):
        return [(self.app_gallery.images[i].name, self.app_gallery.images[i].pure_path) for i in range(len(self.app_gallery.images))]

    def get_name_executive(self):
        self.app = GetNameExecutiver.GetNameExecutiver(self.master, self.entry_executiver,self.my_connect,self.my_cursor)

    def get_data_from_selected_row(self):
        for i in range(len(self.list_widgets)):
            self.list_widgets[i].insert("end", self.list_data_selected_row[i])

    def close_windows(self):
        self.master.destroy()

    def edit(self):
        # done
        self.list_widgets = [self.entry_id, self.entry_number, self.entry_subject, self.entry_costing,
                             self.entry_payment, self.entry_contr_time, self.entry_note]

        list_status = ["исполнено", "не исполнено"]
        dict_names = {}
        row = list()
        self.my_cursor.execute("select * from contract.employee_name")
        names = [name for name in self.my_cursor]
        for i in range(len(names)):
            dict_names[names[i][0]] = names[i][1]
        for text in self.list_widgets:
            row.append(text.get("1.0", 'end-1c'))
        try:
            row.insert(1,
                       datetime.datetime.strptime("-".join(str(self.entry_date.get("1.0", 'end-1c')).split(".")[::-1]),
                                                  '%Y-%m-%d').date())
        except:
            self.successful_window(text="Ошибка в дате")
            return "error"
        try:
            row.insert(5,
                       datetime.datetime.strptime(
                           "-".join(str(self.entry_end_date.get("1.0", 'end-1c')).split(".")[::-1]),
                           '%Y-%m-%d').date())
        except:
            self.successful_window(text="Ошибка в дате окончания")
            return "error"

        if self.entry_executiver.get("1.0", 'end-1c') in dict_names.values():
            row.insert(6, list(dict_names.keys())[list(dict_names.values()).index(self.entry_executiver.get("1.0", 'end-1c'))])
        else:

            sql = ("INSERT INTO employee_name (name) VALUES (%s);")
            self.my_cursor.execute(sql, (self.entry_executiver.get("1.0", 'end-1c'),))
            self.my_connect.commit()
            self.my_cursor.execute("SELECT MAX(Id) FROM employee_name;")
            row.insert(6, [last_id[0] for last_id in self.my_cursor][0])

        try:
            row.insert(9,
                       datetime.datetime.strptime(
                           "-".join(str(self.entry_approval.get("1.0", 'end-1c')).split(".")[::-1]),
                           '%Y-%m-%d').date())
        except:
            self.successful_window(text="Ошибка в дате согласования")
            return "error"

        row.insert(10, list_status[self.combobox_status.current()])

        self.my_cursor.execute(f"SELECT id from `contract`.`additional` WHERE (`id_info` = {self.entry_id.get('1.0', 'end-1c')});")
        try:
            for id_image in self.my_cursor:
                self.my_cursor.execute(f"DELETE FROM `contract`.`additional` WHERE (`id_info` = {self.entry_id.get('1.0', 'end-1c')}) and (`id`= {id_image[0]});")

            for path in self.ok_button_command():
                with open(path[0], "rb") as file:
                    BinaryData = file.read()
                    SQLStatement = (f"INSERT INTO additional (image, name, pure_path, id_info) VALUES (%s,%s,%s,%s);")
                    self.my_cursor.execute(SQLStatement, (BinaryData, path[0], path[1], self.entry_id.get("1.0", 'end-1c')))
                    self.my_connect.commit()
        except:
            print("Without image changing")

        check_data = CheckFormatData.Check_format_data(self.master, row)

        self.successful_window(check_data.check_on_formate_adding_data(row))

        if check_data.check_on_formate_adding_data(row) == "Запись успешно добавлена в базу данных":
            print(row)
            self.my_cursor.execute("""
                       UPDATE info,employee_name
                       SET info.id=%s, date=%s, number=%s, subject=%s, costing=%s, end_date=%s, id_executiver=%s,
                       payment=%s, contr_time=%s, approval=%s, status=%s, note=%s
                       WHERE info.id=%s
                    """, (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
            row[0]))

            self.my_connect.commit()

            for record in self.table.table.get_children():
                self.table.table.delete(record)

            Table.Table.insert_data_from_dbf(self.table)
            Table.Table.create_indicator_by_date(self.table)
            Table.Table.default_selected_row(self.table)
            self.master.destroy()
        else:
            return "error"

    def successful_window(self, text="Формат даты неправильно указан"):
        self.successful_action = tk.Toplevel(self.master)
        self.succsessful_frame = tk.Frame(self.successful_action)
        self.succsessful_frame.pack(fill="both")

        if text == "Запись успешно добавлена в базу данных":
            color = "green"
        else:
            color = "red"

        self.successful_label = tk.Label(self.succsessful_frame, text=text, fg=color)
        self.successful_label.grid(row=0, column=0, padx=5, pady=10)

        self.successful_button = tk.Button(self.succsessful_frame, text="Ок", command=self.successful_action.destroy,
                                           width=25)
        self.successful_button.grid(row=1, column=0, padx=5, pady=10)
        return text