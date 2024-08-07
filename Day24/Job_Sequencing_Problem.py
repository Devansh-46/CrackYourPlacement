class Solution:
    
    def __init__(self):
        self.maxProfit = float('-inf')
        self.count = 0

    @staticmethod
    def comparison(first, second):
        if first.deadline < second.deadline:
            return -1
        if first.deadline > second.deadline:
            return 1
        if first.profit < second.profit:
            return 1
        return -1
        
    def find(self, arr, curr, n, t, profit, cnt):
        if curr >= n:
            if profit > self.maxProfit:
                self.maxProfit = profit
                self.count = cnt
            return
        if arr[curr].deadline > t:
            self.find(arr, curr + 1, n, t + 1, profit + arr[curr].profit, cnt + 1)
        self.find(arr, curr + 1, n, t, profit, cnt)
        
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key=lambda job: (job.deadline, -job.profit))
        self.maxProfit = float('-inf')
        self.count = 0
        self.find(Jobs, 0, n, 0, 0, 0)
        return [self.count, self.maxProfit]
