#!/usr/bin/python3
#Coded by Abid Ahmad [Root Intrud3r]
#Last Update: 14-03-21
#Version: 1.3

import re , urllib.request, urllib.error, urllib.parse  , sys , os, requests

print("\n")
print("\033[1;33;40m          +-+-+ +-+-+-+-+-+-+-+-+-+")
print("\033[1;36;40m          |R|M| \033[1;31;40m|D|u|p|l|i|c|a|t|3|")
print("\033[1;33;40m          +-+-+ +-+-+-+-+-+-+-+-+-+\033[0;37;40m \n")
print("\033[1;37;40m    Remove Duplicate Domain or URL from a File & get Clean File \n")
print("\033[1;32;40m         Cod3d by Abid Ahmad \033[1;36;40m[@Root_Intrud3r]\n")
print("\033[1;37;40m          \n")

in1 = input('  Input File >> ')
read = open(in1 , 'r').readlines()
set1 = set(read)
out1 = input('  Output File >> ')
print("\033[1;33;40m          \n")
write = open(out1 , 'w')
for line in set1:
    write.write(line)
    print('[=] ', line)

print('\033[1;32;40m   [+] File Saved as:', out1)