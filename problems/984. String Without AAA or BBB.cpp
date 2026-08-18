/*
=== 984. String Without AAA or BBB ===

Given two integers A and B, return any string S such that:
    - S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
    - The substring 'aaa' does not occur in S;
    - The substring 'bbb' does not occur in S.

Example 1:
    Input: A = 1, B = 2
    Output: "abb"
    Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:
    Input: A = 4, B = 1
    Output: "aabaa"
 
Note:
    1. 0 <= A <= 100
    2. 0 <= B <= 100
    3. It is guaranteed such an S exists for the given A and B.
*/
// 0 ms //
char* strWithout3a3b(int A, int B) {
    char* ans = (char*) malloc((A+B+1)*sizeof(char));
    ans[A+B] = '\0';
    
    int tokens, subtokens;
    int anum, bnum;
    char a, b;
    if(A >= B){
        tokens = (A+1)/2;
        subtokens = B-tokens;
        a = 'a', b = 'b';
        anum = A, bnum = B;
    }
    else{
        tokens = (B+1)/2;
        subtokens = A-tokens;
        a = 'b', b = 'a';
        anum = B, bnum = A;
    }
    
    int i=0;
    while(anum>0){
        ans[i] = a;
        --anum;
        ++i;
        if(anum>0){
            ans[i] = a;
            ++i;
            --anum;
        }
        if(bnum > 0){
            ans[i] = b;
            ++i;
            --bnum;
        }
        if(subtokens > 0){
            ans[i] = b;
            ++i;
            --bnum;
            --subtokens;
        }
        //printf("%d\n",i);
    }
    while(i<A+B){
        ans[i] = b;
        ++i;
    }
    return ans;
}