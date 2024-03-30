# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 00:52:43 2024

@author: debkumar
"""
"""
f = open('test01.xsd','r')

print(f.name)

print(f.mode)
f.close()
"""

#open file using context manager

#remove comments and execute the code to see how read() works
with open("test02.xsd", "r") as f:
    pass
    #print(f.name)
    #print(f.read())
    #f_content =f.readline()
    #f_content =f.readline()
   #f_content =f.readline()
    
    #for line in f:
     #   print(line, end = '')
    #print(f_content)
    #print(type(f_content))
    

    """
    read()-> reads whole file
    readlines() ->returns list of all lines
    readline() ->rerurn only the first line
    read(size) ->reads file of chunks in "size"
    tell() -> given current position
    seek(position) -> reset to a specific position
    
    """
    
#copy a file
with open("test02.xsd", "r") as rf:
    with open("test1.xsd", "w") as wf:
        for line in rf:
            wf.write(line)
            

#copy a .jpg-open in binary mode

with open("monaLisa.jpg", "rb") as rf:
    with open("maani.jpg","wb") as wf:
        for line in rf:
            wf.write(line)
            
# copy file in chunks - instead of reading and writing line by line

with open("monaLisa.jpg", "rb") as rf:
    with open("monaLisa_new.jpg","wb") as wf:
        size_of_chunk = 1000
        chunk = rf.read(size_of_chunk)
        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(size_of_chunk)





