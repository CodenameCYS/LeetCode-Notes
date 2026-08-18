/*
=== 1175. Prime Arrangements ===

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7.
 
Example 1:
    Input: n = 5
    Output: 12
    - Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:
    Input: n = 100
    Output: 682289015
 
Constraints:
    1. 1 <= n <= 100
*/
bool is_prime(int n){
    int primes[] = {2,3,5,7};
    if(n <= 10){
        return n == 2 || n == 3 || n == 5 || n == 7;
    }
    for(int i=0; i<4; ++i){
        if(n % primes[i] == 0){
            return false;
        }
    }
    return true;
}

int count_prime(int n){
    if(n == 1){
        return 0;
    }
    int ans = 0;
    for(int i=2; i<=n; ++i){
        if(is_prime(i)){
            ++ ans;
        }
    }
    return ans;
}
// === 0ms && 6.8MB === //
int numPrimeArrangements(int n){
    long ans = 1;
    int m = count_prime(n);
    int size = m > n-m ? m : n-m;
    long f[size+1];
    f[0] = 1;
    for(int i=1; i<=size; ++i){
        f[i] = (i * f[i-1]) % 1000000007;
    }
    ans = (f[m] * f[n-m]) % 1000000007;
    return ans;
}

