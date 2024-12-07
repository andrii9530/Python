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
# Запускаємо 
numbers = getnumber()
print(len(numbers))


# декоратор який ніби просто числа менше 0 змінює на 1 але на ділі це було набагато важче ніж здавалось
def overZero(func):
    def notZero(*args):
        newargs = tuple(1 if isinstance(i, int) and i < 0 else i for i in args)
        return func(newargs)
    return notZero

# Наша легка фунція по виводу інформації в обіймах декоратора
@overZero
def printN(*args):
    for i in args:
        print(i)
    return 0

printN("Привіт",2,6,-2,7,-1,0)
