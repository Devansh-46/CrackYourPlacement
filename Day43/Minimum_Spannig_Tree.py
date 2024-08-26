from functools import cmp_to_key

def compare(a,b) :
    if a[0]!=b[0] :
        return a[0]-b[0]
    return a[1]-b[1]

class Solution:
    
    def __init__(self):
        self.parent = []
        self.rank = []

    def make_set(self,v):
        self.parent[v]=v
        self.rank[v]=0
    
    #Function to find set of an element v (using path compression technique).
    def  find_set(self,v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    #Function that does union of two sets x and y (using union by rank).
    def union_sets(self,a,b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b :
            if (self.rank[a] < self.rank[b]) :
                temp = a
                a = b
                b = temp
            
            self.parent[b] = a 
            if self.rank[a] == self.rank[b] : 
                self.rank[a]+=1
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        res = []

        for i in range(V) :
            for j in range(len(adj[i])) :
                x = adj[i][j]

                temp = []
                temp.append(x[1])
                temp.append(min(i,x[0]))
                temp.append(max(i,x[0]))

                res.append(temp)
        
        #sorting according to the weight of the edges.
        res = sorted(res, key=cmp_to_key(compare))

        graph = []
        for e in res :
            graph.append(e)

        cost = 0;
        self.parent = [0]*V
        self.rank = [0]*V

        for i in range(V) :
            self.make_set(i)

        for e in graph :
            
            #if set of e[1] and e[2] is not equal, we update cost 
            #and perform union of the two sets.
            if self.find_set(e[1]) != self.find_set(e[2]) :
                cost+=e[0]
                self.union_sets(e[1],e[2])

        return cost
