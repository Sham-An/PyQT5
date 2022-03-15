from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import csv


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 104)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 50, 321, 23))
        self.pushButton.setObjectName("pushButton")
#        self.pushButton.clicked.connect(self.on_click)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

#    def on_click(self):
#        file, _ = QFileDialog.getOpenFileName(self,'Open file',None,"Image (*.png *.jpg *jpeg)")[0]
#        file, _ = QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")


class Demo(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
#        file, _ = QFileDialog.getOpenFileName(self,'Open file',None,"Image (*.png *.jpg *jpeg)")[0]
#        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', "All (*.*)")
        file_txt = file

        if file:
            print(file)

################################################
        with open(file, 'r') as f:
            #sample = f.read(100) #читаем первые 100 символов (или весь файл)
            sample = f.readline()
#     # пример проверки, что файл имеет заголовки
            header = csv.Sniffer().has_header(sample)
            print('В файле есть заголовки: ', header)
            print(sample)
#     # создаем диалект
            dialect = csv.Sniffer().sniff(sample)
            print(dialect)
#
#            with open('file.csv', 'r') as f:
#     # передаем диалект и читаем файл
            reader = csv.reader(f, dialect)
            for row in reader:
               print(row)
               if reader.line_num > 5:
                    break


    #######################################################
#Чтобы напечатать диапазон строк, в данном случае от строки 4 до 7

        print("\n Чтобы напечатать диапазон строк, в данном случае от строки 4 до 7")
        with open(file, 'r') as csv_file:
            data = csv.reader(csv_file)
###########################################################
            csv_file.readline() #считывает первую строку заголовок
            str_ = csv_file.readline() #считывает вторую строку (первая данных)
            lenstr = int(len(str_))*4

            print("\n    ___________     DATA   ___________       \n")
#            mple = csv_file.read(496) #читаем 496 знака (байт) из файла методом файла
            sample = str_+csv_file.read(lenstr)  # читаем 496 знака (байт) из файла методом файла

#lenstr = len(lenstr)
            print(f"            Print SAMPLE {lenstr}   \n{sample}")
#############################################################
            for row in list(data)[0:7]:
                print(f"ROW = {row}")
                #print(list(data))

########################################################
#def read_csv():
        print("\n Чтение CSV-файла обычным способом read_csv() as file \n")

        with open(file, 'r') as file:
            reader = csv.reader(file)  # Возвращает повторяемый объект, который можно пройти только один раз
            #numstr=5
            # для строки в списке (читатель): # возвращает двумерный массив
            #             print(row)
            for row in reader:  # Может использовать .next, чтобы получить строку данных
            #for row in numstr:
                print(reader.line_num, row)
                if reader.line_num > 5:
                    break
#def read_to_dict()
        print("Читать CSV-файл как словарь  read_to_dict(): \n")
        with open(file_txt, 'r') as file:
            reader2 = csv.reader(file)  # Возвращает повторяемый объект, который можно пройти только один раз
            #Читать CSV-файл как словарь
            for row in reader2:
                print(row)
                if reader2.line_num > 5:
                    break

        print("Экспортировать данные CSV-Dict  export_with_Dict(): \n")
        fieldName = ['GTIN', 'SN']
        data = [
                {'GTIN': '04607022750508', 'SN': "001EAcl2qQpCX"},
        ]


        with open('example2.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldName)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
                print(row)
            # Записать несколько строк writer.writerrows (данные)
        print('export success \n')

        print("Экспорт формы списка данных CSV  export_with_list(): \n")
        data = [
            ['GTIN', 'SN'],
            ['04607022750508',"001EAcl2qQpCX"],
            ['04607022750508',"002Ro3TPVnd0d"],
            ['04607022750508',"002WufvucsRqd"],
        ]
        with open('exmplae3.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
                print(row)
            # Написать несколько строк writer.writerows (данные)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Demo()
#    ui = Ui_Form()
#    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


# Создание шаблона диалекта
# Если у вас используется множество разных параметров и идет нарушение принципов DRY (dont repeat yorself), то вы можете использовать диалект (или просто шаблон). В примере мы регистрируем параметры под общим названием 'myDialect' и передаем в функцию или класс:
#
# import csv
#
# csv.register_dialect('myDialect',
#                      delimiter=';',
#                      skipinitialspace=True,
#                      quoting=csv.QUOTE_ALL)
#
# with open('file1.csv', 'r') as f:
#     data = csv.reader(f, dialect='myDialect')
#     for row in data:
#         print(row)
#
# with open('file2.csv', 'r') as f:
#     data = csv.reader(f, dialect='myDialect')
#     for row in data:
#         print(row)
# Автоматическое определение параметров CSV файла
# Если используются разные файлы CSV и в каждом из них разные параметры для чтения, мы можем определить их автоматически с классом 'Sniffer'. Результат работы этого класса мы можем передать как диалект:
#
# import csv
#
# with open('file.csv', 'r') as f:
#     # читаем первые 100 символов (или весь файл)
#     sample = f.read(100)
#     # пример проверки, что файл имеет заголовки
#     header = csv.Sniffer().has_header(sample)
#     print('В файле есть заголовки: ', header)
#     # создаем диалект
#     dialect = csv.Sniffer().sniff(sample)
#
# with open('file.csv', 'r') as f:
#     # передаем диалект и читаем файл
#     reader = csv.reader(f, dialect)
#     for row in reader:
#         print(row)
#Метод 'has_header()' проверяет есть ли в файле заголовки. Аналогично этому
#методу могут быть использованы и другие методы проверяющие кавычки, делимитры и т.д.
