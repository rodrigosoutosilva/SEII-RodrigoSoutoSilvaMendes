
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.figure(figsize=(8,5), dpi=100)

plt.plot(x,y, 'b^--', label='2x')

x2 = np.arange(0,4.5,0.5)

plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2')

plt.plot(x2[5:], x2[5:]**2, 'r--')


plt.title('Our First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})


plt.xlabel('X Axis')
plt.ylabel('Y Axis')


plt.xticks([0,1,2,3,4,])

plt.legend()

n)
plt.savefig('mygraph.png', dpi=300)

plt.show()

labels = ['A', 'B', 'C']
values = [1,4,2]

plt.figure(figsize=(5,3), dpi=100)

bars = plt.bar(labels, values)

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.savefig('barchart.png', dpi=300)

plt.show()


gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 18})

plt.plot(gas.Year, gas.USA, 'b.-', label='United States')
plt.plot(gas.Year, gas.Canada, 'r.-')
plt.plot(gas.Year, gas['South Korea'], 'g.-')
plt.plot(gas.Year, gas.Australia, 'y.-')


plt.xticks(gas.Year[::3].tolist()+[2011])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()

fifa = pd.read_csv('fifa_data.csv')

fifa.head(5)