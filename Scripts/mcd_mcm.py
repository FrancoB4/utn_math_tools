def mcd(a: int,
        b: int) -> int:
    """This function returns the greatest common divisor from a and b.

    Args:
        a (int): dividend.
        b (int): divider.
    Returns:
        int: the GCD from a and b.
    """
    if a % b == 0:
        return b

    return mcd(b, a % b)


def mcm(a: int,
        b: int) -> int:
    """This function returns the least common multiple from a and b.

    a: [int] factor 1.
    b: [int] factor 2.
    return: [int] the LCM from a and b.
    """
    return int(a * b / mcd(a, b))