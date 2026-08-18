'''
=== 228. Summary Ranges ===

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
    Input:  [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    - Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:
    Input:  [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    - Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''
# === 36ms(75.77%) & 13MB(5.19%) === #
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ans = []
        st = -1
        ed = -1
        for n in nums:
            if st == -1:
                st = n
                ed = n
            elif n == ed + 1:
                ed += 1
            else:
                if st == ed:
                    ans.append('{}'.format(st))
                else:
                    ans.append('{}->{}'.format(st, ed))
                st = n
                ed = n
        if st == ed:
            ans.append('{}'.format(st))
        else:
            ans.append('{}->{}'.format(st, ed))
        return ans