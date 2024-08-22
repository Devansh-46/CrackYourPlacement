class Solution:

    #Function to check if it is possible to partition the given array into k subsets with equal sum.
    def isKPartitionPossible(self, nums, k):
        nums.sort() # Sorting the array in ascending order.
        target, rem = divmod(sum(nums), k) # Calculating the target sum and remainder.
        if rem or nums[-1] > target: # If there is a remainder or the largest number is greater than the target sum, return False.
            return False
    
        dp = [False] * (1 << len(nums)) # Creating an array to store if a state (subset) is possible.
        dp[0] = True # The state with an empty subset is possible.
        total = [0] * (1 << len(nums)) # Creating an array to store the total sum of each state.
    
        for state in range(1 << len(nums)): # Iterating through all possible states.
            if not dp[state]: continue # If the current state is not possible, continue to the next state.
            for i, num in enumerate(nums): # Iterating through each number in the array.
                future = state | (1 << i) # Creating a new state by adding the current number to the current state.
                if state != future and not dp[future]: # If the new state is different from the current state and is not possible yet.
                    if (num <= target - (total[state] % target)): # Checking if the current number can fit into the target sum of the new state.
                        dp[future] = True # Marking the new state as possible.
                        total[future] = total[state] + num # Updating the total sum of the new state.
                    else:
                        break # If the current number cannot fit into the target sum, break the loop and try the next number.
        return dp[-1] # Returning the value of the final state, indicating if it is possible to partition the array into k subsets with equal sum.
