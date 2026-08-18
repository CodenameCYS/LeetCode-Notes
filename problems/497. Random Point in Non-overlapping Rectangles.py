'''
=== 497. Random Point in Non-overlapping Rectangles ===

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:
    1. An integer point is a point that has integer coordinates. 
    2. A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
    3. ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
    4. length and width of each rectangle does not exceed 2000.
    5. 1 <= rects.length <= 100
    6. pick return a point as an array of integer coordinates [p_x, p_y]
    7. pick is called at most 10000 times.

Example 1:
    Input: 
    ["Solution","pick","pick","pick"]
    [[[[1,1,5,5]]],[],[],[]]
    Output: 
    [null,[4,1],[4,1],[3,3]]
Example 2:
    Input: 
    ["Solution","pick","pick","pick","pick","pick"]
    [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
    Output: 
    [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
    Explanation of Input Syntax:
    The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
'''
# === 200ms(62.79%) && 16.5MB(100%) === #
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # self.area = []
        for i, rect in enumerate(rects):
            s = (rect[2] - rect[0]+1)*(rect[3]-rect[1]+1)
            if i == 0:
                self.area = [s]
            else:
                self.area.append(self.area[-1] + s)

    def find_rect(self, val):
        i = 0; j = len(self.rects) - 1
        if val <= self.area[0]:
            return self.rects[0]
        while j-i > 1:
            mid = (i+j) // 2
            if self.area[mid] < val:
                i = mid
            elif self.area[mid] > val:
                j = mid
            else:
                return self.rects[mid]
        return self.rects[j]
                
    def pick(self) -> List[int]:
        seed = random.random() * self.area[-1]
        rect = self.find_rect(seed)
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()