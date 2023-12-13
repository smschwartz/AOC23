# Day 10, Stephanie Schwartz
import numpy as np

def processInput(lines):
    patterns = []
    pattern = []
    for line in lines:
        if not line:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append([*line])
    patterns.append(pattern)
    return patterns
		
def findReflection(lines,horizontal,butnot=-1):
     lines = np.array(lines)
     if not horizontal:
          lines = np.transpose(lines)
     found = False
     for i,line in enumerate(lines[:-1]):
          same = True
          #avoid previous answer if in part2
          if i == butnot-1:
            continue
          #pair-wise zips
          for offset in range(0,max(i+1,len(lines)//2)):
               if i-offset >= 0 and offset+i+1 < len(lines):
                    zipped = list(zip(lines[i-offset],lines[i+offset+1]))
                    if any([False if c1 == c2 else True for (c1,c2) in zipped]):
                            same = False
                            break
               else:
                    same = True
                    break
          if same:
               return (i+1)*100 if horizontal else i+1
     return 0
               
          

          
def part1(patterns):
     origfold={}
     #horiz, vertical
     sum = 0
     for i,pattern in enumerate(patterns):
          h,v = 0,0
          h = findReflection(pattern,True)
          if not h:
            v = findReflection(pattern,False)
          #print("pattern",i,"horizontal:",h,"vertical:",v)
          origfold[i]=(h/100,v)
          sum += h+v   
     return (sum,origfold)

def part2(patterns,origfold):
     #horiz, vertical
     sum = 0
     for i,pattern in enumerate(patterns):
          h,v = 0,0
          (origh,origv) = origfold[i]
          for row,line in enumerate(pattern):
              for col,spot in enumerate(line):
                  pattern[row][col] = '.' if pattern[row][col]=='#' else '#'
                  h = findReflection(pattern,True,origh)
                  if not h:
                        v = findReflection(pattern,False,origv)
                  pattern[row][col] = '.' if pattern[row][col]=='#' else '#'
                  if (h or v):
                       #print("pattern",i,"horizontal:",h,"vertical:",v,"(row,col)",(row,col))
                       break
              else:
               continue
              break
          sum += h+v
     return sum       

with open("input13.txt") as f:
	lines = f.read().splitlines()

patterns = processInput(lines)

(sum,origfold) = part1(patterns)
print("part1:",sum)
print("part2:",part2(patterns,origfold))













	







