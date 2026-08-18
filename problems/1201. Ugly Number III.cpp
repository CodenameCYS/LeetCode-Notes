/*
=== 1201. Ugly Number III ===

Write a program to find the n-th ugly number.
Ugly numbers are positive integers which are divisible by a or b or c.

Example 1:
    Input: n = 3, a = 2, b = 3, c = 5
    Output: 4
    - Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:
    Input: n = 4, a = 2, b = 3, c = 4
    Output: 6
    - Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 12... The 4th is 6.
Example 3:
    Input: n = 5, a = 2, b = 11, c = 13
    Output: 10
    - Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:
    Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
    Output: 1999999984
 
Constraints:
    1. 1 <= n, a, b, c <= 10^9
    2. 1 <= a * b * c <= 10^18
    3. It's guaranteed that the result will be in range [1, 2 * 10^9]
*/
long lcm(long a, long b){
    long m = a * b;
    while(a % b != 0){
        int tmp = a % b;
        a = b;
        b = tmp;
    }
    return m / b;
}

long count_ugly_number(long n, long a, long b, long c){
    long ab = lcm(a, b);
    long bc = lcm(b, c);
    long ac = lcm(a, c);
    long abc = lcm(ab, ac);
    // printf("%ld, %ld, %ld, %ld", ab, ac, bc, abc);
    return n/a + n/b + n/c - n/ab - n/ac - n/bc + n/abc;
}

bool is_ugly_number(int n, int a, int b, int c){
    return n % a == 0 || n % b == 0 || n % c == 0;
}
// === 4ms && 6.9MB === //
int nthUglyNumber(int n, int a, int b, int c){
    long min = 1, max = 2*1e9;
    if(count_ugly_number(min, a, b, c) == n && is_ugly_number(min, a, b, c)){
        return min;
    }
    else if(count_ugly_number(max, a, b, c) == n && is_ugly_number(max, a, b, c)){
        return max;
    }
    while(true){
        long tmp = (min + max) / 2;
        // printf("%d\t", tmp);
        if(count_ugly_number(tmp, a, b, c) > n){
            max = tmp;
        }
        else if(count_ugly_number(tmp, a, b, c) < n){
            min = tmp;
        }
        else if(!is_ugly_number(tmp, a, b, c)){
            max = tmp;
        }
        else{
            // printf("%d", count_ugly_number(tmp, a, b, c));
            return tmp;
        }
    }
    return 1;
}

