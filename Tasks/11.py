#задача на выведение суммы и количества элементов
#ввод списка
spisok = input('Введите список любых целых чисел: ')

probel = spisok.replace(" ", "")
numbers = probel.split(',')

#вариант проверки ввода
try:
	nums = [int(item) for item in numbers]
except ValueError:
	print ('Некорректный ввод. Вводите только целые числа.')
	exit()

a = input ('Введите число: ')
try: 
	a = int(a)
except ValueError:
	print ('Некорректный ввод. Вводите только целые числа.')
	exit()

# Решение
result = []
for i in nums:
    if i > a and i < 0:
        result.append(i)
print(sum(result))
print(len(result))
