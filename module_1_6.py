my_dict = {'Мария': 1996, 'Рита': 1988, 'Ольга': 1990}
print('Словарь: ', my_dict)
print('Дата рождения: ', (my_dict['Ольга']))
print(my_dict.get('Алина', 'Такого имени нет'))
my_dict.update({'Иван': 2004, 'Василий': 2015})
print(my_dict)
my_dict.pop('Рита')
print(my_dict)

my_set = {1, 'z', True, (5.5, 7, 1), 1, 16, 16, False, True, 'a', 'b', 'z', 48, True}
print('Набор:', my_set)
my_set.update(['gorilla'], ['stone'])
print('Новый набор: ', my_set)
