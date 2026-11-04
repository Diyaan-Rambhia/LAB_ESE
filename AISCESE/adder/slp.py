import numpy as np
X=np.array([
[-1,-1],[-1,1],[1,-1],[1,1]])
Y=np.array([-1,-1,-1,1])
w=np.zeros(2)
b=0
alpha=0.1
X_train = X[:3]
Y_train = Y[:3]

X_test = X[3:]
Y_test = Y[3:]
for epoch in range(10):
	for i in range(len(X_train)):
		net=np.dot(X_train[i],w)+b
		if net>=0:
			output=1
		else:
			output=-1
		if output!=Y_train[i]:
			w=w+alpha*Y_train[i]*X_train[i]
			b=b+alpha*Y_train[i]
print("Final weights:",w)
print("Final bias:",b)
print("Predictions:")
for x in X_test:
	net=np.dot(x,w)+b
	if net>=0:
		output=1
	else:
		output=-1
	print(x,":",output)
