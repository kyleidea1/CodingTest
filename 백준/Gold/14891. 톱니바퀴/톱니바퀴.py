import sys
from collections import deque

def rotate_cw(n):
   tmp = wheels[n].pop()
   wheels[n].appendleft(tmp)

def rotate_ccw(n):
   tmp = wheels[n].popleft()
   wheels[n].append(tmp)

def process(n,d):
   rot = [(n-1,d)]
   cur_dir = d
   
   # 왼쪽
   for i in range(n-2,-1,-1):
       if wheels[i][2] != wheels[i+1][6]:
           cur_dir *= -1
           rot.append((i,cur_dir))
       else:
           break
           
   # 오른쪽
   cur_dir = d
   for i in range(n,4):
       if wheels[i-1][2] != wheels[i][6]:
           cur_dir *= -1
           rot.append((i,cur_dir))
       else:
           break
   
   for num,dir in rot:
       if dir == 1:
           rotate_cw(num)
       else:
           rotate_ccw(num)

input = sys.stdin.readline
wheels = [deque(list(input().strip())) for _ in range(4)]
k = int(input())

for _ in range(k):
   n, d = map(int, input().split())
   process(n,d)

score = sum(int(wheels[i][0]) * (1 << i) for i in range(4))
print(score)