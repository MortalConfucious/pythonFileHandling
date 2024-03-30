# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:09:26 2024

@author: debi
"""
import csv

path = "SampleCSVFile.csv"

#this part of the code shows how next() works.
"""
with open(path,"r",newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    data = next(reader)
    print(header)
    print(data)
        
"""  

# prints firstline of  the file.

"""
with open(path, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    data = [line for line in reader]
    print( data [0])
   
"""
# csvDict() fucntion

with open(path, "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames = ["serial_no", "item", "name", "quantity", "profit","revenue","rating","location","work_stream","efficiency"])
    for line in reader:
        print(line)

# csv read and write

with open(path, "r", newline="" ) as csv_reader:
    reader = csv.reader(csv_reader)
    with open ("new_file.csv", "w", newline ="") as csv_writer:
        writer = csv.writer(csv_writer,delimiter ="|")
        
        for line in reader:
            writer.writerow(line)
    
