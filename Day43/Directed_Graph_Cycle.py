# Back-end Complete function Solution for Python


class Solution:

    def DFSUtil(self, adj, v, visited, recStack):

        #marking the current node as visited and part of recursion stack.
        visited[v] = True
        recStack[v] = True

        #calling function recursively for all neighbours
        #if any neighbour is visited and is in recStack then graph is cyclic.
        for neighbour in adj[v]:
            if visited[neighbour] == False:
                if self.DFSUtil(adj, neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        #removing the vertex from recursion stack.
        recStack[v] = False
        return False

    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):

        #marking all vertices as not visited and not a part of recursion stack
        visited = [False] * V
        recStack = [False] * V

        #calling the recursive helper function to detect cycle in
        #different DFS trees.
        for node in range(V):
            if visited[node] == False:
                if self.DFSUtil(adj, node, visited, recStack) == True:
                    return True
        return False
