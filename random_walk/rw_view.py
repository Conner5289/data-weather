import matplotlib.pyplot as plt
import time

from random_walk import randomWalk

while True:
    rw = randomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()
