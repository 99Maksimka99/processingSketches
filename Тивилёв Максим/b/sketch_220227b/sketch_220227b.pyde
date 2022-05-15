tasks=[u'поспать',u'покушать',u'пойти гулять']
inputKey=u''
def setup():
    size(600,400)
def draw():
    global inputKey, tasks
    background(0)
    text(inputKey,20,40)
    for l in tasks:
        fill(random(200,255),random(200,255),random(200,255))
        text(l,60,40)
        translate(0,30)
def keyPressed():
    global inputKey, tasks
    if key!=CODED and key!=ENTER and key!=RETURN and key!=BACKSPACE:
        inputKey= inputKey + key
    elif key==ENTER or key==RETURN:
         tasks.append(inputKey)
         inputKey=u''
    elif key==BACKSPACE:
        if len(tasks)>0:
            poslednyy=len(tasks)-1
            del tasks[poslednyy]
    
