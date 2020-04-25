'''
Lattice paths
   
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

n = 20

previousColumn = [i + 1 for i in range(0, n + 1)]
thisColumn = [1 for i in range(0, n + 1)]

for col in range(2, n + 1):
    for row in range(1, n + 1):
        thisColumn[row] = thisColumn[row - 1] + previousColumn[row]
    previousColumn = thisColumn

print(f'Number of paths through a {n}x{n} lattice = {thisColumn[n]}')
# Number of paths through a 20x20 lattice = 137846528820