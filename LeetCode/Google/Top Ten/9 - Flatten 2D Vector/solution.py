class Flatten2DVector:

    def __init__(self, data):
        self.data = data

    def next(self):

        # if queue is empty, raise exception
        if self.hasNext() is False:
            raise Exception("no next element to iterate")

        # pop top of queue into result
        result = self.data[0].pop(0)

        # if cur list gets empty, remove it
        if len(self.data[0]) == 0:
            self.data.pop(0)
        
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
    iterator = Flatten2DVector(test)
    while iterator.hasNext():
        result.append(iterator.next())
    print(result)
