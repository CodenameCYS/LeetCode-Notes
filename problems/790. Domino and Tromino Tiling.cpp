/*
=== 790. Domino and Tromino Tiling ===

We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.
    XX  <- domino

    XX  <- "L" tromino
    X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.
(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

Example:
    Input: 3
    Output: 5
    Explanation: 
    The five different ways are listed below, different letters indicates different tiles:
    XYZ XXZ XYY XXY XYY
    XYZ YYZ XZZ XYY XXY

Note:
    1. N  will be in range [1, 1000].
*/
// === 8ms(100%) && 5.1MB(100%) === //
int numTilings(int N){
    if(N <= 2){
        return N;
    }
    long dp[N+1];
    dp[0] = 1, dp[1] = 1, dp[2] = 2;
    for(int i=3; i<=N; ++i){
        dp[i] = dp[i-1] + dp[i-2];
        for(int j=i-3; j>=0; --j){
            dp[i] += 2 * dp[j];
        }
        dp[i] = dp[i] % 1000000007;
    }
    return dp[N];
}

