/*
=== 50. Pow(x, n) ===

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
    Input: 2.00000, 10
    Output: 1024.00000
Example 2:
    Input: 2.10000, 3
    Output: 9.26100
Example 3:
    Input: 2.00000, -2
    Output: 0.25000
    - Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
    1. -100.0 < x < 100.0
    2. n is a 32-bit signed integer, within the range [−231, 231 − 1]
*/
// === 4ms(65.09%) & 6.8MB(100%) === //
double myPow(double x, int n){
    if(n == 0 || x == 1){
        return 1;
    }
    else if(x == 0){
        return 0;
    }
    else if(n < 0){
        return 1/x * myPow(1/x, -(n+1));
    }
    else{
        if(n % 2 == 0){
            double tmp = myPow(x, n/2);
            return tmp * tmp;
        }
        else{
            return x * myPow(x, n-1);
        }
    }
}

