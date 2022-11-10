class Check_format_data:
    def __init__(self,master,row):
        self.master = master
        self.row = row

    def check_on_formate_adding_data(self, row):
        if not self.check_on_formate_number_adding_data(row[4]):
            return "Стоимость неправильно указана"
        elif not self.check_on_formate_contract_time_adding_data(row[8]):
            return "Срок исполнения неправильно указан"
        else:
            return "Запись успешно добавлена в базу данных"

    def check_on_formate_date_adding_data(self, date):
        days = str(date).split(".")
        if len(days) == 3:
            if int(days[0]) > 31 or int(days[0]) < 1 or int(days[1]) > 12 or int(days[1]) < 1 or int(days[2]) > 9999 or int(days[2]) < 1900:
                return False
            return True
        else:
            return False

    def check_on_formate_number_adding_data(self, number):
        try:
            check_on_number = float(number)
            return True
        except ValueError:
            return False

    def check_on_formate_contract_time_adding_data(self, contract_time):
        contr_time = contract_time.split()
        if len(contr_time) == 2:
            if (contr_time[0].isnumeric() == False) or (contr_time[1][0] not in ["р", "б", "к"]):
                return False
            else:
                return True