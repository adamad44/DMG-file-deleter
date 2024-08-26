import os

#grab the downloads folder automatically so the user doesn't have to enter it
downloadsDirectory = os.path.expanduser("~/Downloads")


listOfDMGFiles = []

for path,subdirs,files in os.walk(downloadsDirectory):
    for file in files:
        if file.endswith(".dmg"):
            listOfDMGFiles.append(os.path.join(path,file))
    for subdir in subdirs:
        if subdir.endswith(".dmg"):
            listOfDMGFiles.append(os.path.join(path,subdir))
    
if len(listOfDMGFiles) == 0:
    print("No DMG files found in your downloads folder")
    exit()

userConsent = input(f"delete all {len(listOfDMGFiles)} DMG files in your downloads folder? (y/n): ")

if userConsent.lower() == "y":
    for file in listOfDMGFiles:
        os.remove(file)
    print("All DMG files have been deleted")

elif userConsent.lower() == "n":
    print("No files have been deleted, goodbye")
