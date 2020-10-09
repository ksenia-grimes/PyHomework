print ('Эта программа поможет вам перевести градусы Цельсия в градусы Фаренгейта и наоборот.')
temp = str(input('Пожалуйста, введите интересующую вас температуру: '))
nums = ('1','2','3','4','5','6','7','8','9','0','-')
letters = ('C','c','F','f')

if temp[0] not in nums:
	print ('Некорректный ввод температуры.')
	exit(0)
elif temp[-1] not in letters:
	print ('Некорректный ввод температуры.')
	exit(0)

answer = float(temp[:-1])
if temp[-1] == 'C' or temp[-1] == 'c':
	far = (1.8 * answer) + 32
	print ('Искомый результат: ',round(far,1),'F')
if temp[-1] == 'F' or temp[-1] == 'f':
	cel = (answer - 32) / 1.8
	print ('Искомый результат: ',round(cel,1),'C')
