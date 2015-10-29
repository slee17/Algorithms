"""@package Algorithms
"""

"""COMMAND-LINE USAGE

   python scripts.py runs all the necessary tests (including tests for correctness
    and running time)

   python scripts.py time <size> <experiments> <k>
                --- Times the four algorithms with a shuffled array of the given
                    <size>, for averaging over <experiments> experiments.
                    If <size> is omitted, the default is 20.
                    If <experiments> is omitted, the default is 3.
"""

import random
import sys
import time

# DEFAULT VALUES
DEFAULT_SIZE = 20
DEFAULT_EXPERIMENTS = 3
DEFAULT_K = 3

from quicksort import quicksort

def sortFind(n, k):
    """Sorts the sequence, and copies out the largest k values.
        @param n: An unsorted array
        @param k: The number of largest elements to be printed
    """
    quicksort(n)
    print n[-k:] # largest k values are the last k elements in the sorted array

def partitionFind(n, k):
    """
    Uses a Randomized Selection algorithm to find and Partition around
    the k-th largest item and copies out the highest k values.
    """
    kthLargest = select(n, k)
    a = n.index(kthLargest)
    # swap
    n[a] = n[-1]
    n[-1] = kthLargest
    decreasingPartition(n, 0, len(n)-1)
    print n[:n.index(kthLargest)+1]

def insertionSort(n):
   for i in range(1,len(n)):
     current = n[i]
     while i>0 and n[i-1]<current:
         n[i]=n[i-1]
         i = i-1
     n[i]=current

def maxHeapFind(n, k):
    """
    Efficiently reorders the n items (in place) into a max heap, and repeatedly
    pulls out the maximum element k times.
    Precondition: k <= n
    """
    returnList = []
    buildHeap(n, "max")
    if (k > n):
        "Cannot extract more elements than what is in the heap. Please enter a \
        new k that is smaller than or equal to the size of n."
    for counter in range(k):
        (max, newN) = extractMax(n)
        if max != -1:
            returnList.append(max)
        n = newN
    return returnList

def minHeapFind(n, k):
    """
    Puts the first k items into a min heap, which will be our collection of
    the k largest items seen so far. Iterate through the remaining n - k
    items, comparing each value x with the current minimum value m
    in the heap; if x is strictly larger, then replace m by x in the heap
    (maintaining the heap invariants!). Return the final heap contents.
    """
    m = n[:k]
    buildMinHeap(m)
    for x in n[k:]:
        if x > m[0]:
            m[0] = x
            minPercolateDown(m, 0)
    return m

"""
HELPER FUNCTIONS
"""
def select(n, k):
    """
    Find the kth largest element from an unsorted array n.
    Partition the array by pivoting on the Bmedian.
    If k <= n/2, recursively select from the lower half.
    If k > n/2, select item (i - n/2) from the upper half.
    """
    # partition the elements of the array n into groups of size 5 and
    # sort each group of 5 in increasing order.
    i = 0
    partitionSorted = []
    b = [] # holds the medians of groups of size 5
    while i+5 < len(n):
        a = n[i:i+5]
        insertionSort(a)
        for m in range (0, 5):
            partitionSorted.append(a[m])
        b.append(a[2])
        i = i+5
    if i != len(n): # if there are left-over elements that have not been sorted
        a = n[i:]
        insertionSort(a)
        for m in range(len(a)):
            partitionSorted.append(a[m])
        b.append(a[len(a)/2])

    # find the median of these groups of 5 (i.e. find Bmedian of n)
    insertionSort(b)
    Bmedian = b[len(b)/2]
    
    BmedianIndex = n.index(Bmedian)
    # swappping the indices of Bmedian and the last element
    n[BmedianIndex] = n[-1]
    n[-1] = Bmedian
    # now call the partition function so that everything before BmedianInPartitioned
    # <= Bmedian, everything after >Bmedian
    BmedianInPartitioned = decreasingPartition(n, 0, len(n)-1)

    if BmedianInPartitioned+1 == k: # lucky! we've found the kth largest
        return Bmedian
    elif BmedianInPartitioned < k:
        return select(n[BmedianInPartitioned+1:], k-(BmedianInPartitioned+1))
    else: # BmedianInPartitioned > k
        return select(n[:BmedianInPartitioned], k)

def decreasingPartition(a, p, r):
    """
    Permutes the elements of a[p..r] (inclusive) in-place:
       first elements > a[r], then a[r], then those <= a[r].
    Returns the new location (index) of pivot value a[r] in the array.
    """
    i = p - 1
    for j in range(p, r):
        if a[j] >= a[r]:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

