'''
=== 120. Triangle ===

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type':'memory'
}
cache = CacheManager(**parse_cache_config_options(cache_opts))

class Solution:
    @cache.cache('test', expire=600)
    def min_total(self, triangle, level, row, col, total):
        if row == level:
            return total
        total += triangle[row][col]
        return min(
                    self.min_total(triangle, level, row+1, col, total), 
                    self.min_total(triangle, level, row+1, col+1, total)
                  )
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.min_total(triangle, len(triangle), 0, 0, 0)