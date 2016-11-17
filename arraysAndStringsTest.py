from arraysAndStrings import *

def isInterleaveTest():
    A = "eZCHXr0CgsB4O3TC DlitYI7kH38rEElI"
    B = "UhSQsB6 CWAHE6zzphz5BIAHqSWIY24D"
    C = "eUZCHhXr0SQsCgsB4O3B6TC WCDlAitYIHE7k6H3z8zrphz5EEBlIIAHqSWIY24D"

    A = "B4O3TC DlitYI7kH38rEElI"
    B = "B6 CWAHE6zzphz5BIAHqSWIY24D"
    C = "B4O3B6TC WCDlAitYIHE7k6H3z8zrphz5EEBlIIAHqSWIY24D"
    print isInterleave(A, B, C)

def isUniqueTwoTest():
	print isUniqueTwo('hi')
	print isUniqueTwo('hello')

def isPermutationTest():
	print isPermutationTwo('hi', 'hello')
	print isPermutationTwo('ellho', 'hello')

def replaceSpaceTest():
	print replaceSpace("h  i")
	print replaceSpace("Mr John Smith    ")

def replaceSpaceTwoTest():
	print replaceSpaceTwo("h  i")
	print replaceSpaceTwo("Mr John Smith    ")

def wordPermsTest():

def scrabbleTest():
    buildMap()
    print wordPerms('actor')

def findRankTest():
	print findRank('baa') # aab, aba, baa rank 3

def longestCommonPrefixTest():
	print longestCommonPrefix([ "abcd", "abcd", "efgh" ])

def editDistanceTest():
    print editDistance("bac", "abc")

def permsOfLengthTest():
    print permsOfLength('cow', 2)

def numCompressionTest():
	print numCompression("hhhoo")

def compressTest():
	print compress('hellllllo')
	print compress('abbaaacc')

def makeZeroTest():
	print makeZero([[1,2,3,2,4,1], [2,0,5,3,0,2], [1,2,5,4,4,0], [2,2,2,2,2,2]])

def isSubstringTest():
	print isSubstring('ell', 'hello')

def isRotationTest():
	print isRotation("waterbottle", "erbottlewat")