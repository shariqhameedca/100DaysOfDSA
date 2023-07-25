number = 371

def armstrong(number):
    sum = 0

    temp = number
    while temp > 0:
        lastD = temp % 10
        sum += lastD ** 3
        temp = int(temp / 10)

    if number == sum:
        return True
    else:
        return False
    
print(armstrong(number))