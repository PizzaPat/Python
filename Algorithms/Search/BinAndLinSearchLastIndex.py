#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

import math
import random
import time

print('This source code calculates run time of Binary Search,')
print('   and Linear Search in random array from range -1000 to')
print('   1000 with n elements, the array is sorted before search.')
print('   In addition, the element value 7000 was being inserted at')
print('   the end to compare the Binary Search and Linear Search')
print('   whether which one can reach the last index first')

#--------------Binary Search--------------#
def binarySearch(key, array):
    if len(array) == 0:
        #print('not found key: ',key)
        return False
    else:
        mid = len(array)//2 # Find index of middle of the array
        if key == array[mid]:
            print('found key: ',key)
            return True
        elif key < array[mid]: #If the key is less than the mid point,
                                            #recursive to the left portion of the array
            return binarySearch(key,array[:mid-1])
                                                #else, recursive to the right
        elif key > array[mid]:
            return binarySearch(key,array[mid+1:])

#---------------Linear Search--------------# 
def linearSearch(key, array):
    for i in range(0, len(array)):
        if array[i] == key:
            print('found key: ',key)
            return True
    print('not found key: ',key)
    return False

#---------------------------------------------

n = int(input("Enter a positive integer n: "))
print()
a=[] #Declare empty list

#Create random integers from -1000 to 1000
for i in range(0,n):
    a.insert(i,random.randrange(-5000,5000))
a = sorted(a) #Sort array in order
a[len(a)-1] = 7000 #Set last array to 7000
key = 7000 #Set searching key to 7000

#Suggested n = 100000 and 10000000

# 1 instruction = time / size
# size = n

#---------------Search starts--------------#
time_list=[]
print('######Binary Search######')
t = time.clock()
binarySearch(key, a)
elaspe = time.clock() - t
print('Search time: ', elaspe)
step = elaspe/math.log(n,2)
print('Line_Instruction: ', step)
print('#######################')
print()
print('######Linear Search#######')
t = time.clock()
linearSearch(key, a)
elaspe = time.clock() - t
print('Search time: ',elaspe)
step = elaspe/n
print('Line_Instruction: ',step)
print('#######################')
