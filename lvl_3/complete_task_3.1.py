import random


class Matrix:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.data = [[None for _ in range(column)] for _ in range(row)]

    def fill_matrix(self, row, column, row_max_value):
        self.row = row
        self.column = column
        self.data = [[random.randint(1, row_max_value)
                      for _ in range(column)] for _ in range(row)]

    def display(self):
        for row in self.data:
            print(row)


print("1. Cоздаем матрицу ")
m = Matrix(5, 9)
m.display()

n = int(input("\n2. Введите N - максимальное значение для заполнения матрицы: "))
# Заполняем матрицу случайными значениями, где каждая колонка - число от 1 до N
m.fill_matrix(5, 9, n)
m.display()
