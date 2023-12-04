
import re
import functools

def staradjacent(star,num):
     (numrow,numstart,numend) = num
     (starrow,starcol) = star
     return starrow in range(numrow-1,numrow+2) and \
        starcol in range(numstart-1,numend+2)
          
with open("input3.txt") as f:
    # have to get rid of \n or it will throw off search
	lines = f.read().splitlines()

sum = 0

matrix = [list(s) for s in lines]
allnums = []
numpositions = []
starpositions = []

for i, line in enumerate(lines):    
    numstars = line.count("*")
    pos = 0
    for s in range(0,numstars):
         newpos = line.find("*",pos)
         starpositions.append((i,newpos))
         pos = newpos+1    
    nums =  re.findall(r'\d+', line)
    pos = 0
    linelen = len(line)
    for num in nums:
          start = line.find(num,pos)
          allnums.append(int(num))
          numpositions.append((i,start,start+len(num)-1))
          # in case the same number appears multiple times in a line
          pos = start + len(num)

for star in starpositions:
    gearratio = 1
    count = 0
    for i,pos in enumerate(numpositions):
        if staradjacent(star,pos):
              gearratio *= allnums[i]
              count+=1
        # small efficiency save to stop checking if we are past adjacency rows
        if pos[0] > star[0]+1:
             break
    if count == 2:
        sum += gearratio
        
              
print(sum)

                
                      




		




