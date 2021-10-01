x = 20 #Переменныя
def setup():
    size(400,600)
def draw():
    background(100)
    global x
    ellipse(x,20,20,20)
    x=x+1
        
