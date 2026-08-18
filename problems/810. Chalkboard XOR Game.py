'''
=== 810. Chalkboard XOR Game ===

We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)
Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.
Return True if and only if Alice wins the game, assuming both players play optimally.

Example:
    Input: nums = [1, 1, 2]
    Output: false
    Explanation: 
    Alice has two choices: erase 1 or erase 2. 
    If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
    If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Notes:
    1. 1 <= N <= 1000. 
    2. 0 <= nums[i] <= 2^16.
'''
# === 76ms(68%) && 14.2MB(100%) === #
class Solution(object):
    '''
    # this method is copied from: https://leetcode.com/problems/chalkboard-xor-game/discuss/190068/O(n)-simple-python3-with-explanation-beats-100
    '''
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        r_xor = 0
        for num in nums:
            r_xor = r_xor ^ num
        
        if r_xor == 0:
            # if xor of all elements is 0, then Alice wins
            return True
        
        # Alice wins if and only if there is an even number of numbers
        return len(nums) % 2 == 0