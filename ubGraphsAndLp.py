import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

gamma1 = 1
gamma2 = 0.85

def avgUB(g):
	c = []
	for i in range(76):
		c.append(-1 / 76)

	b = []
	A = []
	for i in range(76):
		Aval = []
		b.append(152 / g)
		for j in range(76):
			if j == i:
				Aval.append(1)
			else:
				Aval.append(75 / 75)
		A.append(Aval)

	bounds = []
	for i in range(76):
		bounds.append((0, np.inf))

	result = linprog(c, A_ub = A, b_ub = b, bounds=bounds, options={"disp": True})

	print(result)

print("Assumption 2, LP For Highest Possible Avg price of rares")

avgUB(1)

print("Assumption 3, LP For Highest Possible Price Of One Rare")

avgUB(0.85)

def rareUB(g):
	x = []
	y = []
	for i in range(21):
		alpha = i / 10
		ub = 152 / g - (76 - 1) * alpha
		x.append(alpha)
		y.append(ub)
		print(str(alpha) + " -> " + str(ub))

	return x, y

print("Assumption 2, Graphing UB for specific rare")

x1, y1 = rareUB(gamma1)

plt.plot(x1, y1, '--bo')

plt.xlabel('alpha')
plt.ylabel('v(r) Upper Bound')

plt.title('Assumption 1.1 and 2')

plt.show()

print("Assumption 3, Graphing UB for specific rare")

x2, y2 = rareUB(gamma2)

plt.plot(x2, y2, '--bo')

plt.xlabel('alpha')
plt.ylabel('v(r) Upper Bound')

plt.title('Assumption 1.1 and 3')

plt.show()

def relaxedRareUB(g):
	x = []
	y = []
	for i in range(21):
		beta = i / 132
		ub = 152 / g - (12 - 1) * beta - (76 - 1) * 12 * beta
		x.append(beta)
		y.append(ub)
		print(str(beta) + " -> " + str(ub))

	return x, y

print("Assumption 2 and 3, no 1, Graphing UB for specific rare")

x21, y21 = relaxedRareUB(gamma1)

x22, y22 = relaxedRareUB(gamma2)

plt.plot(x21, y21, '--bo')

plt.plot(x22, y22, '--bo')

plt.xlabel('beta')
plt.ylabel('v(r) Upper Bound')

plt.title('')

plt.show()