letters=u'поспать',u'покушать',u'пойти гулять'
inputKey=u'0'
def setup():
    size(600,400)
def draw():
    global inputKey
    background(100)
    text(inputKey,20,40)
    for letter in letters:
        fill(random(200,255),random(200,255),random(200,255))
        text(letter,60,40)
        translate(0,30)
def keyPressed():
    global inputKey
    if key!=CODED and key!=ENTER and key!=RETURN and key!=BACKSPACE:
        inputKey=key
    elif key==ENTER or key==RETURN:
        letters.append(inputKey)
    elif key==BACKSPACE:
        if len(letters)>0:
            poslednyy=len(letters)-1
            del letters[poslednyy]
    
