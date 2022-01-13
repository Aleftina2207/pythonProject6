# 1
def input_div_num():
     st1 = int(input("Введите целое число № 1:"))
     st2 = int(input("Введите целое число № 2:"))
     return int(st1)/int(st2)
print (input_div_num())

# 2

def print_user(name, surname, year_birth, city, email, phone):
    #print(f"Имя: {name}, фамилия: {surname}, год рождения: {year_birth}, ваш город: {city}, ваш email: {email},  телефон -{phone}")


print_user(name=input("ваше Имя"), surname=input("введите вашу фамилию"), year_birth=input("введите ваш год рождения"), city=input("введите ваш город"), email=input("введите вашу почту"), phone=input("введите ваш телефон"))



# 3
def max_two(s_1, s_2, s_3):
    try:
        s_list = [int(s_1), int(s_2), int(s_3)]
        s_list.remove(min(s_list))
        max_1 = s_list[0]
        max_2 = s_list[1]
        summary = max_1 + max_2
        print(f"Summ of 2 biggest numbers of your list:", summary)
    except ValueError:
        print("You entered wrong symbols, you must enter numbers!")


max_two(input("Enter number:"), input("Enter number:"), input("Enter number:"))



 #4

def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x >> 0 >> y:
            power_x = x ** y
            print("Result: x to the power of y = ", power_x)
        else:
            print("x must be > 0 and y must be < 0!")
    except ValueError as k:
        print(k)


my_func(input("Enter number x > 0: "), input("Enter number y < 0: "))


#5
def num_prit():
    input('введите несколько чисел':).split()
    for

        try:
            div_1 = int(div_1)
            div_2 = int(div_2)
            division = int(div_1) / int(div_2)
            print(f"{division:.2f}")
        except ValueError:
            print("You entered wrong symbols, you must enter numbers!")
        except ZeroDivisionError as t:
            print(t)

        my_first_func(input("Enter number: "), input("Enter divisor(!=0): "))

#6
def int_func():
    words = input("Enter words in small english letters using space between:")
    word_case = []
    for word in words.split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
                word_case.append(word.title()) if chars == len(word) else ""
    words_final = " ".join(word_case)
    return words_final


print(int_func())










