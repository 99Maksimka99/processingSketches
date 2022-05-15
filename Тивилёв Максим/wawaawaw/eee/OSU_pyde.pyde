from snegovik import snegovik
def setup():
    size(600,400)
    frameRate(10000)
def draw():
    background(255)
    
    snegovik
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
