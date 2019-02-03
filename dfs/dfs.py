class DFS:
    '''DFS is a class to help with a recursive depth-first search of a 2D Array/Matrix'''
    def __init__(self, arr):
        self.count = 1
        self.arr = arr
    def LargestRegion(self):
        '''LargestRegion returns the count of the largest region'''
        largest = 0
        for x in range(len(self.arr)):
            for y in range(len(self.arr[x])):
                if self.arr[x][y] == 1:
                    self.count = 1
                    self.Search(x, y)
                    if self.count > largest:
                        largest = self.count
        return largest
    def Search(self, x, y):
        '''Search performs recursive dfs search on arr'''
        rowNbr = [-1,1,0,0]
        colNbr = [0,0,-1,1]
        self.arr[x][y] = 0
        for i in range(4):
            row = x + rowNbr[i]
            col = y + colNbr[i]
            if self.IsSafe(row, col):
                self.count += 1
                self.Search(row, col)
    def IsSafe(self, x, y):
        '''IsSafe ensures x and y are not out of bounds and arr[x][y] is not 0'''
        if x < 0 or y < 0:
            return False
        if x >= len(self.arr) or y >= len(self.arr[x]):
            return False
        if self.arr[x][y] == 0:
            return False
        return True

# Test dfs class
arr = [
[0,0,0,1,0,1],
[0,1,1,0,1,1],
[0,0,1,1,1,1],
[0,0,0,0,1,0]
]
dfs = DFS(arr)
print(dfs.LargestRegion())