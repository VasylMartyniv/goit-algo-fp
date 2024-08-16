import math

import matplotlib.pyplot as plt


def draw_pythagoras_tree(ax, x, y, angle, depth, size):
    if depth > 0:
        x1 = x + size * math.cos(math.radians(angle))
        y1 = y + size * math.sin(math.radians(angle))
        ax.plot([x, x1], [y, y1], color="green")

        new_size = size * math.sqrt(2) / 2
        draw_pythagoras_tree(ax, x1, y1, angle - 45, depth - 1, new_size)
        draw_pythagoras_tree(ax, x1, y1, angle + 45, depth - 1, new_size)


def visualize_pythagoras_tree(level):
    fig, ax = plt.subplots()
    draw_pythagoras_tree(ax, 0, 0, 90, level, 100)
    ax.set_aspect(1)
    plt.show()


visualize_pythagoras_tree(5)
