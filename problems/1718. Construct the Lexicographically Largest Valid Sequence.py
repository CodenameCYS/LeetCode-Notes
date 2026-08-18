'''
=== 1718. Construct the Lexicographically Largest Valid Sequence ===

Given an integer n, find a sequence that satisfies all of the following:
    - The integer 1 occurs once in the sequence.
    - Each integer between 2 and n occurs twice in the sequence.
    - For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.
Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.
A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

Example 1:
    Input: n = 3
    Output: [3,1,2,3,2]
    Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:
    Input: n = 5
    Output: [5,3,1,4,3,5,2,4,2]
 
Constraints:
    1. 1 <= n <= 20
'''
# === 52ms && 14.2MB === #
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0 for _ in range(2*n-1)]
        status = [0 for _ in range(n+1)]
        
        def dfs(idx):
            nonlocal res
            # print(res)
            # print(status)
            # print("=" * 10)
            if idx >= 2*n-1:
                return True
            for i in range(n, 0, -1):
                if status[i] == 1:
                    continue
                if i != 1 and idx + i < 2*n-1 and res[idx+i] == 0:
                    res[idx] = i
                    res[idx+i] = i
                    status[i] = 1
                    nxt_idx = res.index(0) if 0 in res else 2*n-1
                    success = dfs(nxt_idx)
                    if success:
                        return True
                    status[i] = 0
                    res[idx] = 0
                    res[idx+i] = 0
                elif i == 1:
                    res[idx] = i
                    status[i] = 1
                    nxt_idx = res.index(0) if 0 in res else 2*n-1
                    success = dfs(nxt_idx)
                    if success:
                        return True
                    status[i] = 0
                    res[idx] = 0
            return False

        dfs(0)
        # print("=" * 20)
        return res
            
                    
                    