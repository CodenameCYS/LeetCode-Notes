/*
=== 279. Perfect Squares ===

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
    Input: n = 12
    Output: 3 
    Explanation: 12 = 4 + 4 + 4.
Example 2:
    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.
*/
// === 100ms(22.29%) & 6.8MB(42.86%) === //
int numSquares(int n) {
    int dp[n+1];
    for(int i=1; i<=n; ++i){
        dp[i] = INT_MAX;
    }
    for(int i=1; i<=(int)sqrt(n); ++i){
        dp[i*i] = 1;
    }
    for(int i=1; i<=n; ++i){
        for(int j=1; i+j*j<=n; ++j){
            int temp = dp[i] + 1;
            dp[i+j*j] = dp[i+j*j] < temp ? dp[i+j*j] : temp;
        }
    }
    return dp[n];
}