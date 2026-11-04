import numpy as np

X = np.array([[0,0,0], [0,0,1],
              [0,1,0], [0,1,1],
              [1,0,0], [1,0,1],
              [1,1,0], [1,1,1]])

def neuron(w, t, x):
    return int(np.dot(w, x) >= t)

def xor(x):
    a = neuron([1,1], 1, x)
    b = neuron([-1,-1], -1, x)
    return neuron([1,1], 2, [a,b])

print("A B Cin Carry Sum")

for x in X:
    a, b, c = x

    s1 = xor([a,b])
    s = xor([s1,c])
    carry = neuron([1,1,1], 2, x)

    print(a, b, " ", c, "  ",  carry, "   ", s)