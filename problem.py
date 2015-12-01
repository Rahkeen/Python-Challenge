
# Python Challenge

# You are given a matrix with m rows and n columns of cells, each of which
# contains either 1 or 0. Two cells are said to be connected if they are
# adjacent to each other horizontally, vertically, or diagonally. The connected
# and filled (i.e. cells that contain a 1) cells form a region. There may be
# several regions in the matrix. Find the number of cells in the largest region
# in the matrix.

# Input Format 
# There will be three parts of the input:
# The first line will contain m, the number of rows in the matrix.
# The second line will contain n, the number of columns in the matrix.
# This will be followed by the matrix grid: the list of numbers that make up the matrix.

# Output Format 
# Print the length of the largest region in the given matrix.

# Constraints
# 0<m<10
# 0<n<10

# Sample Input:
# 4
# 4
# 1 1 0 0
# 0 1 1 0
# 0 0 1 0
# 1 0 0 0

# Sample Output:
# 5

# Explanation
# X X 0 0
# 0 X X 0
# 0 0 X 0
# 1 0 0 0
# The X characters indicate the largest connected component, as per the given
# definition. There are five cells in this component.

# Task: 
# Write the complete program to find the number of cells in the largest region.

# You will need to read from stdin for the input and write to stdout for the output
# If you are unfamiliar with what that means:
# raw_input is a function that reads from stdin
# print statements write to stdout
# You are not required to use raw_input or print statements, but it is the
# simplest and most common way to read and write to stdin/out

# The test cases are located in the test-cases directory.

# run-tests.py is not part of your challenge.  It is simply a convenience program
# that will test your code against all the test cases, one after another, and
# then tell you whether it passed or failed, and what the expected and actual
# outputs are.  You may review and modify run-tests.py as much as you want, but
# it will not score or lose you any points

# Included in the top level directory are four "hard" test cases that
# are square grids of side lengths 10, 25, 50, 100, and 1000 cells.
# These were randomly generated using generate-hard-test-case.py, and
# they do not come with an expected output.  You may generate test
# cases of various dimensions using generate-test-case.py, but the
# ability of your algorithm to solve extra test cases you've created
# will not be considered in our evaluation of this challenge.  Your
# algorithm should be able to find a correct solution in a timely
# manner up to the 1000x1000 grid.

# Finally, you may not use third party libraries to complete this challenge.  You
# may only use the libraries available on a fresh Python 2.7 install.  I doubt
# you will need to use any libraries at all as this is just an algorithmic
# challenge.

##############################################################################

from Queue import Queue

def bfs(matrix, visited, start):

	frontier = Queue()
	region = 0

	frontier.put(start)
	visited.add(start)

	while not frontier.empty():
		node = frontier.get()
		region += 1 

		# test neighbors
		x,y = node

		#right
		if x+1 < rows and matrix[x+1][y] == 1 and (x+1,y) not in visited:
			neighbor = (x+1,y)
			frontier.put(neighbor)
			visited.add(neighbor)
		#left
		if x-1 >= 0 and matrix[x-1][y] == 1 and (x-1,y) not in visited:
			neighbor = (x-1,y)
			frontier.put(neighbor)
			visited.add(neighbor)
		#up
		if y-1 >= 0 and matrix[x][y-1] == 1 and (x,y-1) not in visited:
			neighbor = (x,y-1)
			frontier.put(neighbor)
			visited.add(neighbor)
		#down
		if y+1 < cols and matrix[x][y+1] == 1 and (x,y+1) not in visited:
			neighbor = (x,y+1)
			frontier.put(neighbor)
			visited.add(neighbor)
		#up_right
		if (x+1 < rows and y-1 >= 0) and matrix[x+1][y-1] == 1 and (x+1,y-1) not in visited:
			neighbor = (x+1,y-1)
			frontier.put(neighbor)
			visited.add(neighbor)
		#up_left
		if (x-1 >= 0 and y-1 >= 0) and matrix[x-1][y-1] == 1 and (x-1,y-1) not in visited:
			neighbor = (x-1,y-1)
			frontier.put(neighbor)
			visited.add(neighbor)
		#down_right
		if (x+1 < rows and y+1 < cols) and matrix[x+1][y+1] == 1 and (x+1,y+1) not in visited:
			neighbor = (x+1,y+1)
			frontier.put(neighbor)
			visited.add(neighbor)
		#down_left
		if (x-1 >= 0 and y+1 < cols) and matrix[x-1][y+1] == 1 and (x-1,y+1) not in visited:
			neighbor = (x-1,y+1)
			frontier.put(neighbor)
			visited.add(neighbor)

	return region

# - Iterate through elements of the matrix
# - Find an an element that equals 1 (is part of some region)
# - If that element has not been visited before, start a BFS
#	at that point
# - Keep track of the largest region seen, return it

## read input and generate matrix 

rows = int(raw_input())
cols = int(raw_input())

matrix = []
visited = set()

for i in xrange(rows):
	row = raw_input()
	row = row.split()
	row = [int(i) for i in row]
	matrix.append(row)

## start interating through the matrix elements

max_region = -1

for x in xrange(rows):
	for y in xrange(cols):
		if matrix[x][y] == 1 and (x,y) not in visited:
			# perform bfs
			max_region = max(max_region, bfs(matrix, visited, (x,y)))

print(max_region)












