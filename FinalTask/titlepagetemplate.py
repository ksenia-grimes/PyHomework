from docxtpl import DocxTemplate
doc = DocxTemplate("example.docx")
context = {'universityname':str(input('Введите полное название вашего ВУЗа: ').strip()),
           'facultyname':str(input('Введите полное название факультета: ').strip()),
           'cathedralname':str(input('Введите полное название кафедры: ').strip()),
           'achievements':str(input('Введите должность/звание руководителя ООП (кратко): ').strip()),
           'profname':str(input('Введите инициалы и фамилию руководителя ООП, например И.И. Иванов: ').strip()),
           'year':str(input('Введите год написания и защиты работы: ').strip()),
           'nameofthesis':str(input('Введите полное название вашей работы без кавычек: ').strip().upper()),
           'numberofcourse':str(input('Введите номер направления ООП: ').strip()),
           'course':str(input('Введите название ООП: ').strip()),
           'fullstudentname':str(input('Введите свое полное имя: ').strip()),
           'leaderachievements':str(input('Введите должность/звание вашего научного руководителя (кратко): ').strip()),
           'leadername':str(input('Введите инициалы и фамилию вашего научного руководителя, например И.И. Иванов: ').strip()),
           'studentname':str(input('Введите ваши инициалы и фамилию: ').strip()),
           'groupnumber':str(input('Введите номер группы: ').strip()),
          'city':str(input('Введите ваш город: ').strip())}
doc.render(context)
doc.save("example-final.docx")
#или doc.save('example.docx')-заменит существующий шаблон
print ('Смотрите файл "example-final.docx" в той же папке, где запускали код :)')
