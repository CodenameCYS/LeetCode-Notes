/*
=== 204. Count Primes ===

Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
*/
bool isprime(int n, int* primes, int pnum){
    for(int i=1; i<pnum; ++i){
        if(primes[i] > sqrt(n)){
            break;
        }
        if(n % primes[i] == 0){
            return false;
        }
    }
    return true;
}
int countPrimes(int n) {
    int psize = n/6 >= 15 ? n/6 : 15;
    int* primes = (int*)malloc(psize * sizeof(int));
    int len=2;
    primes[0]=2, primes[1]=3;
    if(n<=2){
        return 0;
    }
    else if(n==3){
        return 1;
    }
    int i = 5;
    while(i < n){
        if(isprime(i, primes, len)){
            primes[len] = i;
            ++ len;
        }
        i += 2;
    }
    return len;
}

/* ==================================================================================================== */
int countPrimes(int n) {
    if(n <= 2){
        return 0;
    }
    bool* state = (bool*)malloc(n*sizeof(bool));
    for(int i=2; i<n; ++i){
        state[i] = false;
    }
    
    int ans = n-2;
    for(int i=2; i<n; ++i){
        if(state[i]){
            -- ans;
            continue;
        }
        for(int j=i; j<n; j+=i){
            state[j] = true;
        }
    }
    return ans;
}