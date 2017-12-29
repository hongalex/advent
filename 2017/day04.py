'''
Advent of Code Day 04

Part 1
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. 
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

Part 2
For added security, yet another system policy has been put in place. 
Now, a valid passphrase must contain no two words that are anagrams of each other - 
that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

Under this new system policy, how many passphrases are valid?


'''

with open('input/day04.txt') as f:
	passphrases = f.readlines()
	# Remove trailing newline characters
	passphrases = [passphrase.strip() for passphrase in passphrases]


# Part 1
num_valid_1 = 0

for passphrase in passphrases:
	words = [word for word in passphrase.split()]
	unique = set()

	valid = True
	for word in words:
		if word not in unique:
			unique.add(word)
		else:
			valid = False
			break
	if valid:
		num_valid_1+=1


# Part 2

num_valid_2 = 0

for passphrase in passphrases:
	words = [word for word in passphrase.split()]

	unique = set()

	valid = True
	for word in words:

		word = ''.join(sorted(word)) 
		if word not in unique:
			unique.add(word)
		else:
			valid = False
			break
	if valid:
		num_valid_2+=1


print(num_valid_1)
print(num_valid_2)