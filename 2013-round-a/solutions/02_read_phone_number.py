# Google Kickstart: Round A, 2013
# Title: Read Phone Number (6 pts, 13 pts)
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434ba1/0000000000434813
# https://github.com/v1neethnc/google-kickstart-solutions

# Run the code using:
# python 02_read_phone_number.py < ../files/02_sample_input1.txt
# python 02_read_phone_number.py < ../files/02_test_input1.txt
# python 02_read_phone_number.py < ../files/02_test_input2.txt
# Compare the console outputs with the ones in the corresponding output files


n = int(input())
prefix_map = {1: '', 2: 'double', 3: 'triple', 4: 'quadruple', 5: 'quintuple', 6: 'sextuple', 7: 'septuple', 8: 'octuple', 9: 'nonuple', 10: 'decuple'}
num_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
for case in range(n):
	num, fmt = input().split(' ')
	fmt = list(map(int, fmt.split('-')))
	strings = []
	prev = 0
	for group in fmt:
		ctr = 1
		start, end = prev, prev + group - 1
		while start < end:
			if num[start] == num[start+1]:
				ctr += 1
				start += 1
				continue
			if ctr > 10:
				for j in range(ctr):
					strings.append(num_map[int(num[start])])
			else:
				strings.append(prefix_map[ctr])
				strings.append(num_map[int(num[start])])
			ctr = 1
			start += 1
		if ctr > 10:
			for j in range(ctr):
				strings.append(num_map[int(num[start])])
		else:
			strings.append(prefix_map[ctr])
			strings.append(num_map[int(num[start])])
		prev = end + 1
	fin_ans = f"Case #{case+1}: {' '.join([i for i in strings if i != ''])}"
	print(fin_ans)