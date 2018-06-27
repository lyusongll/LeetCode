# 双栈法：
# 维护两个栈inStack与outStack，其中inStack接收push操作新增的元素，outStack为pop/peek操作提供服务

# 由于栈具有后进先出（Last In First Out）的性质，栈A中的元素依次弹出并压入空栈B之后，栈A中元素的顺序会被逆转

# 当执行pop或者peek操作时，如果outStack中元素为空，则将inStack中的所有元素弹出并压入outStack，然后对outStack执行相应操作

# 由于元素至多只会从inStack向outStack移动一次，因此peek/pop操作的平摊开销为O(1)

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.inStack = []
        self.outStack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.inStack.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        self.outStack.pop()

    # @return an integer
    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    # @return an boolean
    def empty(self):
        return len(self.inStack) + len(self.outStack) == 0


# 单栈法：
# 在执行push操作时，使用辅助栈swap，将栈中元素顺序按照push顺序的逆序存储。

# 此时，push操作的时间复杂度为O(n)，其余操作的时间复杂度为O(1)
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        swap = []
        while self.stack:
            swap.append(self.stack.pop())
        swap.append(x)
        while swap:
            self.stack.append(swap.pop())

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def peek(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0