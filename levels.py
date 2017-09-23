levels = {}

def addLevel(levelNum, option0, option1, option2=None, option3=None):
    global levels 

    options = []
    for option in [option0, option1, option2, option3]:
        if option != None: options=options+[option]
    
    levels[levelNum] = options

def showLevel(levelNum):
    i=1
    for level in levels[levelNum]:
        print str(i) + ':' + level 
        i+=1

    return int(raw_input('What option do you choose?\n'))

addLevel(0, 'Survive', 'Die')