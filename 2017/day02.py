'''
Advent of Code 2017 Day 02

Part 1
The spreadsheet consists of rows of apparently-random numbers. 
To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. 
For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

Part 2
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - 
that is, where the result of the division operation is a whole number. 
They would like you to find those numbers on each line, divide them, and add up each line's result.
'''
import sys

part1 = sys.argv[1] == '1'

# Part2- Finds the two numbers in a list that are evenly divisible, and returns the result of the division
def findEvenlyDivisible(listVal):
	listVal.sort(reverse=True)

	length = len(listVal)

	for i in range(0, length):
		for j in range(i+1,length):
			if listVal[i] % listVal[j] == 0:
				return listVal[i] // listVal[j]


with open('input/day02.txt') as f:
	lines = f.readlines()
	# Remove trailing newline characters
	lines = [line.strip() for line in lines]

sum = 0

if part1:
	for line in lines:
		lineValues = [int(val) for val in line.split('\t')]
		maxValue = max(lineValues)
		minValue = min(lineValues)
		sum += maxValue - minValue
else:
	for line in lines:
		lineValues = [int(val) for val in line.split('\t')]
		sum += findEvenlyDivisible(lineValues)

print(sum)


