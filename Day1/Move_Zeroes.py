class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        c = 0
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == 0:
                nums.remove(0)
                c += 1
                i -= 1
            else:
                i -= 1
                continue
        for j in range(c):
            nums.append(0)
                
                
        