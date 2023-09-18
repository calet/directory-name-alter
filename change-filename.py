import os
import random 
import sys

basedir = 'INSERT DIRECTORY NAME'

#original dir
print("original dir:")
for subdir in os.listdir(basedir):
    print(f"{subdir}: ", os.listdir(f"{basedir}//{subdir}"))

#renaming dir(s)
print("\nrenaming dir(s)...\n")
for subdir in os.listdir(basedir):
    new_name = str(random.randrange(sys.maxsize))
    try:
        os.rename(f"{basedir}//{subdir}", f"{basedir}//{new_name}")
    except:        
        while new_name in os.listdir(basedir):
            new_name = str(random.randrange(4))
        os.rename(f"{basedir}//{subdir}", f"{basedir}//{new_name}")

#final dir(s)
print("final directory:")
for subdir in os.listdir(basedir):
    inside_folder = f"{basedir}//{subdir}"
    print(f"{subdir}: ", os.listdir(inside_folder))
