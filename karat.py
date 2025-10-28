def karatsuba(x, y):
    """
    Perform multiplication of two integers using Karatsuba algorithm.

    Args:
    x, y : int
        Numbers to multiply.

    Returns:
    int
        Product of x and y.
    """
    # Base case for small numbers
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits of the largest number
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the numbers
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # Recursive calls
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    # Combine the results
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    a = 1234
    b = 5678
    product = karatsuba(a, b)
    print(f"{a} * {b} = {product}")
