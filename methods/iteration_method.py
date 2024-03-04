from math import e, log


def function(x: int | float) -> int | float:
    return 1 + e ** -x - 5 ** x


def transform_func(x: int | float) -> float:
    return log(1 + e ** -x, 5)


def derivative(x: int | float) -> float:
    return -1 / (log(5) * (e ** x + 1))


def get_root(a: int | float, b: int, eps: float = 1e-6) -> dict[[str, int | float], [str, int]] | None:
    if abs(derivative(a)) < 1:
        x0 = a
    elif abs(derivative(b)) < 1:
        x0 = b
    else:
        print('Заданная функция не подходит')
        return

    iter_counter = 0
    middle = 1

    while middle > eps:
        x1 = transform_func(x0)
        middle = abs(x1 - x0)
        x0 = x1
        iter_counter += 1

    return {'root': x0, 'iter_counter': iter_counter}
