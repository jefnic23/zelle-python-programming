infileName = input('Name of file to load: ')
infile = open(infileName + '.txt', 'r')

def toNumbers(strList):
    return [eval(n.strip()) for n in infile.readlines()]

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums

def sumList(nums):
    return sum(nums)

nums = toNumbers(infile)
print(sumList(squareEach(nums)))
infile.close()

