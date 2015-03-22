#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:53:15 2015

@author: dmamartin
"""
"""This imports the sys module"""
import sys 

if len(sys.argv)!=3: #if this is run it will print the text in the quotation marks below
    print """Run this parser with the following arguments:
    parsemultalign.py multalign_file output_file
    """
    exit(0)

"""Opens the data file"""
infile=sys.argv[1] #This is the name of the input file
outfile=sys.argv[2] #This is the name of the output file

print("Parsing input file %s, writing results to %s"%(infile, outfile)) #This prints out a message to indicate success with writing the results to the files.

"""Opens the output files"""
ifh=open(infile)
ofh=open(outfile, "w")

""" Read the first line and then reads more lines while the line doesnt match a specific pattern"""
line= ifh.readline()

identifiers=[] 

while line[1:6] != 'Index': #This will read from the first to the sixth character until it reaches the word index
    line=ifh.readline()


"""This initialises a for loop"""   
for line in ifh.readlines():
    if line[9]=='>': #reads up to line 9, or up until it doesnt follow a certain pattern, once it reaches the greater than sign it will stop
        identifiers.append(line[13:32].strip()) #...then read the characters 12 to 32
    else: #If the 9th line doesnt start with > then carry out the following comands 
        if line[5]== 'I': #If the 5th line starts with 'I' then
            headers=line.strip().split() #
            headers.append('PWMATCH')
            ofh.write("\t".join(headers)+"\n")
            continue
        if line[1:6]=='Times':
            break        
        fields=[x.strip() for x in (line[0:6], line[6:11],line[11:16],line[16:21], #this breaks the; lines 1 to 6, 7 to 11, 12 to 16, 17 to 21 onto a different line 
                line[21:31],line[31:38], line[38:45],line[45:52], line[52:62], #same as above but for the corresponding lines
                line[62:72], line[72:82],line[82:89], line[89:99], line[99:109],
                line[109:119], line[119:126])]
        fields[0]=identifiers[int(fields[0])-1] 
        fields[1]=identifiers[int(fields[1])-1]
        ofh.write("\t".join(fields)+"\n") #joins up the fields on new lines

"""Closes the created files after the data has been written to them"""
ofh.close()
ifh.close()
