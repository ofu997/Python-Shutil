import shutil
import os

srcRaw = input("What is your source folder?")

src = srcRaw.replace('\\','\\\\')

dstRaw = input("What is your destinatin folder?")

dst = dstRaw.replace('\\','\\\\')

# If src and dst are not in C:\xx\xx format:

#for HARD-CODING USE: src = "C:\\Users\\Oliver\\Desktop\\folder_A"

# FOR HARD-CODING USE: dst = "C:\\Users\\Oliver\\Desktop\\folder_B"

myfiles = os.listdir(src)

def Mover(src,dst):
  for file in myfiles:
    if file.endswith(".txt"):
      filepath = src + "/" + file
      shutil.move( filepath , dst )

Mover(src,dst)




