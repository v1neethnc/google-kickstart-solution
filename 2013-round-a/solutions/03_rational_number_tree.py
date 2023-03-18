# Google Kickstart: Round A, 2013
# Title: Rational Number Tree (9 pts, 12 pts)
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434ba1/0000000000434b3c
# https://github.com/v1neethnc/google-kickstart-solutions

# Run the code using:
# python 03_rational_number_tree.py < ../files/03_sample_input1.txt
# python 03_rational_number_tree.py < ../files/03_test_input1.txt
# python 03_rational_number_tree.py < ../files/03_test_input2.txt
# Compare the console outputs with the ones in the corresponding output files

from fractions import Fraction

class fusc_calculator:
	
	def __init__(self) -> None:
		self.fusc_values = {0: 0, 1: 1}

	def fusc_calc(self, n):
		if n in self.fusc_values.keys():
			return self.fusc_values[n]
		if n % 2:
			res = self.fusc_calc(n//2) + self.fusc_calc(n//2 + 1)
		else:
			res = self.fusc_calc(n//2)
		self.fusc_values[n] = res
		return res
	
n = int(input())
for case in range(n):
	nums = list(map(int, input().split(' ')))
	# Using Calkin-Wilf Sequence calculation using Stern's diatomic sequence
	fusc_obj = fusc_calculator()
	if nums[0] == 1:
		print(f"Case #{case+1}: {fusc_obj.fusc_calc(nums[1])} {fusc_obj.fusc_calc(nums[1]+1)}")
	else:
		fr_val = Fraction(nums[1], nums[2])
		lst_vals = []
		while fr_val != Fraction(0, 1):
			if fr_val.numerator < fr_val.denominator:
				if lst_vals == []:
					lst_vals.append(0)
				fr_val = Fraction(fr_val.denominator, fr_val.numerator)
			val = fr_val.numerator // fr_val.denominator
			lst_vals.append(val)
			fr_val = fr_val - Fraction(val, 1)
		if not len(lst_vals) % 2:
			last = lst_vals[-1]
			lst_vals[-1] -= 1
			lst_vals.append(1)
		bin_str = ''
		for ind, val in enumerate(lst_vals):
			bin_str = str((ind + 1)%2)*val + bin_str
		print(f"Case #{case+1}: {int(bin_str, 2)}")