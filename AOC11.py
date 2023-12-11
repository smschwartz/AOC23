# Day 10, Stephanie Schwartz
import numpy as np
import itertools as it
from dataclasses import dataclass

@dataclass
class distance:
    val: int
    blanks: int

def expandUniverse(lines,factor):
	# find indexes of blank rows and cols
    blankRows = []
    for i,line in enumerate(lines):
        lines[i] = [*line]
        if all([True if x == '.' else False for x in lines[i]]):
            blankRows.append(i)
    blankRows.sort(reverse=True)
    blankCols = []
    for i in range(0,len(lines[0])):
        np.x = np.array(lines)
        if all([True if x== '.' else False for x in np.x[:,i]]):
            blankCols.append(i)
    blankCols.sort(reverse=True)
    univ = lines.copy()
    for blank in blankRows:
        for _ in it.repeat(None, factor-1):
            univ.insert(blank,['.' for x in range(0,len(univ[blank]))])
    for blank in blankCols:
        for _ in it.repeat(None, factor-1):
            univ = np.insert(univ,blank,['.' for x in range(0,len(univ))],1)     
    return univ

def getDistancePairs(lines,factor):
    univ = expandUniverse(lines,factor)
    galaxies = []
    for i, line in enumerate(univ):
        for j, spot in enumerate(univ[i]):
            if univ[i][j] == '#':
                galaxies.append((i,j))
    pairs = list(it.combinations(galaxies, 2))    
    d = []
    for pair in pairs:
        ((x1,y1),(x2,y2)) = pair
        d.append((abs(x1-x2),abs(y1-y2))) 
    return d

def part2(lines,factor):

    d1 = getDistancePairs(lines,1)
    d2 = getDistancePairs(lines,2)
    ddiff = list(zip(d1,d2))
    distances = []
    for pair in ddiff:
        distances.extend(createDistances(pair))
    return sum(list(map(lambda d: d.val + (d.blanks*(factor-1)),distances)))

    

def part1(lines,factor):
    pairs = getDistancePairs(lines,factor)
    sum = 0
    for pair in pairs:
        (v1,v2) = pair
        sum += v1 + v2
    return sum  
		
def createDistances(distpair):
    ((dx1,dy1),(dx2,dy2)) = distpair
    d1 = distance(dx1,abs(dx1-dx2))
    d2 = distance(dy1,abs(dy1-dy2))
    return [d1,d2]


with open("input11.txt") as f:
	lines = f.read().splitlines()

res = part1(lines,2)
print("part1:",res)

print("part2",part2(lines,1000000))





	







