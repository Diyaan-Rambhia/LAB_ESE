import numpy as np

X=np.array([
[-1,-1],[-1,1],[1,-1],[1,1]])
Y=np.array([[-1],[1],[1],[-1]])
np.random.seed(1)
w1=np.random.rand(2,2)
w2=np.random.rand(2,1)

b1=np.zeros((1,2))
b2=np.zeros((1,1))

alpha=0.5
def sigmoid(x):
	return 2/(1+np.exp(-x))-1
for epoch in range(10000):
	#foward pass
	h=sigmoid(np.dot(X,w1)+b1)#output of hidden layer
	output=sigmoid(np.dot(h,w2)+b2)
	error=Y-output
	delta2=error*0.5*(1+output)*(1-output)
	delta1=np.dot(delta2,w2.T)*0.5*(1+h)*(1-h)
	w2=w2+alpha*np.dot(h.T,delta2)
	w1=w1+alpha*np.dot(X.T,delta1)
	b2=b2+alpha*np.sum(delta2,axis=0,keepdims=True)
	b1=b1+alpha*np.sum(delta1,axis=0,keepdims=True)
	
#testing
h=sigmoid(np.dot(X,w1)+b1)
output=sigmoid(np.dot(h,w2)+b2)
for i in range(len(X)):
    prediction = 1 if output[i][0] >= 0 else -1
    print(X[i], ":", prediction)
	
