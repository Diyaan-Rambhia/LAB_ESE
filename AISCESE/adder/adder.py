import numpy as np
def mp(x,w,theta):
	total=np.sum(x*w)
	return 1 if total>=theta else 0
def half_adder(A,B):
	OR=mp(np.array([A,B]),np.array([1,1]),1)
	AND=mp(np.array([A,B]),np.array([1,1]),2)
	NOT_AND=1-AND
	S=mp(np.array([OR,NOT_AND]),np.array([1,1]),2)
	return S,AND
def full_adder(A,B,C):
	S1,C1=half_adder(A,B)
	S2,C2=half_adder(S1,C)
	Cout=mp(np.array([C1,C2]),np.array([1,1]),1)
	return S2,Cout
X = np.array([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
])
Y=np.array([full_adder(A,B,Cin) for A,B,Cin in X])
print("A B Cin | Sum Carry")
print(np.column_stack((X,Y)))
