#selection sorting

def selection(arr):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1,len(arr)):
            if arr[min_ind]>arr[j]:
                min_ind=j
                
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
    return arr

arr=[2,17,5,13,19,23,21,4,7]
selection(arr)

for i in range(len(arr)):
    print("% d" % arr[i], end=" ")



#insertion sorting

def insertion(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr

arr=[5,2,4,3,1,7]
insertion(arr)
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")



#Bubble Sorting 


def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return

arr = [64, 34, 25, 12, 22, 11, 90]`

bubbleSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

import math
from turtle import*
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
           math.cos(2*k)-2*\
           math.cos(3*k)-\
           math.cos(4*k)
speed(0)
bgcolor("black")
for i in range(10000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()
