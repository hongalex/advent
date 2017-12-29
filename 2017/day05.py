'''
Advent of Code Day 05

Part 1
The message includes a list of the offsets for each jump. 
Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. 
Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. 
So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

How many steps does it take to reach the exit?

Part 2
Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?

'''

with open('input/day05.txt') as f:
	input = f.readlines()
	instructions_1 = [int(line.strip()) for line in input]
	instructions_2 = [int(line.strip()) for line in input]

# Part 1

index = 0
num_steps_1 = 0
while index < len(instructions_1):
	offset = instructions_1[index]
	instructions_1[index]+=1
	index += offset

	num_steps_1 += 1

# Part 2

index = 0
num_steps_2 = 0
while index < len(instructions_2):
	offset = instructions_2[index]
	if offset >= 3:
		instructions_2[index] -= 1
	else:
		instructions_2[index] += 1

	index += offset

	num_steps_2 += 1


print(num_steps_1)
print(num_steps_2)