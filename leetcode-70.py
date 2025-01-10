def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        x = 0
        p = 1
        q = 2
        for i in range(3, n+1):
            x = p + q
            p = q
            q = x
        return x
            

print(climbStairs(2))