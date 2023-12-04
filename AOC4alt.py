
import re
import functools
import operator


with open("input4.txt") as f:
	lines = f.read().splitlines()

def part1(lines):
    sum = 0
    for line in lines:    
        parts = re.split(':|\|',line)
        winning = set(map(int,parts[1].split()))
        guesses = set(map(int,parts[2].split()))
        correct = len(winning.intersection(guesses))
        if correct:
            sum += 2**(correct-1)
    return sum

numcards =  {}
numcorrect = {}

def processCard(card, lines):
    # if we know solution, return it
    if card in numcards.keys():
        return numcards[card]
    # card is adding at least the immediate copies it yields
    count = 1
    for line in range(card+1,card+numcorrect[card]+1):
        count += processCard(line,lines)
    # record result so it can be reused
    numcards[card]=count
    return count

def part2(lines):
     for i,line in enumerate(lines):
         parts = re.split(':|\|',line)
         card = int(re.findall('\d+',parts[0])[0])
         winning = set(map(int,parts[1].split()))
         guesses = set(map(int,parts[2].split()))
         correct = len(winning.intersection(guesses)) 
         numcorrect[card] = correct
         if not correct:
             numcards[card]=1 
     for card in range(1,len(lines)+1):
         numcards[card] = processCard(card, lines)
     return functools.reduce(operator.add,numcards.values())
              
print("part 1",part1(lines))
print("part 2",part2(lines))

                
                      




		




