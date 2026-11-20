# Made on 18/11/2026 (updated the 2023 version)
# By Euan Hao
# V4 saved as OTPE v4 Picture loader
# Title:  One Time Picture Exchange - IMG file loader

### pyinstaller version for executables and all related modules

import os
import pathlib

this_path = pathlib.Path(__file__).parent.resolve()
print(this_path)
#os.chdir(this_path)
filePaths = (os.listdir(this_path))
filePaths.sort()
#print(filePaths)


parent_path = this_path.parent.absolute()
print(parent_path)


print("\n")
for f in os.listdir(parent_path):
    if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', 'png'):
        oldimgpath = (os.path.join(parent_path, f))
        os.remove(oldimgpath)
        


newlocation = str(this_path) + "\\" + str(filePaths[0])
oldlocation = str(parent_path) + "\\" + str(filePaths[0])

os.replace(newlocation, oldlocation)

countFilePath = str(parent_path) + "\\System_Files\\OTPE2_COUNT.txt"
file = open(countFilePath, "w")
file.write("0")
file.close()

noticeFilePath = str(parent_path) + "\\NOTICE - SEND ME.txt"
file = open(noticeFilePath, "w")
file.write("The image file has been replaced.")
file.write("\n")
file.write(str(filePaths[0]))

print(noticeFilePath)