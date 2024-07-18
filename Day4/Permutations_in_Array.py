class Solution:
    def isPossible(self,a, b, n, k):
        a.sort()
        b.sort(reverse=True)

        # Check if the sum of corresponding elements is always greater than or equal to k
        for i in range(n):
            if a[i] + b[i] < k:
                return False

        return True