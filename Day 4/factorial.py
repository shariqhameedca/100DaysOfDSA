# Parameterized way
def factorial_v1(n):
    if n == 1:
        return 1
    else:
        return n * factorial_v1(n-1)
    
print(factorial_v1(5))

# Functional way
def factorial_v2(i, factorial):
    if i == 1:
        return factorial
    
    return factorial_v2(i-1, i * factorial)

print(factorial_v2(5, 1))