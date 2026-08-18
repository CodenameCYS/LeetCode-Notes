'''
=== 554. Brick Wall ===

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
Output: 2

Note:
    1. The width sum of bricks in different rows are the same and won't exceed INT_MAX.
    2. The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.
'''
# === 192ms(64.54%) && 17.5MB(50%) === #
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap = {}
        for bricks in wall:
            l = 0
            for b in bricks[:-1]:
                l += b
                gap[l] = 1 if l not in gap.keys() else gap[l] + 1
        gap = sorted(gap.items(), key=lambda x:x[1], reverse=True)
        # print(gap)
        if len(gap) == 0:
            return len(wall)
        else:
            return len(wall) - gap[0][1]