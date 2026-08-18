'''
=== 733. Flood Fill ===

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.

Example 1:
    Input: 
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: 
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.

Note:
    1. The length of image and image[0] will be in the range [1, 50].
    2. The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
    3. The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''
# === 80ms(47.71%) && 13MB(100%) === #
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        have_seen = set()
        queue = [(sr, sc)]
        color = image[sr][sc]
        lr = len(image)
        lc = len(image[0])
        while queue != []:
            r, c = queue.pop()
            image[r][c] = newColor
            if (r-1,c) not in have_seen and r-1 >= 0 and image[r-1][c] == color:
                queue.append((r-1,c))
            if (r+1,c) not in have_seen and r+1 < lr and image[r+1][c] == color:
                queue.append((r+1,c))
            if (r,c-1) not in have_seen and c-1 >= 0 and image[r][c-1] == color:
                queue.append((r,c-1))
            if (r,c+1) not in have_seen and c+1 < lc and image[r][c+1] == color:
                queue.append((r,c+1))
            have_seen.update([(r-1,c), (r+1,c), (r, c-1), (r, c+1)])
        return image
        