def readFile(filename):
    f = open(filename,"r")
    lines = f.readlines()
    f.close()
    return lines

def saveFile(filename,string):
    f = open(filename,"a")
    f.write(string)
    f.close()