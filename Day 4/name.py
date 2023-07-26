def print_name(i, n):
    if i>n:
        return
    
    print('Shariq')
    print_name(i+1, n)

print_name(1, 20)