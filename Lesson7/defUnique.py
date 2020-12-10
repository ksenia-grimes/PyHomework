def Unique (numbers):
 spisok = []
 for i in numbers:
  if i not in spisok:
   spisok.append(i)
 return sorted(spisok)
numbers = [1,5,7,9,5,2,19,16,18,7]
print(Unique(numbers))
