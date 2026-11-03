import random


start_list = []                #создаём рандомный список
while len(start_list)<100:
    x = random.randint(0, 1_000_000)
    if x not in start_list:                             #смотрим чтобы не было дублекатов
        start_list.append(x)                            #если такого же элемента нет в списке добавляем его

print(f'Начальный список {start_list}')
start_list.sort()                                       #сортируем список
print(f'Отсортированный список {start_list}')


#линейный поиск
comparison_l = 0
y = int(input('Введите число которое хотите найти '))
if y in start_list:                                                                 #проверяем есть ли искомый элемент в списке
    for i in range(0,len(start_list)):                                              #проходимся по всем элементам списка и сравниваем не являеется ли этот элемент искомым
        if y == start_list[i]:
            index_l = i
            break
        comparison_l += 1
    print(f'По линейному поиску\nИндекс вашего числа в списке {index_l}, ваше число {index_l+1} по счёту\nКоличество сравнений {comparison_l}')
else:
    print('Вашего числа нету в списке')

print('='*150)

#бинарный поиск
comparison_b = 0
first = 0
last = len(start_list)-1
index_b = -1

if y in start_list:                                                                 #проверяем есть ли искомый элемент в списке
    while (first <= last) and (index_b == -1):                                      #ищем по бинарному поиску
        mid = (first+last)//2
        if start_list[mid] == y:
            index_b = mid
        else:
            if y<start_list[mid]:
                last = mid -1
            else:
                first = mid +1
            comparison_b += 1
        comparison_b += 1 
    print(f'По бинарному поиску\nИндекс вашего числа в списке {index_b}, ваше число {index_b+1} по счёту\nКоличество сравнений {comparison_b}')
else:
    print('Вашего числа нету в списке')


