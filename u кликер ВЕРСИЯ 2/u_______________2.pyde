pipyka = 0
lotus=30
def setup():
    size(500,500)
    ellipseMode(CENTER)
    rectMode(CENTER)
    frameRate(10)
def draw():
    global pipyka,lotus
    fill(255)
    background(126)
    textSize(15)
    fill(0)
    ellipse(250,250, 100,100)
    textSize(25)
    text(pipyka,10,25)
    textSize(25)
    text(lotus,10,50)
    lotus= lotus-1
    if pipyka>30:
        background(255)
        text("You survived:(",200,250)
    if lotus <0:
        background(0)
        fill(250,0,0)
        text("You died;)",200,250)
    
def mouseClicked():
    global pipyka

    xDif=250-mouseX
    yDif=250-mouseY
    if sqrt(xDif*xDif+yDif*yDif)<50:
        pipyka=pipyka +1

      
    
