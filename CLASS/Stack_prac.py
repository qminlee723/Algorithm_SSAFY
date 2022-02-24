# a = []
#
# a.append(1)
# a.append(2)
# a.append(3)
# print(a)
#
# for i in range(len(a)):
#     print(a.pop())

def is_empty(self):
    return True if self.top == -1 else False

def is_full(self):
    return True if self.top == self.size else False

def push(self, item):
    if self.is_full():
        raise Exception('It is full!')
    self.top += 1
    self.items[self.top] = item

def pop(self):
    if self.is_empty():
        raise Exception('It is empty!')
    else:
        value = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return value
    return self.pop[self.pop]