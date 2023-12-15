# Day 10, Stephanie Schwartz
import numpy as np
import functools
from textwrap import wrap

def settleStoneNW(plank,stone):
    plank = list(plank)
    if stone == 0 or plank[stone-1] in ['O','#']:
        return plank
    plank[stone-1] = 'O'
    plank[stone] = '.'
    return settleStoneNW(plank,stone-1)

def settleStoneSE(plank,stone):
    plank = list(plank)
    if stone == len(plank)-1 or plank[stone+1] in ['O','#']:
       return plank
    plank[stone+1] = 'O'
    plank[stone] = '.'
    return settleStoneSE(plank,stone+1)
	
def tiltPlank(plank,d):
	# settle each stone in the row("plank"), using the new plank
    if d in ['N','W']:
          return functools.reduce(settleStoneNW,[i for (i,v) in enumerate(plank) if v == 'O'],plank)
    else:
          return functools.reduce(settleStoneSE,[i for (i,v) in reversed(list(enumerate(plank))) if v == 'O'],plank)
	
def tilt(platform,d):
	# settle all of the stones in all of the rows("planks")
    if d in ['N','S']:
        platform = np.transpose(platform)
    platform = [tiltPlank(p,d) for p in list(platform)]
    if d in ['N','S']:
        platform = np.transpose(platform)
    return platform
	
def part1(platform):
	platform = tilt(platform,'N')
	return calcLoad(platform)

def part2(platform):
    cycleEnd = 1
    platformDict = {}
    platformDict[''.join(str(c) for plank in platform for c in plank)] = 0
    cycleBegin = -1
    while True:
        platform = functools.reduce(tilt,['N','W','S','E'],list(platform))
        platformString = ''.join(str(c) for plank in platform for c in plank)
        if platformString in platformDict:
            cycleBegin = platformDict[platformString]
            break
        else:
             platformDict[platformString] = cycleEnd
        cycleEnd += 1
    cycles = 1000000000  
    lastCycles = (cycles-cycleBegin)%(cycleEnd-cycleBegin)
    #restore platform for beginning/end of cycle
    platform = [[*row] for row in wrap(platformString,width=len(platform[0]))]
    for i in range(0,lastCycles):
        platform = functools.reduce(tilt,['N','W','S','E'],list(platform))
    return calcLoad(platform)

def calcLoad(platform):
     return sum([sum([(len(platform)-i) for t in plank if t=='O']) for i,plank in enumerate(platform)])

with open("input14.txt") as f:
	lines = f.read().splitlines()
platform = np.array([[*line] for line in lines])

print("Part1:",part1(platform))
print("Part2:",part2(platform))















	







