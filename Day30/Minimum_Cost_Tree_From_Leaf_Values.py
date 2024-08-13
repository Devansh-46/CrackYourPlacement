class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        roots = [] 
        ans = 0
        for a in arr:
            while len(roots) > 1 and roots[-2] <= a:
                ans += roots[-2]*roots[-1]
                roots.pop()

            if roots and roots[-1] <= a:

                ans += roots[-1]*a
                roots[-1] = a 
            else:
                roots.append(a)


        while len(roots) > 1:
            ans += roots[-1]*roots[-2]
            roots.pop()

        return ans
