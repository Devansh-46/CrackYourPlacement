class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        fr = [0]*k
        fr[0]=1
        counter = 0
        ans = 0
        for num in nums:
            if num>=0:
                counter+=num
            else:
                counter+=(num%k)+k
            counter%=k

            ans += fr[counter]
            fr[counter]+=1
        
        return ans