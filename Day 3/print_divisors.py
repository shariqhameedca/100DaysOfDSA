import math
number = 36

def divisors(number):
    divisors_ = []

    for num in range(1, int(math.sqrt(number)) + 1):
        if number % num == 0:
            divisors_.append(num)
            if int(number/num) != num:
                divisors_.append(int(number / num))

    return divisors_

print(divisors(36))