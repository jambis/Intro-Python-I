def isPrime(n):
    n = abs(n)

    if n == 0 or n == 1:
        return False

    for num in range(2, n+1):
        if n % num == 0 and n == num:
            return True
        elif n % num == 0:
            return False
        else:
            continue


print(isPrime(2))  # True
print(isPrime(3))  # True
print(isPrime(4))  # False
print(isPrime(6))  # False
print(isPrime(7))  # True
print(isPrime(30))  # False
print(isPrime(5))  # True
print(isPrime(-3))  # True