def extractMax(n):
    """
    Extracts the max element of a heap n. Note that n must already be heapsorted.
    """
    # base case
    if len(n) < 1:
        return

    # save the root's value
    root = n[0]

    # take and put the last element of the tree at the root
    n[0] = n[len(n)-1]
    n = n[:-1]

    # adjust to maintain heap property
    maxPercolateDown(n, 0)
    return (root, n)

def buildHeap(n, ordering):
    for i in range(len(n), -1, -1):
        if isLeaf(n, i):
            continue    # a leaf is already a heap
        elif ordering == "max":
            maxPercolateDown(n, i)
        elif ordering == "min":
            minPercolateDown(n, i)

def isLeaf(n, k):
    """
    Returns true if the kth element of n is a leaf, false otherwise.
    """
    if 2*k+1 > len(n):
        return True
    return False

def maxPercolateDown(n, k):
    """
    Percolates down the kth element in n to the right index (according to max heap order).
    Note that maxPercolateDown does not do anything if there is no need to percolate
    the kth element down (i.e. the kth element is already heap-sorted in relation
    to its children).
    """
    leftChild = 2*k+1
    rightChild = 2*k+2

    if leftChild >= len(n): # we're at a leaf, so we're done
        return

    # find the largest of k, its left child, and its right child
    if rightChild >= len(n): # if there's only one leaf
        if n[leftChild] > n[k]: # compare just the left child and the root
            largest = leftChild
        else:
            largest = k
    elif n[leftChild] > max(n[rightChild], n[k]):
        largest = leftChild
    elif n[rightChild] > max(n[leftChild], n[k]):
        largest = rightChild
    else:
        largest = k

    # if the trio we are looking at is already heap-sorted, we're done
    if largest == k:
        return

    # otherwise swap the values and recurse
    else:
        temp = n[k]
        n[k] = n[largest]
        n[largest] = temp
        maxPercolateDown(n, largest)

def buildMinHeap(n):
    for i in range(len(n), -1, -1):
        if isLeaf(n, i):
            continue    # a leaf is already a heap
        else:
            maxPercolateDown(n, i)

def minPercolateDown(n, k):
    """
    Percolates down the kth element in n to the right index (according to min heap order).
    Note that minPercolateDown does not do anything if there is no need to percolate
    the kth element down (i.e. the kth element is already heap-sorted in relation
    to its children).
    """
    leftChild = 2*k+1
    rightChild = 2*k+2

    if leftChild >= len(n): # we're at a leaf, so we're done
        return

    # find the smallest of k, its left child, and its right child
    if rightChild >= len(n): # if there's only one leaf
        if n[leftChild] < n[k]: # compare just the left child and the root
            smallest = leftChild
        else:
            smallest = k
    elif n[leftChild] < min(n[rightChild], n[k]):
        smallest = leftChild
    elif n[rightChild] < min(n[leftChild], n[k]):
        smallest = rightChild
    else:
        smallest = k

    # if the trio we are looking at is already heap-sorted, we're done
    if smallest == k:
        return

    # otherwise swap the values and recurse
    else:
        temp = n[k]
        n[k] = n[smallest]
        n[smallest] = temp
        minPercolateDown(n, smallest)

"""
TESTING CODES
"""
def insertionSortTest():
    n = [12, 3, 1, 6, 3, 50, 10, 29, 20, 5, 2]
    insertionSort(n)
    print n

def partitionTest():
    n = [12, 3, 1, 6, 3, 50, 10, 29, 20, 5, 2]
    partition(n, 0)
    print n

def buildHeapTest():
    n = [12, 3, 1, 6, 3, 50, 10, 29, 20, 5, 2]
    buildHeap(n, "max")
    print n
    buildHeap(n, "min")
    print n

def dTest():
    n = [12, 3, 1, 6, 3, 50, 10, 29, 20, 5, 2]
    print d(n, 3)

# NOTE: the below codes were taken largely from the given quicksort.py file
def random_array(n):
    """
    Returns an n-element array containing 0..(n-1) in random order
    """
    new_array = range(n)
    random.shuffle(new_array)
    return new_array

