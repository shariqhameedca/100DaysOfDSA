n1, n2 = 20, 15

def gcd(num1, num2):
    
    while num1 > 0 and num2 > 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    
    if num1 == 0:
        return num2
    else:
        return num1

print(gcd(n1, n2))