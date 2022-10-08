# Google Kickstart: Practice Round, 2013
# Title: Captain Hammer (22 pts)
# https://github.com/v1neethnc/google-kickstart-solutions

# Run the code using:
# python 02_captain_hammer.py < ../files/02_sample_input1.txt
# python 02_captain_hammer.py < ../files/02_test_input1.txt
# Compare the console outputs with the ones in the corresponding output files


from math import asin, pi

n = int(input())
ctr, g = 0, 9.8
while ctr < n:
	v, d = map(int, input().split(' '))
	temp_val = min(1, (g*d)/(v*v))
	res = (180 * asin(temp_val) / (2 * pi))
	ctr += 1
	print(f"Case #{ctr}: {round(res, 9):.9f}")
