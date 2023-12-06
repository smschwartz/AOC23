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

rev_num_dict = {
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
}
sum = 0
for line in lines:
	temp = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
	temp2 = [int(x) if x.isdigit() else num_dict[x] for x in temp]
	if not temp[-1].isdigit():
		revLine = line[::-1]
		words = re.findall(r"eno|owt|eerht|ruof|evif|xis|neves|thgie|enin",revLine)
		last = rev_num_dict[words[0]]
		if not (temp2[-1] == last):
			temp2[-1] = last
	num = 10 * temp2[0] + temp2.pop()
	sum += num
	print(num)
		
		

print(sum)


