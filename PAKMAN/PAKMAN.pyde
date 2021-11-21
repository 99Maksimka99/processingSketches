x=300
y=200


def setup():
    size(600,400)
    frameRate(10000)
def draw():
    global x,y,xel,yel
    background(255)
    ellipse(x,y,10,10)
    fill(255,255,0)



    
def keyPressed():
    global x,y
    if key == CODED:
        if keyCode==RIGHT:
            x=x+1
        if keyCode==DOWN:
            y=y+1
        if keyCode==LEFT:
            x=x-1
        if keyCode==UP:
            y=y-1


        
        
