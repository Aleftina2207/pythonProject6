№1
from sys import argv
try:
    hours, fee, bonus = argv[1:]
    hours, fee, bonus = float(hours), float(fee), float(bonus)
    salary = hours * fee + bonus
    print(f"Salary of the employee in this month - {salary}")
except ValueError:
    print("You must add 3 numbers!")

№1
initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [initial_list[el] for el in range(1, len(initial_list)) if initial_list[el] > initial_list[el]-1]
print(new_list)


№3
print("Числа кратные 20 в диапазоне от 20 до 240:", [n for n in range(20, 241, 20)])

print("Числа кратные 21 в диапазоне от 20 до 240:", [n for n in range(20, 240) if n % 21 == 0])


initial_l = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_l = [el for el in initial_l if initial_l.count(el) == 1]
print(new_l)


№4
from functools import reduce

thousand = [n for n in range(100, 1001, 2)]
print(thousand)
print(reduce(lambda n, m: n*m, thousand))


№5
from itertools import count, cycle

list_1 = []
for el in count(3):
    list_1.append(el)
    if el >= 10:
        print(list_1)
        c = 0
        for n in cycle(list_1):
            if c > 20:
                break
            print(n)
            c += 1
        quit()


№6
from math import factorial
from itertools import count


def fact():
    for el in count(1):
        yield factorial(el)

№7
generate = fact()
n = input("enter number to get its factorial: ")
c = 0
try:
    for i in generate:
        if c >= int(n):
            break
        else:
            c += 1
            print(f"Factorial {c} = {i}")
except ValueError as c:
    print(c)
