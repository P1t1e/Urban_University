# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
# from math import inf
def divide(first, second):
     if second != 0:
         return first / second
     if second == 0:
         return 'Ошибка!'