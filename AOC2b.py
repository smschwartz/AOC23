
import re
import functools

with open("input2.txt") as f:
	lines = f.readlines()

sum = 0

for line in lines:
    # parse into game # and data
    temp = line.split(":")
    game = int((re.findall(r'\d+', temp[0]))[0])
    # break data into individual draws
    draws = temp[1].split(";")
    # find largest number of blocks for each color
    rgb = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        data = draw.split(",")
        for item in data:
                nums = map(int,re.findall(r'\d+',item))
                colors = re.findall(r'blue|green|red',item)
                for (num, color) in zip(nums,colors):
                      rgb[color] = max(rgb[color],num)
    #find power of set and accumulate it in sum
    sum += rgb['green'] * rgb['blue'] * rgb['red']
 
print(sum)

                
                      




		




