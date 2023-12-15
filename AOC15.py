# Day 10, Stephanie Schwartz

import functools
import re

#Determine the ASCII code for the current character of the string.
#Increase the current value by the ASCII code you just determined.
#Set the current value to itself multiplied by 17.
#Set the current value to the remainder of dividing itself by 256.

def hashLetter(acc,letter):
	res = functools.reduce(lambda a,f: f(a),[lambda x: x+acc,lambda x: x*17,lambda x: x%256],ord(letter)) 
	return res

def hashChunk(step):
	return functools.reduce(hashLetter,[*step],0)

def part1(steps):
	return sum(list(map(hashChunk,steps)))

def parseStep(step):
    label = (re.split('-|=',step))[0]
    op = step[len(label)]
    focal = None if len(step)==len(label)+1 else int(''.join(str(c) for c in step[len(label)+1:]))
    return(label,op,focal)

def addLens(label,focal,boxes):
	hash = hashChunk(label)
	lenses = boxes[hash]
	if not any([True if l==label else False for (l,f) in lenses]):
		boxes[hash].append((label,focal))
	else:
		#change focal length
		loc = lenses.index(next(lens for lens in lenses if lens[0]==label))
		boxes[hash][loc] = (label,focal)
	return boxes	
	
def removeLens(label,boxes):
	hash = hashChunk(label)
	lenses = boxes[hash]
	if not any([True if l==label else False for (l,f) in lenses]):
		return boxes
	else:
		#remove
		lens = (next(lens for lens in lenses if lens[0]==label))
		boxes[hash].remove(lens)
		
	return boxes	
	
def processStep(boxes,step):
	match step:
		case (label,op,focal) if op == '=': boxes = addLens(label,focal,boxes)
		case (label,op,None) if op == '-': boxes = removeLens(label,boxes)
	return boxes

def sumBox(boxnum,contents):
	return sum([boxnum*(i+1)*v[1] for i,v in enumerate(contents)])
	
def part2(steps):
	boxes = {i: [] for i in range(0,256)}
	steps = list(map(parseStep,steps))
	boxes = functools.reduce(processStep,steps,boxes)
	return sum([sumBox(box+1,boxes[box]) for box in boxes])
		
	

with open("input15.txt") as f:
	steps = f.read().split(',')

print("Part1:",part1(steps))
part2(steps)
print("Part2:",part2(steps))















	







