x=0
mode="вправо"
def setup():
    size(600,400)
    frameRate(10)
def draw():
    global x,mode
    background(random(0,255),random(0,255),random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(x,200,40,40)
    if mousePressed == True:
        fill(random(0,255),random(0,255),random(0,255))
    if mousePressed == False:
        if x >=600:
            mode="влево"
        
        
        if x<=0:
            mode="вправо"
        if mode == "вправо":
            x=x+20
        if mode == "влево": 
            x=x-20

    
        

    
