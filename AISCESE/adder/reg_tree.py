import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5])
Y = np.array([10, 20, 30, 50, 80])

# Split condition
split = 2.5

# Divide data
left = Y[X <= split]
right = Y[X > split]

# Calculate predictions
left_mean = np.mean(left)
right_mean = np.mean(right)

# Predict
Y_pred = []

for x in X:
    if x <= split:
        Y_pred.append(left_mean)
    else:
        Y_pred.append(right_mean)

print("Predicted values:", Y_pred)

# Graph
plt.scatter(X, Y, label="Actual Data")
plt.step(X, Y_pred, where="mid", color="red", label="Regression Tree")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()
