
class Permutation:
	
	def __init__(self, text, order = 0):
		"""
		The constructor takes in cyclic notation for a permutation 
		in the form of a string. Also, it doesn't do that much error
		checking so it's on the user to make sure they input the
		permutation definition correctly.

		The first optional argument let's one specify the order. If the input order
		is smaller than the largest number in the text, the constructor will
		automatically default to what is in the text.
		"""
		
		# initialize attributes
		self.cycleTree = []
		self.order = order
		self.storedMap = []

		# tokenize the text and clean the tokens
		tokens = text.split(')')
		tokens.pop()
		tokens = [token[1:] for token in tokens]
		# parses out spaces
		tokens = [token.split() for token in tokens]
		# converts strings to ints
		tokens = [[int(num) for num in token] for token in tokens ]

		# find order
		self.order = max([self.order, max([max(token) for token in tokens])])

		# verification step
		arr = [i for i in range(1, self.order + 1)]
		for token in tokens:
			# shift indices around so that least element is first in list
			indMin = token.index(min(token))
			tokenP = [token[(i + indMin) % len(token)] for i in range(len(token))]

			for num in tokenP:
				if arr[num - 1] == 0:
					raise Exception("There is a cycle input mistake. Problem noticed at " + str(token))
				arr[num - 1] = 0
			
			self.cycleTree.append(tokenP)
		
		# little more clean-up:
		for num in arr:
			if not(num == 0):
				self.cycleTree.append([num])
		self.cycleTree.sort(key=lambda token: token[0])

		# create storedMap
		self.storedMap = [i for i in range(order)]
		for branch in self.cycleTree:
			for i in range(len(branch)):
				self.storedMap[branch[i] - 1] = branch[(i + 1) % len(branch)]
	

	def __repr__(self):
		"""
		This prints the cyclic notation of a permutation.
		"""
		treeStrings = []
		for branch in self.cycleTree:
			temp = [str(num) + ' ' for num in branch]
			temp.append(temp.pop()[:-1])
			treeStrings.append(['('] + temp + [')'])

		return ''.join(sum(treeStrings, []))
	

	def __call__(self, num):
		"""
		This let's you call the permutation like a function.
		"""
		return self.storedMap[num - 1]




a = Permutation('(5 4)(3 1 6)(8 2)', 10)

print(a)
for num in range(1, a.order + 1):
	print("a(" + str(num) +") = " + str(a(num)))


