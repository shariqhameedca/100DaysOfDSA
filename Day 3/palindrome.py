number = 116656611

def palindrome_check(number):
    reverseN = 0
    temp = number
    while temp > 0:
        lastD = temp % 10

        reverseN = reverseN * 10 + lastD
        temp = int(temp/10)

    print(number)
    print(reverseN)
    if reverseN == number:
        return True
    else:
        return False

print(palindrome_check(number=number))