'''
=== 2337. Move Pieces to Obtain a String ===

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:
    - The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
    - The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

Example 1:
    Input: start = "_L__R__R_", target = "L______RR"
    Output: true
    Explanation: We can obtain the string target from start by doing the following moves:
    - Move the first piece one step to the left, start becomes equal to "L___R__R_".
    - Move the last piece one step to the right, start becomes equal to "L___R___R".
    - Move the second piece three steps to the right, start becomes equal to "L______RR".
    Since it is possible to get the string target from start, we return true.
Example 2:
    Input: start = "R_L_", target = "__LR"
    Output: false
    Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
    After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
Example 3:
    Input: start = "_R", target = "R_"
    Output: false
    Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
 
Constraints:
    1. n == start.length == target.length
    2. 1 <= n <= 105
    3. start and target consist of the characters 'L', 'R', and '_'.
'''
# === 629ms && 17.1MB === #
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        cnt1, cnt2 = Counter(start), Counter(target)
        if cnt1["L"] != cnt2["L"] or cnt1["R"] != cnt2["R"]:
            return False
        
        lcnt, rcnt = 0, 0
        for ch1, ch2 in zip(start, target):
            if ch1 == "L":
                lcnt += 1
            elif ch1 == "R":
                rcnt +=1
            
            if ch2 == "L":
                lcnt -= 1
            elif ch2 == "R":
                rcnt -=1
            
            if lcnt > 0 or rcnt < 0:
                return False
        
        lr1, lr2 = [], []
        cnt1, cnt2 = 0, 0
        for ch1, ch2 in zip(start, target):
            if ch1 == "R":
                cnt1 += 1
            elif ch1 == "L":
                lr1.append(cnt1)
            
            if ch2 == "R":
                cnt2 += 1
            elif ch2 == "L":
                lr2.append(cnt2)
        
        return all(x == y for x, y in zip(lr1, lr2))
        