number = 12345

reverseNum = 0

while number > 0:
    lastD = number % 10
    number = int(number/10)

    reverseNum = reverseNum * 10 + lastD

print(reverseNum)
    