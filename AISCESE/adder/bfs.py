from collections import *
graph={
	"A":["B","C"],
	"B":["D","C"],
	"C": ["F"],
    	"D": [],
    	"E": [],
    	"F": []}
visited=set()
Q=deque()
start="A"
Q.append(start)
visited.add(start)
while Q:
	node=Q.popleft()
	print(node,end=" ")
	for nh in graph[node]:
		if nh  not in visited:
			visited.add(nh)
			Q.append(nh)

	
