import os

downloadsDirectory = os.path.expanduser("~/Downloads")
documentsDirectory = os.path.expanduser("~/Documents")
desktopDirectory = os.path.expanduser("~/Desktop")




def getDMGFiles(directory):
    listOfDMGFiles = []
    for path,subdirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".dmg"):
                listOfDMGFiles.append(os.path.join(path,file))
        for subdir in subdirs:
            if subdir.endswith(".dmg"):
                listOfDMGFiles.append(os.path.join(path,subdir))
        
    return listOfDMGFiles

