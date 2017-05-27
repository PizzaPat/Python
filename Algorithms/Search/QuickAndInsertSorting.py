#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

import math
import random
import time

print('This source code calculates run time of Quick Sort,')
print('   and Insertion Sort in random array from range -7000 to')
print('   7000 with n elements size n. The time is calculated by the end')
print('   of sorting in each function, then it is averaged by 100 loops')

#--------------Quick Sort--------------#
def quick_sort(a):
    if len(a) <= 1:# if the length of the array is 1 or lower, then
                        #return back the original array
        return a
    tmpLeftArray = []#Create left array tmp to pass into next recursive
    tmpRightArray = []#Create right array tmp to pass into next recursive
    mid = len(a)//2
    pivot = a[mid]#Get a pivot between recusive step
    a = a[:mid] + a[mid+1:]
    for i in a:
        if i <= pivot:
            tmpLeftArray.append(i) #If value of current index a[i] is less than,
                                                    #insert into left array
        else:
            tmpRightArray.append(i) #else insert to the right array

    return (quick_sort(tmpLeftArray)+ [pivot] + quick_sort(tmpRightArray))

#---------------Insertion Sort--------------# 
def insertion_sort(a):
    for i in range(1,len(a)):#Iterate from 1st element to last element
        key = a[i]#Set current index value to a current key
        j = i - 1#Get the previous index
        while(j>=0 and key < a[j]):#switching if the key is less than the current iteration
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key#move to the next key
    return a

n = int(input("Enter a positive integer n: "))
print()
a=[] #Declare empty list
#Create random integers from -7000 to 7000
for i in range(0,n):
    a.insert(i,random.randrange(-7000,7000))

# 1 instruction = time / size
# size = n
# number 7, find time = 1 second

#---------------Search starts--------------#
print('######Quick Sort######')
tmpAverage=[]
for i in range(0,100):
    t = time.clock()
    sortedArr = quick_sort(a)
    elaspe = time.clock() - t
    tmpAverage.insert(0,elaspe)
print('-------------------------------')
print('Average time: ',sum(tmpAverage)/len(tmpAverage))
print('#######################')
print('-------------------------------------------')
print()
print('######Insertion Sort#######')
tmpAverage=[]
for i in range(0,100):
    t = time.clock()
    insertion_sort(a)
    elaspe = time.clock() - t
    tmpAverage.insert(0,elaspe)
print('------------------------------')
print('Average time: ',sum(tmpAverage)/len(tmpAverage))
print('#######################')
print()
#print('Number of instructions for 1 second ', ((sum(tmpAverage)/len(tmpAverage) / (n**2))))
print('Number of instructions for 1 second of Quick Sort: ', (1 / (n*math.log(n,2))))
print('Number of instructions for 1 second of Insertion Sort: ', (1 / (n**2)))
