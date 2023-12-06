
import re
import timeit

with open("input5.txt") as f:
	lines = f.read().splitlines()

def parseInput(lines):
    mykey = ("","")
    maps = {}
    label = False
    for line in lines[1:]:
        if label:
            parts = re.split('-| ',line)
            mykey = (parts[0],parts[2])
            maps[mykey] = []
            label = False
            continue
        if not line.strip():
            label = True
            mykey = ('','')
            continue
        (maps[mykey]).append(tuple(map(int,line.split())))
    return maps

# for chaining forward from seed
def findNext(val,map):
     res = val
     for (d,s,r) in map:
          if val in range(s,s+r):
               offset = val - s
               res = d + offset
               break         
     return res

# for chaining backwards from loc
def findPrev(val,map):
     res = val
     for (d,s,r) in map:
          if (val >= d) and (val < d+r):
               offset = val - d
               res = s + offset
               break         
     return res

#starting with seed num, find loc
def findLoc(val,maps):
     mapkeys = maps.keys()
     source = "seed"
     res = val
     while True:
        (vals,dest) =[(value,key[1]) for key,value in maps.items() if key[0]==source][0]
        res = findNext(res,vals)
        if dest == "location":
            break
        source = dest
     return res

#starting with loc, find seed      
def findSeed(val,maps):
     mapkeys = maps.keys()
     dest = "location"
     res = val
     while True:
        (vals,source) =[(value,key[0]) for key,value in maps.items() if key[1]==dest][0]
        res = findPrev(res,vals)
        if source == "seed":
            break
        dest = source
     return res

# given a seed num, was it sowed (for part 2)
def sowSeed(seed,seedranges):
     for (start,length) in seedranges:
          if (seed >= start and seed < (start+length)):
               return True
     return False

def part1(lines,maps):          
    seeds = list(map(int,(lines[0].split())[1:]))           
    locs = [findLoc(seed,maps) for seed in seeds]
    return min(locs)


def part2(lines,maps):
     temp = list(map(int,(lines[0].split())[1:]))    
     ranges = list(zip(temp[::2], temp[1::2]))
     source = "seed"
     for item in ranges:
          (vals,dest) =[(value,key[1]) for key,value in maps.items() if key[0]==source][0]
     
     while True:
        (vals,dest) =[(value,key[1]) for key,value in maps.items() if key[0]==source][0]
        res = findNext(res,vals)
        if dest == "location":
            break
        source = dest
     return res
           

maps = parseInput(lines)
print("part1:",part1(lines,maps))
start = timeit.default_timer()
print("part2:",part2(lines,maps))
print("The elapsed time in seconds is :", (timeit.default_timer() - start))





