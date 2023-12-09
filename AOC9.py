# Day 9, Stephanie Schwartz

def processSeq(line):
	temp = []
	temp.append(line)
	i = 0
	while any(temp[i]):
		temp.append([v2 - v1 for v1, v2 in zip(temp[i], temp[i][1:])])
		i += 1
	temp[-1].append(0)
	for i, row in reversed(list(enumerate(temp))[:-1]):
		temp[i-1].append(temp[i-1][-1]+row[-1])
	return temp[0][-1]
	

	
def part1():
	total = 0
	for line in lines:
		total += processSeq(line)
	return total

with open("input9.txt") as f:
	lines = f.read().splitlines()
for i,line in enumerate(lines):
	lines[i] = (list(map(int,line.split())))

	
print("part 2:",part1())
for i in range(0,len(lines)):
	lines[i] = list(reversed(lines[i][:-1]))
print("part 1:",part1())






