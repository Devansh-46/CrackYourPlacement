from typing import List
class Solution:
    
    
    def isCycleUtil(self, u, par, adj, vis):
        
        #marking the current vertex as visited.
        vis[u] = True
        
        #iterating on all the adjacent vertices.
        for v in adj[u]:
            
            if(v == par):
                continue
            
            #if current vertex is visited, we return true else we 
			#call the function recursively to detect the cycle.
            elif(vis[v]):
                return True
            else:
                if(self.isCycleUtil(v, u, adj, vis)):
                    return True
        return False
        
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        
        #using a boolean list to mark all the vertices as not visited.
        vis = [False for i in range(V)]
        
        #iterating over all the vertices.
        for i in range(V):
            
            #if vertex is not visited, we call the function to detect cycle.
            if(vis[i] == False):
                
                #if cycle is found, we return true.
                if(self.isCycleUtil(i, -1, adj, vis)):
                    return True
        return False
        
        
