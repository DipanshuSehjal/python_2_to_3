from os import walk, getcwd
import os
import subprocess

mypath = getcwd()
print(mypath)

f = []

for (dirpath, dirnames, filenames) in walk(mypath):

    # print(filenames)
    for files in filenames:
        ext = os.path.splitext(files)[1]
        if ext == ".py":
            full_path = dirpath + "/" + files
            f.append(full_path)
            


# convert the 2to3
#
for a_file in f:
    print(a_file)
    subprocess.Popen('2to3 -w {}'.format(a_file), shell=True)
    print("converting from 2 to 3 and editing the same file")



