#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

def inverse(e,r,m):
    eInv = 1
    while(((eInv*e) % m) != (r % m)):
        eInv = eInv + 1
    return eInv
