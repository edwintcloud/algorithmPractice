# Find length of the largest region in Boolean Matrix
Consider a matrix with rows and columns, where each cell contains either a ‘0’ or a ‘1’ and any cell containing a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally .If one or more filled cells are also connected, they form a region. find the length of the largest region.

Examples:
```
Input : M[][5] = { 0 0 1 1 0
                   1 0 1 1 0
                   0 1 0 0 0
                   0 0 0 0 1 }
Output : 6 
Ex: in the following example, there are 2 regions one with length 1 and the other as 6.
    so largest region : 6
```