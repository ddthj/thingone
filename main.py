<<<<<<< HEAD
'''hi'''
=======
'''
Diabetes tracker by raiz and goose

Disclaimer - does not actually track diabetes

v1.0
'''

from datetime import date




def readFile(file):
    data = []
    file = open(file,'r')
    for item in file:
        data.append(item)
    return data

def writeFile(data, file):
    f = open(file,'w')
    for item in data:
        f.write(item)
    f.close()
        

def maketime():
    x = ""
    x += str(date.today().year)
    x += str(date.today().month)
    x += str(date.today().day)
    return x

time = maketime()

class day():
    def __init__(self):
        self.date = maketime()

        self.codeRed = 0
        self.voltage = 0
        self.regular = 0
        
    def add(self,x):
        if x == "1":
            self.codeRed += 1
        elif x == "2":
            self.voltage += 1
        else:
            self.regular += 1

print("1: Code red\n2: Voltage\n3: Regular")

legit = True
while legit:
    
    a = input(">")
    
    if a == "1" or a == "2" or a == "3":
        legit = False
        break
    
    print("stupid")


try:
    days = readFile("diabetes.dat")
    print(day)
except Exception as e:
    print(e)
    days = []
    print("no file found")

flag = True

for day in days:
    if day.date == time:
        flag = False
        day.add(a)


if flag:
    day = day()
    day.add(a)
    #days.append(newDay)


writeFile(days,"diabetes.dat")
>>>>>>> 7337a1155e0222504513d3dfc6d7fa4ae196e935
