
# --------------------------
# Title: BINGO 2
# By: Zane Dax
# March 4, 2021
# Notes: the game information came from Wikipedia
# --------------------------

#  BINGO

# numbers 1 - 75
# 5 columns 
# 15 numbers in each column
#  B = 1 - 15 
#  I = 16 - 30
#  N = 31 - 45
#  G = 46 - 60
#  O = 61 - 75

# possible Bingo cards 
# P(15,5) * P(15,5) * P(15,5) * P(15,5) * P(15,5) = 5.52e26

import random 

# columns = ['B','I','N','G','O']
# x = random.randint(0,(len(columns)-1))

columns = ['B','I','N','G','O']
x = random.randint(0,(len(columns)-1))
number = random.randint(1,76)


print("\n ***** BINGO *****")

# print(columns[n], number)
# print(number)


if columns[x] == 'B':
	b = random.randint(1,16)
	print(' ', columns[x], b)


if columns[x] == 'I':
	i = random.randint(16,31)
	print(' ',columns[x],i)


if columns[x] == 'N':
	n = random.randint(31,46)
	print(' ', columns[x], n)


if columns[x] == 'G':
	g = random.randint(46,61)
	print(' ', columns[x],g)


if columns[x] == 'O':
	o = random.randint(61,76)
	print(' ', columns[x],o)



	

print(" ***** BINGO *****\n")












