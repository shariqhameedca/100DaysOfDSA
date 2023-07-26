# Parameterized way
def sum_first_n_v1(i, sum):
    if i < 1:
        return sum
    return sum_first_n_v1(i-1, sum+i)

print(sum_first_n_v1(5, 0))

# Functional way
def sum_first_n_v2(n):
    if n == 0:
        return 0
    else:
        return n + sum_first_n_v2(n-1)
    
print(sum_first_n_v2(5))