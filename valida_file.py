# -*- coding: utf-8 -*-
file1 = raw_input("Enter the path of your first file: ")
file2 = raw_input("Enter the path of your second file: ")
Basex = open(file1).read().split()
Basey = open(file2).read().split()
if Basex != Basey:
    print("The files are different!")
else:
    print("The files are the same!")
