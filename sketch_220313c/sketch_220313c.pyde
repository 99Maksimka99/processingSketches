spisok=[['white','white','white','white','white'],
        ['white','white','white','white','white'],
        ['white','white','white','white','white'],
        ['blue','blue','blue','blue','blue'],
        ['blue','blue','blue','blue','blue'],
        ['blue','blue','blue','blue','blue'],
        ['blue','blue','blue','blue','blue'],
        ['red','red','red','red','red'],
        ['red','red','red','red','red'],
        ['red','red','red','red','red']]
numRyad = len(spisok) 
numStolbets = len(spisok[0])
def setup():
    size(600,600)
def draw():
    global finRyad,finStolbets
    for nRyada in range(numRyad): 
    
        for nStolbtsa in range(numStolbets):
        
            if spisok[nRyada][nStolbtsa] == 'red':
                fill(255, 0, 0)
            if spisok[nRyada][nStolbtsa] == 'blue':
                fill(0,0,255)
            if spisok[nRyada][nStolbtsa]=='white':
                fill(255)
            rect(nStolbtsa*30,nRyada*30,30,30)
