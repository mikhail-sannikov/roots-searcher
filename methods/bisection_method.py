def function(x: int | float) -> int | float:
    return 3 * x ** 4 + 4 * x ** 3 - 12 * x ** 2 - 7


def get_root(x1: int | float, x2: int, eps: float = 1e-6) -> dict[[str, int | float], [str, int]] | None:
    c = (x1 + x2) / 2
    iter_counter = 0

    while abs(function(c)) > eps:
        iter_counter += 1
        if function(x1) * function(c) < 0:
            x2 = c
        elif function(x2) * function(c) < 0:
            x1 = c
        else:
            return
        c = (x1 + x2) / 2

    return {'root': c, 'iter_counter': iter_counter}
