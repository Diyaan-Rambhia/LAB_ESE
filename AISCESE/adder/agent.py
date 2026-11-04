import numpy as np 
import pandas as pd
import string
import math
from collections import deque
n = int(input("Enter matrix size: "))

rooms = {}

for i in range(n):
    for j in range(n):
        rooms[(i,j)] = input(f"Room ({i},{j}): ")
location=(0,0)
visited=set()
queue=deque([location])
visited.add(location)

rr=[0,1,-1,0]
cc=[1,0,0,-1]
while queue:
	location=queue.popleft()
	r,c=location
	if rooms[location]=="Dirty":
		print("\nAgent at:", location)
		print(f"cleanining room {location} ")
		rooms[location]="Clean"
	
	for i in range(4):
		if(r+rr[i]>=0 and r+rr[i]<n and c+cc[i]>=0 and c+cc[i]<n):
			if((r+rr[i],c+cc[i]) not in visited):
				location=(r+rr[i],c+cc[i])
				visited.add(location)
				queue.append(location)
print("\nAll rooms cleaned:")
print(rooms)		
		
	

