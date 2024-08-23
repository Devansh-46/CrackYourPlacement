# Function to create the graph based on the prerequisites
def make_graph(graph, N, prereq):
    for p in prereq:
        graph[p[1]].add(p[0])
    
# Function to perform depth-first search to detect cycles in the graph
def dfs_cycle(graph, i, onpath, vis):
    if vis[i]:
        return 0
    onpath[i] = 1
    vis[i] = 1

    for neigh in graph[i]:
        if onpath[neigh] or dfs_cycle(graph, neigh, onpath, vis):
            return 1
    onpath[i] = 0
    return 0

class Solution:
    def isPossible(self, N, P, prereq):
        # Create an empty graph
        graph = []
        for i in range(N):
            graph.append(set())

        # Create the graph using the prerequisites
        make_graph(graph, N, prereq)

        # Create arrays to track visited nodes and nodes on the current path
        vis = [0] * N
        onpath = [0] * N

        # Check for cycles in the graph using depth-first search
        for i in range(N):
            if vis[i] == 0 and dfs_cycle(graph, i, onpath, vis):
                return False

        return True
