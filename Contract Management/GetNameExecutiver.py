import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

class GetNameExecutiver:
    def __init__(self, master, entry_executiver,my_connect,my_cursor):
        self.master = master
        self.my_connect = my_connect
        self.my_cursor = my_cursor
        self.entry_executiver = entry_executiver
        self.newWindow = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.newWindow)
        self.main_frame_executiver.pack(fill="both")

        self.button_from_database = tk.Button(self.main_frame_executiver, text="С базы данных", width=40,
                                              command=self.get_executiver_from_db)
        self.button_from_excel = tk.Button(self.main_frame_executiver, text="С excel", width=40,
                                           command=self.get_executiver_from_excel)

        self.button_from_database.grid(column=0, row=0, pady=5, padx=10)
        self.button_from_excel.grid(column=0, row=1, pady=5, padx=10)

    def get_executiver_from_db(self):
        self.newWindow.destroy()
        self.Window_executiver_from_db = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_executiver_from_db)
        self.main_frame_executiver.pack(fill="both")

        self.label_executiver = tk.Label(self.main_frame_executiver, text="C базы данных", width=15, )
        self.combobox_executiver = ttk.Combobox(self.main_frame_executiver, width=40, values=self.get_list_names_db())
        self.combobox_executiver.bind('<KeyRelease>', self.check_input)
        self.button_executiver = tk.Button(self.main_frame_executiver, text="Ок", width=20,
                                           command=self.insert_name_from_db)

        self.label_executiver.grid(column=0, row=0, sticky="w", )
        self.combobox_executiver.grid(column=0, row=1, padx=10)
        self.button_executiver.grid(column=1, row=1, padx=10, pady=5)

    def get_executiver_from_excel(self):
        self.newWindow.destroy()
        self.Window_executiver_from_excel = tk.Toplevel(self.master)
        self.main_frame_executiver = tk.Frame(self.Window_executiver_from_excel)
        self.main_frame_executiver.pack(fill="both")

        self.label_executiver = tk.Label(self.main_frame_executiver, text="C excel", width=15, )
        self.combobox_executiver = ttk.Combobox(self.main_frame_executiver, width=40,
                                                values=self.get_list_names_excel())
        self.combobox_executiver.bind('<KeyRelease>', self.check_input)
        self.button_executiver = tk.Button(self.main_frame_executiver, text="Ок", width=20,
                                           command=self.insert_name_from_excel)

        self.label_executiver.grid(column=0, row=0, sticky="w", )
        self.combobox_executiver.grid(column=0, row=1, padx=10)
        self.button_executiver.grid(column=1, row=1, padx=10, pady=5)

    def get_list_names_db(self):
        self.my_cursor.execute("select name from contract.employee_name")
        list_names = [name[0] for name in self.my_cursor]
        return list_names

    def get_list_names_excel(self):
        list_names = pd.read_excel("Executivers.xlsx", sheet_name='Лист1').values.tolist()
        list_names = [name[0] for name in list_names]
        return list_names

    def check_input(self, event):
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

    def insert_name_from_db(self):
        self.entry_executiver.configure(state='normal')
        self.entry_executiver.delete('1.0', 'end')
        self.entry_executiver.insert("end", self.combobox_executiver['values'][self.combobox_executiver.current()])
        self.entry_executiver.configure(state='disabled')
        self.Window_executiver_from_db.destroy()

    def insert_name_from_excel(self):
        self.entry_executiver.configure(state='normal')
        self.entry_executiver.delete('1.0', 'end')
        self.entry_executiver.insert("end", self.combobox_executiver['values'][self.combobox_executiver.current()])
        self.entry_executiver.configure(state='disabled')
        self.Window_executiver_from_excel.destroy()