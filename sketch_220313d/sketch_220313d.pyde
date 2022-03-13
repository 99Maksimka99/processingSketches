pole = [['white','white','white','white','white'],
        ['white','white','white','white','white'],
        ['white','white','white','white','white'],
        ['white','white','white','white','white']]



numRyad = len(pole)
numStolbets = len(pole[0]) 
def setup():
    size(600,400)
    
def draw():
    
    global pole,finRyad, finStolbets
    for nRyada in range(numRyad): 
    
        for nStolbtsa in range(numStolbets):
           
            if pole[nRyada][nStolbtsa] == 'white':
                fill(255, 0, 0)
            if mousePressed==True:
                if mouseX>nStolbtsa+30 and mouseY>nStolbtsa+30+30:
                    pole[nRyada][nStolbtsa] = 'black'
                    fill(0,255,0)
       
            rect(nStolbtsa*30,nRyada*30,30,30)
