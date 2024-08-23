#Back-end complete function template for Python

class Solution:

    #Function to find the shortest distance between any two nodes in the graph.
    def shortest_distance(self, matrix):
        #Code here

        INF = 1<<32 
        n = len(matrix)

        #Replacing -1 with infinite distance.
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = INF

        #Applying Floyd-Warshall algorithm to find the shortest distance.
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] < INF and matrix[k][j] < INF and matrix[i][k] + matrix[k][j] < INF:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        #Replacing infinite distances with -1.
        for i in range(n):
            for j in range(n):
                if matrix[i][j] >= INF:
                    matrix[i][j] = -1
