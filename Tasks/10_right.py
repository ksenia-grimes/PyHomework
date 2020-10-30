# Вывести все элементы списка, стоящие до максимального элемента этого списка

#ввод данных
spisok = input('Введите список любых целых чисел: ')
guide = ['1','2','3','4','5','6','7','8','9','0',',',' ']
for i in spisok:
	if i not in guide:
		print ('Некорректный ввод. Вводите только целые числа.')
		exit()

#блок удаления пробелов и деления на список
probel = spisok.replace(" ", "")
numbers = probel.split(',')
nums = [int(item) for item in numbers]

# блок решения
maximum = max(nums)
lugar = nums.index(maximum)

print(nums[:lugar])
