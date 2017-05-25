#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

import math
from modExp import modExp
from gcd import gcd
from congruence import inverse

def decryptRSA(s,p,q,e):
    #Dictionary of a letter
    deconversion = {"00":"A", "01":"B", "02": "C" , "03":"D","04":"E",
                  "05":"F", "06": "G",  "07":"H", "08":"I", "09":"J",
                  "10":"K", "11":"L",  "12":"M", "13":"N", "14":"O",
                  "15":"P", "16": "Q", "17":"R", "18":"S", "19":"T",
                  "20":"U", "21":"V", "22":"W", "23":"X", "24": "Y",
                  "25":"Z"}
    p = int(p)
    q = int(q)
    if(len(s)%4 != 0):
        print('invalid code')
        return
    eInv = int(inverse(e,1, (p-1)*(q-1)))
    eInv = int("{0:b}".format(eInv))
    s = [s[i:i+4] for i in range(0,len(s),4)]
    strReturn = []
    returnTuple = []
    for d in s:
        tmpDecrypt = str(modExp(int(d),eInv,p*q))
        while(len(tmpDecrypt) % 4 != 0):
            tmpDecrypt = '0' + tmpDecrypt
        tmpDecrypt = "".join(tmpDecrypt.split())
        strReturn = [ tmpDecrypt[i:i+2] for i in range(0,len(tmpDecrypt),2)]
        returnTuple.append(strReturn[0])
        returnTuple.append(strReturn[1])
        digits =""
        for m in returnTuple:
            digits = digits + deconversion[m]
    return digits

def decryptRSAPrivate(s,eInv,n):
    #Dictionary of a letter
    deconversion = {"00":"A", "01":"B", "02": "C" , "03":"D","04":"E",
                  "05":"F", "06": "G",  "07":"H", "08":"I", "09":"J",
                  "10":"K", "11":"L",  "12":"M", "13":"N", "14":"O",
                  "15":"P", "16": "Q", "17":"R", "18":"S", "19":"T",
                  "20":"U", "21":"V", "22":"W", "23":"X", "24": "Y",
                  "25":"Z"}
    eInv = int("{0:b}".format(eInv))
    s = [s[i:i+4] for i in range(0,len(s),4)]
    strReturn = []
    returnTuple = []
    for d in s:
        tmpDecrypt = str(modExp(int(d),eInv,n))
        while(len(tmpDecrypt) % 4 != 0):
            tmpDecrypt = '0' + tmpDecrypt
        tmpDecrypt = "".join(tmpDecrypt.split())
        strReturn = [ tmpDecrypt[i:i+2] for i in range(0,len(tmpDecrypt),2)]
        returnTuple.append(strReturn[0])
        returnTuple.append(strReturn[1])
        digits =""
        for m in returnTuple:
            digits = digits + deconversion[m]
    return digits

