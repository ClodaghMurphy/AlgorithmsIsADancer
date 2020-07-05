#1. Import required libraries
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2.Implementation of sorting algorithms: BubbleSort, mergeSort, insertionSort, TimSort, countSort
#Python program to implement bubbleSort
#Create a function bubble_sort that takes anArray as argument.
#Code adapted from https://www.geeksforgeeks.org/bubble-sort/
def bubbleSort(myArray): 
    n = len(myArray) 
#All elements of the list should be traversed  

    for i in range(n): 

#create inner loop with variable that counts from 0 up to i – 1
        for j in range(0, n-i-1): 


# if the elements at indexes j and j + 1 are out of order, then swap them
            if myArray[j] > myArray[j+1] : 
                myArray[j], myArray[j+1] = myArray[j+1], myArray[j] 
#Python program to implement merge sort 
#Create a function mergeSort that takes an array as argument.
#Code adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
def mergeSort(myArray):

#The "base case" i.e. function should only continue if the list is greater than one element
# if the array is greater than 1 then
    if len(myArray)>1:
#Identify the mid of the array, it doesn't matter if both sides are not equal
        mid = len(myArray)//2
# Call python slice operator to divide the array elements into a left half and right half
        lefthalf = myArray[:mid]
        righthalf = myArray[mid:]
        
#To sort the lefthalf and then the right
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        
#Copy array items to temporary arrays L[] and R[]
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                myArray[k]=lefthalf[i]
                i=i+1
            else:
                myArray[k]=righthalf[j]
                j=j+1
            k=k+1

# Check to see if any element leftover.          
       
        while i < len(lefthalf):
            myArray[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            myArray[k]=righthalf[j]
            j=j+1
            k=k+1
#Implementation of sorting algorithm
#Python program to implement insertionSort
#Create a function insertionSort that takes an Array as argument.
#Code adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
def insertionSort(array):
#for loop traverses key values from 1 to last available    
   for index in range(1,len(array)):
     key = array[index]
     position = index
#search for elements of a lower value to the left
     while position>0 and array[position-1]>key:
#All elements moved right one position        
         array[position]=array[position-1]
#To continue to next element            
         position = position-1
#key assigned to correct position
     array[position]=key
 #Implementation of sorting algorithm
# Python3 program to perform TimSort. 
#TimSort algorithm implementation using python
#Adapted from https://www.codespeedy.com/timsort-algorithm-implementation-in-python/
#Algorithm looks for an ideal minimum size called “minrun”, usually set between 32 and 64
run = 32
# This insertion sort function sorts consecutive sets of 32(minirun) elements
#and traverses the region of the array passed into it
# start is the starting element’s index number and end is the index of the last element of the region
#Use of indices is a departure from usual insertionsort method
def InsSort(myArray,start,end):    
    for i in range(start+1,end+1):
        elem = myArray[i]
        j = i-1
        while j>=start and elem<myArray[j]:
            myArray[j+1] = myArray[j]
            j -= 1
        myArray[j+1] = elem
    return myArray
 
#function to mergsort the two subarray indices
def merge(myArray,start,mid,end):
    if mid==end:
        return myArray
#first and last arrays = difference in the indices
    first = myArray[start:mid+1]
    last = myArray[mid+1:end+1]
    len1 = mid-start+1
    len2 = end-mid
    ind1 = 0
    ind2 = 0
    ind  = start
     
    while ind1<len1 and ind2<len2:
        if first[ind1]<last[ind2]:
            myArray[ind] = first[ind1]
            ind1 += 1
        else:
            myArray[ind] = last[ind2]
            ind2 += 1
        ind += 1
     
    while ind1<len1:
        myArray[ind] = first[ind1]
        ind1 += 1
        ind += 1
              
    while ind2<len2:
        myArray[ind] = last[ind2]
        ind2 += 1
        ind += 1   
#returns merged subarrays              
    return myArray
            
#This function acts like a "driver function"to test the 
#previous functions with values aligned to the logic of TimSort algorithm
def TimSort(myArray):
    n = len(myArray)
#find starting points for each subarray  
#run defined as 32 in line 6 of this code
    for start in range(0,n,run):
        end = min(start+run-1,n-1)
        myArray = InsSort(myArray,start,end)
#After every merge, left side doubled until < n,the length of the array         
    curr_size = run
    while curr_size<n:    
        for start in range(0,n,curr_size*2):
            mid = min(n-1,start+curr_size-1)
            end = min(n-1,mid+curr_size)
# Merged array returned to myArray
            myArray = merge(myArray,start,mid,end)
        curr_size *= 2
    return myArray

#Python program to implement Counting Sort
#Create a function countSort that takes an Array as argument.
#Code adapted from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
def countSort(myArray):
# Count occurences of each key value in the array
#Counting sort works on the assumption that the range of the input is known, therefore maximum value is hard coded into the function at m
#because this assignment randomly generated integers with values between 0 and 99
    m = 100 + 1
    count = [0] * m                
    
    for a in myArray:
# Count each item and place in appropriate index
        count[a] += 1             
    i = 0
    for a in range(m):    
#Then construct sorted result array from counting step
        for c in range(count[a]):  
            myArray[i] = a
            i += 1
    return myArray
#3. Benchmarking Method
#Code adapted from https://github.com/RitRa/Algorithms-project-
#Code adapted from Benchmarking Algorithms in Python Lecture Notes
#function takes as input a value n and returns an array of n randomly generated integers with values between 0 and 99.
def random_array(n):
#Create an array variable
    arrray =[]
#Create variable i based on value n
    for i in range (0, n, 1):
#Apppend random integers between 0 and 100 to the array
        arrray.append(random.randint(0,100))
    return arrray  
# assign the random array to alist
array100 = random_array(100)
array250 = random_array(250)
array500 = random_array(500)
array750 = random_array(750)
array1000 = random_array(1000)
array1250 = random_array(1250)
array2500 = random_array(2500)
array3750 = random_array(3750)
array5000 = random_array(5000)
array6250 = random_array(6250)
array7500 = random_array(7500)
array8750 = random_array(8750)
array10000 = random_array(10000)

# def benchmark_bubblesort():
#Per Project Specification:The running time (in milliseconds) for each algorithm should be measured 10 times  
#Code adapted from Benchmarking Algorithms in Python Lecture Notes
#It measures the time taken to execute the bubbleSort() function.
#global keyword is used to create global variables from inside a function.
global bubblesort_avg
bubblesort_avg = []

num_runs = 10
results = []

def benchmark_bubblesort():
    for r in range(num_runs):
#Log the time in seconds, starting right now = time.time()
        start_time = time.time()
    #Call the function to benchmark
        bubbleSort(array100)
#Log the endtime in seconds
        end_time = time.time()
#Calculate the elapsed time(time_elapsed)
    time_elapsed = end_time - start_time
#Call for results to be appended on each loop
#muliplied by 1000 to provide result in milliseconds format
    results.append(time_elapsed*1000)
#Calculate the average value of the num_runs for each algorithm:
#sum of the numbers in the list divided by a count of numbers in the list - always 10
x = sum(results)
average = (x/10)
#format to 3 decimal places using python round() function
average = round(average, 3)
bubblesort_avg.append(average)
                
#Per Project Specification suggested size of arrays to test              
                
for r in range(num_runs):
    start_time = time.time()
bubbleSort(array250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)              
                
for r in range(num_runs):
    start_time = time.time()
bubbleSort(array500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)   

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array1000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array1250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array2500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array3750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array5000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array6250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array7500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)
                
