from abc import ABC

class Ship(ABC):
    def __init__(self,name,tyne,weight,price) -> None:
        self.tyne = tyne
        self.weight = weight
        self.name = name
        self.price = price

    def pr():
        print(f"Хаарктеристика\n {self.name} {self.tyne},\n {self.weight},\n {self.price}")

    def __str__(self):
        return f"Хаарктеристика\n {self.name} {self.tyne},\n {self.weight},\n {self.price}"


class Frigate(Ship):
    def __init__(self,speed,name,tyne,weight,price) -> None:
        super().__init__(name,tyne,weight,price)
        self.speed = speed

    def appspeed(self, sp):
        self.speed += sp

    def subspeed(self,sp):
        self.speed -= sp

class Destroyer(Ship):
    def __init__(self,fruct,name,tyne,weight,price) -> None:
        super().__init__(name,tyne,weight,price)
        self.fruct = fruct

    def setfruct():
        return Destroyer.fruct
    
class Clruiser(Ship):
    def __init__(self,power,name,tyne,weight,price) -> None:
        super().__init__(name,tyne,weight,price)
        self.power = power

    def setpower():
        return Clruiser.power
    

nvie = Frigate(23,"Абрамс","Легкий","Багато","500000")

nvie.appspeed(12)


class Airplane:
    def __init__(self,name,type,capacity,nOP):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.nOP = nOP


    def __eq__(self, other):
        return self.type == other.type

    def __add__(self, num):
        if self.capacity > self.nOP + num:
            print("Успішно додали пасажирів")
            self.nOP + num
        else:
            print("Кількість нових пасажирів є завеликою")
        return self

    def __sub__(self, num):
        if self.nOP > num:
            print("Успішно відняли пасажирів")
            return self.nOP - num
        else:
            print("Кількість пасажирів яку бажаєте забрати завеликою")
            return    

    def __iadd__(self, num):
        if self.capacity > self.nOP + num:
            print("Успішно додали пасажирів")
            self.nOP += num
        else:
            print("Кількість нових пасажирів є завеликою")
        return self


    def __isub__(self, num):
        if self.nOP > num:
            print("Успішно відняли пасажирів")
            self.nOP -= num
        else:
            print("Кількість пасажирів яку бажаєте забрати завеликою")
        return self

    def __gt__(self, other):
        return self.capacity > other.capacity
        

    def __lt__(self, other):
        return self.capacity < other.capacity
    
    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity
        
    def __str__(self):
        return f"Airplane {self.name} ({self.type}): Capacity {self.capacity}, Passengers {self.nOP}"
    
    def __int__(self):
        return self.nOP

    
    
plane1 = Airplane("Boeing 737", "Passenger", 200, 150)
plane2 = Airplane("Airbus A320", "Passenger", 180, 160)




print(plane1)  
print(plane2)

print(plane1 == plane2)

plane1 + 30 
plane1 + 50

plane2 - 50
plane2 - 200

print(plane1 > plane2)
print(plane1 <= plane2)

plane1 += 20
plane2 -= 30

print(plane1)
print(plane2)