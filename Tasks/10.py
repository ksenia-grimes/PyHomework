# задача на вывод всех элементов кроме максимального и удаление повторяющихся элементов
spisok = input ('Введите список целых чисел через запятую: ')
guide = ['1','2','3','4','5','6','7','8','9','0',',',' ']
for i in spisok:
	if i not in guide:
		print ('Некорректный ввод. Вводите целые числа через запятую.')
		exit()
#попытка решить ввод без запятой. работает только если совсем нет запятых.
if guide[10] not in spisok:
	print ('Пожалуйста, вводите через запятую.')
	exit()

probel = spisok.replace (' ','') #убираются пробелы
numbers = probel.split(',') #запятая как делитель для создания списка

nums = [] 

#вывод
maximum = max(numbers, key=int)
for j in numbers:
	if j != maximum:
		nums.append(j)

new_nums = [] #удаляю повторяющиеся элементы
for elem in nums:
	if elem not in new_nums:
		new_nums.append(elem)

print('Список без максимального числа: ',new_nums)
