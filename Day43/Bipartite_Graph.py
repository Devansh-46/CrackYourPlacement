from collections import deque

class Solution:

    # Function to check if the graph is bipartite or not.
    def isBipartite(self, V, adj):
        is_bipartite = True

        # Initializing a queue and a color array.
        q = deque()
        color = [-1 for i in range(V)]

        # Loop through all the vertices.
        for i in range(V):
            if(color[i] == -1):
                q.append(i)
                color[i] = 0

                # BFS traversal starting from vertex i.
                while(len(q)):
                    u = q.pop()

                    # Traverse all adjacent vertices of vertex u.
                    for v in adj[u]:
                        if(color[v] == -1):

                            # Assigning alternate color to the adjacent vertex.
                            color[v] = color[u] ^ 1
                            q.append(v)
                        else:

                            # Checking if the adjacent vertices have the same color,
                            # which means it is not a bipartite graph.
                            is_bipartite  = is_bipartite & (color[v] != color[u])
        
        return is_bipartite
