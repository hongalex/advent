'''
Advent of Code Day 03

Part 1
Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. 

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the 
only access port for this memory system) by programs that can only move up, down, left, or right. 
They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

'''

import math

input = 347991

distance = 0

# First, find the length of the side of the last full spiral dimension
fullSideLength = math.floor(math.sqrt(input))
# The inner full square has to always of odd size
if fullSideLength % 2 == 0:
	fullSideLength -= 1

# Number of squares in the full grid
numFullSquares = fullSideLength**2

# Number of squares to place in last level of incompletes
numOuterSquares = input - numFullSquares

# Find where on the outer side the square is on 
index = numOuterSquares % (fullSideLength+1) 

outerSideLength = fullSideLength + 1

# Add the distance to the middle square, then to the center 
distance += abs(index - outerSideLength//2)
distance += outerSideLength // 2

print(distance)

