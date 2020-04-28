import matplotlib.pyplot as plt
import pylab as plt
import pandas as pd
import math

f = open('resistivity-data.csv', 'r')
data = pd.read_csv(f)
R = []
for i in range(len(data)):
    r = float(data['V(V)'][i])/float(data['I(A)'][i])
    R.append(round(r, 2))

data['R'] = R
radius = (2.7/2 * (10**-4))
area = math.pi * radius**2

resistivity = []
LbyA = []
for i in range(len(data)):
    res = (area * float(data['R'][i]))/float(data['L(m)'][i])
    resistivity.append(res)
    LbyA.append(float(data['L(m)'][i])/area)

data['rho'] = resistivity
sum = 0
for i in range(10):
    sum+=float(data['rho'][i])
print('\nData Table:\n')
print(data)
print(f'\nMean Resistivity = {sum/10}\n')
plt.scatter(LbyA, R)
print(plt.polyfit(LbyA, R, 1))
plt.show()
