'''
=== 1654. Minimum Jumps to Reach Home ===

A certain bug's home is on the x-axis at position x. Help them get there from position 0.
The bug jumps according to the following rules:
    - It can jump exactly a positions forward (to the right).
    - It can jump exactly b positions backward (to the left).
    - It cannot jump backward twice in a row.
    - It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.
Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

Example 1:
    Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
    Output: 3
    Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
Example 2:
    Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
    Output: -1
Example 3:
    Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
    Output: 2
    Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.
    
Constraints:
    1. 1 <= forbidden.length <= 1000
    2. 1 <= a, b, forbidden[i] <= 2000
    3. 0 <= x <= 2000
    4. All the elements in forbidden are distinct.
    5. Position x is not forbidden.
'''
# === 100ms && 19.6MB === #
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        
        seen = {0}
        path = [0]
        
        @lru_cache(None)
        def dfs(loc, can_back):
            if loc == x:
                return 0
            if loc < x:
                if loc + a not in forbidden and loc + a not in seen:
                    seen.add(loc + a)
                    path.append(loc + a)
                    tmp = dfs(loc+a, True)
                    if tmp != -1:
                        return tmp + 1
                    seen.remove(loc+a)
                    path.pop()
                if can_back and loc - b >= 0 and loc - b not in seen and loc-b not in forbidden:
                    seen.add(loc-b)
                    path.append(loc-b)
                    tmp = dfs(loc-b, False)
                    if tmp != -1:
                        return tmp + 1
                    seen.remove(loc-b)
                    path.pop()
                return -1
            else:
                if b-a <= 0 and loc > x+b:
                    return -1
                if can_back and loc - b >= 0 and loc - b not in seen and loc-b not in forbidden:
                    seen.add(loc-b)
                    path.append(loc-b)
                    tmp = dfs(loc-b, False)
                    if tmp != -1:
                        return tmp + 1
                    seen.remove(loc-b)
                    path.pop()
                if loc >= 4000:
                    return -1
                if loc + a not in forbidden and loc + a not in seen:
                    seen.add(loc + a)
                    path.append(loc+a)
                    tmp = dfs(loc+a, True)
                    if tmp != -1:
                        return tmp + 1
                    seen.remove(loc+a)
                    path.pop()
                return -1
        return dfs(0, True)