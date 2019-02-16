class Matrix2D:
    '''Matrix2D is a class to help sum regions in a 2d matrix'''

    def __init__(self, data):
        self.data = data

    def update(self, x, y, i):
        try:
            self.data[x][y] = i 
        except IndexError:
            print("x and/or y are not a valid index in the matrix")

    def sumRegion(self, x1, y1, x2, y2):
        try:
            result = 0
            for i in range(x1, y2+2):
                result += sum(self.data[i][y1:x2])
            return result
        except IndexError:
            print("x1, y1, x2, and/or y2 are not a valid index in the matrix")

## TEST ##
matrix = Matrix2D([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
print(matrix.sumRegion(2, 1, 4, 3))
matrix.update(3, 2, 2)
print(matrix.sumRegion(2, 1, 4, 3))