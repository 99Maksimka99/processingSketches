
x=10
def setup():
    size(500,500)
def draw():
    global x
    background(255) 
    stroke(random(0,255),random(0,255),random(0,255))
    translate(250,250)
    rotate(radians(x))
    line(0,0,x,100)
    x+=1

    
