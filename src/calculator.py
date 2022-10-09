"""
The Calculator class which facilitates the calculation methods
"""


def calculator(method: str, value1: int, value2: int):
    """

    :param method:
    :param value1:
    :param value2:
    :return:
    """
    if method == "Addition":
        return value1 + value2

    elif method == "Subtraction":
        if value2 < value1:
            return value1 - value2
        else:
            return value2 - value1

    elif method == "Multiplication":
        return value1 * value2

    elif method == "Division":
        return value1 / value2
