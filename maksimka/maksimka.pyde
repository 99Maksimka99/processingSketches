#Переменные
x =10
y =0 #инициализация переменных
xel = 100
yel = 100
sizexel=30
sizeyel=90
mode = "вправо"
def setup():
    size(600,400)
    frameRate(50)
    strokeWeight(5)
def draw():
    global x,y,xel,yel,sizexel,sizeyel,mode #объявление переменной
    background(0,240,40)
    point(x,y)
    y+=1
    if y == 400:
        y-=1
    if mousePressed == True:
        fill(random(0,255),random(0,255),random(0,255))
    if mousePressed == False:
        if x >=600:
            mode="влево"
        if x<=0:
            mode="вправо"
        if mode == "вправо":
            x=x+20
        if mode == "влево": 
            x=x-20
    
    
    
