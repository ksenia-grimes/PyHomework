# задача на включене элементов в список (конкретно после 2 элемента)

# Ввод данных
spisok = input('Введите список любых целых чисел: ')
guide = ['1','2','3','4','5','6','7','8','9','0',',',' ']
for i in spisok:
	if i not in guide:
		print ('Некорректный ввод. Вводите только целые числа.')
		exit()
#есть проблема ввода без запятых (3 8 4 8 43), он тогда не может создать список и программа не работает

probel = spisok.replace(" ", "")
numbers = probel.split(',')

#проверка трех элементов
a1 = input ('Введите число: ')
for p in a1:
	if p not in guide:
		print ('Некорректный ввод числа.')
		exit()
a11=a1.replace(' ','')

a2 = input ('Введите число: ')
for p in a2:
	if p not in guide:
		print ('Некорректный ввод числа.')
		exit()
a22 = a2.replace(' ','')

a3 = input ('Введите число: ')
for p in a3:
	if p not in guide:
		print ('Некорректный ввод числа.')
		exit()
a33 = a3.replace (' ','')

numbers.insert(2, a11)
numbers.insert(3, a22)
numbers.insert(4, a33)

print(numbers)
