'''
=== 2271. Maximum White Tiles Covered by a Carpet ===

You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.
You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.
Return the maximum number of white tiles that can be covered by the carpet.

Example 1:
    Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
    Output: 9
    Explanation: Place the carpet starting on tile 10. 
    It covers 9 white tiles, so we return 9.
    Note that there may be other places where the carpet covers 9 white tiles.
    It can be shown that the carpet cannot cover more than 9 white tiles.
Example 2:
    Input: tiles = [[10,11],[1,1]], carpetLen = 2
    Output: 2
    Explanation: Place the carpet starting on tile 10. 
    It covers 2 white tiles, so we return 2.
    
Constraints:
    1. 1 <= tiles.length <= 5 * 104
    2. tiles[i].length == 2
    3. 1 <= li <= ri <= 109
    4. 1 <= carpetLen <= 109
    5. The tiles are non-overlapping.
'''
# === 1395ms && 39.6MB === #
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles = sorted(tiles)
        n = len(tiles)
        cnt = [0] + [t[1] - t[0] + 1 for t in tiles]
        cnt = list(accumulate(cnt))
        res = 0
        for i in range(n):
            ed = tiles[i][0] + carpetLen
            j = bisect.bisect_left(tiles, [ed, ed])
            if j >= n or tiles[j][0] == ed:
                res = max(res, cnt[j]-cnt[i])
            else:
                res = max(res, cnt[j-1]-cnt[i] + min(tiles[j-1][1]+1, ed) - tiles[j-1][0])
        return res
        