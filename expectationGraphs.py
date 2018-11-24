import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from mpl_toolkits import mplot3d
import numpy as np

def w0(p):
	return (1-p) ** 2

def w1(p):
	return 2 * p * (1-p) ** 2

def w2(p):
	return 3 * p ** 2 * (1 - p) ** 2

def w3(p):
	return 4 * p ** 3 * (1 - p) ** 2

def w4(p):
	return 5 * p ** 4 * (1 - p) ** 2

def w5(p):
	return 5 * p ** 5 * (1 - p) + p ** 5

print(w0(0.50))
print(w1(0.50))
print(w2(0.50))
print(w3(0.50))
print(w4(0.50))
print(w5(0.50))

print(w0(0.5) + w1(0.5) + w2(0.5) + w3(0.5) + w4(0.5) + w5(0.5))

print("Expected Number Of Packs Per Run")

x1 = []
y1 = []
for i in range(56):
	x = i + 40
	p = x / 100
	y = w4(p) + 2 * w5(p)
	x1.append(p)
	y1.append(y)

plt.plot(x1, y1, '--bo')

plt.xlabel('Win Probability')
plt.ylabel('Expected Packs')

plt.title('Expected Number Of Packs Per Run')

plt.show()

print("Expected Number Of Runs Per Ticket")

x2 = []
y2 = []
for i in range(46):
	x = i + 40
	p = x / 100
	y = 1 / (1 - (w3(p) + w4(p) + w5(p)))
	x2.append(p)
	y2.append(y)

plt.plot(x2, y2, '--bo')

plt.xlabel('Win Probability')
plt.ylabel('Expected Runs')

plt.title('Expected Number Of Runs Per Ticket')

plt.show()

print("Expected Number Of Packs Per Ticket")

x2 = []
y2 = []
for i in range(56):
	x = i + 40
	p = x / 100
	y = 1 / (1 - (w3(p) + w4(p) + w5(p)))
	x2.append(p)
	y2.append(y)

plt.plot(x2, y2, '--bo')

plt.xlabel('Win Probability')
plt.ylabel('Expected Runs')

plt.title('Expected Number Of Runs Per Ticket Extended')

plt.show()

print("Expected Number Of Packs Per Ticket")

x3 = []
y3 = []
for i in range(46):
	x = i + 40
	p = x / 100
	y = (w4(p) + 2 * w5(p)) / (1 - (w3(p) + w4(p) + w5(p)))
	x3.append(p)
	y3.append(y)

plt.plot(x3, y3, '--bo')

plt.xlabel('Win Probability')
plt.ylabel('Expected Packs')

plt.title('Expected Number Of Packs Per Ticket')

plt.show()

x3 = []
y3 = []
for i in range(56):
	x = i + 40
	p = x / 100
	y = (w4(p) + 2 * w5(p)) / (1 - (w3(p) + w4(p) + w5(p)))
	x3.append(p)
	y3.append(y)

plt.plot(x3, y3, '--bo')

plt.xlabel('Win Probability')
plt.ylabel('Expected Packs')

plt.title('Expected Number Of Packs Per Ticket Extended')

plt.show()

print("Expected Number Of Runs Per Ticket With Recycling")

x4 = []
y4 = []
z4 = []

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(21):
	for j in range(11):
		z = j / 10 + 1
		x = i + 40
		p = x / 100
		y = (w4(p) + 2 * w5(p)) / (1 - (w3(p) + w4(p) * (1 + z) + w5(p) * (1 + 2 * z)))
		x4.append(p)
		y4.append(y)
		z4.append(z)
		ax.scatter(p, z, y, c='b')

ax.set_xlabel('Win Probability')
ax.set_ylabel('Recycle Rate')
ax.set_zlabel('Expected Number Of Runs')

plt.show()