#!/usr/bin/env python


import sys

#imports/finds the module, "sys", which provides access to some
# varibles used or maintaind by the interpreter and to functions that ineract
# strongly with the interpreter


USAGE = "Usage: ./find.py word filename [filename]*" #defines the variable "USAGE"


def fail(msg): #creates the function fail, with the paramater msg (note: fail is not a builtin function)
    print >> sys.stderr, USAGE # fail(USAGE) prints "Usage: ./find.py word filename [filename]*"
    print >> sys.stderr, msg #fail(msg) prints file objects corresponding to msg (msg doesn't seem to have been defined yet)
    sys.exit() #exits from python

try:
    word = sys.argv[1] #list of strings representing the first argument after the script for word
except:
    fail("Please provide a word to find.") 

filenames = sys.argv[2:] #gets the second argument after a filename
if not filenames:
    fail("Please enter at least one filename.")

for filename in filenames:
    try:
        file_pointer = open(filename) #file_pointer creates the file object, "filename"
    except IOError:
        print >> sys.stderr, "Could not open file:", filename
        continue

    for line in file_pointer:
        if word in line:
            print filename
            break
