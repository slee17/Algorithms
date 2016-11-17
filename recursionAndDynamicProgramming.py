def fib(n):
	"""
	Returns the nth fibonacci number.
	"""
	if n < 0:
		return
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-1) + fib(n-2)


def fibDP(n):
	"""
	Returns the nth fibonacci number in linear time.
	"""
	fibSeq = [0, 1]
	for i in range (2, n+1):
		fibSeq.append(fibSeq[i-1]+fibSeq[i-2])
	return fibSeq[n]

def climbStairs(n):
	"""
	Returns the number of distinct ways in which you can climb n steps, given
	you can climb either 1 step or 2 steps each time.
	"""
	if A == 0:
		return 0
	if A == 1:
		return 1
	if A == 2:
		return 2
	return climbStairs(n-1) + climbStairs(n-2)

def climbStairsDP(n):
	"""
	Returns the number of distinct ways in which you can climb n steps in linear time,
	given you can climb either 1 step or 2 steps each time.
	"""
	assert n >= 0

	# Create the dp table.
	dpTable = [None] * (n+1)
	i = 0
	
	# Fill in the table for base cases.
	while i < 3 and i <= n:
		dpTable[i] = i
		i += 1

	# Now fill in the rest.
	for j in range(3, n+1):
		dpTable[j] = dpTable[j-1] + dpTable[j-2]
	return dpTable[n]