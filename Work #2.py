#Додаємо для роботи з часом
import time
# Це щоб очищати термінал
import os

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

# Друга домашка за цю пару
os.system('cls')
thisdict = {}
# Меню
name = ""
password = ""
num = 1
text = ""
while num != 0:
    num = int(input("\tМеню\n1)Додати нового користувача\n2)Видали користувача\n3)Змінити пароль\n4)Перевірити пароль\n5)Отримати пароль (за логіном)\n6)Зберегти в файл\n0)Вийти\nВиберіть дію: "))
    if num == 1:
        # Додати нового користувача
        name = input("Ведіть логін: ")
        if len(thisdict) != 0:
            if name in thisdict:
                print("Такий користувач уже існує")
            else:
                password = input("Ведіть пароль: ")
                thisdict[name] = password
                print("Користувача додано")
                time.sleep(1)
        else:
            password = input("Ведіть пароль: ")
            thisdict[name] = password
            print("Користувача додано")
            time.sleep(1)
        os.system('cls')
    elif num == 2:
        # Видали користувача
        if len(thisdict) != 0:
            name = input("Ведіть логін користувача якого хочете видалити: ")
            if name in thisdict:
                thisdict.pop(name)
                print(f"Користувача{name} успішно було видаленно")
            else:
                print("Такого корисутача немає")

        else:
            print("Ще не було доданого користувача і в звязку з цим немає кого видаляти")
        time.sleep(3)
        os.system('cls')
    elif num == 3:
        # Змінити пароль (Має бути захищеним тобто не манше 6 символів*)
        if len(thisdict) != 0:
            name = input("Ведіть голін: ")
            if name in thisdict:
                password = input("Ведіть новий пароль: ")
                if thisdict[name] != password:
                    thisdict[name] = password
                    print("Пароль успішно змінено")
                else:
                    print("Паролі одинакові, спроба змінити пароль не є успішною")
                    time.sleep(2)
            else:
                print("Такого логіну немає")
                time.sleep(1)
        else:
            print("Ще не було доданого користувача і в звязку з цим не можна змінити пароль")
        time.sleep(3)
        os.system('cls')
    elif num == 4:
        # Перевірити паролі
        n = 0
        if len(thisdict) != 0:
            for key,password  in thisdict.items():
                if len(password) < 6:
                    print(f"Пароль {password} є незахищеним ")
                else:
                    n += 1
            if n == len(thisdict):
                print("Всі паролі є захищеними")
            time.sleep(1)
        else:
            print("Ще не було доданого користувача і в звязку з цим немає що редагувати")
        time.sleep(3)
        os.system('cls')
    elif num == 5:
        # Отримати пароль
        if len(thisdict) != 0:
            name = input("Ведіть логін користувача щоб переглянути пароль: ")
            if name in thisdict:
                print(f"Ваш пароль {thisdict[name]}")
            else:
                print("Інформацію не вдалося отримати, дані не є коректними")
            time.sleep(3)
        else:
            print("Ще не було доданого користувача і в звязку з цим немає що редагувати")
        time.sleep(3)
        os.system('cls')
    elif num == 6:
        # Зберегти в файл
        with open("text.txt", "a") as t:
            for key,password  in thisdict.items():
                t.write(f"{key}: {password}\n")
        print("Дані успішно збережено в файл text.txt")
        time.sleep(2)
        os.system('cls')
    else:
        print("Вихід успішний")
