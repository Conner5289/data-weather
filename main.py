import matplotlib.pyplot as plt

squares = [2, 4, 8, 16, 32, 64, 128, 246, 512]
plt.style.use('fast')
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
