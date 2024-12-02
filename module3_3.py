def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params('stop')
print_params('boom', 'klik')
print_params(45, 4, None)
print_params(b=25)
print_params(c=[1, 2, 3])
print()
values_list = ['code', 3.14, False]
values_dict = {'a': 'int', 'b': True, 'c': 0}
print_params(*values_list)
print_params(**values_dict)

values_list2 = [113, 'string']
print_params(*values_list2, 42)
