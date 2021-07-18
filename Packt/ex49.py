def is_prime(x):
    for i in range(2,x):
        if (x%i)==0:
            return False
        else:
            return True

def is_prime_2(x):
    for i in range(2,x):
        if (x%i)==0:
            return False
    return True

print(is_prime(5))
print(is_prime_2(5))