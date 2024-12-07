citi1 = {"Рівне","Костопіль","Київ","Житомир","Львів"}
citi2 = {"Рівне","Березне","Костопіль","Сарни","Житомир","Львів"}
citi3 = citi2.intersection(citi1)
print(citi3)
citi3 = citi1.difference(citi2)
print(citi3)
citi3 = citi2.difference(citi1)
print(citi3)

print("Четверте завдання")
def getnumber(a,b):
    i = a
    while i < b:
        if i % 2 == 0 and i >= a and i <= b:
            yield i
        i += 1
for i in getnumber(2,9):
    print(i)


print("П'яте завдання")
number = [3,4,5,8,1,35,578,234,4]
def getnumber(a,b, num):
    for i in num:
        if i > a and i < b:
            yield i
        i += 1

for i in getnumber(2,9,number):
    print(i)       