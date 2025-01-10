def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    def recur(n, m=0):
        if n > 0:
            return recur(n-1) + recur(n-2)
        elif n == 0:
            return m + 1
        else:
            return 0
    return recur(n)

print(climbStairs(3))