#Back-end complete function Template for Python 3


def isSafe(graph, v, colour, c, V):

    for i in range(V):
        #checking if the connected nodes to v have same colour as c.
        if (graph[v][i] == 1 and colour[i] == c):
            return False

    #returning true if no connected node has same colour.
    return True


def graphColourUtil(graph, m, colour, v, V):

    #if all vertices have been assigned colour then we return true.
    if v == V:
        return True

    for c in range(1, m + 1):

        #checking if this colour can be given to a particular node.
        if (isSafe(graph, v, colour, c, V) == True):

            #assigning colour to the node.
            colour[v] = c

            #calling function recursively and checking if other nodes
            #can be assigned other colours.
            if (graphColourUtil(graph, m, colour, v + 1, V) == True):
                #returning true if the current allocation was successful.
                return True
            #if not true, we backtrack and remove the colour for that node.
            colour[v] = 0

    #if no colour can be assigned, we return false.
    return False


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    colour = [0] * V

    #checking if colours can be assigned.
    if (graphColourUtil(graph, k, colour, 0, V) == False):
        return False
    return True
