calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]
    #return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Danatelo'))
print(string_info('Lamborjini'))
print(string_info('Miki'))
print(is_contains('Summer', ['son', 'listen', 'sUMMer']))
print(is_contains('music', ['MUZ', 'muSIcality']))
print(is_contains('UrBan', ['urbOn', 'Urban', 'Boom']))
print(calls)