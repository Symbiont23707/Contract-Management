from dbfread import DBF
import tkinter as tk
import tkinter.ttk as ttk


class MainForm:
    def __init__(self, master):
        self.master = master

        self.search_frame = tk.Frame(self.master)
        self.frame = tk.Frame(self.master)
        self.menu_frame = tk.LabelFrame(self.master)

        self.table = Table(self.frame)

        self.search_label = tk.Label(self.search_frame,text="Поиск по",)

        self.search_combobox = ttk.Combobox(self.search_frame,values=columns)
        self.search_combobox.current(0)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_button = tk.Button(self.search_frame,width=4,height=1,text="Поиск",command=self.search)
        self.default_button = tk.Button(self.search_frame, width=4, height=1, text="Сброс",command=self.reset)

        self.Addbutton = tk.Button(self.menu_frame, text='Добавить', width=25, command=self.add_window)
        self.Editbutton = tk.Button(self.menu_frame, text='Изменить', width=25, command=self.edit_window)
        self.DeleteButton = tk.Button(self.menu_frame, text='Удалить', width=25,command=self.delete)

        self.search_frame.pack(fill="both")
        self.frame.pack(fill="both",expand=True)
        self.menu_frame.pack()

        self.default_button.pack(side="right",padx=5,pady=3)
        self.search_button.pack(side="right",padx=5,pady=3)
        self.search_entry.pack(side="right",padx=7,pady=3)
        self.search_combobox.pack(side="right",padx=7,pady=3)
        self.search_label.pack(side="right",padx=7,pady=3)

        self.Addbutton.pack(side="left")
        self.Editbutton.pack(side="left")
        self.DeleteButton.pack(side="left")

    def search(self):
        for record in self.table.table.get_children():
            self.table.table.delete(record)
        for row in DBF(r"C:\Users\Lenovo\OneDrive\Документы\Visual FoxPro Projects\contract_table.dbf"):
            list_row = []
            for column in columns:
                list_row.append(row[column])
                print(self.search_entry.get().upper())
                print()
            if self.search_entry.get().upper() in str(list_row[self.search_combobox.current()]).upper():
                self.table.table.insert("", "end", values=list_row)

    def reset(self):
        for record in self.table.table.get_children():
            self.table.table.delete(record)
        for row in DBF(r"C:\Users\Lenovo\OneDrive\Документы\Visual FoxPro Projects\contract_table.dbf"):
            list_row = []
            for column in columns:
                print(row)
                list_row.append(row[column])
            self.table.table.insert("", "end", values=list_row)
        self.search_combobox.current(0)
        self.search_entry.delete(0,"end")

    def add_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = AddingForm(self.newWindow,self.table)

    def edit_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Edit_row(self.newWindow,self.table)

    def delete(self):
        # Get selected item to Delete
        selected_item = self.table.table.selection()[0]
        self.table.table.delete(selected_item)

class Table:
    def __init__(self, master):
        self.master = master
        self.table = ttk.Treeview(self.master)

        self.take_columns_dbf()
        self.create_table_columns()
        self.insert_data_from_dbf()
        self.create_y_scrollbar()
        self.create_x_scrollbar()

    def insert_data_from_dbf(self):
        for row in DBF(r"C:\Users\Lenovo\OneDrive\Документы\Visual FoxPro Projects\contract_table.dbf"):
            list_row = []
            for column in columns:
                list_row.append(row[column])
            self.table.insert("", "end", values=list_row)
        self.table.pack(fill="both",expand=True)

    def create_table_columns(self):
        self.table["column"] = columns
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column,command=lambda c=column: self.sortby(self.table, c, 0))

    def search_filter(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = SearchFiler(self.newWindow,self.table)

    def take_columns_dbf(self):
        global columns
        columns = []
        for k in range(1):
            for i in DBF(r"C:\Users\Lenovo\OneDrive\Документы\Visual FoxPro Projects\contract_table.dbf"):
                columns = list(i)

    def create_y_scrollbar(self):
        self.y_scrollbar = ttk.Scrollbar(self.table, orient="vertical", command=self.table.yview)
        self.y_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.y_scrollbar.set)

    def create_x_scrollbar(self):
        self.x_scrollbar = ttk.Scrollbar(self.table, orient="horizontal", command=self.table.xview)
        self.x_scrollbar.pack(side="bottom", fill="x")
        self.table.configure(xscrollcommand=self.x_scrollbar.set)

    def sortby(self,table, col, descending):
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(self.table.set(child, col), child) for child in self.table.get_children('')]
        # if the data to be sorted is numeric change to float
        # data =  change_numeric(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            self.table.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        self.table.heading(col, command=lambda col=col: self.sortby(self.table, col, int(not descending)))


