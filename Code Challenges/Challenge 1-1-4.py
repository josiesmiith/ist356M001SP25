numbergrade = int(input('Enter your number grade: '))
if numbergrade >= 95 and numbergrade <= 120:
    lettergrade = 'A'
elif numbergrade >= 75 and numbergrade < 95:
    lettergrade = 'B'
elif numbergrade >= 50 and numbergrade < 75:
    lettergrade = 'C'
elif numbergrade < 50 and numbergrade < 0:
    lettergrade = 'F'
elif numbergrade > 120 or numbergrade < 0:
    lettergrade = 'Bad grade'
else:
    lettergrade = 'Error'

print('Your letter grade is:', lettergrade)
