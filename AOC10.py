# Day 10, Stephanie Schwartz

	

	

def findConnections(loc,lines,visited):
	res = []
	(y,x) = loc
	match lines[y][x]:
		case 'F': res.extend([(y+1,x),(y,x+1)])
		case 'J': res.extend([(y-1,x),(y,x-1)])
		case '|': res.extend([(y-1,x),(y+1,x)])
		case '-': res.extend([(y,x-1),(y,x+1)])
		case '7': res.extend([(y+1,x),(y,x-1)])
		case 'L': res.extend([(y-1,x),(y,x+1)])
	for (y,x) in res[:]:
		if not y in range(0,len(lines)+1) or not x in range(0,len(lines[y])+1):
			res.remove((y,x))
		elif visited[y][x] == '1':
			res.remove((y,x))
	return res

def findStartConnections(start,lines,visited):
	(y,x) = start
	res = []
	for i in range(max(y-1,0),min(y+2,len(lines))):
		for j in range(max(0,x-1),min(len(lines[i]),x+2)):
			conns = findConnections((i,j),lines,visited)
			if (y,x) in conns:
				res.append((i,j))
	sym = None
	return res
				
def calcNeighbors(row,col,lines,newv):	
	# for each visited spot, calculate connections for newv based on character in lines
	sym = lines[row][col]
	lastrow = len(lines)-1
	lastcol = len(lines[0])-1
	dirs = []
	match sym:
		case 'F': dirs = ['Down','Right']
		case 'J': dirs = ['Up','Left']
		case '|': dirs = ['Up','Down']
		case '-': dirs = ['Left','Right']
		case '7': dirs = ['Left','Down']
		case 'L': dirs = ['Up','Right']	
	if 'Down' in dirs and row != lastrow:
			newv[2*row+1][2*col] = "1"
	if 'Up' in dirs and row != 0:
			newv[2*row-1][2*col] = "1"
	if 'Left' in dirs and col != 0:
			newv[2*row][2*col-1] = "1"
	if 'Right' in dirs and col != lastcol:
		newv[2*row][2*col+1] = "1"
	return newv

def part2(visited,lines):
	#print("visited:")
	#for v in visited:
	#	print(v)

	#create new visited grid with filler rows and columns to allow 0 width "pipes"
	newv=[[' ' for i in range(0,2*len(visited[0]))] for j in range(0,2*len(visited))]
	for row,line in enumerate(newv):
		for col,spot in enumerate(line):
			if row % 2 != 0:
				newv[row][col] = "."
			elif col % 2 != 0:
				newv[row][col] = "."
			else:
				newv[row][col] = visited[row//2][col//2]
	#for each visited spot in new grid, calculate the filler values
	for row,line in enumerate(visited):
		for col,spot in enumerate(line):
			if spot == "1":
				newv = calcNeighbors(row,col,lines,newv)
			
	#print("new visited:")
	#for v in newv:
	#	print(v)
	
	# do flood fille
	for row in [0,len(newv)-1]:
		for col in range(0,len(newv[0])):
			floodFill(row,col,newv)
	for row in range(0,len(newv)):
		for col in [0,len(newv[0])-1]:
			floodFill(row,col,newv)
	counts = 0
	for row in range(0,len(newv)):
		for col in range(0,len(newv[0])):
			# need to not count filler rows as empty ground			
			if (row%2==0) and (col%2==0) and newv[row][col]=='.':
				counts += 1
				newv[row][col]='*'
	#print("Flooded with good spots marked *:")
	#for v in newv:
	#	print(v)
	return counts

def floodFill(sr, sc, grid):
        # adapted from https://leetcode.com/problems/flood-fill/solutions/2051987/python-iterative/
        if grid[sr][sc] == '#':
          return grid
        if grid[sr][sc] == "1":
          return grid
        
        stack = [(sr, sc)]
        while stack:
            x, y = stack.pop()
            if grid[x][y] != '.': continue
                
            grid[x][y] = '#'
            
            if x > 0: stack.append((x-1, y))
            if y > 0: stack.append((x, y-1))
            if x < len(grid)-1: stack.append((x+1, y))
            if y < len(grid[0])-1: stack.append((x, y+1))

        return grid


 
def part1(start,lines):
	visited = [['.' for i in range(0,len(lines[j]))] for j in range(0,len(lines))]
	paths = findStartConnections(start,lines,visited)
	steps = 1
	visited[start[0]][start[1]] = '1'
	while (len(paths) == len(set(paths))) and paths:
		newpaths = []
		for path in paths:
			visited[path[0]][path[1]] = '1'
			newpaths.extend(findConnections(path,lines,visited))
		paths = newpaths
		steps += 1
	# mark last spot visited
	setpaths = set(paths)
	for path in setpaths:
		if paths.count(path) != 1:
			visited[path[0]][path[1]] = '1'
	return (visited,steps)
	

		

with open("input10.txt") as f:
	lines = f.read().splitlines()
start = None
for i,line in enumerate(lines):
	lines[i] = [*line]
	for j,sym in enumerate(lines[i]):
		if lines[i][j] == 'S':
			start = (i,j)
	

(visited,steps) = part1(start,lines)
print("part1: ",steps)
print("part2: ",part2(visited,lines))


	







