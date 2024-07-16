#User function Template for python3

class Solution:

    def findMinDiff(self, arr,n,m):

        if (m==0 or n==0):
            return 0

        arr.sort()
        if (n < m):
            return -1

        min_diff = arr[n-1] - arr[0]

        for i in range(len(arr) - m + 1):
            min_diff = min(min_diff ,  arr[i + m - 1] - arr[i])
    
        
        return min_diff

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends