
import timeit
import operator
import functools
from dataclasses import dataclass
from ordered_enum import OrderedEnum

HandType = OrderedEnum('HandType', ['High','Pair','TwoPairs','Three','Full','Four','Five'])
CardType = OrderedEnum('CardType',['J','2','3','4','5','6','7','8','9','T','Q','K','A'])

@dataclass
class Hand:
    cards: list[CardType]
    bid: int
    cat: HandType=None

def classifyVersion(cards):
      unique = set(cards)
      cardinality = len(unique)
      counts = []
      counts = list(map(lambda x: cards.count(x),unique))
      counts.sort(reverse=True)
      match (cardinality,counts):
            case (1,x) : return HandType['Five']
            case (2,[4,1]) : return HandType['Four']
            case (2,[3,2]) : return HandType['Full']
            case (3,[3,*_]) : return HandType['Three']
            case (3,[2,2,1]) : return HandType['TwoPairs']
            case (4,[2,*_]) : return HandType['Pair']
            case _ : return HandType['High']
    
def classifyHand(cards): 
      if CardType['J'] in cards:
           best = HandType['High']
           for cand in [e.name for e in CardType]:
                candHand = [x if x != CardType['J'] else CardType[cand] for x in cards]
                newCat = classifyVersion(candHand)
                if newCat > best:
                     best = newCat
           return best          
      else:
           return classifyVersion(cards)


def compare(hand1, hand2):
    if hand1.cat > hand2.cat:
         return 1
    if hand1.cat < hand2.cat:
         return -1
    #otherwise, they have the same category. Look to individual cards.
    for i in range(0,6):
          if hand1.cards[i] > hand2.cards[i]:
                return 1
          elif hand1.cards[i] < hand2.cards[i]:
                return -1
    # should never happen
    return 0
  

with open("input7.txt") as f:
	lines = f.read().splitlines()
hands = []
for line in lines:
      input = line.split()
      hand = Hand([CardType[x] for x in [*input[0]]],int(input[1]))
      hand.cat = classifyHand(hand.cards)
      hands.append(hand)
rankedHands = sorted(hands, key=functools.cmp_to_key(compare))
score = 0
for i,hand in enumerate(rankedHands):
   score += (i+1)*hand.bid
  
print("part2: ", score)



#start = timeit.default_timer()
#print("part1:",part1(lines))
#print("part2:",part2(lines))
#print("The elapsed time in ms is :", (timeit.default_timer() - start))





