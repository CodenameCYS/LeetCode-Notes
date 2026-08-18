/*
=== 935. Knight Dialer ===

A chess knight can move as indicated in the chess diagram below:

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.
Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.
How many distinct numbers can you dial in this manner?
Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:
Input: 1
Output: 10

Example 2:
Input: 2
Output: 20

Example 3:
Input: 3
Output: 46

Note:
1. 1 <= N <= 5000
*/
void update(long* s){
    long ss[10];
    ss[0] = (s[4]+s[6])%1000000007;
    ss[1] = (s[6]+s[8])%1000000007;
    ss[2] = (s[7]+s[9])%1000000007;
    ss[3] = (s[4]+s[8])%1000000007;
    ss[4] = (s[3]+s[9]+s[0])%1000000007;
    ss[5] = 0;
    ss[6] = (s[1]+s[7]+s[0])%1000000007;
    ss[7] = (s[2]+s[6])%1000000007;
    ss[8] = (s[1]+s[3])%1000000007;
    ss[9] = (s[2]+s[4])%1000000007;
    for(int i=0; i<10; ++i){
        s[i] = ss[i];
    }
}
int knightDialer(int N) {
    long s[10];
    for(int i=0; i<10; ++i){
        s[i] = 1;
    }
    for(int i=0; i<N-1; ++i){
        update(s);
    }
    long ans = 0;
    for(int i=0; i<10; ++i){
        ans += s[i];
    }
    ans = ans % 1000000007;
    return (int)ans;
}