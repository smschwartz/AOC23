
import timeit
import re

from dataclasses import dataclass
from math import lcm

@dataclass
class node:
    name: str
    left: str
    right: str

def steps(start,end):
      total = 0
      while not start.endswith(end):
            dir = dirs[total%len(dirs)]
            start = nodes[start].left if dir == "L" else nodes[start].right
            total += 1    
      return total


def allpaths():
      total = []
      for node in [node for node in nodes if node.endswith("A")]:
            total.append(steps(node,"Z"))
      return lcm(*total)

with open("input8.txt") as f:
	lines = f.read().splitlines()
memo = {}
dirs = lines[0]
nodes = {}
for i in range(2,len(lines)):
      nums = re.findall(r'\w+', lines[i])
      #print("read",lines[i],nums)
      nodes[nums[0]] = node(nums[0],nums[1],nums[2])
print("part 1:",steps("AAA","ZZZ"))
print("part 2:", allpaths())




#start = timeit.default_timer()
#print("part1:",part1(lines))
#print("part2:",part2(lines))
#print("The elapsed time in ms is :", (timeit.default_timer() - start))





