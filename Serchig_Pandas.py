import pandas as pd

# загрузка файла в переменную file с индексацией по первой колонке
file = pd.read_excel('./asd.xlsx', index_col='device_name')
# посмотреть первые 5 строк и колонок
# print(file.head())
# в первые кавычки device_name, в кавычки внутри вторых квадратных скобок названия колонок
# print(file.loc['vmAkrikhin', ['transfered_bytes', 'time_end']])
