# Вывести все элементы списка, стоящие до максимального элемента этого списка
# Ввод: X = [3, 0, 7, 0, 0, 3]
# Вывод: [3, 0]

# Ввод данных
spisok = input('Введите список любых целых чисел: ')
guide = ['1','2','3','4','5','6','7','8','9','0',',',' ']
for i in spisok:
	if i not in guide:
		print ('Некорректный ввод. Вводите только целые числа.')
		exit()

#блок удаления пробелов и деления на список
probel = spisok.replace(" ", "")
numbers = probel.split(',')

# блок решения
maximum = max(numbers, key=int)
lugar = numbers.index(maximum)

print(numbers[:lugar])
