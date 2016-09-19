import random
import math

# random_numbers = [range(0, 49, 2)]
# print(random_numbers)
# print random.shuffle(random_numbers)

my_random_numbers = list()

for number in range(20):
	my_random_numbers.append(random.randint(0,49))

print(my_random_numbers, 'my_random_numbers')


my_squared_numbers = list()

# x = float(x)

my_squared_numbers = [x*x for x in my_random_numbers]

print(my_squared_numbers, 'my_squared_number')



# my_squared_numbers(math.sqrt(my_random_numbers).float)

