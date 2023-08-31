# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

digit_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = [int(i) for i in digit_list]

def minimum(num_list):
    min_digit = num_list[0]
    for j in num_list:
        if j < min_digit:
            min_digit = j
    return min_digit

def maximum(num_list):
    max_digit = num_list[0]
    for k in num_list:
       if k > max_digit:
           max_digit = k
    return max_digit

min_digit = minimum(num_list)
max_digit = maximum(num_list)

print("min = ", min_digit,"," " max = ", max_digit)




    

