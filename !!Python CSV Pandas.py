import pandas as pd

titanic_data = pd.read_csv('titanic.csv')
titanic_data.head()
print(titanic_data.head())
col_names = ['Id',
             'Survived',
             'Passenger Class',
             'Full Name',
             'Gender',
             'Age',
             'SibSp',
             'Parch',
             'Ticket Number',
             'Price', 'Cabin',
             'Station']

titanic_data = pd.read_csv(r'titanic.csv', names=col_names, skiprows=[0], sep=',')#, sep=';')
print(titanic_data.head())

#Запись CSV-файлов с помощью to_csv()
#Опять же, DataFrame являются табличными.
# Превратить DataFrame в CSV – файл так же просто, как превратить
# CSV – файл в DataFrame – мы вызываем функцию write_csv() у экземпляра DataFrame .

cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
cities.to_csv('cities.csv')
#Индексы из DataFrame в итоге превратились в новый столбец, который теперь Unnamed.
df = pd.read_csv('cities.csv')
print(f'{df} \n')

#При сохранении файла необходимо обязательно отбросить индекс DataFrame:
cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
cities.to_csv('cities.csv', index=False)

df = pd.read_csv('cities.csv')
print(f'{df} \n')

#Обработка пропущенных значений
#Иногда DataFrame имеют пропущенные значения, которые мы оставили как NaN или NA . В таких случаях вы можете отформатировать их при записи в CSV-файл. Вы можете использовать аргумент na_rep и установить значение, которое будет помещено вместо пропущенного значения:
cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida'], ['Washington DC', pd.NA]], columns=['City', 'State'])
cities.to_csv('cities.csv', index=False, na_rep='Unknown')

df = pd.read_csv('cities.csv')
print(f'{df} \n')
#В статье показано, как читать и писать CSV-файлы с помощью Python библиотеки Pandas.
# Для чтения CSV-файла используется метод read_csv().
# Можно также передавать пользовательские имена заголовков
# при чтении CSV-файлов через атрибут names метода read_csv().
# Наконец, для записи CSV-файла с помощью Pandas
# сначала необходимо создать объект Pandas DataFrame,
# а затем вызвать метод to_csv() у DataFrame.
