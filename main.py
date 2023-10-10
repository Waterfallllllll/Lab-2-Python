#first
x = int(input("Введите число от 1 до 9: "))
if x > 0 and x <=3:
    s = input("Введите строку: ")
    n = int(input("Введите число повторов строки: "))
    for i in range(n):
        print(s)
elif x > 3 and x <=6:
    m = int(input("Введите степень, в которую следует возвести число: "))        
    print(pow(x, m))
elif x > 6 and x < 9:
    for i in range(10):
        x += 1
        print(x)
else:
    print("Ошибка ввода")

#second
# print("Общество в начале XXI века")
# age = int(input("Введите свой возраст: "))
# if age >= 0 and age < 7:
#     print("Вам в детский сад")
# elif age >= 7 and age < 18:
#     print("Вам в школу")
# elif age >= 18 and age < 25:
#     print("Вам в профессиональное учебное заведение")
# elif age >= 25 and age < 60:
#     print("Вам на работу")
# elif age >= 60 and age <= 120:
#     print("Вам предоставляется выбор")
# elif age < 0 or age > 120:
#     for i in range(5):
#         print("Ошибка! Это программа для людей!")