for r in range(num_runs):
    start_time = time.time()
bubbleSort(array8750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)    

for r in range(num_runs):
    start_time = time.time()
bubbleSort(array10000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
bubblesort_avg.append(average)

# def benchmark_mergeSort():
#Per Project Specification:The running time (in milliseconds) for each algorithm should be measured 10 times  
#Code adapted from Benchmarking Algorithms in Python Lecture Notes
#It measures the time taken to execute the mergeSort() function.
#global keyword is used to create global variables from inside a function.
global mergeSort_avg
mergeSort_avg = []

num_runs = 10
results = []

def benchmark_mergeSort():
    for r in range(num_runs):
#Log the time in seconds, starting right now = time.time()
        start_time = time.time()
#Call the function to benchmark
        mergeSort(array100)
#Log the endtime in seconds
        end_time = time.time()
#Calculate the elapsed time(time_elapsed)
    time_elapsed = end_time - start_time
#Call for results to be appended on each loop
#muliplied by 1000 to provide result in milliseconds format
    results.append(time_elapsed*1000)
#Calculate the average value of the num_runs for each algorithm:
#sum of the numbers in the list divided by a count of numbers in the list - always 10
x = sum(results)
average = (x/10)
#format to 3 decimal places using python round() function
average = round(average, 3)
mergeSort_avg.append(average)
                
#Per Project Specification suggested size of arrays to test              
                
for r in range(num_runs):
    start_time = time.time()
mergeSort(array250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)              
                
for r in range(num_runs):
    start_time = time.time()
mergeSort(array500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)   

for r in range(num_runs):
    start_time = time.time()
mergeSort(array750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
mergeSort(array1000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
mergeSort(array1250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
mergeSort(array2500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
mergeSort(array3750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
mergeSort(array5000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
mergeSort(array6250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
mergeSort(array7500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)
                
for r in range(num_runs):
    start_time = time.time()
mergeSort(array8750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)    

for r in range(num_runs):
    start_time = time.time()
mergeSort(array10000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
mergeSort_avg.append(average)

#def benchmark_insertionSort():
#Per Project Specification:The running time (in milliseconds) for each algorithm should be measured 10 times  
#Code adapted from Benchmarking Algorithms in Python Lecture Notes
#It measures the time taken to execute the insertionSort() function.
#global keyword is used to create global variables from inside a function.
global insertionSort_avg
insertionSort_avg = []

num_runs = 10
results = []

def benchmark_insertionSort():
    for r in range(num_runs):
#Log the time in seconds, starting right now = time.time()
        start_time = time.time()
    #Call the function to benchmark
        insertionSort(array100)
#Log the endtime in seconds
        end_time = time.time()
#Calculate the elapsed time(time_elapsed)
    time_elapsed = end_time - start_time
#Call for results to be appended on each loop
#muliplied by 1000 to provide result in milliseconds format
    results.append(time_elapsed*1000)
#Calculate the average value of the num_runs for each algorithm:
#sum of the numbers in the list divided by a count of numbers in the list - always 10
x = sum(results)
average = (x/10)
#format to 3 decimal places using python round() function
average = round(average, 3)
insertionSort_avg.append(average)
                
#Per Project Specification suggested size of arrays to test 
for r in range(num_runs):
    start_time = time.time()
insertionSort(array250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)              
                
for r in range(num_runs):
    start_time = time.time()
insertionSort(array500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)   

for r in range(num_runs):
    start_time = time.time()
insertionSort(array750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
insertionSort(array1000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
insertionSort(array1250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
insertionSort(array2500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
insertionSort(array3750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
insertionSort(array5000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
insertionSort(array6250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
insertionSort(array7500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)
                
for r in range(num_runs):
    start_time = time.time()
insertionSort(array8750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)    

for r in range(num_runs):
    start_time = time.time()
insertionSort(array10000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
insertionSort_avg.append(average)

#def benchmark_TimSort():
#Per Project Specification:The running time (in milliseconds) for each algorithm should be measured 10 times  
#Code adapted from Benchmarking Algorithms in Python Lecture Notes
#It measures the time taken to execute the TimSort() function.
#global keyword is used to create global variables from inside a function.
global TimSort_avg
TimSort_avg = []

num_runs = 10
results = []

def benchmark_TimSort():
    for r in range(num_runs):
#Log the time in seconds, starting right now = time.time()
        start_time = time.time()
    #Call the function to benchmark
        TimSort(array100)
#Log the endtime in seconds
        end_time = time.time()
#Calculate the elapsed time(time_elapsed)
    time_elapsed = end_time - start_time
#Call for results to be appended on each loop
#muliplied by 1000 to provide result in milliseconds format
    results.append(time_elapsed*1000)
#Calculate the average value of the num_runs for each algorithm:
#sum of the numbers in the list divided by a count of numbers in the list - always 10
x = sum(results)
average = (x/10)
#format to 3 decimal places using python round() function
average = round(average, 3)
TimSort_avg.append(average)
                
#Per Project Specification suggested size of arrays to test              
                
for r in range(num_runs):
    start_time = time.time()
TimSort(array250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)              
                
for r in range(num_runs):
    start_time = time.time()
TimSort(array500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)   

for r in range(num_runs):
    start_time = time.time()
TimSort(array750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
TimSort(array1000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
TimSort(array1250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
TimSort(array2500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
TimSort(array3750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
TimSort(array5000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
TimSort(array6250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
TimSort(array7500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)
                
for r in range(num_runs):
    start_time = time.time()
TimSort(array8750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)    

for r in range(num_runs):
    start_time = time.time()
TimSort(array10000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
TimSort_avg.append(average)


#def benchmark_countSort():
#Per Project Specification:The running time (in milliseconds) for each algorithm should be measured 10 times  
#Code adapted from Benchmarking Algorithms in Python Lecture Notes
#It measures the time taken to execute the countSort() function.
#global keyword is used to create global variables from inside a function.
global countSort_avg
countSort_avg = []

num_runs = 10
results = []

def benchmark_countSort():
    for r in range(num_runs):
#Log the time in seconds, starting right now = time.time()
        start_time = time.time()
    #Call the function to benchmark
        countSort(array100)
#Log the endtime in seconds
        end_time = time.time()
#Calculate the elapsed time(time_elapsed)
    time_elapsed = end_time - start_time
#Call for results to be appended on each loop
#muliplied by 1000 to provide result in milliseconds format
    results.append(time_elapsed*1000)
#Calculate the average value of the num_runs for each algorithm:
#sum of the numbers in the list divided by a count of numbers in the list - always 10
x = sum(results)
average = (x/10)
#format to 3 decimal places using python round() function
average = round(average, 3)
countSort_avg.append(average)

#Per Project Specification suggested size of arrays to test              
                
for r in range(num_runs):
    start_time = time.time()
countSort(array250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average) 

for r in range(num_runs):
    start_time = time.time()
countSort(array500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)   

for r in range(num_runs):
    start_time = time.time()
countSort(array750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
countSort(array1000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
countSort(array1250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
countSort(array2500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
countSort(array3750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
countSort(array5000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
countSort(array6250)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)

for r in range(num_runs):
    start_time = time.time()
countSort(array7500)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)
                
for r in range(num_runs):
    start_time = time.time()
countSort(array8750)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)    

for r in range(num_runs):
    start_time = time.time()
countSort(array10000)
end_time = time.time()
time_elapsed= end_time - start_time
results.append(time_elapsed*1000)
x = sum(results)
average = (x/10)
average = round(average, 3)
countSort_avg.append(average)


import pandas as pd
import numpy as np

df = pd.DataFrame(columns = ['Size','Bubble Sort', 'Merge Sort', 'Insertion Sort', 'Counting Sort', 'Tim Sort'])
df['Size'] = [100, 250, 500, 750, 1000, 1250, 2500, 3570, 5000, 6250, 7500, 8750, 10000]


df['Bubble Sort'] = bubblesort_avg
df['Merge Sort'] = mergeSort_avg
df['Insertion Sort'] = insertionSort_avg
df['Counting Sort'] = countSort_avg
df['Tim Sort'] = TimSort_avg
#transpose function is called to ensure layout of rows and columns is in the desired format.
#df.transpose()
print (df.transpose())
#The df.describe() command is used to view statistical details #e.g. mean, standard, minimum and maximum in a table.
print(df.describe())

#Code adapted from https://github.com/RitRa/Algorithms-project-
#give the plot a Title
title="Benchmarking Sorting Algorithms"
#Set aesthetic parameters
#use of darkgrid and rainbow palettefor contrast
#rc ‘run command’ used with sns.set will override standard
#use figure with the figsize keyword to set dimensions
sns.set(style="darkgrid", palette="gist_rainbow",font_scale = 2, rc={'figure.figsize':(20,10)})
#Load the data from pd Dataframe created from the average lists in previous benchmarking steps
#If bubble sort data is omitted, the results of the other algorithms can be seen more clearly.
bubble = sns.lineplot( x="Size", y="Bubble Sort", data=df, marker='o', label="Bubble Sort")
merge = sns.lineplot( x="Size", y="Merge Sort", data=df, marker=">", label="Merge Sort")
insertion = sns.lineplot( x="Size", y="Insertion Sort", data=df, marker=">",  label="Insertion Sort")
counting = sns.lineplot( x="Size", y="Counting Sort", data=df, marker=">", label="Counting Sort")
tim= sns.lineplot( x="Size", y="Tim Sort", data=df, marker=">",label="Tim Sort")
#Insert instruction for axes and plot title
plt.xlabel('Random Array size n', fontsize=20)
plt.ylabel('Running Time in milliseconds',fontsize=20)
plt.title(title, fontsize=26)

# Call show to display data visualisation
plt.show()

#Code adapted from https://github.com/RitRa/Algorithms-project-
#give the plot a Title
title="Benchmarking Sorting Algorithms"
#Set aesthetic parameters
#use of darkgrid and rainbow palettefor contrast
#rc ‘run command’ used with sns.set will override standard
#use figure with the figsize keyword to set dimensions
sns.set(style="darkgrid", palette="gist_rainbow",font_scale = 2, rc={'figure.figsize':(20,10)})
#Load the data from pd Dataframe created from the average lists in previous benchmarking steps
#If bubble sort data is omitted, the results of the other algorithms can be seen more clearly.
#bubble = sns.lineplot( x="Size", y="Bubble Sort", data=df, marker='o', label="Bubble Sort")
merge = sns.lineplot( x="Size", y="Merge Sort", data=df, marker=">", label="Merge Sort")
insertion = sns.lineplot( x="Size", y="Insertion Sort", data=df, marker=">",  label="Insertion Sort")
counting = sns.lineplot( x="Size", y="Counting Sort", data=df, marker=">", label="Counting Sort")
tim= sns.lineplot( x="Size", y="Tim Sort", data=df, marker=">",label="Tim Sort")
#Insert instruction for axes and plot title
plt.xlabel('Random Array size n', fontsize=20)
plt.ylabel('Running Time in milliseconds',fontsize=20)
plt.title(title, fontsize=26)

# Call show to display data visualisation
plt.show()





    
