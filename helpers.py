from matplotlib.lines import Line2D
from matplotlib.axes import Axes


def compute_output(weights: list, variables: list) -> int:
    """
    :param weights: list of weights should be n + 1 length, where n is count of input values
    :param variables: analogically with weights, list, should be n + 1 length
    :return: -1 if result lower than 0 and 1 otherwise
    """
    output = 0.0
    for index in range(len(weights)):
        output += variables[index] * weights[index]

    return -1 if output < 0 else 1


def format_weights(weights: list) -> str:
    """
    :param weights: list of weights to display
    :return: formatted string with weights
    """
    return f'w0 ={weights[0]:5.2f}, w1 ={weights[1]:5.2f}, w2 ={weights[2]:5.2f}'


def add_weights_line(weights: list, axes: Axes, color: str = 'red') -> None:
    """

    :param weights: list of weights
    :param axes: pyplot axes
    :param color: color of line
    :return: none
    """
    x1_values = []
    x2_values = []
    for x1 in range(-100, 101):
        x1 = x1 / 100
        for x2 in range(-150, 151):
            x2 = x2 / 100
            if (weights[0] * 1.0 + weights[1] * x1 + weights[2] * x2) == 0:
                x1_values.append(x1)
                x2_values.append(x2)

    axes.add_line(Line2D(x2_values, x1_values, color=color))
