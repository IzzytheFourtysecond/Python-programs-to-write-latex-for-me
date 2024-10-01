
class Permutation:
	
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Permutation initialization Tools

	def __init__(self, text, order = 0, AlreadyHaveTheTreeMade = (False, [])):
		"""
		The constructor takes in cyclic notation for a permutation 
		in the form of a string. Also, it doesn't do that much error
		checking so it's on the user to make sure they input the
		permutation definition correctly.

		The first optional argument let's one specify the order. If the input order
		is smaller than the largest number in the text, the constructor will
		automatically default to what is in the text.

		The second optional argument is for if you already have the cycle-tree formed.
		That's an option for making functions more efficient. This argument expects a
		tuple: (boolean: isMade, list: theActualTree). Also, it's expected that you are
		specifying the order up front if you set isMade to True. As for text to input,
		you can submit anything since it won't be looked at if isMade is set to True.
		"""
		
		# initialize attributes
		self.cycleTree = []
		self.order = order
		self.storedMap = []

		if AlreadyHaveTheTreeMade[0] == True:
			self.order = order
			self.cycleTree = AlreadyHaveTheTreeMade[1]

		else:	
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
		self.storedMap = [i for i in range(self.order)]
		for branch in self.cycleTree:
			for i in range(len(branch)):
				self.storedMap[branch[i] - 1] = branch[(i + 1) % len(branch)]
	

	# Some Special Important Permutation Functions
	def One(order):
		return Permutation("", order, (True, [[i + 1] for i in range(order)]))
	
	def Transpose(order, pair = (1, 2)):
		return Permutation("(" + str(pair[0]) + " " + str(pair[1]) + ")", order)
	
	def ShiftRight(order):
		return Permutation("", order, (True, [[(i + 1) for i in range(order)]]))
	
	def ShiftLeft(order):
		return Permutation._inverse(Permutation("", order, (True, [[(i + 1) for i in range(order)]])))


	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Arithmetic and Displaying Functions

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
	

	def __str__(self):
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
	

	def __mul__(self, other):
		"""
		This returns the function composition of two permutations
		"""

		# Debug Printing
		# print("self: " + str(self))
		# print("other: " + str(other))

		# Type Checking
		if not isinstance(other, (Permutation)):
			return NotImplemented
		if self.order != other.order:
			return NotImplemented
		
		# Making the NewCycleTree
		newCycleTree = []
		arr = [i for i in range(1, self.order + 1)]
		for ind in range(len(arr)):
			if (t := arr[ind]) == 0:
				continue

			branch = [t]
			arr[t - 1] = 0
			t = self(other(t))

			while (t != branch[0]):
				branch.append(t)
				arr[t - 1] = 0
				t = self(other(t))

			newCycleTree.append(branch)

		return Permutation("", self.order, (True, newCycleTree))
	

	def _inverse(perm):
		"""
		Helper method for taking the inverse of a permutation...
		"""
		newCycleTree = [[branch[0 - i] for i in range(len(branch))] for branch in perm.cycleTree]
		return Permutation("", perm.order, (True, newCycleTree))
	

	def __pow__(self, other):
		"""
		This implements raising a permutation to an integer power...
		"""
		# Debug Printing
		# print(self)
		# print(other)

		# Type Checking
		if not isinstance(other, (int)):
			return NotImplemented
		
		# Case for when the exponent is zero
		result = Permutation.One(self.order)
		if other == 0:
			return result
		
		# Repeated multiplication
		temp = self
		if other < 0:
			temp = Permutation._inverse(temp)
			other = -other
		for i in range(other):
			result *= temp
		
		return result
	

	def __bool__(self):
		"""
		This represents the parity of a permutation. 
		True ----> Even
		False ---> Odd
		"""
		return (sum([len(branch) - 1 for branch in self.cycleTree], 0) % 2) == 0
	

	def __eq__(self, other):
		"""
		Returns True if two permutations represent the same function.
		"""
		if not isinstance(other, Permutation):
			return NotImplemented
		
		return self.storedMap == other.storedMap
	

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Everything below is just me writing random tests as I need them...


# a = Permutation.Transpose(5, (1, 2))
# b = Permutation.One(5)
# c = Permutation.Transpose(5, (3, 5))

# print(a*c)
# print((a * c) ** -1)
# print(a * c == (a * c) ** -1)

