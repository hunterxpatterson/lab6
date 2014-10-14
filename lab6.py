#1st
total = 0

print 'Number of numbers of first part'
userInput = int(raw_input())

for x in range(userInput):
    print 'Number'
    userInput = int(raw_input())
    total = total + userInput
print total

#2nd
totalCost = []

print 'Number of numbers of second part'
userInput = int(raw_input())

for x in range(userInput):
    print 'Number'
    userInput = int(raw_input())
    totalCost.append(userInput)
print sum(totalCost)

#3rd
total = 0

print 'What number would you like to take the factorial of?'
userInput = int(raw_input())

for x in range(userInput):
    import math
    factorial = math.factorial(userInput)
print factorial

#4th

print 'What number do you want to factor?'
userInput = int(raw_input())
for i in range(1, userInput+ 1):
       if userInput % i == 0:
           print i
