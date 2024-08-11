#User function Template for python3

import sys

class Solution:
    def solveWordWrap(self, nums, k):
	    n = len(nums)
	    dp = [0] * n    # initialize dp array with 0
	    ans = [0] * n   # initialize ans array with 0
	    dp[n - 1] = 0   # set value of dp for last word to 0
	    ans[n-1] = n-1  # set value of ans for last word to n-1
	    
	    # iterate from second last word to first word
	    for i in range(n-2, -1,-1):
	        currlen = -1    # initialize currlen with -1
	        dp[i] = sys.maxsize   # set value of dp for current word to maximum possible value
	        for j in range(i, n):
	            currlen += (nums[j] + 1)    # update currlen with length of current word
	            if currlen > k:   # if currlen exceeds the given limit, break the loop
	                break
	            if j  == n - 1:   # if the current word is the last word, set cost to 0
	                cost = 0
	            else:
	                cost = ((k - currlen)*(k - currlen) + dp[j + 1])   # calculate the cost
	            if cost < dp[i]:   # if current cost is less than dp for the current word, update dp and ans
	                dp[i] = cost
	                ans[i] = j
	    
	    i = 0   # initialize i to 0
	    res = 0   # initialize res to 0
	    while i < n:
	        pos = 0   # initialize pos to 0
	        for j in range(i, ans[i] + 1):
	            pos = pos + nums[j]   # calculate the sum of lengths of words in the line
	        x = ans[i] - i   # calculate the number of extra spaces in the line
	        if ans[i] + 1 != n:
	            res = res + (k - x - pos)**2   # calculate the additional cost for the line
	        i = ans[i] + 1   # move to the next line
	    return res   # return the total cost of word wrapping
