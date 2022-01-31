#1
Date:
    def __init__(self):
        self.date = str(input("Введите дату в формате чч-мм-гггг:"))

    @classmethod
     mode(cls, obj):
        date = obj.date
        date_mode = []
        for i in date.split("-"):
            date_mode.append(i)
        try:
            return f"Day {int(date_mode[0])}, month - {int(date_mode[1])}, year - {int(date_mode[2])}"
        except ValueError as k:
            return k

    @staticmethod
     defvalidation(day, month, year):
        if 0 <= year <= 2021:
            if 1 <= month <= 12:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if 1 <= day <= 31:
                        return f"ok"
                    else:
                        return f"В январе, марте, мае, июле, августе, октябре и декабре 31 день"
                 elifmonth in [4, 6, 9, 11]:
                    if 1 <= day <= 30:
                        return f"ok"
                    else:
                        return f"В апреле, июне, сентябре и носябре 30 дней"
                 elifyear % 4 != 0:
                    if month in [2]:
                        if 1 <= day <= 29:
                            return f"ok"
                        else:
                            return f"В феврале невисокосного года 28 дней"
                 elifyear % 4 == 0:
                    if month in [2]:
                        if 1 <= day <= 28:
                            return f"ok"
                        else:
                            return f"В феврале високосного года 29 дней"
            else:
                return f"В году всего 12 месяцев"
        else:
            return f"Принимаем год от 0 но 2021 н.э."

    def get_date(self):
        d = self.date.split("-")
        try:
            return int(d[0])
        except ValueError as k:
            return k

    def get_month(self):
        d = self.date.split("-")
        try:
            return int(d[1])
        except ValueError as k:
            return k

    def get_year(self):
        d = self.date.split("-")
        try:
            return int(d[2])
        except ValueError as k:
            return k


a = Date()
print(Date.mode(a))
print(validation(a.get_date(), a.get_month(), a.get_year()))

#2
class MyZeroDiv(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        dividend = float(input("Enter number which you want to divide: "))
        divisor = float(input("Enter divisor: "))
        if divisor == 0:
            raise MyZeroDiv("We can't divide by 0!")
    except MyZeroDiv as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print(dividend / divisor)
        break

#3
class (Exception):
    def __init__(self, text):
        self.text = text


while True:
    num = input("Enter number to add it in the list or 's' if you want to exit: ")
    fin_list = []
    if num == "s" or num == "S":
        print(f"Final list is {fin_list}")
        break
    try:
        if not num.isdigit():
            raise OnlyNumbers("Only numbers can be added to the list")
    except OnlyNumbers as ON:
        print(ON.)
    else:
        num = int(num)
        fin_list.append(num)
        print(fin_list)

#7
""" Операции с комплексными числами"""


class ComplexNum:
    def __init__(self):
        self.a = input("Enter real number a of the complex: ")
        self.b = input("Enter real number b of the complex: ")
        try:
            self.num = complex(int(self.a), int(self.b))
        except TypeError as v:
            print(v)

    def __add__(self, other):
        try:
            # return self.num + other.num # более простая реализация
            add_a = int(self.a) + int(other.a)
            add_b = int(self.b) + int(other.b)
            add_complex = complex(add_a, add_b)
            return add_complex
        except AttributeError as ae:
            return ae

    def __mul__(self, other):
        try:
            return self.num * other.num
        except AttributeError as ae:
            return ae


n_1 = ComplexNum()
n_2 = ComplexNum()
print(f"Sum of complex numbers n_1 and n_2 is {n_1 + n_2}")
print(f"Multiplication of complex numbers n_1 and n_2 is {n_1 * n_2}")