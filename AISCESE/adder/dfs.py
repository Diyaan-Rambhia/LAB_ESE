from collections import *
graph={
	"A":["B","C"],
	"B":["D","C"],
	"C": ["F"],
    	"D": [],
    	"E": [],
    	"F": []}
visited=set()
st=[]
start="A"
st.append(start)
visited.add(start)
while st:
	node=st.pop()
	print(node,end=" ")
	for nh in reversed(graph[node]):
		if nh  not in visited:
			visited.add(nh)
			st.append(nh)

visited.clear()
def dfs(node):

    visited.add(node)
    print(node, end=" ")

    for nh in graph[node]:
        if nh not in visited:
            dfs(nh)

dfs("A")
	
