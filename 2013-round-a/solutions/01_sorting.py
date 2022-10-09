# Google Kickstart: Round A, 2013
# Title: Sorting (5 pts, 8 pts)
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434ba1/0000000000434ad6
# https://github.com/v1neethnc/google-kickstart-solutions

# Run the code using:
# python 01_sorting.py < ../files/01_sample_input1.txt
# python 01_sorting.py < ../files/01_test_input1.txt
# python 01_sorting.py < ../files/01_test_input2.txt
# Compare the console outputs with the ones in the corresponding output files


n = int(input())
ctr = 0
while ctr < n:
	arr_len = int(input())
	arr_vals = list(map(int, input().split(' ')))
	first_indices = [i for i in range(0, arr_len) if arr_vals[i] % 2 == 0]
	second_indices = [i for i in range(0, arr_len) if arr_vals[i] % 2 != 0]
	first_arr = [arr_vals[i] for i in first_indices]
	second_arr = [arr_vals[i] for i in second_indices]
	first_arr.sort(reverse=True)
	second_arr.sort()
	res = [0 for i in range(0, arr_len)]
	c1 = 0
	for i in first_indices:
		res[i] = first_arr[c1]
		c1 += 1
	c2 = 0
	for i in second_indices:
		res[i] = second_arr[c2]
		c2 += 1
	ctr += 1
	res = ' '.join([str(i) for i in res])
	print(f"Case #{ctr}: {res}")
