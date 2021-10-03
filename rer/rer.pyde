#Переменные
x = 100
y = 200 #инициализация переменных
xel = 100
yel = 100
sizexel=30
sizeyel=90
def setup():
    size(900,800)
    frameRate(5)
    strokeWeight(5)
def draw():
    global x,y,xel,yel,sizexel,sizeyel #объявление переменной
    background(0,240,40)
    point(x,y)
    ellipse(xel,yel,sizexel,sizeyel)
    y+=1

    
    
