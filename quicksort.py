import random

# DEFAULT VALUES
DEFAULT_SIZE = 10000
DEFAULT_EXPERIMENTS = 5

# RANDOMIZED QUICKSORT
def partition(a, p, r):
    """Permutes the elements of a[p..r] (inclusive) in-place: first elements <= a[r], then a[r],
    then those > a[r]. Returns the new location (index) of pivot value a[r] in the array."""
    i = p - 1
    for j in range(p, r):
        if a[j] <= a[r]:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def randomized_partition(a, p, r):
    """Moves a random value from a[p..r] (inclusive) into the pivot position a[r], and then partitions
    relative to that pivot value."""
    m = random.randint(p, r)
    a[m], a[r] = a[r], a[m]
    return partition(a, p, r)

def rquicksort(a, p, r):
    """Sorts the given array a[p..r] (inclusive) in-place using the randomized Quicksort algorithm."""
    if p < r:
        q = randomized_partition(a, p, r)
        rquicksort(a, p, q-1)
        rquicksort(a, q+1, r)

def quicksort(a):
    """Sorts the given array a in-place using the randomized Quicksort algorithm."""
    rquicksort(a, 0, len(a)-1)