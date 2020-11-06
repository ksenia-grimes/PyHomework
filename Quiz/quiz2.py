start = input('Введите текст:')

#сортировка
sort = sorted(start)
#добавление в словарь
my_dict = {}
for i in sort:
    if i in my_dict:
        my_dict[i] += 1 #если этот ключ уже есть, увеличивается его значение на 1
    else:
        my_dict[i] = 1 #если ключа нет, добавляется и присваивается значение 1
for i in my_dict:
	  print (i, '=', my_dict[i])
