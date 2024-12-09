#####################################################################
#misc

def testingThingy():
    print("BLAAAHAHAhA")
    
#####################################################################
# BASICS

def write(txt,input): # Write mode
    with open(txt, "w") as file:
        file.write(input)

def read(txt): # Read mode
    with open(txt, "r") as file:
        return file.read()

def append(txt, input): # Append mode
    with open(txt, "a") as file:
        file.append(input)
        
#####################################################################
# LISTS

def createList(txt,seperator): # Split command
    with open(txt, "r") as file:
        return txt.split(seperator)     

def split(txt,seperator):
    return createList(txt,seperator)

def writeLines(txt,lines): # Writelines
    with open(txt, "r") as file:
        file.writelines(lines)
