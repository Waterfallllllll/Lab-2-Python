# N1

import csv

# Чтение данных из исходного CSV-файла с кодировкой 'cp1251'
with open('dataset.csv', 'r', encoding='cp1251') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Разделение данных на даты и данные
dates = []
values = []

for row in data:
    # Проверка, что строка содержит достаточно элементов
    if len(row) >= 2:
        dates.append(row[0])
        # Сохраняем все данные после запятой
        data_values = ','.join(row[1:])
        values.append(data_values)

# Пишем даты в X.csv
with open('X.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for date in dates:
        writer.writerow([date])

# Пишем данные в Y.csv
with open('Y.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for value in values:
        writer.writerow([value])

# N2

import csv
from datetime import datetime
import sys

# Открываем файл для записи стандартного вывода
sys.stdout = open('output.txt', 'w')

# Читаем данные из исходного CSV файла
with open('dataset.csv', 'r') as csvfile:
    # Считываем все строки из файла и удаляем пустые строки
    data = [row for row in csvfile.readlines() if row.strip()]

# Создаем словарь для хранения данных, где ключ - это год, а значение - это строки данных
data_by_year = {}

# Парсим и собираем даты из исходных данных
for row in data:
    date_str = row.split(',')[0]
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        year = date_obj.year
        if year not in data_by_year:
            data_by_year[year] = []
        data_by_year[year].append(row)
    except ValueError:
        print(f"Неверный формат даты в строке: {date_str}")
        continue

# Записываем данные в файлы по годам с учетом дня и месяца
for year, data in data_by_year.items():
    # Находим первую и последнюю дату для данного года
    min_date = min(data, key=lambda x: datetime.strptime(x.split(',')[0], '%d.%m.%Y'))
    max_date = max(data, key=lambda x: datetime.strptime(x.split(',')[0], '%d.%m.%Y'))
    start_date = datetime.strptime(min_date.split(',')[0], '%d.%m.%Y').strftime('%Y%m%d')
    end_date = datetime.strptime(max_date.split(',')[0], '%d.%m.%Y').strftime('%Y%m%d')
    
    # Формируем имя файла в формате "годмесяцдень_годмесяцдень.csv"
    filename = f'{start_date}_{end_date}.csv'
    
    # Записываем данные в файл
    with open(filename, 'w', newline='') as csvfile:
        csvfile.writelines(data)

    print(f"Файл {filename} создан успешно.")

# Закрываем файл для записи стандартного вывода
sys.stdout.close()

# Восстанавливаем стандартный вывод
sys.stdout = sys.__stdout__

# N3

import csv
from datetime import datetime, timedelta
import sys

# Открываем файл для записи стандартного вывода
sys.stdout = open('output.txt', 'w')

# Читаем данные из исходного CSV файла
with open('dataset.csv', 'r') as csvfile:
    # Считываем все строки из файла и удаляем пустые строки
    data = [row for row in csvfile.readlines() if row.strip()]

# Создаем словарь для хранения данных, где ключ - это номер недели, а значение - это строки данных
data_by_week = {}

# Парсим и собираем даты из исходных данных и группируем их по неделям
for row in data:
    date_str = row.split(',')[0]
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        week_number = date_obj.isocalendar()[1]  # Получаем номер недели в году
        if week_number not in data_by_week:
            data_by_week[week_number] = []
        data_by_week[week_number].append(row)
    except ValueError:
        print(f"Неверный формат даты в строке: {date_str}")
        continue

# Записываем данные в файлы по неделям с учетом первой и последней даты в неделе
for week_number, data in data_by_week.items():
    # Находим первую и последнюю дату для данной недели
    week_start = datetime.strptime(data[0].split(',')[0], '%d.%m.%Y')
    week_end = datetime.strptime(data[-1].split(',')[0], '%d.%m.%Y')

    # Формируем имя файла в формате "годмесяцдень_годмесяцдень.csv"
    start_date = week_start.strftime('%Y%m%d')
    end_date = week_end.strftime('%Y%m%d')
    filename = f'{start_date}_{end_date}.csv'
    
    # Записываем данные в файл
    with open(filename, 'w', newline='') as csvfile:
        csvfile.writelines(data)

    print(f"Файл {filename} создан успешно.")

# Закрываем файл для записи стандартного вывода
sys.stdout.close()

# Восстанавливаем стандартный вывод
sys.stdout = sys.__stdout__

# N4

import csv
from datetime import datetime

def get_data_from_csv(date):
    with open('dataset.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # Проверяем, что в строке есть достаточно элементов для обработки
            if len(row) >= 4:
                row_date = datetime.strptime(row[0], '%d.%m.%Y')
                if row_date == date:
                    return row[1:]  # Возвращаем все элементы, начиная со второго
    return None

date_str = '01.09.2023'
date = datetime.strptime(date_str, '%d.%m.%Y')

# Вызываем функцию и получаем данные для заданной даты
data = get_data_from_csv(date)

if data:
    print(f"Данные для {date_str}: {data}")
else:
    print(f"None")