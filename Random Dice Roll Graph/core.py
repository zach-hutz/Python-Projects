import random

from matplotlib import pyplot as plt

# Random Dice roll
def dice_roll():
    return random.randint(1, 6)

x_axis = []
y_axis = []

def generate_graph():
    for i in range(100):
        rand = dice_roll()
        x_axis.append(i)
        y_axis.append(rand)

    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis)

    ax.set(xlabel='Iterations', ylabel='Dice Rolls',
        title='Dice rolls per iteration')
    ax.grid()
    plt.show()


generate_graph()