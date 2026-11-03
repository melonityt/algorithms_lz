import random

start_list = []                #создаём рандомный список
for i in range(0,10):
    x = random.randint(0, 1_000_000)
    if x not in start_list:
        start_list.append(x)
print(f'Начальный список {start_list}')
start_list.sort                                         #сортируем список
print(f'Отсортированный список {start_list}')


#линейный поиск
y = int(input('Введите число которое хотите найти '))
if y in start_list:
    for i in range(0,len(start_list))


else:
    print('Вашего числа нету в списке')