x=350
y=200
spisok = [['blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','white','white','blue','blue','white','white','white','white','white'],
        ['blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','white','white','blue','blue','white','blue','blue','blue','blue'],
        ['blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','white','white','blue','blue','white','white','white','blue','blue'],
        ['blue','blue','blue','blue','white','white','white','blue','blue','blue','blue','white','white','blue','blue','blue','blue','white','blue','blue'],
        ['blue','blue','blue','blue','white','blue','white','blue','blue','blue','blue','white','white','white','blue','blue','blue','white','blue','blue'],
        ['blue','blue','blue','blue','white','blue','white','blue','blue','blue','blue','white','blue','white','white','white','blue','white','blue','blue'],
        ['white','white','white','white','white','blue','white','blue','blue','blue','blue','white','blue','blue','blue','white','blue','white','blue','blue'],
        ['white','blue','blue','blue','blue','blue','white','blue','blue','blue','white','white','blue','blue','blue','white','blue','white','blue','blue'],
        ['white','white','blue','blue','blue','blue','white','white','blue','blue','white','blue','blue','blue','blue','white','white','white','blue','blue'],
        ['blue','white','white','blue','blue','blue','blue','white','blue','blue','white','blue','blue','blue','blue','blue','blue','blue','blue','blue'],
        ['blue','blue','white','blue','blue','blue','blue','white','blue','blue','white','blue','blue','blue','blue','blue','blue','blue','blue','blue'],
        ['blue','white','white','blue','blue','blue','blue','white','blue','white','white','blue','blue','blue','blue','blue','blue','blue','blue','blue'],   
        ['blue','white','blue','blue','blue','blue','blue','white','white','white','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue'],     
        ['blue','white','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue'],           
        ['white','white','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue','blue']]                    
numRyad = len(spisok)
numStolbets = len(spisok[0]) 

def setup():
    size(600,400)

def draw():
    global spisok,finRyad, finStolbets, x,y,xel,yel
    for nRyada in range(numRyad): 
    
        for nStolbtsa in range(numStolbets):
            if spisok[nRyada][nStolbtsa] == 'blue':
                fill(0,0,255)
            if spisok[nRyada][nStolbtsa]=='white':
                fill(255)
            if x>=nStolbtsa*30 and x<=nStolbtsa*30+30 and y>=nRyada*30 and y<=nRyada*30+30:
                if spisok[nRyada][nStolbtsa] == 'blue':
                    exit()
            
           
        
            rect(nStolbtsa*30,nRyada*30,30,30)


    fill(255,0,0)
    ellipse(x,y,10,10)


           
            
       



    
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
    if key==CODED:
        if keyCode==ENTER:
            background(0)
