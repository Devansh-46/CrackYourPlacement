class Solution:
    def climbStairs(self, n: int) -> int:
        step_one = 1   
        step_two = 1
        for i in range(n-1):
            temp = step_one
            step_one += step_two
            step_two = temp
        return step_one