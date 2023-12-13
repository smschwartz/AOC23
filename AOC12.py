# Day 10, Stephanie Schwartz
import functools


@functools.cache   
def solveOne(current,line,sizes):
    if not line:
        if current and sizes:
            return 0 if len(current) != sizes[0] else solveOne("",line,sizes[1:])
        return 1 if not sizes else 0
    elif not sizes:
        return 1 if all([True if x in ['.','?'] else False for x in line]) else 0
    elif line[0] == '#':
        return 0 if len(current)+1 > sizes[0] else solveOne(current+'#',line[1:],sizes)
    elif line[0] == '.':
        if current:
            return 0 if len(current) != sizes[0] else solveOne("",line[1:],sizes[1:])
        else:
            return solveOne("",line[1:],sizes)
    else:
        return solveOne(current,"."+line[1:],tuple(sizes)) + solveOne(current,"#"+line[1:],sizes)


def part1(lines):
    sum = 0
    for i,line in enumerate(lines):
        input,broken=line.split()
        broken = list(map(int,broken.split(',')))
        temp = solveOne("",input,tuple(broken))
        sum += temp
    return sum

def part2(lines):
   sum = 0
   for i,line in enumerate(lines):
        input,broken=line.split()
        broken = list(map(int,broken.split(',')))
        newinput = input
        for j in range(0,4):
           newinput += "?" + input
        newbroken = [x for xs in [broken for x in range(0,5)] for x in xs]
        temp = solveOne("",newinput,tuple(newbroken))
        sum += temp
   return sum

with open("input12.txt") as f:
	lines = f.read().splitlines()
print("part1:",part1(lines))
print("part2:",part2(lines))












	







