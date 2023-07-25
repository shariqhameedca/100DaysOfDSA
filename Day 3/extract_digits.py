number = 7789
digits = []

while number > 0:
    digits.append(number % 10)
    number /= 10
    number = int(number)

print(digits)