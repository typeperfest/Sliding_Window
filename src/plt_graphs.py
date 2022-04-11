import matplotlib.pyplot as plt
import numpy as np


def make_graph(left_border, right_border, function):
    x = np.arange(left_border, right_border, 0.001)
    plt.plot(x, function(x))
    plt.grid(True)


def make_frequency(args, values, color):
    plt.scatter(args, values, color=color)


def make_plot(args, values, color):
    plt.plot(args, values, color=color)


def show_figures():
    plt.show()
