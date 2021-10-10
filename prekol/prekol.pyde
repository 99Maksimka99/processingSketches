x=30
x=30
def setup():
    size(500,500)
def draw():
    global x
    translate(250,250)
    rotate(radians(x))
    line(0,0,100,100)
    x+=1

    
