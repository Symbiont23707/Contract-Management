import tkinter as tk
import tkinter.ttk as ttk

columns = ["Id", "Дата", "№", "Предмет", "Стоимость", "Дата окончания действия договора", "Ответственное лицо",
           "Порядок оплаты", "Срок исполнения", "Дата согласования", "Статус исполнения", "Примечание"]

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