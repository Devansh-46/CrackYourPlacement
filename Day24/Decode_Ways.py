class Solution:
    def numDecodings(self, s: str) -> int:
        str_len = len(s)

        dp = [0] * (str_len + 1)

        dp[0] = 1

        if s[0] != "0":
            dp[1] = 1
        else:

            return 0

        for i in range(2, str_len + 1):

            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]

        return dp[str_len]
