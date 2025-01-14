def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def x(nums, sumList):
        length = len(nums)
        if length >= 4:
            b = nums[3:]
            b[0] += nums[0]
            x(b, sumList)
        if length >= 3:
            a = nums[2:]
            a[0] += nums[0]
            x(a, sumList)
        if length <= 2:
            sumList.append(nums[0] if length == 1 or nums[0] > nums[1] else nums[1])
            return
    length = len(nums)
    if length == 1:
        return nums[0]
    elif length == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    elif length == 3:
        return nums[0] + nums[2] if nums[0] + nums[2] > nums[1] else nums[1]
    sumList = []
    x(nums, sumList)
    x(nums[1:], sumList)
    return max(sumList)