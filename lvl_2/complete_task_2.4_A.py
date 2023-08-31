# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# 1 вариант (любой вводимый текст)

def remove_exclamation_marks(s):

    return s.replace("!", "")

print(remove_exclamation_marks("Hi! Hello!"))

# 2 вариант (со стоками из примера)

str_1 = "Hi! Hello!"
str_2 = ""
str_3 = "Oh, no!!!"

def remove_exclamation_marks(str_1, str_2, str_3):

    return str_1.replace("!", ""), str_2.replace("!", ""), str_3.replace("!", "")

print(remove_exclamation_marks(str_1, str_2, str_3))

    