class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.oldest = 0

    def append(self, item):

        if len(self.buffer) == self.capacity:
            self.buffer[self.oldest] = item
            self.oldest += 1
            if self.oldest == self.capacity:
                self.oldest = 0
        else:
            self.buffer.append(item)

    def get(self):
        return self.buffer
