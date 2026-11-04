import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4, 5])
Y = np.array([5, 10, 25, 50, 85])

coeff=np.polyfit(X,Y,2)

p=np.poly1d(coeff)
Y_pred=p(X)

print("coeff:", coeff)

x=6
print("Predicted marks:", p(x))

plt.scatter(X,Y,label="actual Data")
plt.plot(X,Y_pred,color="red",label="Reg curve")
plt.xlabel("Hours study")
plt.ylabel("Marks")
plt.legend()
plt.show()
