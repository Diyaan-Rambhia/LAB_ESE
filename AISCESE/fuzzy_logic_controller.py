import numpy as np

def trimf(x, a, b, c):
    if x == b:
        return 1
    if x <= a or x >= c:
        return 0
    if x < b:
        return (x-a)/(b-a)
    return (c-x)/(c-b)

temp = 25

cold = trimf(temp, 0, 0, 20)
warm = trimf(temp, 10, 20, 30)
hot = trimf(temp, 20, 40, 40)

x = np.arange(101)

slow = np.array([trimf(i, 0, 0, 50) for i in x])
medium = np.array([trimf(i, 25, 50, 75) for i in x])
fast = np.array([trimf(i, 50, 100, 100) for i in x])

output = np.maximum.reduce([
    np.minimum(cold, slow),
    np.minimum(warm, medium),
    np.minimum(hot, fast)
])

speed = np.sum(x * output) / np.sum(output)

print("Fan Speed:", round(speed, 2))