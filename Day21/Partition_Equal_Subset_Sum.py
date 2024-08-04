# Back-end complete function Template for Python3

class Solution:
    def equalPartition(self, n, arr):
        # code here
        if sum(arr)&1:
            return 0
        sumo = sum(arr)//2+1
        dp = [[-1 for i in range(sumo)] for j in range(n+1)]
        def solve(i,s):
            if i == 0:
                return 0
            if dp[i][s] !=-1:
                return dp[i][s]

            if s == arr[i-1]:
                dp[i][s] = 1
                return 1
            if s >arr[i-1]:
                dp[i][s] = solve(i-1,s-arr[i-1])|solve(i-1,s)
            else:
                dp[i][s] = solve(i-1,s)
            return dp[i][s]
        return solve(n,sumo-1)
            
