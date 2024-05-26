first = input('Введите 1-е число: ')
second = input('Введите 2-е число: ')
third = input('Введите 3-е число: ')
if first == second == third:
    print('Вывод 1 усл.: ', third)
elif first == second or second == third or first == third:
    print('Вывод 2 усл.: ', second)
elif first != second and second != third and first != third:
    print('Вывод 3 усл.: ', 0)