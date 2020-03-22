score  = eval(input('Enter exam score: '))

def grade(score):
    grades = 'F' * 60 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11
    return grades[score]

print('Grade: {}'. format(grade(score)))
