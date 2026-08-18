'''
=== 777. Swap Adjacent in LR String ===

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:
    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Output: True
    Explanation:
    We can transform start to end following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX

Note:
    1. 1 <= len(start) = len(end) <= 10000.
    2. Both start and end will only consist of characters in {'L', 'R', 'X'}.
'''
# === 52ms(38.03%) && 13.6MB(14.26%) === #
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X", "") != end.replace("X", ""):
            return False
        st = [(c, i) for i, c in enumerate(start) if c != "X"]
        ed = [(c, i) for i, c in enumerate(end) if c != "X"]
        return all(x[1] <= y[1] for x, y in zip(st, ed) if x[0] == "R") and \
               all(x[1] >= y[1] for x, y in zip(st, ed) if x[0] == "L")