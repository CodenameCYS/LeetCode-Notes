'''
=== 1739. Building Boxes ===

You have a cubic storeroom where the width, length, and height of the room are all equal to n units. You are asked to place n boxes in this room where each box is a cube of unit side length. There are however some rules to placing the boxes:
    - You can place the boxes anywhere on the floor.
    - If box x is placed on top of the box y, then each side of the four vertical sides of the box y must either be adjacent to another box or to a wall.
Given an integer n, return the minimum possible number of boxes touching the floor.

Example 1:
    Input: n = 3
    Output: 3
    Explanation: The figure above is for the placement of the three boxes.
    These boxes are placed in the corner of the room, where the corner is on the left side.
Example 2:
    Input: n = 4
    Output: 3
    Explanation: The figure above is for the placement of the four boxes.
    These boxes are placed in the corner of the room, where the corner is on the left side.
Example 3:
    Input: n = 10
    Output: 6
    Explanation: The figure above is for the placement of the ten boxes.
    These boxes are placed in the corner of the room, where the corner is on the back side.
 
Constraints:
    1. 1 <= n <= 109
'''
# === 28ms && 14.4MB === #
class Solution:
    def minimumBoxes(self, n: int) -> int:
        def S(n):
            return (n*n*n + n*n*3 + n*2)/6
        
        def a(n):
            return n * (n+1) / 2
        
        if n == 1:
            return 1
        
        i, j = 1, n
        while i < j-1:
            m = (i+j) // 2
            if S(m) > n:
                j = m
            else:
                i = m
        res = i * (i+1) // 2
        delta = n - S(i)
        
        i, j = 0, delta
        while i < j-1:
            m = (i+j) // 2
            if a(m) >= delta:
                j = m
            else:
                i = m
        return int(res + j)