spisok = input('Введите список любых целых чисел через запятую: ')
guide = ['1','2','3','4','5','6','7','8','9','0',',',' ']
for i in spisok:
	if i not in guide:
		print ('Некорректный ввод. Вводите только целые числа.')
		exit()
#при вводе без запятых программа не работает

probel = spisok.replace(" ", "")
numbers = probel.split(',')

#проверка числа b
b = input ('Введите искомое число: ')
for p in b:
	if p not in guide:
		print ('Некорректный ввод искомого числа.')
		exit()

nums = []
#блок исключения
if b in numbers:
	for j in numbers:
		if b!=j: 
			nums.append(j)
	print (nums) #почему если сдвинуть на несколько табов вправо, то print в результате выглядит по-другому?
else:
	print ('В списке чисел нет искомого числа.')
