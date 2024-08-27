#Back end complete function Template for Python

class Solution:
    
    def DFSUtil(self,graph,v,visited):
        
        #marking the current node as visited.
        visited[v]= True
        
        #iterating over adjacent vertices and calling function 
        #recursively if any adjacent vertex is not visited.
        for i in graph[v]:
            if visited[i]==False:
                self.DFSUtil(graph,i,visited)


    def fillOrder(self,adj,v,visited, stack):
        
        #marking the current node as visited.
        visited[v]= True
        
        #iterating over adjacent vertices and calling function 
        #recursively if any adjacent vertex is not visited.
        for i in adj[v]:
            if visited[i]==False:
                self.fillOrder(adj, i, visited, stack)
                
        #pushing vertex into the stack.
        stack = stack.append(v)
    

    #Function that creates transpose of the adjacency list.
    def getTranspose(self, V, adj):
        g = [[] for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                g[j].append(i)
        return g

    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        
        ans=0
        stack = []
        
        #using boolean list to mark visited nodes and currently 
        #marking all the nodes as false.
        visited =[False]*V
        
        #filling vertices in stack according to their finishing times.
        for i in range(V):
            if visited[i]==False:
                self.fillOrder(adj, i, visited, stack)

        #creating transpose of adjacency list.
        gr = self.getTranspose(V,adj)
         
        #marking all the nodes as not visited again.
        visited =[False]*V

        #now processing all vertices in order defined by stack.
        while stack:
            
            #popping a vertex from stack.
            i = stack.pop()
            
            #if vertex is not visited, we call DFSUtil function 
            #and increment the counter.
            if visited[i]==False:
                self.DFSUtil(gr, i, visited)
                ans+=1 
        
        #returning the count.
        return ans
        
        
        
        
