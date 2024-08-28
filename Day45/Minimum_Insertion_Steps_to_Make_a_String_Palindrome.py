class Solution:
	def minInsertions(self, s: str) -> int:

		def LeastCommonSubsequence(string, reverse_string, row, col):

			dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

			for r in range(1, row + 1):
				for c in range(1, col + 1):

					if string[r - 1] == reverse_string[c - 1]:

						dp[r][c] = dp[r - 1][c - 1] + 1

					else:
						dp[r][c] = max(dp[r - 1][c] , dp[r][c - 1])

			return dp[row][col]

		length = len(s)

		result = length - LeastCommonSubsequence(s , s[::-1] , length , length)

		return result
		
