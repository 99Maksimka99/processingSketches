angle=10
enter=10
def setup():
    size(500,500)
    frameRate(100)
def draw():
    global angle,enter
    background(random(0,255))
    push()
    translate(300,300)
    rotate(radians(angle))
    fill(random(0,255),random(0,255),random(0,255))
    rect(0,0,20,20)
    pop()
    angle-=1
    push()
    translate(250,250)
    rotate(radians(enter))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(0,0,50,20)
    pop()
    enter+=1

    
