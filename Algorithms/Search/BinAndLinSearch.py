#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

import math
import random
import time

print('This source code calculates run time of Binary Search,')
print('   and Linear Search in random array from range -1000 to')
print('   1000 with n elements, the array is sorted before search')

#--------------Binary Search--------------#
def binarySearch(key, array):
    if len(array) == 0:
        #print('not found key: ',key)
        return False
    else:
        mid = len(array)//2
        if key == array[mid]:
            #print('found key: ',key)
            return True
        elif key < array[mid]:
            return binarySearch(key,array[:mid])
        elif key > array[mid]:
            return binarySearch(key,array[mid+1:])

#---------------Linear Search--------------# 
def linearSearch(key, array):
    for i in range(0, len(array)):
        if array[i] == key:
           #print('found key: ',key)
            return True
    #print('not found key: ',key)
    return False

n = int(input("Enter a positive integer n: "))
print()
a=[] #Declare empty list

#Create random integers from -1000 to 1000
for i in range(0,n):
    a.insert(i,random.randrange(-1000,1000))
a = sorted(a) #Sort array in order
key = a[random.randint(0,len(a)-1)]

#Suggested n = 100000

#---------------Search starts--------------#
tmpAverage=[]
print('The key that is being searched is: ', key)
print('######Binary Search######')
for i in range(0,30):
    t = time.clock()
    binarySearch(key, a)
    elaspe = time.clock() - t
    tmpAverage.insert(0,elaspe)
print('-------------------------------')
print('Average time: ',sum(tmpAverage)/len(tmpAverage))
print('#######################')
print()
tmpAverage=[]
print('######Linear Search#######')
for i in range(0,30):
    t = time.clock()
    linearSearch(key, a)
    elaspe = time.clock() - t
    tmpAverage.insert(0,elaspe)
print('-------------------------------')
print('Average time: ',sum(tmpAverage)/len(tmpAverage))
print('#######################')
