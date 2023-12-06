
import timeit
import operator
import functools

with open("input6.txt") as f:
	lines = f.read().splitlines()


def countWaysToWin(race):
      sum = 0
      (length,record) = race
      return len(list(filter(lambda l : ((length - l) * l) > record, range(1,length))))

def part1(lines):
       times = list(map(int,(lines[0].split())[1:]))
       distances = list(map(int,(lines[1].split())[1:]))
       races = (list(zip(times,distances)))
       return functools.reduce(operator.mul,[countWaysToWin(race) for race in races])

def part2(lines):
      time = int(((lines[0].split(':'))[1]).replace(' ',''))
      distance = int(((lines[1].split(':'))[1]).replace(' ',''))
      return countWaysToWin((time,distance))  

start = timeit.default_timer()
print("part1:",part1(lines))
print("part2:",part2(lines))
print("The elapsed time in ms is :", (timeit.default_timer() - start))





