"""
package Algorithms
author Rachel Lee
"""

import random

# DEFAULT VALUES
DEFAULT_SIZE = 20
DEFAULT_NUMTEST = 5

def quicksort(A, p, r):
	"""
	quicksort sorts the array in place, by selecting the element at r to be the
	pivot and partitioning the remaining items into two subgroups: those smaller
	than the pivot and those larger than the pivot, then recursing on the subgroups.
	This algorithm runs in \Theta(n^2) in the worst case, and \Theta(nlogn) in
	the best case, where n is the number of elements in A.
		param A: array to be sorted
		param p: the index of the first element in the array being sorted
		param r: the index of the last element in the array being sorted (i.e. the pivot)
	"""

def partition(A, p, r):
	"""
	partition partitions the array into two groups: those smaller than r and
	those greater than r.
		param A: array to be partitioned
		param p: the index of the first element in the array to be partitioned
		param r: the index of the pivot element in the array to be partitioned (i.e. the pivot)
	"""
	i = p-1
	for j in range(p, r):
		if A[j] <= A[r]:
			i+=1
			swap(A[i], A[j])
	swap(A[i+1], A[r])
	return (i+1, A)

def swap(n, m):
	temp = n
	n = m
	m = temp

def mergeSort(A):
	assert len(A) >= 0

	# base cases
	if len(A) == 0 or len(A) == 1:
		return A
	
	# splitting
	mid = len(A)/2
	leftHalf = A[:mid]
	rightHalf = A[mid:]
	mergeSort(leftHalf)
	mergeSort(rightHalf)

	# merging
	i = 0
	j = 0
	k = 0
	while i<len(leftHalf) and j<len(rightHalf):
		if leftHalf[i] < rightHalf[j]:
			A[k] = leftHalf[i]
			i += 1
		else:
			A[k] = rightHalf[j]
			j += 1
		k += 1
	while i<len(leftHalf):
		A[k] = leftHalf[i]
		i += 1
		k += 1
	while j<len(rightHalf):
		A[k] = rightHalf[j]
		j += 1
		k += 1

	return A

def insertionSort(A):
	for index in range(1, len(A)):
		current = A[index]
		position = index

		while position > 0 and A[position-1]>current:
			A[position] = A[position-1]
			position = position-1

		A[position] = current

	return A

# TEST CODE
def randomArray(n):
    """
    Returns an n-element array containing 0..(n-1) in random order.
    """
    newArray = range(n)
    random.shuffle(newArray)
    return newArray

def partitionTest(size=DEFAULT_SIZE, numTest=DEFAULT_NUMTEST):
	arrays = [randomArray(size) for _ in range(numTest)]
	for array in arrays:
		print "Array %d before partition: " % arrays.index(array), array
		p = random.randint(0, size)
		r = array[-1]
		pivot = array[r] # save the pivot value for testing
		(pivotPosition, partitioned) = partition(array, p, r)
		# print out the results
		print "Array %d after partition: " % arrays.index(array), partitioned
		for i in range(0, pivotPosition):
			if partitioned[i] > pivot:
				print "INCORRECT: partition didn't work. Problem found at %d." % i
		if partitioned[pivotPosition] != pivot:
			print "INCORRECT: partition didn't work. The pivot is out of place."
		for i in range(pivotPosition+1, size):
			if partitioned[i] < pivot:
				print "INCORRECT: partition didn't work. Problem found at %d." % i

if __name__ == '__main__':
	A = [1,4,2,5,3]
	insertionSort(A)
	print A
	#print partition(A, 0, len(A))
	#partitionTest()
