# import csv
# from bs4 import BeautifulSoup
# import os
# import requests

# URL = "https://www.gismeteo.ru/diary/4980/2023/9/"
# html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})

# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(html_page.text)

# with open("index.html", encoding="utf8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")

# page_temp = soup.find_all("td", class_="first_in_group positive")
# page_data = soup.find_all("td", class_="first")
# page_pressure = soup.find_all("td", class_="pressure")
# page_wind = soup.find_all("span", class_="wind")

# with open("dataset.csv", "w", encoding="utf-8") as csv_file:
#     writer = csv.writer(csv_file)
#     for date, temp, pressure, wind in zip(page_data, page_temp, page_pressure, page_wind):
#         formatted_date = f"{date.text}.09.2023"  # Добавляем месяц (09) и год (2023)
#         writer.writerow([formatted_date, temp.text, pressure.text, wind.text])

# input_numbers = input("Введите список чисел, разделенных запятыми: ")

# numbers = [int(num.strip()) for num in input_numbers.split(',')]

# total_sum = sum(numbers)

# print("Сумма введенных чисел:", total_sum)


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operator = input("Введите оператор (+, -, *, /): ")


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":

    if num2 != 0:
        result = num1 / num2
    else:
        print("Ошибка: деление на ноль невозможно.")
        result = None
else:
    print("Ошибка: неверный оператор.")
    result = None


if result is not None:
    print("Результат:", result)