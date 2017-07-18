import shutil
import os

print ( "~ This tool moves all .txt files from a source folder to a destination folder ~")
srcRaw = input("What is your source folder?")

src = srcRaw.replace('\\','\\\\')

dstRaw = input("What is your destination folder?")

dst = dstRaw.replace('\\','\\\\')

# If srcRaw and dstRaw are not in C:\xx\xx format:

#for HARD-CODING USE: src = "C:\\Users\\Oliver\\Desktop\\folder_A"

# FOR HARD-CODING USE: dst = "C:\\Users\\Oliver\\Desktop\\folder_B"

myfiles = os.listdir(src)

def Mover(src,dst):
  for file in myfiles:
    if file.endswith(".txt"):
      filepath = src + "/" + file
      print(filepath + " has been moved to " + dst)
      shutil.move( filepath , dst )      

Mover(src,dst)




