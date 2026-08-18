'''
=== 3320. Count The Number of Winning Sequences ===

Alice and Bob are playing a fantasy battle game consisting of n rounds where they summon one of three magical creatures each round: a Fire Dragon, a Water Serpent, or an Earth Golem. In each round, players simultaneously summon their creature and are awarded points as follows:
    - If one player summons a Fire Dragon and the other summons an Earth Golem, the player who summoned the Fire Dragon is awarded a point.
    - If one player summons a Water Serpent and the other summons a Fire Dragon, the player who summoned the Water Serpent is awarded a point.
    - If one player summons an Earth Golem and the other summons a Water Serpent, the player who summoned the Earth Golem is awarded a point.
    - If both players summon the same creature, no player is awarded a point.
You are given a string s consisting of n characters 'F', 'W', and 'E', representing the sequence of creatures Alice will summon in each round: 
    - If s[i] == 'F', Alice summons a Fire Dragon.
    - If s[i] == 'W', Alice summons a Water Serpent.
    - If s[i] == 'E', Alice summons an Earth Golem.
Bob’s sequence of moves is unknown, but it is guaranteed that Bob will never summon the same creature in two consecutive rounds. Bob beats Alice if the total number of points awarded to Bob after n rounds is strictly greater than the points awarded to Alice.
Return the number of distinct sequences Bob can use to beat Alice.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: s = "FFF"
    Output: 3
    Explanation:
    Bob can beat Alice by making one of the following sequences of moves: "WFW", "FWF", or "WEW". Note that other winning sequences like "WWE" or "EWW" are invalid since Bob cannot make the same move twice in a row.
Example 2:
    Input: s = "FWEFW"
    Output: 18
    Explanation:
    Bob can beat Alice by making one of the following sequences of moves: "FWFWF", "FWFWE", "FWEFE", "FWEWE", "FEFWF", "FEFWE", "FEFEW", "FEWFE", "WFEFE", "WFEWE", "WEFWF", "WEFWE", "WEFEF", "WEFEW", "WEWFW", "WEWFE", "EWFWE", or "EWEWE".

Constraints:
    1. 1 <= s.length <= 1000
    2. s[i] is either 'F', 'W', or 'E'.
'''
MOD = 10**9+7

pn = [1 for _ in range(1001)]
for i in range(1, 1001):
    pn[i] = (2 * pn[i-1]) % MOD
# === 4936ms && 284.6MB === #
class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        
        def beats(c1, c2):
            if c1 == "F" and c2 == "E":
                return True
            elif c1 == "E" and c2 == "W":
                return True
            elif c1 == "W" and c2 == "F":
                return True
            return False
        
        @lru_cache(None)
        def dp(idx, forbid, points):
            if idx >= n:
                return 1 if points > 0 else 0
            if points > (n-idx):
                return pn[n-idx]
            elif points <= -(n-idx):
                return 0
            ans = 0
            for creature in "FWE":
                if creature == forbid:
                    continue
                if creature == s[idx]:
                    ans += dp(idx+1, creature, points)
                elif beats(creature, s[idx]):
                    ans += dp(idx+1, creature, points+1)
                else:
                    ans += dp(idx+1, creature, points-1)
            return ans % MOD
        
        return dp(0, "", 0)
                
            
            