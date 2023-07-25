number = 1

count = 0
while number > 0:
    count += 1
    number /= 10
    number = int(number)

print(count)