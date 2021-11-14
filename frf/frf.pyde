def setup():
    size(600,400)
    background(100)
def draw():
    background(204)

    if mousePressed== True:
        rect(mouseX,mouseY,300,200)
    if mousePressed==False:
        rect(300,200,50,50)
        fill(255,0,0)
 
    