class AddingForm:
    def __init__(self, master,table):
        self.master = master
        self.table = table

        self.main_frame = tk.Frame(self.master)

        self.frame_labels1 = tk.Frame(self.main_frame)
        self.frame_textbox1 = tk.Frame(self.main_frame)
        self.frame_labels2 = tk.Frame(self.main_frame)
        self.frame_textbox2 = tk.Frame(self.main_frame)

        self.main_frame.pack(fill="both")
        self.frame_labels1.grid(row=0,column=0)
        self.frame_textbox1.grid(row=0,column=1)
        self.frame_labels2.grid(row=0,column=2)
        self.frame_textbox2.grid(row=0, column=3)

        size = int(len(columns)/2)
        self.my_list_of_labels1 = []
        for label_name in columns[:size]:
            self.my_list_of_labels1.append(tk.Label(self.frame_labels1,text=label_name,anchor="w"))
            self.my_list_of_labels1[-1].pack(side="bottom",expand=True)

        self.my_list_of_text1 = []
        for text_name in columns[:size]:
            self.my_list_of_text1.append(tk.Text(self.frame_textbox1, height=1, width=30))
            self.my_list_of_text1[-1].pack(side="bottom",expand=True)

        self.my_list_of_labels2 = []
        for label_name in columns[size:]:
            self.my_list_of_labels2.append(tk.Label(self.frame_labels2,text=label_name,anchor="w"))
            self.my_list_of_labels2[-1].pack(side="bottom",expand=True)

        self.my_list_of_text2 = []
        for text_name in columns[size:]:
            self.my_list_of_text2.append(tk.Text(self.frame_textbox2, height=1, width=30))
            self.my_list_of_text2[-1].pack(side="bottom",expand=True)

        self.quitButton = tk.Button(self.main_frame, text='Выйти', width=15, command=self.close_windows)
        self.addButton = tk.Button(self.main_frame,text="Добавить",width=25,command=self.add_row)
        self.quitButton.grid(row=1,column=1)
        self.addButton.grid(row=1,column=2)

        self.my_list_of_label = self.my_list_of_labels1+self.my_list_of_labels2
        self.my_list_of_text = self.my_list_of_text1+self.my_list_of_text2

    def add_row(self):
        row = list()
        for textbox in self.my_list_of_text:
            print(textbox)
            row.append(textbox.get("1.0", "end-1c"))
        self.table.table.insert("","end",values=row)
        self.master.destroy()

    def close_windows(self):
        self.master.destroy()

class Edit_row():
    def __init__(self, master,table):
        self.master = master
        self.table = table
        self.row = self.table.table.focus()

        self.list_data_selected_row = list(self.table.table.item(self.row).values())[2]

        self.main_frame = tk.Frame(self.master)

        self.frame_labels1 = tk.Frame(self.main_frame)
        self.frame_textbox1 = tk.Frame(self.main_frame)
        self.frame_labels2 = tk.Frame(self.main_frame)
        self.frame_textbox2 = tk.Frame(self.main_frame)

        self.main_frame.pack(fill="both")
        self.frame_labels1.grid(row=0,column=0)
        self.frame_textbox1.grid(row=0,column=1)
        self.frame_labels2.grid(row=0,column=2)
        self.frame_textbox2.grid(row=0, column=3)

        size = int(len(columns)/2)
        self.my_list_of_labels1 = []
        for label_name in columns[:size]:
            self.my_list_of_labels1.append(tk.Label(self.frame_labels1,text=label_name,anchor="w"))
            self.my_list_of_labels1[-1].pack(side="bottom",expand=True)

        self.my_list_of_text1 = []
        for text_name in columns[:size]:
            self.my_list_of_text1.append(tk.Entry(self.frame_textbox1, width=30))
            self.my_list_of_text1[-1].pack(side="bottom",expand=True)

        self.my_list_of_labels2 = []
        for label_name in columns[size:]:
            self.my_list_of_labels2.append(tk.Label(self.frame_labels2,text=label_name,anchor="w"))
            self.my_list_of_labels2[-1].pack(side="bottom",expand=True)

        self.my_list_of_text2 = []
        for text_name in columns[size:]:
            self.my_list_of_text2.append(tk.Entry(self.frame_textbox2, width=30))
            self.my_list_of_text2[-1].pack(side="bottom",expand=True)

        self.quitButton = tk.Button(self.main_frame, text='Выйти', width=15, command=self.close_windows)
        self.editButton = tk.Button(self.main_frame,text="Изменить",width=25,command=self.edit)
        self.quitButton.grid(row=1,column=1)
        self.editButton.grid(row=1,column=2)

        self.my_list_of_text = self.my_list_of_text1+self.my_list_of_text2

        self.get_data_from_selected_row()

    def get_data_from_selected_row(self):
        for i in range(len(self.my_list_of_text)):
            self.my_list_of_text[i].insert(0, self.list_data_selected_row[i])

    def close_windows(self):
        self.master.destroy()

    def edit(self):
        row = list()
        for textbox in self.my_list_of_text:
            row.append(textbox.get())
        selected_item = self.table.table.selection()[0]
        self.table.table.item(selected_item,values=row)
        self.close_windows()


class SearchFiler:
    def __init__(self,master,table):
        self.master = master
        self.table = table


def main():
    root.title('Contract app')
    root.geometry('1440x960')
    app = MainForm(root)
    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    counter_id = 0
    main()