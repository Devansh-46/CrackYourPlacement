class UnionFind:
    def __init__(self, n: int):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, p: int) -> int:
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    def union(self, p: int, q: int):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return
        
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

        self.count -= 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        uf = UnionFind(n)
        x_dict = {}
        y_dict = {}
        for i, (x, y) in enumerate(stones):
            if x in x_dict:
                uf.union(i, x_dict[x])
            else:
                x_dict[x] = i
            
            if y in y_dict:
                uf.union(i, y_dict[y])
            else:
                y_dict[y] = i

        return n - uf.count

        
