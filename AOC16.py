# Day 16, Stephanie Schwartz
import sys

def move(coord,dir):
    match dir:
        case 'E': newcoord=(coord[0],coord[1]+1)
        case 'W': newcoord=(coord[0],coord[1]-1)
        case 'N': newcoord=(coord[0]-1,coord[1])
        case 'S': newcoord=(coord[0]+1,coord[1])
    return newcoord

checked = []

def solveOne(active,curmove):
    active = list(active)
    (coord,dir)=curmove
    if (coord,dir) in checked:
        return active
    checked.append((coord,dir))
    newcoord = move(coord,dir)
    dir90={"\\": {'E':'S','W':'N','S':'E','N':'W'}, "/": {'N':'E','E':'N','S':'W','W':'S'} }
    if not (coord[0] in [-1,len(surface)] or coord[1] in [-1,len(surface[0])]):
        active[coord[0]][coord[1]] = '#'          
    if newcoord[0] in [-1,len(surface)] or newcoord[1] in [-1,len(surface[0])]:
        return active
    current = surface[newcoord[0]][newcoord[1]]
 
    match current:
        case '#':return solveOne(active,(newcoord,dir))
        case '|' if dir in ['E','W']:return solveOne(solveOne(active,(newcoord,'N')),(newcoord,'S'))
        case '-' if dir in ['N','S']: return solveOne(solveOne(active,(newcoord,'E')),(newcoord,'W'))
        case '\\' : return solveOne(active,(newcoord,dir90['\\'][dir]))
        case '/' : return solveOne(active,(newcoord,dir90['/'][dir]))
        case _: return solveOne(active,(newcoord,dir))
 
def printGrid(surface):
    for s in surface:
        print("".join(s))

def part1():
    activated = [row[:] for row in surface]
    activated = list(solveOne(activated,((0,-1),'E')))
    return sum([row.count('#') for row in activated])

def part2(surface):
    global checked
    counts = []
    for j in [-1,len(surface[0])]:
        for i in range(0,len(surface)):
            activated = [row[:] for row in surface]
            checked = []
            match (i,j):
                case (x,-1): dir='E'
                case (x,y) if y==len(surface[0]): dir = 'W'
            activated = solveOne(activated,((i,j),dir))
            counts.append(sum([row.count('#') for row in activated]))
    for i in [-1,len(surface)]:
        for j in range(0,len(surface[0])):
            activated = [row[:] for row in surface]
            checked = []
            match (i,j):
                case (-1,x): dir='S'
                case (y,x) if y==len(surface): dir = 'N'
            activated = solveOne(activated,((i,j),dir))
            counts.append(sum([row.count('#') for row in activated]))  
    print("counts:",counts)
    return max(counts)

sys.setrecursionlimit(6000)
with open("input16.txt") as f:
	lines = f.read().splitlines()
surface = [[*line] for line in lines]

print(part1())
print(part2(surface))













	







