'''
=== 756. Pyramid Transition Matrix ===

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.
We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.
We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.
Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D
We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
 
Example 2:
Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
 
Note:
    1. bottom will be a string with length in range [2, 8].
    2. allowed will have length in range [0, 200].
    3. Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
'''
# === 40ms(41.90%) && 14.1MB(100%) === #
class Solution:
    def update_upper_layer(self, upper_layer_list, up_colors):
        if upper_layer_list == []:
            return up_colors
        ans = set()
        for tmp in upper_layer_list:
            for c in up_colors:
                ans.add(tmp + c)
        return list(ans)
        
    def build_upper_pyramid(self, bottom, allowed_pattern):
        if len(bottom) == 1:
            return True
        if bottom in self.cache.keys():
            return self.cache[bottom]
        
        upper_layer_list = []
        for i in range(len(bottom)-1):
            up_colors = allowed_pattern.get(bottom[i:i+2], [])
            if up_colors == []:
                self.cache[bottom] = False
                return False
            upper_layer_list = self.update_upper_layer(upper_layer_list, up_colors)
        # print(upper_layer_list)
        for layer in upper_layer_list:
            if self.build_upper_pyramid(layer, allowed_pattern):
                self.cache[bottom] = True
                return True
        self.cache[bottom] = False
        return False
    
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        self.cache = {}
        allowed_pattern = {}
        for pattern in allowed:
            if pattern[:2] not in allowed_pattern.keys():
                allowed_pattern[pattern[:2]] = [pattern[-1]]
            else:
                allowed_pattern[pattern[:2]].append(pattern[-1])
        # print(allowed_pattern)
        ans = self.build_upper_pyramid(bottom, allowed_pattern)
        # # print(self.cache)
        return ans