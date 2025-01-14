def tribonacci(n):
    """
    :type n: int
    :rtype: int
    """
    a = 0
    b = 1
    c = 1
    if n == 0: 
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        x = 0
        for i in range(3, n+1):
            x = a + b + c
            a = b
            b = c
            c = x
        return x

print(tribonacci(3))