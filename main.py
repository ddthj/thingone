
'''
Diabetes tracker by raiz and goose

Disclaimer - does not actually track diabetes

v1.1
'''

from datetime import date




def readFile(file):
    data = []
    file = open(file,'r')
    for item in file:
        data.append(day(item))
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
    def __init__(self,men):
        self.date = maketime()

        self.codeRed = 0
        self.voltage = 0
        self.regular = 0
        if len(men) >0:
            bloke = men.split(";")
            self.date = bloke[0]
            self.codeRed = int(bloke[1])
            self.voltage = int(bloke[2])
            self.regular = int(bloke[3])
    def tostring(self):
        bigboi = ""
        bigboi += self.date + ","
        bigboi += str(self.codeRed) + ","
        bigboi += str(self.voltage) + ","
        bigboi += str(self.regular) + "\n"
        return bigboi
        
    def add(self,x):
        if x == "1":
            self.codeRed += 1
        elif x == "2":
            self.voltage += 1
        elif x == "3":
            self.regular += 1

print("1: Code red\n2: Voltage\n3: Regular")

try:
    days = readFile("diabetes.dat")
except Exception as e:
    print(e)
    days = []
    #print("no file found")

running = True
while running:
    legit = True
    while legit:
        
        a = input(">")
        
        if a == "1" or a == "2" or a == "3":
            legit = False
            break
        elif a == "save":
            running = False
            legit = False
            break
        
        print("stupid")

    flag = True

    for d in days:
        if d.date == time:
            flag = False
            d.add(a)


    if flag:
        newday = day("")
        newday.add(a)
        #print(newday.tostring())
        days.append(newday)

someboi = []
for some in days:
    someboi.append(some.tostring())

print(someboi)
    
writeFile(someboi,"diabetes.dat")
