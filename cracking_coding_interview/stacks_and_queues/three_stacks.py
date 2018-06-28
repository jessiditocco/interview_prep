class MultiStack(object):

    def __init__(self, stack_capacity):
        self.numstacks = 3
        self.arr = [0] * (stack_capacity * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stack_capacity = stack_capacity

    def is_full(self, stacknum):
        # if stacknum not in range(len(self.sizes)):
        #     raise Exception("Not valid stacknum")  
        return self.sizes[stacknum] == self.stack_capacity

    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0

    def push(self, item, stacknum):
        if self.is_full(stacknum):
            raise Exception("Stack is full")
        else:
            self.sizes[stacknum] += 1
            self.arr[self.index_of_top(stacknum)] = item

    def index_of_top(self, stacknum):
        offset = stacknum * self.stack_capacity
        return offset + self.sizes[stacknum] - 1


    def push(self, stacknum, item):
        if self.is_full(stacknum):
            raise Exception("Stack is full!")

        else:
            self.sizes[stacknum] += 1
            top_stack_index = self.index_of_top(stacknum)
            self.arr[top_stack_index] = item

    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception("Stack is empty")

        value = self.array[self.index_of_top(stacknum)]
        self.array[self.index_of_top(stacknum)] = 0
        self.sizes[stacknum] -= 1

        return value

    def peak(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception("Stack is empty")

        return self.array[self.index_of_top(stacknum)]

if __name__ == "__main__":
    three_stacks = MultiStack(2)


    