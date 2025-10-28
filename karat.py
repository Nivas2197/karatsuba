import cmath
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    X = [0]*N
    for k in range(N//2):
        factor = cmath.exp(-2j * cmath.pi * k / N) * odd[k]
        X[k] = even[k] + factor
        X[k + N//2] = even[k] - factor
    return X

def ifft(X):a
    N = len(X)
    X_conj = [x.conjugate() for x in X]
    x_time = fft(X_conj)
    return [x.conjugate()/N for x in x_time]

def multiply_numbers(a, b):
    try:
        A = list(map(int, str(a)))
        B = list(map(int, str(b)))
    except Exception:
        print("Please enter only integers!")
        return None

    A = A[::-1]
    B = B[::-1]

    n = 1
    while n < len(A) + len(B):
        n *= 2

    A += [0] * (n - len(A))
    B += [0] * (n - len(B))

    FA = fft([complex(d) for d in A])
    FB = fft([complex(d) for d in B])

    FC = [FA[i] * FB[i] for i in range(n)]

    C = ifft(FC)
    C = [int(round(c.real)) for c in C]

    for i in range(len(C)):
        if C[i] >= 10:
            if i + 1 >= len(C):
                C.append(0)
            C[i+1] += C[i] // 10
            C[i] %= 10

    while len(C) > 1 and C[-1] == 0:
        C.pop()

    return int(''.join(map(str, C[::-1])))
test_cases = [
    (12, 34),
    (123, 456),
    (99999, 99999),
    (1000, 1000),
    (0, 98765),
    ('abc', 123),
    (456, None),
    ('', 789),
    (3.14, 2),
    ([1, 2, 3], 456),
]

print("------ Running Test Cases ------")
for i, (a, b) in enumerate(test_cases, 1):
    print(f"Test Case {i}: a = {a}, b = {b}")
    result = multiply_numbers(a, b)
    if result is not None:
        print(f"Result: {result}")
    print()
