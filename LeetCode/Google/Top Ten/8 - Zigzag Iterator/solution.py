class ZigzagIterator:

    def __init__(self, data):
        if len(data) < 2:
            raise Exception("data must contain at least 2 vectors")

        self.data = data
        self.ptr = 0

    def next(self):

        # pop element from list into result
        result = self.data[self.ptr].pop(0)

        # if list at ptr becomes empty, remove it 
        # from data and decrease ptr
        if len(self.data[self.ptr]) == 0:
            self.data.pop(self.ptr)
            self.ptr -= 1
    
        # increment pointer until it reaches len(data)
        self.ptr += 1
        if self.ptr >= len(self.data):
            self.ptr = 0
        
        # return result
        return result

    def hasNext(self):
        return False if len(self.data) == 0 else True


## TEST ##
tests = [
    [[1, 2], [3, 4, 5, 6]],
    [[1, 2, 3],
     [4, 5, 6, 7],
        [8, 9]]
]
for test in tests:
    result = []
    iterator = ZigzagIterator(test)
    while iterator.hasNext():
        result.append(iterator.next())
    print(result)
