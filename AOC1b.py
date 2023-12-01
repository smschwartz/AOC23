import re

with open("input1.txt") as f:
	lines = f.readlines()

num_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

sum = 0
for line in lines:
	temp = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
	temp = [int(x) if x.isdigit() else num_dict[x] for x in temp]
	sum += 10 * temp[0] + temp.pop()
		
		

print(sum)


