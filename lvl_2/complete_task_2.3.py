# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


digit = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine'
}

def switch_it_up(number):
    match number:
        case 1:
            print(digit[1])
        case 2:
            print(digit[2])
        case 3:
            print(digit[3])
        case 4:
            print(digit[4])   
        case 5:
            print(digit[5])
        case 6:
            print(digit[6])
        case 7:
            print(digit[7])
        case 8:
            print(digit[8])  
        case 9:
            print(digit[9])
        case _:
            print("None")


switch_it_up(1)

