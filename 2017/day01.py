''' 
Advent of Code 2017 Day 1 

Part 1
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the 
next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

Part 2
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. 
That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. 
Fortunately, your list has an even number of elements.
'''

import sys 

input = open('input/day01.txt','r').read()

part1 = sys.argv[1] == '1'

sum = 0

if part1:
	# Since it is circular, the first character can match with the last character
	currChar = input[-1]

	for i in input:
		nextChar = i
		if currChar == nextChar:
			sum += int(nextChar)
		currChar = nextChar

else:
	inputLen = len(input)
	halfwaySteps = inputLen//2
	
	for i in range(inputLen):
		nextCharIndex = (i + halfwaySteps) % inputLen

		currChar = input[i]
		nextChar = input[nextCharIndex]

		if currChar == nextChar:
			sum += int(nextChar)
		currChar = nextChar

print(sum)
