def reverse(arr):
    arr.reverse()

# test reverse function
numbers = [1,2,3,4,5,6,7,8,9,10]
arr = [i for i in numbers]
reverse(arr)
print("Numbers: ", numbers)
print("Reversed: ", arr)