import numpy as np
import matplotlib.pyplot as plt
X=np.array([1,2,3,4,5])
Y=np.array([10,20,30,40,50])
x_mean=np.mean(X)
y_mean=np.mean(Y)
m=np.sum((X-x_mean)*(Y-y_mean))/np.sum((X-x_mean)**2)
c=y_mean-m*x_mean
Y_pred=m*X+c

print("Slope:", m)
print("Intercept:", c)
x=6
print("Predicted marks:", m*x+c)
plt.scatter(X,Y,label="actual Data")
plt.plot(X,Y_pred,color="red",label="Reg line")
plt.xlabel("Hours study")
plt.ylabel("Marks")
plt.legend()
plt.show()
