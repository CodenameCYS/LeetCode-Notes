/*
=== 887. Super Egg Drop ===

You are given K eggs, and you have access to a building with N floors from 1 to N. 
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
Your goal is to know with certainty what the value of F is.
What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

Example 1:
    Input: K = 1, N = 2
    Output: 2
    Explanation: 
    Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
    Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
    If it didn't break, then we know with certainty F = 2.
    Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:
    Input: K = 2, N = 6
    Output: 3
Example 3:
    Input: K = 3, N = 14
    Output: 4
 
Note:
    1. 1 <= K <= 100
    2. 1 <= N <= 10000
*/
// === 0ms(100%) && 5.7MB(100%) === // 可参考解法：https://leetcode.com/problems/super-egg-drop/discuss/465960/Simple-C%2B%2B-DP-solution-with-comments
int superEggDrop(int K, int N){
    int dp[N+1][K+1];
    for(int moves=0; moves<=N; ++moves){
        for(int eggs=0; eggs<=K; ++eggs){
            if(moves == 0 || eggs == 0){
                dp[moves][eggs] = 0;
                continue;
            }
            dp[moves][eggs] = dp[moves-1][eggs-1] + 1 + dp[moves-1][eggs];
            // printf("%d ", dp[moves][eggs]);
            if(dp[moves][eggs] >= N){
                return moves;
            }
        }
        // printf("\n");
    }
    return -1;
}

// 另外参考B站李永乐的解法可以得到另一种解法如下：
// 不过该解法会导致超时
/*
int max(int x, int y){
    return x > y ? x : y;
}
int superEggDrop(int K, int N){
    int dp[K+1][N+1];
    for(int k=0; k<=K; ++k){
        for(int n=0; n<=N; ++n){
            if(n == 0 || k == 0){
                dp[k][n] = 0;
            }
            else if(k == 1){
                dp[k][n] = n;
            }
            else if(n == 1){
                dp[k][n] = 1;
            }
            else{
                int fkn = n;
                for(int i=1; i<=n; ++i){
                    int fi = max(dp[k-1][i-1], dp[k][n-i]) + 1;
                    fkn = fkn < fi ? fkn : fi;
                }
                dp[k][n] = fkn;
            }
        }
    }
    return dp[K][N];
}
*/