# -*- coding: utf-8 -*-
"""
Program Finder telephone number in message

Created on Tue Apr 29 22:46:00 2023

@author: LN Starmark
@e-mail: ln.starmark@ekatra.io
@e-mail: ln.starmark@gmail.com
@tel:    +380 66 9805661
"""

import re
import str_common as strc

LEN_TEL = 14
PROBEL= '-'

def isPhoneNumber(txt):
    if(len(txt) != LEN_TEL):
        return False
    for i in range(0,2):
        if(not txt[i].isdecimal()):
            return False
    if(txt[2] != PROBEL):
        return False
    for i in range(3,6):
        if(not txt[i].isdecimal()):
            return False
    if(txt[6] != PROBEL):
        return False
    for i in range(7,14):
        if(not txt[i].isdecimal()):
            return False
    return True

def Finder(ms):
    for i in range(len(ms)):
        chunk = ms[i:i+LEN_TEL]
        if(isPhoneNumber(chunk)):
            print(f"Finded tel number: {chunk}")
    print("End")

def Find_re(ms):
    phoneNumRegex = re.compile(r"(\d\d)-(\d\d\d)-(\d\d\d\d\d\d\d)")

    print("Find first tel number and out")
    mo = phoneNumRegex.search(ms)
    #print(f"Findet tel. numbers: {mo.group()}")
    print(f"Findet tel. numbers: {mo.group(0)}")
    print(f"Findet tel. numbers: {mo.group(1)}")
    print(f"Findet tel. numbers: {mo.group(2)}")
    print(f"Findet tel. numbers: {mo.group(3)}")
    print(f"Findet tel. numbers: {mo.groups()}")
    print()

    print("Now with method findall() finded all tels")
    moall = phoneNumRegex.findall(ms)
    for tel in moall:
        print(f"Findet tel. numbers: {tel}")

def main():
    strc.titleprogram("Test Finder tel. number in message",
                      "2 Tests: simple and trought re",
                      "ln.starmark@gmail.com\tln.starmark@ekatra.io")

    mess = r"tel. number Starmark: 38-066-9805661 and 35-457-5555555 and 38-050-5117634, noch -> 38-098-5678327 end"

    strc.zagolovok("Finding tel. numbers in  with simple method")
    Finder(mess)

    print()

    strc.zagolovok("Finding tel. numbers in  with simple method")
    Find_re(mess)
 


if __name__ == '__main__':
    main()