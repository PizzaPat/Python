#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

import math
from encryptRSA import encryptRSA
from decryptRSA import decryptRSAPrivate
from decryptRSA import decryptRSA
from modExp import modExp
from congruence import inverse

end = False
while(end!=True):
    print('#################################')
    print('#            1.) Encrypt                                      #')
    print('#            2.) Decrypt                                     #')
    print('#            3.) Example Encryption                 #')
    print('#            4.) Example Decryption                 #')
    print('#            5.) End Program                             #')
    print('#################################')
    choice = int(input('--->'))
    if(choice == 1):
        message = input('Message: ')
        p = int(input('Enter prime p: '))
        q = int(input('Enter prime q: '))
        e = int(input('Enter prime e: '))
        print('Encrypted Message: ', encryptRSA(message,p,q,e))
        print('Private Key: ', int(inverse(e,1, (p-1)*(q-1))))
    elif(choice == 2):
        code = input('Code: ')
        eInv = int(input('Enter Private Key (e inverse): '))
        n = int(input('Enter Public Key (n): '))
        print('Decrypted Message: ',decryptRSAPrivate(code,eInv,n))
        
    elif(choice == 3):
        print()
        print('---Example of encryption---')
        print()
        print('Definition: ')
        print('p and q are both primes')
        print('e is an integer only if gcd(e,(p-1)(q-1)) = 1')
        print('format -> encryptRSA(message, p, q, e)\n')
        print('encryptRSA(\'STOP\',p=43,q=59,e=13): ',encryptRSA('STOP',43,59,13))
        print('encryptRSA(\'meet at noon\',p=43,q=59,e=13): ',encryptRSA('meet at noon',43,59,13))
        print('encryptRSA(\'upload\',p=53,q=61,e=17): ',encryptRSA('upload',53,61,17))
        print()
    elif(choice == 4):
        print('\n---Example of encryption---\n')
        print('Definition: ')
        print('e Inverse is a private key that decrypted with a private prime number')
        print('n is public key given it is combination of two primes')
        print('format -> decryptRSAPrivate(code,eInv,e)\n')
        print('decryptRSAPrivate(\'09810461\',937,2537): ',decryptRSAPrivate('09810461',937,2537))
        print()
    elif(choice == 5):
        print('Exited')
        end = True
    else:
        print('Invalid input')
