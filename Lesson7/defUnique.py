def Unique(numbers):
	spisok=[]
	for i in numbers:
		if i not in spisok:
			spisok.append(i)
	return sorted(spisok)
numbers = [90,90,76,56,76,32,9,1,0,87,-9]
print (Unique(numbers))
