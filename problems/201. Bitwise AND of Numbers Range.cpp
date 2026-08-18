/*
=== 201. Bitwise AND of Numbers Range ===

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
    Input: [5,7]
    Output: 4
Example 2:
    Input: [0,1]
    Output: 0
*/
// === 24ms(57.83%) & 7.1MB(9.52%) === //
int rangeBitwiseAnd(int m, int n) {
    if(m == n){
        return m;
    }
    long temp = 1;
    long ans = 0;
    while(m != 0 || n != 0){
        ans = m%2==n%2 ? ans+(m%2)*(n%2)*temp : 0;
        m /= 2;
        n /= 2;
        temp *= 2;
    }
    return (int)ans;
}