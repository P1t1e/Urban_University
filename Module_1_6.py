my_dict = {'Ruslan': 2001, 'Alim': 2000, 'Nidal': 1999, 'Aslan': 1989}
print(my_dict)
my_dict['Astemir'] = 2005
print(my_dict['Alim'])
print(my_dict.get('Dasha'))
my_dict.update({'Masha': 2003, 'Nasty': 2002})
removed_ = my_dict.pop('Nidal')
print(removed_)
print(my_dict)

print()

my_set = {66, 66, 'list', True, 'list', 2, 5, 'potato', 7, 6, 8, 9}
print(my_set)
my_set.add('d')
my_set.add(13)
my_set.remove(2)
print(my_set)
