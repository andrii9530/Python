# Це для затримок в роботі*
import time
# Це щоб очищати термінал
import os

os.system('clear')

# Перше та друге завдання
print("-----Перше завдання у поєднанні з другим-----")

# Водимо назву фрукта
f = input("Ведіть фрукт клькіст якого бажаєте дізнатись: ")

# Котедж з фруктами
Fruits = ("banana","cherry","Orange","cherry","Orange","bananac")

# Лічильник
num = 0

for i in Fruits:
    if f == i or f in i:
        num += 1
print(f"В списку {num} {f}")
time.sleep(1)
os.system('clear')


# третє завдання
print("----------------Третє завдання----------------")

# Котедж з Автомобілями
Cars = ("Volkswagen","Tesla","Volkswagen","Toyota","Volkswagen","BMW")



print("Всі доступні автомарки для заміни")
for i in Cars:
        print(i, "\t")

car = input("Яку бажаєте змінити? ")
newCar = input("На яку бажаєте змінити? ")
Cars = list(Cars)

num = 0
for i in Cars:
    num += 1
    if i == car:
        Cars[num - 1] = newCar

Cars = tuple(Cars)

for i in Cars:
        print(i, "\t")
time.sleep(3)
os.system('clear')

# Чeтверте завдання
print("------------Четверте завдання--------------")

numbers = (45, 578, 6643, 1234409857)
num = 0
for i in numbers:
        i = str(i)
        num += 1
        print(f"Цифра {num} Має {len(i)} елементи")

