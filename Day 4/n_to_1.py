def from_n_to_1_v1(i):
    if i<1:
        return
    print(i)
    from_n_to_1_v1(i-1)

from_n_to_1_v1(20)

def from_n_to_1_v2(i, n):
    if i>n:
        return
    from_n_to_1_v2(i+1, n)
    print(i)

from_n_to_1_v2(1, 20)