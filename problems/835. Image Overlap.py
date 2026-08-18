'''
=== 835. Image Overlap ===

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?

Example 1:
    Input: A = [[1,1,0],
                [0,1,0],
                [0,1,0]]
           B = [[0,0,0],
                [0,1,1],
                [0,0,1]]
    Output: 3
    Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes: 
    1. 1 <= A.length = A[0].length = B.length = B[0].length <= 30
    2. 0 <= A[i][j], B[i][j] <= 1
'''
# === 1336ms(10.97%) && 14.2MB(33.33%) === #
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a_point = [(x, y) for x in range(len(A)) for y in range(len(A[0])) if A[x][y] == 1]
        b_point = [(x, y) for x in range(len(B)) for y in range(len(B[0])) if B[x][y] == 1]
        pset = set(b_point)
        have_seen = set()
        ans = 0
        for xa, ya in a_point:
            for xb, yb in b_point:
                deltax = xb-xa
                deltay = yb-ya
                if (deltax, deltay) in have_seen:
                    continue
                ans = max(ans, len([1 for xa, ya in a_point if (xa+deltax,ya+deltay) in pset]))
                have_seen.add((deltax, deltay))
        return ans