def naive_search(l, t):
	for i in range(len(l)):
		if l[i] == t:
			return i
	return -1

def binary_search(l, t, low=None, high=None):
	if low is None:
		low = 0
	if high is None:
		high = len(l) - 1
	if high < low:
		return -1
	midpoint = (low + high) // 2
	if l[midpoint] == t:
		return midpoint
	elif t < l[midpoint]:
		return binary_search(l, t, low, midpoint-1)
	else:
		return binary_search(l, t, midpoint+1, high)

if __name__ == '__main__':
	l = [1,3,5,10,12]
	t = 10
	print(naive_search(l,t))
	print(binary_search(l,t))
