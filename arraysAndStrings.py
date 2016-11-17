from collections import defaultdict, Counter

def isUnique(s):
	"""
	Returns True if all characters in a string are distinct, False otherwise.
	Time complexity: O(n)
	Space complexity: O(n)
	"""
	soFar = defaultdict()
	for c in s:
		if c in soFar:
			return False
		else:
			soFar[c] = True
	return True

def isUniqueTwo(s):
	"""
	Returns True if all characters in a string are distinct, False otherwise.
	Time complexity: O(n)
	Space complexity: O(128) = O(1), arguably so
	"""
	# preliminary heuristic
	if len(s) > 128:
		return False

	seen = [False] * 128
	for c in s:
		if seen[ord(c)-1]:
			return False
		seen[ord(c)-1] = True
	return True

def ridSpace(s):
	"""
	Given a string s, returns the string without the spaces.
	"""
	normalized = ""
	for c in s:
		if c != " ":
			normalized += c
	return normalized

def isPermutation(s, t):
	"""Case sensitive, spaces don't matter
    (i.e. 'dog' is not a permutation of 'God   ' or 'God'). """
	normalizedS = ridSpace(s)
	normalizedT = ridSpace(t)

	if len(normalizedS) != len(normalizedT):
		return False

	sortedS = sorted(normalizedS)
	sortedT = sorted(normalizedT)
	for i in range(len(normalizedS)):
		if sortedS[i] != sortedT[i]:
			return False
	return True

def isPermutationTwo(s, t):
	"""Case-sensitive, spaces matter
    (i.e. 'dog' is a permutation of 'God' and 'God   ')."""
	if len(s) != len(t):
		return False
	countedS = Counter(s)
	countedT = Counter(t)
	for i in range(len(countedS.items())):
		if countedS.items()[i] != countedT.items()[i]:
			return False
	return True

def replaceSpace(s):
	"""Makes a copy."""
	# get rid of blank spaces at the end of s
	modifiedS = s
	j = len(s) - 1
	while j >= 0:
		if s[j] != " ":
			break
		else:
			modifiedS = modifiedS[:-1] 
		j -= 1

	condensed = ""
	i = 0
	counter = 0
	while i < len(modifiedS):
		# if the space is the first space of the space chunk
		if modifiedS[i] == " " and counter == 0:
			condensed += "%20"
			counter += 1
		elif modifiedS[i] == " ":
			counter += 1
		else:
			condensed += modifiedS[i]
			counter = 0
		i += 1
	return condensed

def replaceSpaceTwo(s):
	"""Replaces spaces with %20 in place."""
	j = len(s) - 1
	
	# Rid spaces at the end of s
	while j >= 0:
		if s[j] != " ":
			break
		else:
			s = s[:-1]
		j -= 1

	s = list(s)

	firstSpace = True

	for i in range(len(s)): # Need fixing
		if s[i] == " " and firstSpace:
			s[i] = "%20"
			firstSpace = False
		# not the first space
		elif s[i] == " ":
		 	s[i] = ""
		else:
			firstSpace = True

	return "".join(s)

def compress(s):
	newSize = numCompression(s)
	
	# if the original string is shorter than the compressed version
	if len(s) < newSize:
		return s

	charArray = [None] * newSize
	counter = 1
	arrayIndex = 0

	for i in range(len(s)-1):
		if s[i] != s[i+1]:
			charArray[arrayIndex] = s[i]
			charArray[arrayIndex+1] = str(counter)
			arrayIndex += 2
			counter = 1
		else:
			counter += 1

	# Account for the last character
	if charArray[-1] is None:
		charArray[-2] = s[-1]
		charArray[-1] = str(counter)

	return ''.join(charArray)

def numCompression(s):
	size = len(s)
	# Accounting for the first character of s
	size += 1
	for i in range(1, len(s)):
		if s[i] != s[i-1]:
			size += 1
		else:
			size -= 1
	return size

def makeZero(M):
	rowIndices = []
	colIndices = []
	
	# find the indices of rows and columns that need to be changed
	for i in range(len(M)):
		if 0 in M[i]:
			colIndices += [k for k, val in enumerate(M[i]) if val == 0]
			rowIndices.append(i)
	
	# change the rows
	for row in rowIndices:
		for j in range(len(M[0])):
			M[row][j] = 0

	# change the columns
	for col in colIndices:
		for j in range(len(M)):
			M[j][col] = 0

	return M

def isRotation(s, t):
	"""Returns True if s is a rotation of t, False otherwise."""
	if len(s) != len(t):
		return False
	temp = s+s
	return isSubstring(t, temp)

def isSubstring(s, t):
	"""Returns True if s is a substring of t, False otherwise."""
	return s in t


from collections import defaultdict, Counter

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

def findRankNoDuplicates(self, A):
    """
    @param A: string
    Returns the rank of the string amongst its permutations sorted lexicographically.
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
    rank = 1
    
    # create a dynamic programming table for factorials
    n = len(A)
    
    # base cases
    if n < 2:
        return rank
    
    Factorials = [None] * n
    Factorials[0] = 1
    Factorials[1] = 1
    # for n time, append to an empty list such that the ith element equals i!
    for i in range(2, n): # 2, 3, ..., n-1
        Factorials[i] = Factorials[i-1] * i
    
    # create a list "Available" which keeps the characters of A in a sorted order
    Available = sorted(A)
    
    numChars = Counter(A)

    # starting from the first letter, loop through each character
    for c in A:
        # if it's not the "optimal" choice (decided by comparing to the first letter in Available), 
        if c != Available[0]:
            # compute the number of (unique) characters that could have been a better choice
            numBetterChar = len(set(Available[0:Available.index(c)]))
            possibilities = Factorials[len(Available)-1]
            # account for duplicates
            numChars[Available[0]] -= 1
            for j in numChars.values():
                possibilities = possibilities/Factorials[j]
            numChars[Available[0]] += 1
            
            rank += possibilities*numBetterChar
            
        Available.remove(c)
        numChars[c] -= 1
    
    return rank % 1000003

def longestCommonPrefix(A):
    # base case
    if len(A) == 1:
        return A[0]
        
    lcp = min(A, key=len)
    
    for strings in A:
        for i in range(len(lcp)):
            if i > len(strings)-1 or i > len(lcp)-1:
                break
            if strings[i] != lcp[i]:
                lcp = lcp[:i]
    
    return lcp

def editDistance(N, M):
    if N == M:
        return 0
    else:
        if len(N) == 0:
            return 2*len(M)
        if len(M) == 0:
            return 2*len(N)
        else:
            while N[-1] == M[-1]:
                N = N[:-1]
                M = M[:-1]
            return min(editDistance(N[:-1], M[:-1])+3,
                        editDistance(N, M[:-1]) + 2,
                        editDistance(N[:-1], M) + 2)

def isInterleave(A, B, C):
    if len(A) + len(B) != len(C):
        print "case 0"
        return 0
    
    listA = list(A)
    listB = list(B)
    listC = list(C)
    
    while listC:
        if len(listA) == 0:
            if listB == listC:
                return 1
            print "case 1"
            return 0
            
        if len(listB) == 0:
            if listA == listC:
                return 1
            print "case 2"
            return 0
        
        else:
            if listC[0] == listA[0]:
                listA = listA[1:]
            
            elif listC[0] == listB[0]:
                listB = listB[1:]
            
            else:
                print "case 3"
                print "listA ", listA, "\n"
                print "listB ", listB, "\n"
                print "listC ", listC, "\n"
                return 0
        
        listC = listC[1:]
    
    return 1