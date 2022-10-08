# Google Kickstart: Practice Round, 2013
# Title: Bad Horse (12 pts, 21 pts)
# https://github.com/v1neethnc/google-kickstart-solutions

# Run the code using:
# python 03_bad_horse.py < ../files/03_sample_input1.txt
# python 03_bad_horse.py < ../files/03_test_input1.txt
# python 03_bad_horse.py < ../files/03_test_input2.txt
# Compare the console outputs with the ones in the corresponding output files

class villian_coloring:
	def  __init__(self):
		self.graph_vals = {}
		self.colours = {}
	
	def add_to_graph(self, key, value):
		if key not in self.graph_vals.keys():
			self.graph_vals[key] = [value]
		else:
			self.graph_vals[key].append(value)
		
		if value not in self.graph_vals.keys():
			self.graph_vals[value] = []
	
	def add_to_color(self, v1, v2):
		if v1 not in self.colours.keys():
			self.colours[v1] = None
		if v2 not in self.colours.keys():
			self.colours[v2] = None

	def colouring(self, key, color):
		self.colours[key] = color
		for val in self.graph_vals[key]:
			if self.colours[val] == color:
				return False
			if self.colours[val] == None and not self.colouring(val, 1-color):
				return False
		return True

n = int(input())
ctr = 0
while ctr < n:
	villian_obj = villian_coloring()
	graph_vals, colours = {}, {}
	temp_ctr = int(input())
	while temp_ctr > 0:
		v, d = input().split(' ')
		villian_obj.add_to_graph(v, d)
		villian_obj.add_to_color(v, d)
		temp_ctr -= 1
	ctr += 1
	res = "Yes"
	for key in villian_obj.graph_vals.keys():
		if villian_obj.colours[key] == None:
			if not villian_obj.colouring(key, 0):
				res = "No"
				break
	print(f"Case #{ctr}: {res}")
