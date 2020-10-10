# O(NK) T O(N) S 
def maxProfitWithKTransactions(prices, k):
	if len(prices) == 0:
		return 0
	list1 = [0 for price in range(len(prices))]
	list2 = [0 for price in range(len(prices))]
	for i in range(1, k+1):
		maxSoFar = float("-inf")
		for j in range(1, len(prices)):
			maxSoFar = max(maxSoFar, list1[j-1]-prices[j-1])
			list2[j] = max(list2[j-1], prices[j]+maxSoFar)
		print(list1, list2)
		list1 = list2
		list2 = [0 for price in range(len(prices))]
	return list1[-1]