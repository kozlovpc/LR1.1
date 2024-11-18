# print("Задача 1")
# print("Задание 1")
#
import itertools
import random
from os.path import isabs

# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
# third = int(input("Введите третье число: "))
# resNegative = 0
# for i in first, second, third:
#     if i<0:
#         resNegative+=1
#
# print("Колличество отрицательных чисел равно: ",resNegative)
#
# print("Задание 2")
# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
# third = int(input("Введите третье число: "))
#
# if first == third:
#     print("Первое и третье")
# elif first == second:
#     print("Первое и второе")
# elif second == third:
#     print("Второе и третье")
# else:
#     print("Нет таких чисел")
#
# print("Задание 3")
# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
# third = int(input("Введите третье число: "))
# resGeometr = (first * second* third)**(1/3)
# print("Среднее геометрическое этих чисел равно:",round(resGeometr,2))

# print("Задание 4")
#
# mounthYear = {"Зима":[1,2,12],
#               "Весна":[3,4,5],
#               "Лето":[6,7,8],
#               "Осень":[9,10,11]}
# key = int(input("Введите число месяца (от 1 до 12) "))
# for i in mounthYear.values():
#     if key in i:
#         res = next((key for key,value in mounthYear.items() if value==i),None)
# print(res)
#
# print("Задание 5")
#
# chetnoe = [int(input()) for i in range(4)]
# for i in chetnoe:
#     if i%2!=0:
#         print(i," является нечётным числом")

# print("Задание 6")
#
# threeVal = int(input("Введите трёхзначное число: "))
# threeVal = list(map(int,list(str(threeVal))))
# test = False
# for i in threeVal:
#     if i==0 or i==9:
#         test = True
# if(test):
#     print("Есть")
# else:
#     print("Нет")

# print("Задание 7")
#
# yearTest = int(input("Впишите пожалуйста год который хотите узнать: "))
#
# if yearTest %4 == 0 or yearTest%400==0:
#     print("Год является високосным")
# elif yearTest %100 == 0:
#     print("Год не является високосным")
# else:
#     print("Год не является високосным")

# print("Задание 8")
#
# testFour = list(map(int,list(input())))
# if(len(set(testFour))==4):
#     print("Повторяющихся чисел нет")
# else:
#     print("Повторяющиеся числа есть")

# print("Задание 9")
#
# chislitel = int(input("Введите числитель "))
# znamenatel = int(input("Введите знаменатель "))
# if chislitel<znamenatel:
#     print("Дробь правильная")
# else:
#     print("Дробь неправильная")

# print("Задание 10")
#
# threeSum = list(map(int,list(input("Введите трёхзначное число"))))
# if(sum(threeSum)%3==0):
#     print("Число делиться на 3")
# else:
#     print("Число не делиться на 3")

# print("Задание 11")
# first = int(input("Введите первое число: "))
# second = int(input("Введите второе число: "))
# third = int(input("Введите третье число: "))
# resMax = max(first, second, third)
# print(resMax)
#
# print("Задание 12")
# testTwo = list(map(int,list(input())))
# testBool = False
# for i in testTwo:
#     if i==1 or i==9:
#         testBool = True
# if testBool:
#     print("Есть")
# else:
#     print("Нет")
# print("Задание 13")
#
# inside = int(input())
#
# if inside not in range(11,20):
#     if inside%10==1:
#         print(f"мы нашли {inside} гриб в лесу")
#     elif inside%10==2 or inside%10==3 or inside%10==4:
#         print(f"мы нашли {inside} гриба в лесу")
#     else:
#         print(f"мы нашли {inside} грибов в лесу")
# else:
#     print(f"мы нашли {inside} грибов в лесу")
#
# print("Задание 14")
# inside = int(input())
#
# if inside not in range(11,20):
#     if inside%10==1:
#         print(f"Мне {inside} год")
#     elif inside%10==2 or inside%10==3 or inside%10==4:
#         print(f"Мне {inside} года")
#     else:
#         print(f"Мне {inside} лет")
# else:
#     print(f"Мне {inside} лет")

# print("Задание 15")
#
# chetnoe = [int(input()) for i in range(4)]
# for i in chetnoe:
#     if i%2==0:
#         print(i," является чётным числом")
# print("Задание 16")
#
# resDict = {0:"Ноль",1:"Один",2:"Два",3:"Три",4:"Четыре",5:"Пять",6:"Шесть",7:"Семь"}
#
# test = int(input())
# try:
#     print(resDict[test])
# except SyntaxError:
#     print("Ошибка")
# except KeyError:
#     print("Ошибка")

