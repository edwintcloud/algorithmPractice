## 975 - Odd Even Jump


# incorrect
def solution(A):
    count = 1
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            count += 1

    return count


class Solution:
    def oddEvenJumps(self, A: 'List[int]') -> 'int':

        # sort indexes of A by values in A
        sorted_indexes = sorted(range(len(A)), key = lambda i: A[i])
        oddnext = self.makeStack(sorted_indexes)
        sorted_indexes.sort(key = lambda i: -A[i])
        evennext = self.makeStack(sorted_indexes)

        odd = [False] * len(A)
        even = [False] * len(A)
        odd[len(A)-1] = even[len(A)-1] = True

        for i in range(len(A)-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
    
    # makes monotonic stack
    def makeStack(self, sorted_indexes):
        result = [None] * len(sorted_indexes)
        stack = []
        for i in sorted_indexes:
            while stack and i > stack[-1]:
                result[stack.pop()] = i
            stack.append(i)
        return result

## test ##
s = Solution()
result = s.oddEvenJumps([2,3,1,1,4])
print(result)