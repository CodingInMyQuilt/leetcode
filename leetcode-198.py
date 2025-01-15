def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def calculateSumList(x):
        sumList = []
        while len(x) != 0:
            index, data = x.pop()
            if index + 2 <= length-1:
                x.append((index+2, data + nums[index + 2]))
            else:
                sumList.append(data)
                continue
            if index + 3 <= length-1:
                x.append((index+3, data + nums[index + 3]))
        return sumList
    length = len(nums)
    if length == 1:
        return nums[0]
    elif length == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    elif length == 3:
        return nums[0] + nums[2] if nums[0] + nums[2] > nums[1] else nums[1]
    else:
        return max(calculateSumList([(0, nums[0]),(1,nums[1])]))

print(rob([4,1,2,7,5,3,1]))