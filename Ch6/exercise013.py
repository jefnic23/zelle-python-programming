strList = ['1', '2', '3', '4', '5']

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])
    return strList

print(strList)
print(toNumbers(strList))
