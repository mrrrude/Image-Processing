#Author:pratikpandey


import os

path = 'Your Directory Path'

folder = os.fsencode(path)

filenames = []#list to store image names

for file in os.listdir(folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpg')): # whatever file types you're using...eg.jpeg,asm,etc.
        filenames.append(filename)

#filenames.sort()
