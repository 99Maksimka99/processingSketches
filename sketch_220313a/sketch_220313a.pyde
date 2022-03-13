spisok=[['blue','blue','blue','blue','blue'],
        ['blue','blue','blue','blue','blue'],
        ['yellow','yellow','yellow','yellow','yellow'],
        ['yellow','yellow','yellow','yellow','yellow']]
numRyad = len(spisok) 
numStolbets = len(spisok[0])
def setup():
    size(600,600)
def draw():
    global finRyad,finStolbets
    for nRyada in range(numRyad): 
    
        for nStolbtsa in range(numStolbets):
        
            if spisok[nRyada][nStolbtsa] == 'yellow':
                fill(255, 255, 0)
            if spisok[nRyada][nStolbtsa] == 'blue':
                fill(0,0,255)
        
            rect(nStolbtsa*30,nRyada*30,30,30)