def check_algorithms(size=DEFAULT_SIZE):
    """
    Create a random array of length size, and make sure that
    our algorithm returns the kth largest values.
    This test checks the correctness of each algorithm by printing out n and k,
    for human inspection.
    """
    print "running the algorithms on %d items: " % size,
    sys.stdout.flush()  # make sure the previous line is displayed now,
                        # rather than waiting for the end-of-line character

    array = random_array(size)
    k = DEFAULT_K
    a(array, k)
    print"a result: the given array was ", array, " and the %d largest elements were: " % k, a(array,k)
    
    b(array, k)
    print"b result: the given array was ", array, " and the %d largest elements were: " % k, a(array,k)
    
    c(array, k)
   
    print"c result: the given array was ", array, " and the %d largest elements were: " % k, a(array,k)
    
    d(array, k)
    print"d result: the given array was ", array, " and the %d largest elements were: " % k, a(array,k)

"""
TIMING CODE
"""

def time_a(size=DEFAULT_SIZE, experiments=DEFAULT_EXPERIMENTS, k=DEFAULT_K):
    arrays = [random_array(size) for _ in range(experiments)]
    print "time to return %d largest items using a" % (DEFAULT_K)
    sys.stdout.flush()  # make sure the previous line is displayed now,
                        # rather than waiting for the end-of-line character

    start = time.clock()    # start the timer
    for b in arrays:
        a(b, k)
    end = time.clock()      # stop the timer

    elapsed = end - start
    average = elapsed / experiments
    print average, " seconds"

    return average

def time_b(size=DEFAULT_SIZE, experiments=DEFAULT_EXPERIMENTS, k=DEFAULT_K):
    # arrays = [random_array(size)]
    arrays = [random_array(size) for _ in range(experiments)]
    print "time to return %d largest items using b" % (DEFAULT_K)
    sys.stdout.flush()  # make sure the previous line is displayed now,
                        # rather than waiting for the end-of-line character

    start = time.clock()    # start the timer
    for array in arrays:
        b(array, k)
    end = time.clock()      # stop the timer

    elapsed = end - start
    average = elapsed / experiments
    print average, " seconds"

    return average

def time_c(size=DEFAULT_SIZE, experiments=DEFAULT_EXPERIMENTS, k=DEFAULT_K):
    # arrays = [random_array(size)]
    arrays = [random_array(size) for _ in range(experiments)]
    print "time to return %d largest items using c" % (DEFAULT_K)
    sys.stdout.flush()  # make sure the previous line is displayed now,
                        # rather than waiting for the end-of-line character

    start = time.clock()    # start the timer
    for array in arrays:
        c(array, k)
    end = time.clock()      # stop the timer

    elapsed = end - start
    average = elapsed / experiments
    print average, " seconds"

    return average

def time_d(size=DEFAULT_SIZE, experiments=DEFAULT_EXPERIMENTS, k=DEFAULT_K):
    # arrays = [random_array(size)]
    arrays = [random_array(size) for _ in range(experiments)]
    print "time to return %d largest items using d" % (DEFAULT_K)
    sys.stdout.flush()  # make sure the previous line is displayed now,
                        # rather than waiting for the end-of-line character

    start = time.clock()    # start the timer
    for array in arrays:
        d(array, k)
    end = time.clock()      # stop the timer

    elapsed = end - start
    average = elapsed / experiments
    print average, " seconds"

    return average


def default_test():
    """
    Does some default checking and timing operations.
    """
    check_algorithms()
    for (size, k) in [(1000, 5), (5000, 10), (10000, 30)]:
        time_a(size, k)
        time_b(size, k)
        time_c(size, k)
        time_d(size, k)

"""
MAIN FUNCTION
"""

def process(arguments):
    """
    Process the command-line, and run appropriate test routines.
    """
    if len(sys.argv) == 1:
        # No command-line arguments other than the name of this python program.
        # Do the default thing, which is some checking and some timing
        default_test()

    elif sys.argv[1] == "time":
        # The command-line argument says we want to time the algorithms on
        # a randomly shuffled input

        # if there's a number following the word "time", that's the
        # array size to use.  Otherwise, we use a default value.
        if len(sys.argv) >= 3:
            size = int(sys.argv[2])
        else:
            size = DEFAULT_SIZE

        # If there's a number following the array size, that's the
        # number of trials to run. Otherwise we use a default value.
        if len(sys.argv) >= 4:
            experiments = int(sys.argv[3])
        else:
            experiments = DEFAULT_EXPERIMENTS

        # If there's a number following the number of experiments, that's the
        # k for k largest elements. Otherwise we use a default value.
        if len(sys.argv) >= 5:
            k = int(sys.argv[4])
        else:
            k = DEFAULT_K

        time_a(size, experiments, k)
        time_b(size, experiments, k)
        time_c(size, experiments, k)
        time_d(size, experiments, k)

    else:
        print "unrecognized argument: ", sys.argv[2]


if __name__ == "__main__":
    process(sys.argv)
