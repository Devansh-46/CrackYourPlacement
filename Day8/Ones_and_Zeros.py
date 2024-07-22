from collections import defaultdict

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
	    # Preprocessing to count 0s and 1s in strings.
        strs = [(s.count('0'), s.count('1')) for s in strs]
		
        dp = defaultdict(int)
		# we cannot form any string without 0 and 1.
        dp[0, 0] = 0
        for a0, a1 in strs:
            for (b0, b1), count in list(dp.items()):
                if a0 + b0 <= m and a1 + b1 <= n:
                    key = (a0 + b0, a1 + b1)
                    dp[key] = max(count + 1, dp[key])
        return max(dp.values())