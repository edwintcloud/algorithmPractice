class MovingAverage:
    '''MovingAverage is a class to calculate the moving average of a data stream'''

    def __init__(self, size):
        self.size = size
        self.data = []

    def __str__(self):
        return str(self.data)

    def next(self, item):
        if len(self.data) >= self.size:
            self.data.pop(0)
        self.data.append(item)
        return sum(self.data)/len(self.data)


## TEST ##
m = MovingAverage(3)
print("m:", m)
print("Moving Average: ", m.next(1))
print("m:", m)
print("Moving Average: ", m.next(10))
print("m:", m)
print("Moving Average: ", m.next(3))
print("m:", m)
print("Moving Average: ", m.next(5))
print("m:", m)
