    # Задайте переменные разных типов данных:
immutable_var = (True, 228, 3.14, 'Hello')
print(immutable_var)
    # Изменение значений переменных:
        #immutable_var[2] = 333.14
        #print(immutable_var)
        #TypeError: 'tuple' object does not support item assignment
# Значения элементов кортежа нельзя изменить, потому что кортеж является неизменяемым типом.
# Данная функция обеспечивает безоппасность данных, от их случайного изменения. Так же Кортежи занимают в памяти меньше места чем список.
    #Создание изменяемых структур данных:
mutable_list = [False, 112, -222, 'homework']
print(mutable_list)
mutable_list[0] = 'hi'
mutable_list[1] = 'my'
mutable_list[2] = 'fried'
mutable_list[3] = True
print(mutable_list)