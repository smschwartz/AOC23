# Day 17, Stephanie Schwartz
import functools
from dataclasses import dataclass
import sys
import operator

def printGrid(surface):
    for s in surface:
        print("".join(s))
   

def succ(cur,minstr,maxstr):
     r,c,dir = cur
     newlocs = []
     match dir:
          case 'U': 
               newlocs = [(nr,c) for nr in range(r-minstr,max(r-maxstr-1,-1),-1)]
               lead = sum([surface[nr][c] for nr in range(r-1,max(r-minstr,-1),-1)])
          case 'D': 
               newlocs = [(nr,c) for nr in range(r+minstr,min(r+maxstr+1,len(surface)))]
               lead = sum([surface[nr][c] for nr in range(r+1,min(r+minstr,len(surface)))])
          case 'R': 
               newlocs = [(r,nc) for nc in range(c+minstr,min(c+maxstr+1,len(surface[0])))]
               lead = sum([surface[r][nc] for nc in range(c+1,min(c+minstr,len(surface[0])))])
          case 'L': 
               newlocs = [(r,nc) for nc in range(c-minstr,max(c-maxstr-1,-1),-1)]
               lead = sum([surface[r][nc] for nc in range(c-1,max(c-minstr,-1),-1)])

     d = lead
     locsd =[]
     for p in newlocs:
          d += surface[p[0]][p[1]]
          locsd.append((p,d))
     
     res = []
     res.extend([((r,c,d),distance) for d in ['U','D'] for ((r,c),distance) in locsd if dir in ['R','L']])
     res.extend([((r,c,d),distance) for d in ['L','R'] for ((r,c),distance) in locsd if dir in ['U','D']])
     return res

def findMin(q,dist):
     minLoc = q[0]
     minDist = dist[minLoc]
     for v in q[1:]:
          if dist[v]<minDist:
               minDist = dist[v]
               minLoc = v
     return minLoc

def dijkstrad(source,target,minstr,maxstr):   
     dist={}
     prev={}
     vertices=[(i,j,d) for d in ['D','U','R','L'] for i,row in enumerate(surface) for j,_ in enumerate(row)]
     q = []
     for v in vertices:
         dist[v] = sys.maxsize if ((v[0],v[1]) != source) else 0
         prev[v] = None
         q.append(v)

     while q:
          u = findMin(q,dist)
          q.remove(u) 
          if (u[0],u[1]) == target:
               return dist[u],dist,prev
          for (n,d) in succ(u,minstr,maxstr):
               if n in q: 
                    alt = dist[u] + d 
                    if alt < dist[n]:
                         dist[n] = alt
                         prev[n] = u  
     return -1,dist,prev 


def part1():
     return dijkstrad((0,0),(len(surface)-1,len(surface[0])-1),1,3)

def part2():
     return dijkstrad((0,0),(len(surface)-1,len(surface[0])-1),4,10)


with open("input17.txt") as f:
	lines = f.read().splitlines()
surface = [list(map(int,[*line])) for line in lines]
target=(len(surface),len(surface[0]))
d,dist,prev = part1()
print("distance",d)
d,dist,prev = part2()
print("distance",d)
















	







