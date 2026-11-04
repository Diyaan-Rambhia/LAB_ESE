
import numpy as np
import matplotlib.pyplot as plt

X=np.array([
    [1,1],
    [1,2],
    [2,1],
    [8,8],
    [8,9],
    [9,8]
])
np.random.seed(1)
weights=np.random.rand(2,2,2)
alpha=0.5
for epoch in range(1000):
	for x in X:
		dist=np.sqrt(np.sum((x-weights)**2,axis=2))
		bmu=np.unravel_index(np.argmin(dist),dist.shape)
		for i in range(2):
    			for j in range(2):
       				grid_dist=(i-bmu[0])**2+(j-bmu[1])**2
        			influence=np.exp(-grid_dist/2)
        			weights[i,j]+=alpha*influence*(x-weights[i,j])
	alpha=0.9*alpha
print("Final weights:")
print(weights)
plt.scatter(X[:,0],X[:,1],label="Input Data")
plt.scatter(weights[:,:,0],weights[:,:,1],
            color="red",marker="X",s=150,label="SOM Neurons")

plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Self Organizing Map")
plt.legend()
plt.show()

