from Puzzle import Puzzle

class PriorityQueue:
    def __init__(self):
        self.buffer = []
    
    def push(self, item):
        self.buffer.append(item)
        self.buffer.sort(key=lambda x: x.cost) # sort by cost in ascending order
    
    def pop(self):
        item = self.buffer[0]
        self.buffer.remove(item)
        return item
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def printQueue(self):
        for item in self.buffer:
            print(item.cost)