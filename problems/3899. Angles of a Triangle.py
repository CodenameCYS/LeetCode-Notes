'''
=== 3899. Angles of a Triangle ===

You are given a positive integer array sides of length 3.
Determine if there exists a triangle with positive area whose three side lengths are given by the elements of sides.
If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in degrees), sorted in non-decreasing order. Otherwise, return an empty array.
Answers within 10-5 of the actual answer will be accepted.

Example 1:
    Input: sides = [3,4,5]
    Output: [36.86990,53.13010,90.00000]
    Explanation:
    You can form a right-angled triangle with side lengths 3, 4, and 5. The internal angles of this triangle are approximately 36.869897646, 53.130102354, and 90 degrees respectively.
Example 2:
    Input: sides = [2,4,2]
    Output: []
    Explanation:
    You cannot form a triangle with positive area using side lengths 2, 4, and 2.

Constraints:
    1. sides.length == 3
    2. 1 <= sides[i] <= 1000
'''
# === 0ms && 19.58MB === #
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        t = sum(sides)/2
        if any(x >= t for x in sides):
            return []
        a, b, c = sides
        s = math.sqrt(t * (t-a) * (t-b) * (t-c))

        angles = sorted([
            math.degrees(math.asin(2 * s / (a * b))),
            math.degrees(math.asin(2 * s / (b * c))),
            math.degrees(math.asin(2 * s / (a * c))),
        ])

        angles[-1] = 180-angles[-1] if sum(angles[:2]) < 90 else angles[-1]

        return angles