#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

import math
from modExp import modExp
from gcd import gcd

# s is string
# n is a public key
# e is a prime public key
def encryptRSA(s,p,q,e):
    p = int(p)
    q = int(q)
    if(gcd((p-1)*(q-1),e)!=1):
        print('invalid mod')
    #Dictionary of a letter
    conversion = {"A": "00", "B": "01", "C": "02", "D": "03", "E": "04",
                  "F": "05", "G": "06", "H": "07", "I": "08", "J": "09",
                  "K": "10", "L": "11", "M": "12", "N": "13", "O": "14",
                  "P": "15", "Q": "16", "R": "17", "S": "18", "T": "19",
                  "U": "20", "V": "21", "W": "22", "X": "23", "Y": "24",
                  "Z": "25"}
    digits=""
    s = "".join(s.split())
    for c in s:
        digits = digits + conversion[c.upper()]
    i=False
    cap = "25"
    while (i!=True):
        if (len(cap)<len(str(p*q)) and int(cap)<(p*q)):
            cap = str(cap)+'25'
        else:
            i=True
    padded = False
    while (padded!=True):
        if(int((len(digits)))%len(str(cap))!=0):
            digits = digits + conversion['X']
        else:
            padded = True   
    tmpTuple = ()
    tmpString = ''
    for x in range(1,len(digits)+1):
        if(int(x%len(cap))!=0):
            tmpString = tmpString+digits[x-1]
        else:
            tmpString = tmpString+digits[x-1]
            tmpTuple = tmpTuple + (tmpString,)
            tmpString = ''
    returnTuple = ()
    for j in tmpTuple:
        returnTuple = returnTuple + (modExp(j,"{0:b}".format(e),(p*q)),)
    return (returnTuple)
