import csv

'''
Чтение CSV-файла обычным способом
'''


def read_csv():
    with open('example.csv', 'r') as file:
        reader = csv.reader(file)  # Возвращает повторяемый объект, который можно пройти только один раз
        # для строки в списке (читатель): # возвращает двумерный массив
        #             print(row)
        for row in reader:  # Может использовать .next, чтобы получить строку данных
            print(reader.line_num, row)


'''
 Читать CSV-файл как словарь
'''


def read_to_dict():
    with open('example.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


'''
 Экспортировать данные CSV-Dict
'''


def export_with_Dict():
    fieldName = ['name', 'age']

    data = [
        {'name': 'Mike', 'age': 12},
        {'name': 'Jack', 'age': 13},
        {'name': 'Bob', 'age': 14},
        {'name': 'Tom', 'age': 15},
    ]

    with open('example.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldName)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        # Записать несколько строк writer.writerrows (данные)

    print('export success')


'''
 Экспорт формы списка данных CSV
'''


def export_with_list():
    data = [
        ['name', 'age'],
        ['Mike', 12],
        ['Jack', 13],
        ['Jerry', 14],
    ]
    with open('exmplae.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
        # Написать несколько строк writer.writerows (данные)


if __name__ == '__main__':
    read_csv()
    #pass