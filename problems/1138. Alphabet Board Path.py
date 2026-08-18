'''
# === 1138. Alphabet Board Path === #

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:
    - 'U' moves our position up one row, if the position exists on the board;
    - 'D' moves our position down one row, if the position exists on the board;
    - 'L' moves our position left one column, if the position exists on the board;
    - 'R' moves our position right one column, if the position exists on the board;
    - '!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

Example 1:
    Input: target = "leet"
    Output: "DDR!UURRR!!DDD!"
Example 2:
    Input: target = "code"
    Output: "RR!DDRR!UUL!R!"
 
Constraints:
    1. 1 <= target.length <= 100
    2. target consists only of English lowercase letters.
'''
# === 40ms(45.74%) & 13.6MB === #
class Solution:
    def moveTo(self, st, ed, route):
        if st == ed:
            route.append("!")
            return ed
        vertical = (ord(ed)-ord("a")) // 5 - (ord(st)-ord("a")) // 5
        horizon = (ord(ed)-ord("a")) % 5 -(ord(st)-ord("a")) % 5
        if vertical < 0:
            if horizon < 0:
                route.extend(["U"]*(-vertical) + ["L"]*(-horizon))
            else:
                route.extend(["U"]*(-vertical) + ["R"]*horizon)
        else:
            if horizon < 0:
                route.extend(["L"]*(-horizon) + ["D"]*vertical)
            else:
                route.extend(["R"]*horizon + ["D"]*vertical)
        route.append("!")
        return ed
            
    def alphabetBoardPath(self, target: str) -> str:
        route = []
        st = 'a'
        for ed in target:
            st = self.moveTo(st, ed, route)
        return ''.join(route)