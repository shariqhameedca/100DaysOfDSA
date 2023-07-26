def n_numbersv1(i, n):
    if i>n:
        return
    
    print(i)
    n_numbersv1(i+1, n)

n_numbersv1(1, 20)

def n_numbersv2(i):
    if i<1:
        return
    
    n_numbersv2(i-1)
    print(i)

n_numbersv2(20)