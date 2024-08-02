class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        q = []
        for i in range(1,len(h)):
            if (d := h[i] - h[i-1]) > 0:
                heappush(q, d)
                if len(q) > l:
                    b -= heappop(q)
                    if b < 0:
                        return i-1

        return len(h)-1
