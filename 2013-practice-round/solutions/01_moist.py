# Google Kickstart: Practice Round, 2013
# Title: Moist (4 pts, 6 pts)
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434944/0000000000434c05
# https://github.com/v1neethnc/google-kickstart-solutions

# Run the code from the 2013-practice-round folder using:
# python solutions/01_moist.py < /files/01_sample_input1.txt
# python solutions/01_moist.py < /files/01_test_input1.txt
# python solutions/01_moist.py < /files/01_test_input2.txt
# Compare the console outputs with the ones in the corresponding output files


n = int(input())
ctr = 0
while ctr < n:
	v = int(input())
	ctr += 1
	names = []
	temp_ctr, res = 0, 0
	while temp_ctr < v:
		ind = 0
		nm = input()
		while len(names) > ind and nm > names[ind]:
			ind += 1
		names.insert(ind, nm)
		if len(names) > 1 and ind != temp_ctr:
			res += 1
		temp_ctr += 1
	print(f"Case #{ctr}: {res}")
