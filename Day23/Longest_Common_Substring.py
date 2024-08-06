class Solution:

    def longestCommonSubstr(self, s1, s2):
        #Initializing variables
        n = len(s1)
        m = len(s2)
        dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

        #Initializing result variable
        res = 0

        #Iterating over the strings and filling up the dp array
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                #If characters match, increment dp[i][j] by 1
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0

                #Updating result with the maximum value of dp[i][j]
                res = max(res, dp[i][j])

        return res
