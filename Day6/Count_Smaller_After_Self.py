class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        arr= sorted(nums)
        ans = []
        
        for num in nums:
            i = bisect_left(arr,num)          
            ans.append(i)                     
            del arr[i]                        
            
        return ans                            