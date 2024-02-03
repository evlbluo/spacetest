from decimal import Decimal, getcontext

def compute_pi(precision):
    getcontext().prec = precision + 1  # Set the precision
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L
    for i in range(1, precision):
        M = (M * (K ** 3 - 16 * K)) // (i ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = C / S
    return str(pi)[:precision + 1]  # Return pi to the specified precision

# Calculate pi to the 100th decimal place
pi_to_100 = compute_pi(100)
print(pi_to_100)
