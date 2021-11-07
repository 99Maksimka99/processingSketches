pipyka = 0
def setup():
    size(500,500)
    ellipseMode(CENTER)
    rectMode(CENTER)
    frameRate(60)
def draw():
    global pipyka
    fill(255)
    background(126)
    textSize(15)
    fill(0)
    ellipse(250,250, 100,100)
    textSize(25)
    text(pipyka, 10,25)
def mouseClicked():
    global pipyka 
    if mouseX >= 250 - 50 and mouseX <= 250+50 and mouseY >= 250 - 50 and mouseY <= 250+50:
        pipyka = pipyka + 1
