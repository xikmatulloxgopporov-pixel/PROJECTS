
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1-task
plt.figure(figsize=(15, 8))

df = pd.DataFrame(data={
    'x':np.random.randint(0, 100, 30),
    'y':np.random.randint(0, 100, 30),
})

plt.figure(figsize=(15, 8))
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

ax1.plot(df.index.values, df['x'], color='green', label='a')
ax1.plot(df.index.values, df['y'], color='brown', label='b')

plt.scatter(df['x'], df['y'], label = "stars", color = "green", marker = "*", s=30)


ax1.legend(loc='upper center')
plt.show()
# 2 task
np.random.seed(0)
x = np.arange(1, 21)
a = np.random.randint(10, 90, size=20)
b = np.random.randint(10, 90, size=20)

fig, axes = plt.subplots(3, 1, figsize=(12, 14))

axes[0].bar(x, a, color='steelblue')
axes[0].set_title("Bar Graph of A")

for i, v in enumerate(a):
    axes[0].text(x[i], v + 1, str(v), ha='center', fontsize=8)

axes[1].bar(x, b, color='steelblue')
axes[1].set_title("Bar Graph of B")

for i, v in enumerate(b):
    axes[1].text(x[i], v + 1, str(v), ha='center', fontsize=8)

axes[2].bar(x, a, color='steelblue', label='A')
axes[2].bar(x, b, bottom=a, color='orange', label='B')
axes[2].set_title("Stacked Bar: A with B on Top")
axes[2].legend()

for i, v in enumerate(a):
    axes[2].text(x[i], v / 2, str(v), ha='center', fontsize=7, color='white')

for i, v in enumerate(b):
    axes[2].text(x[i], a[i] + v / 2, str(v), ha='center', fontsize=7, color='black')

plt.tight_layout()
plt.show()