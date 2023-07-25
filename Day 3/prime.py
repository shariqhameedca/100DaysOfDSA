number = 11
import math
def prime(number):

    divisors_ = []
    sqrt_num = int(math.sqrt(number))
    for num in range(1, sqrt_num):
        if number % num == 0:
            divisors_.append(num)
            if (number / num != num):
                divisors_.append(int(number/num))
        
    if len(divisors_) == 2:
        return True, divisors_
    else:
        return False, divisors_
    
print(prime(number))
