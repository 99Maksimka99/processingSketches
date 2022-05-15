x=100
x2=300
y=200
y2=200
photo1=0
photo2=0
def setup(): 
    global photo1,photo2
    size(600,600)
    photo1=loadImage("tank1.jpg")
    photo2=loadImage("tank2.jpg")
def draw():
    background(0,128,0)
    global photo1,photo2,x,x2,y,y2
    image(photo1,x,y,100,100)
    image(photo2,x2,y2,100,100)
    if keyPressed and key == 'w':
        y-=2
    if keyPressed and key == 'd':
        x+=2
    if keyPressed and key == 's':
        y+=2
    if keyPressed and key== 'a':
       x-=2
    if keyPressed and keyCode == UP:
        y2-=2
    if keyPressed and keyCode == RIGHT:
        x2+=2
    if keyPressed and keyCode == DOWN:
        y2+=2
    if keyPressed and keyCode == LEFT:
       x2-=2
    if x<=x1+100 and y<=y1+100 and x>=x1 and y>=y1:
        exit()
        
    
