
import re
import timeit


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

def makeDict(lines):
    numcopies = {}
    for line in lines:
         parts = re.split(':|\|',line)
         card = int(re.findall('\d+',parts[0])[0])
         winning = set(map(int,parts[1].split()))
         guesses = set(map(int,parts[2].split()))
         correct = len(winning.intersection(guesses)) 
         numcopies[card] = correct
    return numcopies

def part2(lines):
     numcopies = makeDict(lines)
     totalcards = len(lines)
     current = numcopies.keys()
     while len(current):
        #set up the next set of cards to be checked
        next = []
        for card in current:
            correct = numcopies[card]
             #if any numbers are winners, need to copy more cards for next time
            if correct:
                next.extend(range(card+1,card+correct+1))
        # count the cards that were added for next round
        totalcards += len(next)
        current = next
     return totalcards
              
print("part 1",part1(lines))
start = timeit.default_timer()
print("The start time is :", start)
print("part 2",part2(lines))
print("The difference of time is :", timeit.default_timer() - start)


                
                      




		




