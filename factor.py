
def bascara(a, b, c):
    x1, x2 = None, None

    try:
        x1 = (-b + (b ** 2 - 4 * a * c) ** (1/2))/(2 * a)
    except:
        pass

    try:
        x2 = (-b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    except:
        pass

    return x1, x2
