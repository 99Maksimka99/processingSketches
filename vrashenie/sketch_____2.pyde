angle=0
#rotate(radians(30)) поворачивает систему координата на 30 градусов относительно начала координата
#чтобы вращать фигуру относительно её центра
#1. с помощью translate сместить начало координата в центре фигуры
#3.rotate -поворот системы координат
#3. нарисовать фигуры в начале координат  в новой системе
def setup():
    size(500,500)
    frameRate(100)
def draw():
    background(0,0,0)
    global angle
    rotate(radians(angle))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(500/2,500/2,50,20)
    rect(80,40,20,20)
    angle+=1
