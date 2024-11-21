first = 234
second = 345
third = 456
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and second != third:
    print(0)
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0