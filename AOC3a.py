
import re
import functools

def symbol(matrix,startrow, endrow, startcol, endcol):
    return any([False if re.match(r'\d|\.',matrix[row][col]) else True \
            for row in range(startrow,endrow+1) for col in range(startcol, endcol+1)])
    #arguably "better"
    #for row in range(startrow,endrow+1):
    #        for col in range(startcol, endcol+1):
    #            if not re.match(r'\d|\.',matrix[row][col]):
    #                    return True
    #return False
                  
def partnum(start,end,row,matrix,num):
    startrow = max(row-1,0)
    endrow = min(row+1,len(matrix)-1)
    startcol = max(start-1,0)
    endcol = min(end+1,len(matrix[row])-1)
    return int(num) if symbol(matrix,startrow,endrow,startcol,endcol) else 0
    

with open("input3.txt") as f:
    # have to get rid of \n or it will throw off search
	lines = f.read().splitlines()

sum = 0

matrix = [list(s) for s in lines]

for i, line in enumerate(lines):
    nums =  (re.findall(r'\d+', line))
    pos = 0
    linelen = len(line)
    for num in nums:
          start = line.find(num,pos,linelen)
          # in case the same number appears multiple times in a line
          pos = start + len(num)
          print("line ",i,"num ",num,"start ",start)
          sum += partnum(start,pos-1,i,matrix,num)

 
print(sum)

                
                      




		




