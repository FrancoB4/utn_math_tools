from mcd_mcm import mcd


def relative_primes(a: int, b: int) -> bool:
    return mcd(a, b) == 1


def prime(a: int) -> bool:
    if a == 2:
        return True
    elif a % 2 == 0:
        return False

    d = int(a**(1/2))

    for i in range(3, d + 1, 2):
        if a % i == 0:
            return False
    
    return True
