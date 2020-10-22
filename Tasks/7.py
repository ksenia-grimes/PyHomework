vvod = input()
nums = []
#все так же проблема с проверкой ввода на буквы и символы

probel = vvod.replace(" ", "")
numbers = probel.split(',')

b = '0'
for i in numbers:
	if not i is b:
		nums.append(i)
print (nums) 

# при работе с известным заранее списком все нормально, например
#a = [0,8,9,45,90,0]
#b = []
#for i in a:
	#if i != 0:
		#b.append(i)
#print (b)
# но с input на просто 0 не реагирует, только если в кавычках через переменную. сколько ни пыталась, не получилось исправить. почему так?
