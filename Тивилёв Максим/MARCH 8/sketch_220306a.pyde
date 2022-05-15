photo1=0
photo2=0
photo3=0
photo4=0
photo5=0
March= []
def setup():
    global photo1,photo2,photo3,photo4,photo5, March
    size(600,600)
    photo1=loadImage("garri.jpg")
    photo2=loadImage("1March8.jpg")                
    photo3=loadImage("2March8.jpg")
    photo4=loadImage("3March8.jpg")
    photo5=loadImage("troll.jpg")
    March.append(photo1)
    March.append(photo2)
    March.append(photo3)
    March.append(photo4)
    March.append(photo5)
def draw():
    #background(0)
    global March,photo1 , photo2 , photo3 , photo4 , photo5
def keyPressed():
    global photo1 , photo2 , photo3 , photo4 , photo5,March
    for i in range(len(March)):
        if key==str(i+1):
            image(March[i],0,0,600,600)
        


                
