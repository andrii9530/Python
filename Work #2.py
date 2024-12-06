#Додаємо для роботи з часом
import time

# Наш декоратор для додавання можливості підрахунку часу виконання функції getnumber
def myDecorator(func):
    def embrace(*a):
        # Вираховуємо до початку
        timeS = time.time()
        # 
        res = func(*a)
        # Та після закінцення
        timeE = time.time()
        # Виводимовре кінцевий результат
        print(f"Час виконання обрахунку {timeE - timeS}")
        return res
    return embrace

# Додаємо нові властивості до функції по підрахунку кількості парних чисел
@myDecorator
def getnumber():
    rez = []
    i = 0
    while i <= 100000:
        if i % 2 == 0:
            rez.append(i)
        i += 1
    return rez

numbers = getnumber()
print(len(numbers))
