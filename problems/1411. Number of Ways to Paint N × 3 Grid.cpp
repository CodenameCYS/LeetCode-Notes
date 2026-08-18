/*
=== 1411. Number of Ways to Paint N × 3 Grid ===

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).
You are given n the number of rows of the grid.
Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:
    Input: n = 1
    Output: 12
    Explanation: There are 12 possible way to paint the grid as shown:
Example 2:
    Input: n = 2
    Output: 54
Example 3:
    Input: n = 3
    Output: 246
Example 4:
    Input: n = 7
    Output: 106494
Example 5:
    Input: n = 5000
    Output: 30228214
 
Constraints:
    1. n == grid.length
    2. grid[i].length == 3
    3. 1 <= n <= 5000
*/
// === 0ms(100%) && 5MB === //
int numOfWays(int n){
    long MOD=1000000007;
    long a = 6, b = 6;
    for(int i=1; i<n; ++i){
        long aa = (2*a + 2*b) % MOD;
        long bb = (2*a + 3*b) % MOD;
        a = aa;
        b = bb;
    }
    return (a + b) % MOD;
}