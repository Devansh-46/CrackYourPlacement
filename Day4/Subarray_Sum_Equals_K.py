class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        sums = 0 
        count = 0 

        for i in range(len(nums)):
            sums += nums[i]\

            if sums - k in d:
                count += d[sums - k]

            if sums in d:
                d[sums] += 1
            else:
                d[sums] = 1

        return count