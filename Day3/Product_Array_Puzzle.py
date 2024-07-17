class Solution:
    def productExceptSelf(self, arr, n):
        if n == 1:
            #print(0)
            return [1]
    
        i, temp = 1, 1

        prod = [1 for i in range(n)]

        for i in range(n):
            prod[i] = temp
            temp *= arr[i]

        temp = 1
    

        for i in range(n - 1, -1, -1):
            prod[i] *= temp
            temp *= arr[i]

        return prod
