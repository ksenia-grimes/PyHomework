# Дан список чисел. Вычислить среднее арифметическое положительных элементов этого списка
# и среднее арифметическое отрицательных элементов этого списка (0 исключать, он ни положителен, ни отрицателен)

# Ввод
spisok = input("Пожалуйста, введите любую последовательность чисел: ")

probel = spisok.replace(" ", "")
numbers = probel.split(',')

#проверка ввода
try:
	nums = [int(item) for item in numbers]
except ValueError:
	print ('Некорректный ввод, вводите только целые числа.')
	exit()

# Решение
plus = []
minus = []

#среднее отрицательных элементов
for j in nums:
    if j < 0:
        minus.append(j)
resultMIN = sum(minus) / len(minus)
print(resultMIN)

#среднее положительных элементов
for i in nums:
    if i > 0:
        plus.append(i)
resultPLUS = sum(plus) / len(plus)
print(resultPLUS)
