#Переменные
x =10
y =0 #инициализация переменных
xel = 100
yel = 100
sizexel=30
sizeyel=90
def setup():
    size(600,400)
    frameRate(50)
    strokeWeight(5)
def draw():
    global x,y,xel,yel,sizexel,sizeyel #объявление переменной
    background(0,240,40)
    point(x,y)
    y+=1
    if y == 400:
        y-=1
    
    
    
