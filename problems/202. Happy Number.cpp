/*
=== 202. Happy Number ===

Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
*/
bool myisHappy(int n, int* history, int hlen){
    if(n == 1){
        return true;
    }
    int ans = 0;
    while(n > 0){
        int lastbit = n%10;
        ans += lastbit*lastbit;
        n = n/10;
    }
    if(ans == 1){
        return true;
    }
    for(int i=0; i<hlen; ++i){
        if(history[i] == ans){
            return false;
        }
    }
    history[hlen] = ans;
    ++hlen;
    return myisHappy(ans, history, hlen);
}
bool isHappy(int n) {
    int history[10000];
    int hlen = 0;
    return myisHappy(n, history, hlen);
}