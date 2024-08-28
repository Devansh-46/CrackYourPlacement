# This Python program finds the number of spanning trees in a
# graph using Matrix Multiplication.

MAX = 100
MOD = 1000000007

# Matrix Multiplication
def multiply(A, B, C):
    for i in range(MAX):
        for j in range(MAX):
            C[i][j] = 0
            for k in range(MAX):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j]) % MOD) % MOD

# Function to find Nth power of A
def power(A, N, result):
    temp = [[0] * MAX for i in range(MAX)]
    for i in range(MAX):
        for j in range(MAX):
            result[i][j] = 1 if i == j else 0
    while N > 0:
        if N % 2 == 1:
            multiply(A, result, temp)
            for i in range(MAX):
                for j in range(MAX):
                    result[i][j] = temp[i][j]
        N = N // 2
        multiply(A, A, temp)
        for i in range(MAX):
            for j in range(MAX):
                A[i][j] = temp[i][j]

# Function to find number of Spanning Trees in a Graph
# using Matrix Multiplication.
def numOfSpanningTree(graph, V):
    result = [[0] * MAX for i in range(MAX)]
    temp = [[0] * MAX for i in range(MAX)]
    # Create a copy of graph as the Adjacency matrix
    # will be changed during the process
    for i in range(V):
        for j in range(V):
            temp[i][j] = graph[i][j]
    # Find (V-2)th power of Adjacency matrix
    power(temp, V - 2, result)
    ans = 0
    # Find sum of all elements in (V-2)th power
    for i in range(V):
        for j in range(V):
            ans = (ans + result[i][j]) % MOD
    return ans

# Driver program
if __name__ == '__main__':
    # Let us create the following graph
    # 2 <-> 3
    # |   |
    # 0 <-1-> 1
    V = 4 # Number of vertices in graph
    E = 5 # Number of edges in graph
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [1, 1, 1, 0]]
    print(numOfSpanningTree(graph, V))