# print("Задание 2 Общее")
#
# print("Задание 1")
# test = False
# for i in range(100000,999998):
#     if sum(list(map(int,list(str(i)))))%7==0 and sum(list(map(int,list(str((i+1))))))%7==0:
#         test = True
#         print(list(map(int, list(str(i)))),list(map(int, list(str((i + 1))))))
#         print(sum(list(map(int, list(str(i))))), sum(list(map(int, list(str((i + 1)))))))
# if(test):
#     print("Могут")
#
# else:
#     print("Не могут")

# print("Задание 2")
#
# testSum = int(input("Укажите сумму реализации"))
#
# testDay = int(input("Введите заданное значение"))
# days = 0
# while testSum<testDay:
#     testSum = round((((testSum/100)*3) + testSum),2)
#     days += 1
# print(testSum)
# print(days)
# print("Задание 3")
# testCounter = int(input("Задаёте колличество учеников в классе"))
# schoolClass = [[(random.choice(['М','Ж'])),(random.randrange(2007,2009)),(random.randrange(160,200)),(random.randrange(20,200))] for i in range(testCounter)]
# boys = 0
# girls = 0
# sumBoys = 0
# sumGirls = 0
# testTall = 0
# testSmallgirl = 200
# testYearGirl = 0
# minYearGirl = 2000
# boyWeigth = 0
# maxWeigth = 0
# for i in schoolClass:
#     print(i[0])
#     if i[0]=="М":
#         boys+=1
#         sumBoys+=i[1]
#         if testTall<i[2]:
#             testTall=i[2]
#             boyWeigth = i[3]
#         if maxWeigth<i[3]:
#             maxWeigth=i[3]
#     elif i[0]=="Ж":
#         girls+=1
#         sumGirls += i[1]
#         if testSmallgirl>i[2]:
#             testSmallgirl=i[2]
#             testYearGirl = i[1]
#         if minYearGirl < i[1]:
#             minYearGirl = i[1]
# print(f"В классе {boys} мальчиков и {girls} девочек")
# print(f"Средний возраст мальчиков является {2024-(sumBoys/boys)}, а средний возраст девочек является {2024 -(sumGirls/girls)}")
# if maxWeigth==boyWeigth:
#     print(f"Самый высокий рост мальчика {testTall} но при этом его вес {boyWeigth} кг является макисмальным среди мальчиков")
# else:
#     print(f"Максимальный вес среди мальчиков является {maxWeigth} при условии что вес самого высокого является {boyWeigth}")
#
# if testYearGirl==minYearGirl:
#     print(f"Рост самой низкой девочки является {testSmallgirl} и она будет самой юной среди девочек с возрастом {2024-testYearGirl}")
# else:
#     print(f"Минимальный возраст является {2024-minYearGirl} при этом возраст самой маленькой девочки {2024-testYearGirl}")
#
#
# print("Задание 4")
#
# resultSum = 0
#
# yearBuy = int(input("Введите пожалуйста в течении скольких лет закупалось оборудование: "))
# countOfEquipment = int(input("Введите пожалуйста колличество оборудования: "))
# percentOfObsolescence = int(input("Введите пожалуйста процент устаревания оборудования: "))
#
# testEquipment = [int(input(f"Введите пожалуйста цену оборудования номер {i+1}: ")) for i in range(countOfEquipment)]
# readyEquipment = [0 for i in range(countOfEquipment)]
# prebuildSum = [0 for i in range(countOfEquipment)]
# resultSum = [0 for i in range(countOfEquipment)]
# for y in range(yearBuy-1):
#     for j in range(yearBuy - y):
#         for q in range(len(readyEquipment)):
#             test = round(float(percentOfObsolescence)/float(100),1)
#             test = (1 - test)**(j)
#             readyEquipment[q] = round(testEquipment[q]*test,1)
#     resultSum = [x+y for x,y in zip(resultSum, readyEquipment)]
# for i in range(len(resultSum)):
#     resultSum[i] += testEquipment[i]
#
# for i in range(len(readyEquipment)):
#     print(f"Цена всего закупленного оборудования номер {i+1} будет равна {round(resultSum[i],2)}")
#
# print("Остальные доделать")


print("Задача 3")

print("Задание 4")

testCount = int(input("Введите колличество чисел: "))
a = [random.randrange(0,99) for i in range(testCount)]
print(f"Минимальное число равно {min(a)}")




