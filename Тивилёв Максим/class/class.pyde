photo=0
class Student():
    
    def info (self,coll, n, a, u,z):
        self.name=n
        self.group=a
        self.us=u
        self.grades=z

        coll.name=n
        coll.group=a
        coll.us=u
        coll.grades=z
def setup():
    global photo
    size(100, 110)
    photo = loadImage("garri.jpg")
    #Студенты
    
    pers1=Student("Max", "3", 4.89, 5)
    pers2=Student("Jeanne", "2", 4.67, 3)
    pers3=Student("Lena", "3", 3.99, 2)
    pers4=Student("Alex", "1", 4.83, 4)
    pers5=Student("Alex", "2", 4.93, 3)
    pers6=Student("Yana", "2", 4.78, 3)
    pers7=Student("Kolya", "1", 4.88, 5)
    pers8=Student("Vika", "3", 4.64, 3)
    pers9=Student("nastya", "1", 4.67, 5)
    pers10=Student("Kirill", "2", 5, 3)
f=[]
f.append(pers1)
f.append(pers2)
f.append(pers3)
f.append(pers4)
f.append(pers5)
f.append(pers6)
f.append(pers7)
f.append(pers8)
f.append(pers9)
f.append(pers10)  
def draw():
    global photo,coll
    image(photo, 0, 0, 60, 70)
    text("There is" + coll.name,70,80)
    text("which is now in" + coll.group,80,90)
    text("the group, and its average score"+coll.us,90,100)
    text("algebra grades" + coll.grades,100,110)
    
        
def info(self):
        print("There is",self.name,"which is now in",self.group,"the group, and its average score",self.us,"algebra grades",self.grades)
    
#Студенты
pers1=Student("Max", "3", 4.89, 5)
pers2=Student("Jeanne", "2", 4.67, 3)
pers3=Student("Lena", "3", 3.99, 2)
pers4=Student("Alex", "1", 4.83, 4)
pers5=Student("Alex", "2", 4.93, 3)
pers6=Student("Yana", "2", 4.78, 3)
pers7=Student("Kolya", "1", 4.88, 5)
pers8=Student("Vika", "3", 4.64, 3)
pers9=Student("nastya", "1", 4.67, 5)
pers10=Student("Kirill", "2", 5, 3)

f=[]
f.append(pers1)
f.append(pers2)
f.append(pers3)
f.append(pers4)
f.append(pers5)
f.append(pers6)
f.append(pers7)
f.append(pers8)
f.append(pers9)
f.append(pers10)
#print('Привет,я',pers.name,',обучаюсь в',pers.group,',моя успеваемость',pers.us,'оценка',pers.grades)


for i in range(len(f)):
    if f[i].us >= 3:
        f[i].info()
