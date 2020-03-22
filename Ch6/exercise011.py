nums = [1, 2, 3, 4, 5]

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

print(squareEach(nums))
    
