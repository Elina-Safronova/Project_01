# Задача 2
# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# РЕШЕНИЕ:

my_favorite_songs = [
    ['Waste a Moment', '3.03'],
    ['New Salvation', '4.02'],
    ['Staying\' Alive', '3.40'],
    ['Out of Touch', '3.03'],
    ['A Sorta Fairytale', '5.28'],
    ['Easy', '4.15'],       
    ['Beautiful Day', '4.04'],
    ['Nowhere to Run', '2.58'],
    ['In This World', '4.02'],
]
import random
anthg_3 = [random.choice(my_favorite_songs) for j in range(3)]
total = 0
for i in anthg_3:
    pass
    if i[0] == 'Waste a Moment':
        total += float(i[1])
    elif i[0] == 'New Salvation':
        total += float(i[1])
    elif i[0] == 'Staying\' Alive':
        total += float(i[1])
    elif i[0] == 'Out of Touch':
        total += float(i[1])
    elif i[0] == 'A Sorta Fairytale':
        total += float(i[1])  
    elif i[0] == 'Easy':
        total += float(i[1])
    elif i[0] == 'Beautiful Day':
        total += float(i[1])
    elif i[0] == 'Nowhere to Run':
        total += float(i[1])
    elif i[0] == 'In This World':
        total += float(i[1])
print("Три песни звучат", round(total, 2), "минут")