from abc import ABC
# Це щоб очищати термінал
import os
# Це щоб було краще)
import time


# Клвсна робота
class Passport(ABC):
    initial_number = 1

    def __init__(self,Surname,Name,Parents,Country,DateOfBirth,ValidUntil) -> None:
        self.surname = Surname
        self.name = Name
        self.parents = Parents
        self.country = Country
        self.dateOfBirth = DateOfBirth
        self.validUntil = ValidUntil

        self.nymber = Passport.initial_number
        Passport.initial_number += 1


class ForeignPassport(Passport):
    def __init__(self,visa,foreignnumber,Surname,Name,Parents,Country,DateOfBirth,ValidUntil) -> None:
        super().__init__(Surname,Name,Parents,Country,DateOfBirth,ValidUntil)
        self.visa = visa
        self.foreignnumber = foreignnumber

    def __str__(self) -> str:
        return f"{self.surname}: {self.name}: {self.parents}: {self.country}: {self.dateOfBirth}: {self.validUntil}"

    
    def date(self):
        print(f"Прізвище {self.surname}\nІм\'я {self.name}\nПо батькові {self.parents}\nКраїна {self.country}\nДата народженя {self.dateOfBirth}\nДійсний до {self.validUntil}")

    def addVisa(self,newVisa):
        self.visa.append(newVisa)
        print(f"Віза {newVisa} Успішно додана")

    def removeVisa(self,nameVisa):
        if nameVisa in self.visa:
            self.visa.remove(nameVisa)
            print(f"Віза {nameVisa} Успішно Видаленна")
        else:
            print("Такої візи немає")



user1 = ForeignPassport(["USA", "Canada"], "8795203039", "Майструк", "Андрій", "Володимирович", "Україна", "13.11.2005", "04.10.2034")
user1.date()

# Додавання нових віз
user1.addVisa("Germany")
user1.addVisa("France")

# Видалення віз
user1.removeVisa("USA")
user1.removeVisa("Japan")  # Спроба видалення неіснуючої візи

# Виведення всіх віз після змін
print("Список віз:", user1.visa)


time.sleep(3)
os.system('cls')
# Домашнє завдання з конвертацією температури
class TemperatureConverter:
    num = 0

# Конвертуєм цельсія в фарангейт
    @staticmethod
    def ctf(cel):
        TemperatureConverter.num += 1
        return cel * 9 / 5 + 32

# Конвертуєм фарангейт в цельсія
    @staticmethod
    def ftc(faht):
        TemperatureConverter.num += 1
        return (faht - 32) * 5 / 9

# Отримуємо кількість операцій
    @staticmethod
    def gettn():
        return TemperatureConverter.num

num = 1
temp = 0

while num != 0:
    num = int(input("\tМеню\n1)Конвертувати градуси цельсія в фарангейт\n2)Конвертувати градути по фарангейту в цельсія\n0)Вихід\nВиберіть дію: "))
    if num == 1:
        temp = int(input("Ведіть градуси цельсія для конвертації в фарангейт:"))
        print(TemperatureConverter.ctf(temp))
        time.sleep(1)
        os.system('cls')
    elif num == 2:
        temp = int(input("Ведіть градуси по фарангейту для конвертації в цельсія:"))
        print(TemperatureConverter.ftc(temp))
        time.sleep(1)
        os.system('cls')
    else:
        num = 0
        print("Вихід успішний")
        time.sleep(1)
        os.system('cls')
        
