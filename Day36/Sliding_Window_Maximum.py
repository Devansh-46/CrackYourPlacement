class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # essentially monotonic stack but u popleft on each new elem
        q = deque()
        ans = []
        for i in range(k):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
        ans.append(q[0][0])
        for i in range(k, len(nums)):
            if q[0][1] == i - k:
                q.popleft()
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
            ans.append(q[0][0])
        return ans


        
        
