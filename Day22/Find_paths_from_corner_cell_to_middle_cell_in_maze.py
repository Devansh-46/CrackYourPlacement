# Python program to find a path from corner cell to
# middle cell in maze containing positive numbers

# Rows and columns in given maze
N = 9

# check whether given cell is a valid cell or not.
def isValid(visited, pt):
	# check if cell is not visited yet to
	# avoid cycles (infinite loop) and its
	# row and column number is in range
	return (pt[0] >= 0) and (pt[0] < N) and (pt[1] >= 0) and (pt[1] < N) and (pt not in visited)

# Function to print path from source to middle coordinate
def printPath(path):
	for i in path:
		print("({}, {}) -> ".format(i[0], i[1]), end="")
	print("MID")
	print()

# For searching in all 4 direction
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

# Coordinates of 4 corners of matrix
_row = [0, 0, N-1, N-1]
_col = [0, N-1, 0, N-1]

def findPathInMazeUtil(maze, path, visited, curr):
	# If we have reached the destination cell.
	# print the complete path
	if curr[0] == N // 2 and curr[1] == N // 2:
		printPath(path)
		return
	# consider each direction
	for i in range(4):
		# get value of current cell
		n = maze[curr[0]][curr[1]]
		# We can move N cells in either of 4 directions
		x = curr[0] + row[i]*n
		y = curr[1] + col[i]*n
		next = (x, y)
		# if valid pair
		if isValid(visited, next):
			# mark cell as visited
			visited.append(next)
			# add cell to current path
			path.append(next)
			# recurse for next cell
			findPathInMazeUtil(maze, path, visited, next)
			# backtrack
			# remove cell from current path
			path.pop()
			visited.remove(next)

# Function to find a path from corner cell to
# middle cell in maze containing positive numbers
def findPathInMaze(maze):
	# list to store complete path
	# from source to destination
	path = []
	# to store cells already visited in current path
	visited = []

	# Consider each corners as the starting
	# point and search in maze
	for i in range(4):
		x = _row[i]
		y = _col[i]
		pt = (x, y)
		# mark cell as visited
		visited.append(pt)
		# add cell to current path
		path.append(pt)
		findPathInMazeUtil(maze, path, visited, pt)
		# backtrack
		# remove cell from current path
		path.pop()
		visited.remove(pt)

if __name__ == "__main__":
	maze = [
		[3, 5, 4, 4, 7, 3, 4, 6, 3],
		[6, 7, 5, 6, 6, 2, 6, 6, 2],
		[3, 3, 4, 3, 2, 5, 4, 7, 2],
		[6, 5, 5, 1, 2, 3, 6, 5, 6],
		[3, 3, 4, 3, 0, 1, 4, 3, 4],
		[3, 5, 4, 3, 2, 2, 3, 3, 5],
		[3, 5, 4, 3, 2, 6, 4, 4, 3],
		[3, 5, 1, 3, 7, 5, 3, 6, 4],
		[6, 2, 4, 3, 4, 5, 4, 5, 1]
	]

	findPathInMaze(maze)
