# Python3 program to 
# acquire all n coins 

import math 

# function to calculate min cost 
def minCost(coin, n, k): 

	# sort the coins value 
	coin.sort() 

	# calculate no. of 
	# coins needed 
	coins_needed = math.ceil(1.0 * n //
							(k + 1)); 

	# calculate sum of all 
	# selected coins 
	ans = 0
	for i in range(coins_needed - 1 + 1): 
		ans += coin[i] 
	
	return ans 

# Driver code 
coin = [8, 5, 3, 10, 
		2, 1, 15, 25] 
n = len(coin) 
k = 3

print(minCost(coin, n, k)) 
