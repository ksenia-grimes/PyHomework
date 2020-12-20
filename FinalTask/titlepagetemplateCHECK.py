#импортируем библиотеку для работы с docx-файлами
from docxtpl import DocxTemplate
#импортируем модуль регулярных выражений для проверки ввода данных
import re

#подключаем к работе шаблон
doc = DocxTemplate('example.docx')


#блок вводных данных и их проверки
universityname = str(input('Введите полное название вашего ВУЗа: ').strip())
while not re.match('^[A-Za-zА-Яа-яЁё\\s\'"().-]*$',universityname):
    print ('Проверьте правильность ввода данных.')
    universityname = str(input('Введите полное название вашего ВУЗа: ').strip())
facultyname = str(input('Введите полное название факультета: ').strip())
while not re.match('^[A-Za-zА-Яа-яЁё\\s\'"().-]*$',facultyname):
    print('Проверьте правильность ввода данных.')
    facultyname = str(input('Введите полное название факультета: ').strip())
cathedralname=str(input('Введите полное название кафедры: ').strip())
while not re.match('^[A-Za-zА-Яа-яЁё\\s\'"().-]*$',cathedralname):
    print('Проверьте правильность ввода данных')
    cathedralname=str(input('Введите полное название кафедры: ').strip())
profname=str(input('Введите инициалы и фамилию руководителя ООП, например И.И. Иванов: ').strip())
while not re.match('^[A-Za-zА-Яа-яёЁ\\s.-]*$', profname):
    print ('Пожалуйста, используйте только буквы алфавита, "." и "-"')
    profname=str(input('Введите инициалы и фамилию руководителя ООП, например И.И. Иванов: ').strip())
achievements=str(input('Введите должность/звание руководителя ООП (кратко): ').strip())
year = str(input('Введите год написания и защиты работы: ').strip())
while year.isdigit() == False:
    print ('Пожалуйста, вводите только цифры. ')
    year = str(input('Введите год написания и защиты работы: ').strip())
nameofthesis=str(input('Введите полное название вашей работы без кавычек: ').strip().upper())
numberofcourse=str(input('Введите номер направления ООП: ').strip())
course=str(input('Введите название ООП: ').strip())
fullstudentname = str(input('Введите ваше полное ФИО: ').strip())
while not re.match('^[A-Za-zА-Яа-яёЁ\\s.-]*$', fullstudentname):
    print ('Пожалуйста, используйте только буквы алфавита, "." и "-"')
    fullstudentname = str(input('Введите ваше полное ФИО: ').strip())
leadername=str(input('Введите инициалы и фамилию вашего научного руководителя, например И.И. Иванов: ').strip())
while not re.match('^[A-Za-zА-Яа-яёЁ\\s.-]*$', leadername):
    print ('Пожалуйста, используйте только буквы алфавита, "." и "-"')
    leadername=str(input('Введите инициалы и фамилию вашего научного руководителя, например И.И. Иванов: ').strip())
leaderachievements=str(input('Введите должность/звание вашего научного руководителя (кратко): ').strip())
studentname=str(input('Введите ваши инициалы и фамилию: ').strip())
while not re.match('^[A-Za-zА-Яа-яЁё\\s.-]*$',studentname):
    print ('Пожалуйста, используйте только буквы алфавита, "." и "-"')
    studentname=str(input('Введите ваши инициалы и фамилию: ').strip())
groupnumber=str(input('Введите номер группы: ').strip())
city=str(input('Введите ваш город: ').strip())
while not re.match('^[A-Za-zА-Яа-яЁё\\s\'"().-]*$',city):
    print ('Пожалуйста, проверьте правильность ввода данных')
    city=str(input('Введите ваш город: ').strip())

#переносим данные в словарь
context = {'universityname':universityname,'facultyname':facultyname,'cathedralname':cathedralname,
           'achievements':achievements,'profname':profname,'year':year,'nameofthesis':nameofthesis,
           'numberofcourse':numberofcourse,'course':course,'fullstudentname':fullstudentname,
           'leadername':leadername,'leaderachievements':leaderachievements,
           'studentname':studentname,'groupnumber':groupnumber,'city':city}
#print(context)
#заменяем все нужные строки в шаблоне полученными данными
doc.render(context)

#сохраняем файл
doc.save("example-final.docx")
#или doc.save('example.docx')-заменит существующий шаблон
print ('Смотрите файл "examaple-final.docx" в той же папке, где запускали код :)')
