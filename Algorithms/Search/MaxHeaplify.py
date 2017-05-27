#This source code is for educational purposes only!
#Any plagiarism or reuse of this source code
#   will be at your own risk

import math
import random
import time

print('This source code demonstrates how Max_Heap is implemented in each')
print('   steps by swapping and the then heaplify to sorted order')

t=0
#Node (parent, current, leftchild, rightchild)
def build_MaxHeap(a):
    n = len(a)
    print('            #####Build_MaxHeap######')
    print('Array given: ', a)
    print('----------------')
    for i in range(len(a)//2,-1,-1): #if len is 5, iteration starts from 2 to 0
        a = max_heapify(a,i)
    print('            #####Finished Build_MaxHeap######')
    return a

#heapify the tree
def max_heapify(a,i):
    current = i
    left = 2*i 
    right = 2*i + 1
    if left <= t and a[left] > a[current]:
        current = left
        #The last if will satisfy
    if right <= t and a[right] > a[current]:
        current = right
        #The last if will satisfy
    if current != i: # if it is not heapify, meaning
        #either left or right child is greater, then we swap
        #then check the current node AFTER swap again
        #for heapify
        tmp = a[i]
        a[i] = a[current]
        a[current] = tmp
        print('after swap',a)
        #recursive once more
        max_heapify(a, current)
    return a

def heap_sort(a):
    global t
    t = len(a) - 1
    a= build_MaxHeap(a)
    for i in range(len(a)-1, -1, -1):
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp
        t = t - 1
        a = max_heapify(a,0)
    return a

tree=[5,3,2,1,9,8,4] #Declare list

#Start Implementation
a = tree
print('++++++++++++++++++++Heaplify++++++++++++++++')
heap_sort(a)
print('After heap_sort: ', a)
