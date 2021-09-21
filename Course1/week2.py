#  PA - 1

NUM_FILENAME = "IntegerArray.txt"

def load_words():

	print ("Loading word list from file...")
	# inFile: file
	inFile = open(NUM_FILENAME, 'r')
	# wordlist: list of strings
	numlist = []
	for line in inFile:
		# numlist.append(line.strip().lower())
		numlist.append(int(line.strip()))
	print ("  ", len(numlist), "numbers loaded.")
	return numlist

intlist = load_words()

def mergesort(lst):
	'''Recursively divides list in halves to be sorted'''
	if len(lst) == 1:
		return lst, 0

	middle = len(lst)//2
	#sorting the first half of list and keeping count of the
	# number of inversions
	left,s1  = mergesort(lst[:middle])
	#sorting the second half of list and keeping count of the
	# number of inversions   
	right,s2 = mergesort(lst[middle:])
	# sorting the entire array and keeping count of the number
	# of split inversions across the two arrays 
	sortedlist, inversions  = merge(left, right)
	# returns the sorted list and the total number of inversions
	# (across the split arrays and within the two arrays) 
	return sortedlist, s1+s2+inversions

def merge(left, right):
	'''Subroutine of mergesort to sort split lists.  Also returns number
	of split inversions (i.e., each occurence of a number from the sorted second
	half of the list appearing before a number from the sorted first half)'''
	i, j = 0, 0
	result = []
	inversions = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			inversions = inversions + len(left[i:])
	result += left[i:]
	result += right[j:]
	return result, inversions

print(mergesort(intlist))
# answer = 2407905288


# OPTIONAL THEORY PROBLEMS IMPLEMENTATION

# FIND SECOND LARGEST NUMBER IN DATA

def findsecondlargest(lst, seconds):
	if len(lst) == 2:
		# print('reached base case', lst)
		if lst[0] > lst[1]: 
			if lst[1] > seconds: return lst[1]
			return seconds
		else: 
			if lst[0] > seconds: return lst[0]
			return seconds
	else:
		largest = []
		i = 0
		while i < len(lst):
			if lst[i] > lst[i+1]: 
				largest.append(lst[i])
				if lst[i+1] > seconds: seconds = lst[i+1]
			else: 
				largest.append(lst[i+1])
				if lst[i] > seconds: seconds = lst[i]
			i+= 2
		secondlargest = findsecondlargest(largest, seconds)
		return secondlargest


# print(findsecondlargest([11,3,28, 109, 4, 7, 34, 78], 0))

# def maxunimodal(lst):
# 	mid = len(lst)//2
# 	if  lst[mid-1] < lst[mid] > lst[mid+1]:
# 		return lst[mid]
# 	elif lst[mid] < lst[mid+1]:
# 		updatedlist = lst[mid:]
# 		return maxunimodal(updatedlist)
# 	else:
# 		updatedlist = lst[:mid+1]
# 		return maxunimodal(updatedlist)

# print(maxunimodal([1,3,4,5,7,8,10,12,13,14,15,10,9,6,2,1]))

# def indexvalmatch(lst, low, high):
# 	mid = (low+high)//2 
# 	print('start mid', mid)
# 	if lst[mid] == mid:
# 		return mid

# 	while  low != high:
# 		if lst[mid] - mid == 0:
# 			return mid
# 		elif mid < lst[mid]:
# 			high = mid - 1
# 			return indexvalmatch(lst, low, high)
# 		else:
# 			low = mid + 1	
# 			return indexvalmatch(lst, low, high)

	
# 	print('its a no go')
# 	return

# lst = [-3, -4, 4 ,5, 7, 8, 9]
# low = 0
# high = len(lst)
# print(indexvalmatch(lst, low, high))


# value = 439
# remainder = str(value%2)
# while (value//2) >0:
# 	value = value//2
# 	remainder = str(value%2) + remainder
 
# count = 0
# maxc = 0
# index  = 0
# for values in remainder:
# 	index += 1
# 	if values == str(1): count += 1
# 	if values == str(0) or index == len(remainder):
# 	# else: 
# 		if count > maxc:
# 			maxc = count
# 		count = 0
# print(maxc)


# print(remainder)