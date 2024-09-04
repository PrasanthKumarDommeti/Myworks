def isPossible(A, n, H, K): 

	time = 0

	for i in range(n): 
		time += (A[i] - 1) // K + 1

	return time <= H 
def minJobSpeed(A, n, H): 
	if H < n:
		return -1

	Max = max(A) 

	lo, hi = 1, Max

	while lo < hi: 
		mi = lo + (hi - lo) // 2
		if not isPossible(A, n, H, mi): 
			lo = mi + 1
		else:
			hi = mi 
	
	return lo 

if __name__ == "__main__": 

	A = [3, 6, 7, 11]
	H = 8

	n = len(A) 

	# Print required maxLenwer 
	print(minJobSpeed(A, n, H)) 

# This code is contributed by Rituraj Jain
