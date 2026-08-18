/*
=== 878. Nth Magical Number ===

A positive integer is magical if it is divisible by either A or B.
Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

 
Example 1:
Input: N = 1, A = 2, B = 3
Output: 2

Example 2:
Input: N = 4, A = 2, B = 3
Output: 6

Example 3:
Input: N = 5, A = 2, B = 4
Output: 10

Example 4:
Input: N = 3, A = 6, B = 4
Output: 8
 

Note:
1. 1 <= N <= 10^9
2. 2 <= A <= 40000
3. 2 <= B <= 40000
*/
# include <stdlib.h>

int gcd(int A, int B){
    if(B == 0){
        return A;
    }
    else{
        return gcd(B, A%B);
    }
}

int* singlelist(int A, int B, int* listlen){
    int lcm = A*B/gcd(A,B);
    *listlen = lcm/A + lcm/B - 1;
    int* ans = (int*)malloc(*listlen * sizeof(int));
    int tempa = A, tempb = B;
    for(int i=0; i<*listlen; ++i){
        if(tempa <= tempb){
            ans[i] = tempa;
            tempa += A;
        }
        else{
            ans[i] = tempb;
            tempb += B;
        }
    }
    return ans;
}

int nthMagicalNumber(int N, int A, int B) {
    int slen;
    int* s = singlelist(A, B, &slen);
    int max = 1e9 + 7;
    if(N%slen == 0){
        return ((long)s[slen-1] * (N/slen)) % max;
    }
    else{
        return ((long)s[slen-1]*(N/slen) + s[N%slen - 1]) % max;
    }
}