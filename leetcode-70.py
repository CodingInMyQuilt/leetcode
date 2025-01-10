def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    record = []
    s = 0
    record.extend([n - 1, n - 2])
    while len(record) > 0:
        r = record.pop()
        if r == 0:
            s += 1
        elif r > 0:
            record.extend([r - 1, r - 2])
    return s
            

print(climbStairs(2))