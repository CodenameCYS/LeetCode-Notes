/*
=== 1022. Smallest Integer Divisible by K ===

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.
Return the length of N.  If there is no such N, return -1.

Example 1:
    Input: 1
    Output: 1
    Explanation: The smallest answer is N = 1, which has length 1.
Example 2:
    Input: 2
    Output: -1
    Explanation: There is no such positive integer N divisible by 2.
Example 3:
    Input: 3
    Output: 3
    Explanation: The smallest answer is N = 111, which has length 3.
 
Note:
    1. 1 <= K <= 10^5
*/
// === 4ms & 6.4MB === //
int smallestRepunitDivByK(int K) {
    if(K%2==0 || K%5==0){
        return -1;
    }
    
    int len = 1;
    long val = 1;
    for(;len<1e6; ++len){
        if(val % K == 0){
            return len;
        }
        val = (10*val+1) % K;
    }
    return -1;
}