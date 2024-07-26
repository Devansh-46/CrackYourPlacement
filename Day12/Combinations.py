class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(i,result,li):
            
            if len(li)==k:
                result.append(li[:])
            
            else:
                
                for j in range(i,n+1):
                    li.append(j)
                    backtrack(j+1,result,li)
                    li.pop()
                    
        result = []
        li = []
        backtrack(1,result,li)
        return result