# Zigzag Iterator
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:
```python
v1 = [1, 2]
v2 = [3, 4, 5, 6]
```
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: `[1, 3, 2, 4, 5, 6]`.

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
For example, given the following input:
```python
[1,2,3]
[4,5,6,7]
[8,9]
```
It should return `[1,4,8,2,5,9,3,6,7]`.