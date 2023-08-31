# Задача 2
# Задача 1.2.
# Пункт B. 

# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

# РЕШЕНИЕ:

my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive' : 3.40,
    'Out of Touch' : 3.03,
    'A Sorta Fairytale' : 5.28,
    'Easy' : 4.15,       
    'Beautiful Day' : 4.04,
    'Nowhere to Run' : 2.58,
    'In This World' : 4.02,
}

from random import sample
anthg_3 = list(my_favorite_songs.items())
soung_3 = sample(anthg_3, 3)
total = 0
for i in soung_3:
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