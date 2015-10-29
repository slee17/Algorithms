from collections import defaultdict

class Scrabble:
    WORDS = defaultdict(list)
    DICT_PATH = "/usr/share/dict/words"

    def buildMap():
        global WORDS
        with open(DICT_PATH) as f:
            content = f.readlines()
        for word in content:
            word = word.strip('\n')
            sortedWord = ''
            L = sorted(word)
            sortedWord = sortedWord.join(L)
            WORDS[sortedWord].append(word)
        return WORDS

    def wordPerms(s):
        """
        Returns all words in the dictionary that can be created with the letters of s.
        """
        sortedWord = ''
        L = sorted(s)
        sortedWord = sortedWord.join(L)
        return WORDS[sortedWord]

class Perms:
    def allPerms(s):
        """
        Returns all possible permutations of a word.
        """
        # Using the built-in function:
        # import itertools
        # itertools.permutations(s)
        if len(s) <= 1:
            yield s
        else:
            for perm in allPerms(s[1:]):
                for i in range(len(s)):
                    yield perm[:i] + s[0:1] + perm[i:]

    def permsOfLength(s, n):
        """
        Returns all possible strings of size n made from the letters of s.
        """
        assert n <= len(s)
        allPerms = []
        if n < 1:
            return allPerms
        if n == 1:
            return list(s)
        # cloud, 3 -> permsOfLength('loud', 2), lo, lu, ld, ol, ou, od, dl, do, du
        # lo -> clo, lco, loc
        for perm in permsOfLength(s[1:], n-1): # lou / (ow, 1)
            for i in range(n): # range(3) -> 0, 1, 2, lo
                temp = perm[:i] + s[0] + perm[i:] # clo, lco, loc
                if temp not in allPerms:
                    allPerms.append(temp)
        return allPerms

def factorialsDP(n):
    """
    @param n: integer
    Returns n! in linear time. Helper for findRank.
    """
    # create a dynamic programming table for factorials
    Factorials = [None] * n
    Factorials[0] = 1
    Factorials[1] = 1
    # for n time, append to an empty list such that the ith element equals i!
    for i in range(2, n): # 2, 3, ..., n-1
        Factorials[i] = Factorials[i-1] * i

def findRanknoDuplicates(self, A):
    """
    @param A: string
    eturns the rank of the string amongst its permutations sorted lexicographically.
    This function assumes that there are no duplicates in the string.
    The answer might not fit in an integer, so return answer % 1000003.
    """
    rank = 1
    n = len(A)
    
    # base case
    if n == 0 or n == 1:
        return rank
    
    # create a dynamic programming table for factorials
    Factorials = [None] * n
    Factorials[0] = 1
    Factorials[1] = 1
    # for n time, append to an empty list such that the ith element equals i!
    for i in range(2, n): # 2, 3, ..., n-1
        Factorials[i] = Factorials[i-1] * i
    
    # create a list "Available" which keeps the characters of A in a sorted order
    Available = sorted(A)
    
    # starting from the first letter, loop through each character
    for c in A:
        # if it's not the "optimal" choice (decided by comparing to the first letter in Available), 
        if c != Available[0]:
            for j in range (Available.index(c)):
                possibilities = Factorials[len(Available)-1]
                rank += possibilities
        Available.remove(c)
    
    return rank % 1000003

def findRank(A):
    """
    @param A: string
    Returns the rank of the string amongst its permutations sorted lexicographically.
    In case of repeated characters, must look at the rank in unique permutations.
    e.g. input: 'aba', output: 2
    The answer might not fit in an integer, so return answer % 1000003.
    """
    # need debugging
    rank = 1
    n = len(A)
    
    # base case
    if n == 0 or n == 1:
        return rank
    
    # create a dynamic programming table for factorials
    Factorials = [None] * n
    Factorials[0] = 1
    Factorials[1] = 1
    # for n time, append to an empty list such that the ith element equals i!
    for i in range(2, n): # 2, 3, ..., n-1
        Factorials[i] = Factorials[i-1] * i
    
    # create a list "Available" which keeps the characters of A in a sorted order
    Available = sorted(A)
    
    # find number of elements that are not unique
    # create a dictionary with elements and their number of occurrence
    numElements = defaultdict(int)
    for c in A:
        numElements[c] += 1
    
    # starting from the first letter, loop through each character
    for c in A:
        # if it's not the "optimal" choice (decided by comparing to the first letter in Available), 
        if c != Available[0]:
            possibilities = Factorials[len(Available)-1]
            numElements[Available[0]] -= 1 
            for num in numElements.values():
                possibilities = possibilities/Factorials[num]
            # compute the number of possibilities had we chosen that optimal choice and add that number to rank
            # e.g. cccba -> ccba: 4!/2!, cbbcca -> bbcca: 5!/2!2!
            # find (n-1)!, find all elements that are not unique
            rank += possibilities
            # add back
            numElements[Available[0]] += 1
        Available.remove(c)
        numElements[c] -= 1
    
    return rank % 1000003

"""
TESTING FUNCTIONS
"""
#def testFactorials

if __name__ == "__main__":
    #buildMap()
    #print wordPerms('actor')
    #print permsOfLength('cow', 2)
    print findRank('baa') # aab, aba, baa rank 3