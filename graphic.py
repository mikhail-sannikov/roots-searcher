import matplotlib.pyplot as plt
import numpy as np


def draw_graphic(a, b, f):
    x1 = -abs(a)
    x2 = abs(b)

    window = plt.figure()
    axes = window.add_subplot()

    axes.set_title('График функции')
    axes.set_xlabel('Ox')
    axes.set_ylabel('Oy')
    axes.grid()

    axes.set_xlim(x1, x2)
    axes.set_ylim(x1, x2)

    x_points = np.linspace(x1, x2, 100)

    axes.plot(
        [x for x in range(x1, x2 + 1)],
        [0 for _ in range(x1, x2 + 1)],
        color='b',
    )
    axes.plot(
        [0 for _ in range(x1, x2 + 1)],
        [y for y in range(x1, x2 + 1)],
        color='b',
    )
    axes.plot(
        x_points,
        [f(x) for x in x_points],
        color='r',
    )

    plt.show()
