
# WEEK 3 

# QuickSort - Programming Assignment

numbers = "quicksort.txt"

print ("Loading word list from file...")
# inFile: file
inFile = open(numbers, 'r')
# wordlist: list of strings
numlist = []
for line in inFile:
	numlist.append(int(line.strip()))
print ("  ", len(numlist), "numbers loaded.")

# Q1 - PIVOT STARTS IN THE BEGINNING EVERYTIME

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin, end):
    if begin >= end:
        return array
    global count
    count += len(array[begin:end])   
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)
    return array, count

# answer = 162085

# # Q2 - PIVOT BEGINS IN THE END!

# def partition(array, begin, end):
#     array[begin], array[end] = array[end], array[begin]
#     pivot = begin
#     for i in range(begin+1, end+1):
#         if array[i] <= array[begin]:
#             pivot += 1
#             array[i], array[pivot] = array[pivot], array[i]
#     array[pivot], array[begin] = array[begin], array[pivot]
#     return pivot

#     # implement the below only when begin and end elements are not swapped.

#     # for i in reversed(range(begin, end)):
#     #     if array[i] >= array[end]:
#     #         pivot = pivot - 1
#     #         array[i], array[pivot] = array[pivot], array[i]
#     # array[pivot], array[end] = array[end], array[pivot]
#     # return pivot


# def quicksort(array, begin, end):
#     if begin >= end:
#         return array
#     global count
#     count += len(array[begin:end])   
#     pivot = partition(array, begin, end)
#     quicksort(array, begin, pivot-1)
#     quicksort(array, pivot+1, end)
#     return array, count

# answer = 164123

# Q3 - PIVOT IS THE MEDIAN ELEMENT!

# def partition(array, begin, end):
#     myarray = array[begin:end+1]
#     first = array[begin]
#     last = array[end]
#     if len(myarray)%2 == 0:
#         middle = myarray[(len(myarray)//2)-1]
#     else: middle = myarray[len(myarray)//2]
#     if  (first-middle)*(last-middle) < 0:
#         median = middle
#     elif (middle-first)*(last-first) < 0:
#         median = first
#     else: median = last
#     medianindex = array.index(median)
#     array[begin], array[medianindex] = array[medianindex], array[begin]
#     pivot = begin
#     for i in range(begin+1, end+1):
#         if array[i] <= array[begin]:
#             pivot += 1
#             array[i], array[pivot] = array[pivot], array[i]
#     array[pivot], array[begin] = array[begin], array[pivot]
#     return pivot


# def quicksort(array, begin, end):
#     if begin >= end:
#         return array
#     global count
#     count += len(array[begin:end])     
#     pivot = partition(array, begin, end)
#     quicksort(array, begin, pivot-1)
#     quicksort(array, pivot+1, end)
#     return array, count

# answer = 138382

array = [3,3,2,5,1,4,7,6]
count = 0
print(quicksort(numlist, 0, (len(numlist) - 1)))


# pseudocode for finding the ith element in linear time
