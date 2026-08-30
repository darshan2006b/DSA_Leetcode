class MyStack(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        pop = self.queue.pop(0)
        return pop

    def top(self):
        return self.queue[0]


    def empty(self):
        if not self.queue:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()