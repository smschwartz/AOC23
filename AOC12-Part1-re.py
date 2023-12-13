# Day 10, Stephanie Schwartz
import re
import itertools as it

perms = {}

   
def processLine(line,broken,sizes):
   unknowns = list(re.findall(r'\?+',line))
   candidates = [line]
   for unknown in unknowns:
      subs = []
      newc = []
      if perms.get(unknown):
        subs = perms[unknown]
      else:
        subs = list(it.product(['.','#'], repeat=len(unknown))) 
        perms[unknown] = subs
      for sub in subs:
         sub = "".join(sub)
         for c in candidates:
            newc.append(c.replace(unknown,sub,1))
         #print("new candidates:",newc)
      candidates = newc
   num = 0
   for c in candidates:
      if re.fullmatch(broken,c):
         num += 1
   return num
   
def buildRequired(brokenList):
   res = "\.*"
   for item in brokenList:
      res += "#" * item + "\.+"
   res = res[:-1] + "*" 
   return res

def part1(lines):
    sum = 0
    for i,line in enumerate(lines):
        input,broken=line.split()
        broken = list(map(int,broken.split(',')))
        brokenString = buildRequired(broken)
        temp = processLine(input,brokenString,broken)
        sum += temp
    return sum



with open("input12.txt") as f:
	lines = f.read().splitlines()
print("part1:",part1(lines))













	







