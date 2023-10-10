# from os import path

# print(path.curdir) // относительный путь
# print(path.abspath(".")) // Абсолютный путь к текущей папке

# from pathlib import Path

# cwd = Path(".")
# # Создали новый класс и указали путь к текущей папке

# print(cwd.absolute()) 
# # Получаем абсолютный путь к текущей папке в которой находится файл

# cwd = Path("C:/") / "Users" / "iliec" / "Desktop" / "Python" / "Django"

# print (cwd.exists())

# print (cwd.mkdir()) 
# В случае, если мы хотим создать новую папку но при этом мы должны указать путь к этому новой папке и саму папку

# cwd.rmdir() 
# Удалить папку


# test_file = open("test.txt", "w")

# test_file.write("First string\n")
# test_file.write("Second string\n")
# # Записываем 2 строки в файл при этом перезаписываем содержимое файла

# test_file.close()

# test_file = open("test.txt ")

# print(test_file.read())

# with open("test.txt", "a") as test_file:
#     test_file.write("First string\n")
#     test_file.write("Second string\n")


# # test_file = open("test.txt ")

# # print(test_file.read())

# # test_file.close()

# # with open("test.txt") as test_file:
# #     print(test_file.read())

# with open("test.txt") as test_file:
#     # lines = test_file.readlines()
#     for line in test_file:
#         print(line)

from requests_html import HTMLSession

session = HTMLSession()
rs = session.get('https://www.gismeteo.ru/diary/4980/2023/9/')
with open('rs_before_js.html', 'w', encoding='utf-8') as f:
    f.write(rs.html.html)

rs.html.render()  # Без этого не будет выполнения js кода

with open('rs_after_js.html', 'w', encoding='utf-8') as f:
    f.write(rs.html.html)



# with open("test.csv", "w") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["user_id", "user_name", "comments_qty"])
#     writer.writerow([5235, "Bogdan", 1352])
#     writer.writerow([523, "Mike", 13])
#     writer.writerow([55, "Elice", 135]) 

# with open("test.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     # for line in reader:
#     #     print(line)
#     # csv_list = list(reader)
#     # print(csv_list) 
#     for line in reader:
#         print(line)