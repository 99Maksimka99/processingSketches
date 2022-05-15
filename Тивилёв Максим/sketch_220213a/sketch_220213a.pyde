def setup():
    size(600,400)
def draw():
    background(0)
    global quotes
    quotes=['it is wolf ','wtf?1']
def keyPressed():
    global quotes
    if key=='1':
        text(quotes[0],200,300)
        fill(random(0,255),random(0,255),random(0,255))
    if key=='2':
        text(quotes[1],200,300)
        fill(random(0,255),random(0,255),random(0,255))
