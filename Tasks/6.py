vvod = input ('Введите список любых целых чисел через запятую: ')
guide = ['1','2','3','4','5','6','7','8','9','0',',',' ']
for i in vvod:
	if i not in guide:
		print ('Некорректный ввод. Вводите только целые числа.')
		exit()
# при вводе без запятых программа не работает
		
probel = vvod.replace (' ','')#убираются пробелы
vvodA = probel.split(',') #запятая как делитель для создания списка, вводА становится списком
vvodB = vvodA.copy() #копируется вводA, чтобы не было путаницы в дальнейшем

maximum = max(vvodA, key=int) #ключ дает понять, что в списке числа и можно выделить макс и мин 
vvodA.remove(maximum)
print('Список без максимального числа: ',vvodA)


minimum = min(vvodB, key=int) #если в инпуте есть 0, не воспринимает его как минимальное число
vvodB.remove(minimum)
print('Список без минимального числа: ',vvodB)
