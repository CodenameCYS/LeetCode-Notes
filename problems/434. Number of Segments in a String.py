'''
=== 434. Number of Segments in a String ===

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.

Example:
    Input: "Hello, my name is John"
    Output: 5
'''
# === 20ms(96.15%) && 12.8MB(100%) === #
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())