'''
=== 2222. Number of Ways to Select Buildings ===

You are given a 0-indexed binary string s which represents the types of buildings along a street where:
    - s[i] = '0' denotes that the ith building is an office and
    - s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.
    - For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

Example 1:
    Input: s = "001101"
    Output: 6
    Explanation: 
    The following sets of indices selected are valid:
    - [0,2,4] from "001101" forms "010"
    - [0,3,4] from "001101" forms "010"
    - [1,2,4] from "001101" forms "010"
    - [1,3,4] from "001101" forms "010"
    - [2,4,5] from "001101" forms "101"
    - [3,4,5] from "001101" forms "101"
    No other selection is valid. Thus, there are 6 total ways.
Example 2:
    Input: s = "11100"
    Output: 0
    Explanation: It can be shown that there are no valid selections.
 
Constraints:
    1. 3 <= s.length <= 105
    2. s[i] is either '0' or '1'.
'''
# === 2938ms && 24.6MB === #
class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        post0 = [0 for _ in range(n)]
        post1 = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            if s[i+1] == "0":
                post0[i] = post0[i+1] + 1
                post1[i] = post1[i+1]
            else:
                post0[i] = post0[i+1]
                post1[i] = post1[i+1] + 1
        # print("post 0: ", post0)
        # print("post 1: ", post1)
                
        post01 = [0 for _ in range(n)]
        post10 = [0 for _ in range(n)]
        for i in range(n-3, -1, -1):
            if s[i+1] == "0":
                post01[i] = post01[i+1] + post1[i+1]
                post10[i] = post10[i+1]
            else:
                post01[i] = post01[i+1]
                post10[i] = post10[i+1] + post0[i+1]
        # print("post 01: ", post01)
        # print("post 10: ", post10)
        
        res = 0
        for i in range(n-2):
            if s[i] == "0":
                res += post10[i]
            else:
                res += post01[i]
        return res
        