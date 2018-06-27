class MinStack:
	def __init__(self):
		self.minstack = []
		self.stack = []

	def push(self, x):
		self.stack.append(x)
		if len(self.minstack) == 0 or x <=self.minstack[-1]:
			self.minstack.append(x)

	def pop(self):
		if self.stack[-1] == self.minstack[-1]:
			self.minstack.pop()
		return self.stack.pop()

	def getMin(self):
		return self.minstack[-1]


	def top(self):
		return self.stack[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-1)
    # print([stack.top(), stack.getMin()])
    a=stack.top()
    stack.getMin()
    print(a)
