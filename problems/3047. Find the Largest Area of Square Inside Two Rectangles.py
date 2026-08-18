'''
=== 3047. Find the Largest Area of Square Inside Two Rectangles ===

There exist n rectangles in a 2D plane. You are given two 0-indexed 2D integer arrays bottomLeft and topRight, both of size n x 2, where bottomLeft[i] and topRight[i] represent the bottom-left and top-right coordinates of the ith rectangle respectively.
You can select a region formed from the intersection of two of the given rectangles. You need to find the largest area of a square that can fit inside this region if you select the region optimally.
Return the largest possible area of a square, or 0 if there do not exist any intersecting regions between the rectangles.

Example 1:
    Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]
    Output: 1
    Explanation: A square with side length 1 can fit inside either the intersecting region of rectangle 0 and rectangle 1, or the intersecting region of rectangle 1 and rectangle 2. Hence the largest area is side * side which is 1 * 1 == 1.
    It can be shown that a square with a greater side length can not fit inside any intersecting region.
Example 2:
    Input: bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]
    Output: 1
    Explanation: A square with side length 1 can fit inside either the intersecting region of rectangle 0 and rectangle 1, the intersecting region of rectangle 1 and rectangle 2, or the intersection region of all 3 rectangles. Hence the largest area is side * side which is 1 * 1 == 1.
    It can be shown that a square with a greater side length can not fit inside any intersecting region.
    Note that the region can be formed by the intersection of more than 2 rectangles.
Example 3:
    Input: bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]
    Output: 0
    Explanation: No pair of rectangles intersect, hence, we return 0.
 
Constraints:
    1. n == bottomLeft.length == topRight.length
    2. 2 <= n <= 103
    3. bottomLeft[i].length == topRight[i].length == 2
    4. 1 <= bottomLeft[i][0], bottomLeft[i][1] <= 107
    5. 1 <= topRight[i][0], topRight[i][1] <= 107
    6. bottomLeft[i][0] < topRight[i][0]
    7. bottomLeft[i][1] < topRight[i][1]
'''
# === 4690ms && 17.4MB === #
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ans = 0
        n = len(bottomLeft)
        
        def get_intersection(rec1, rec2):
            if rec1[0] > rec2[0]:
                return get_intersection(rec2, rec1)
            if rec1[2] <= rec2[0]:
                return 0
            elif rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
                return 0
            l = min(rec2[2], rec1[2]) - rec2[0]
            if rec1[1] <= rec2[1]:
                h = min(rec1[3], rec2[3]) - rec2[1]
            else:
                h = min(rec1[3], rec2[3]) - rec1[1]
            d = min(h, l)
            return d * d
        
        for i in range(n):
            rec1 = [bottomLeft[i][0], bottomLeft[i][1], topRight[i][0], topRight[i][1]]
            for j in range(i+1, n):
                rec2 = [bottomLeft[j][0], bottomLeft[j][1], topRight[j][0], topRight[j][1]]
                ans = max(ans, get_intersection(rec1, rec2))
        return ans