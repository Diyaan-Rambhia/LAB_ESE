from collections import *
A=5
B=7
start=(0,0)
q=deque()
visited=set()
q.append((start,[]))
visited.add(start)
while q:
	(a,b),path=q.popleft()
	if a==2 or b==2 :
		print("solution :")
		for state in path+[(a,b)]:
			print(state)
		break
	states=[
	(a,B),(A,b),(0,b),(a,0),(a-min(a,B-b),b+min(a,B-b)),(a+min(A-a,b),b-min(A-a,b))]
	for state in states:
		if state not in visited:
			q.append((state,path+[(a,b)]))
			visited.add(state)
	


