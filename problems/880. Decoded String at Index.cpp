/*
=== 884. Decoded String at Index ===

An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:
If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 
Example 1:
Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:
Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:
Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
 

Note:
1. 2 <= S.length <= 100
2. S will only contain lowercase letters and digits 2 through 9.
3. S starts with a letter.
4. 1 <= K <= 10^9
5. The decoded string is guaranteed to have less than 2^63 letters.
*/
# include <stdlib.h>

char* decodeAtIndex(char* S, int K) {
    // printf("begin");
    char* ans = (char*)malloc(2 * sizeof(char));
    ans[1] = '\0';
    char s_eff[100];
    long s_len[100];
    s_eff[0] = S[0],    s_len[0] = 1;
    
    // printf("begin preprocess!\n");
    int len = 1;
    while(S[len] != '\0'){
        if(S[len] >= '2' && S[len] <= '9'){
            s_eff[len] = s_eff[len-1];
            s_len[len] = s_len[len-1] * (S[len] - '0');
        }
        else{
            s_eff[len] = S[len];
            s_len[len] = s_len[len-1] + 1;
        }
        // printf("%d:\t%c->%d\n", len, s_eff[len], s_len[len]);
        if(s_len[len] >= K){
            break;
        }
        ++ len;
    }
    // printf("len = %d\n", len);
    // printf("preprocess finished!\n");
    while(s_len[len] >= K){
        // printf("K=%d:\tlen=%d\t->\tslen=%d\n",K,len,s_len[len]);
        if(s_len[len] == K){
            *ans = s_eff[len];
            break;
        }
        else{
            if(len == 0){
                *ans = s_eff[len];
                break;
            }
            else if(s_len[len-1] == s_len[len] -1){
                -- len;
            }
            else{
                K = K % s_len[len-1];
                if(K == 0){
                    *ans = s_eff[len];
                    break;
                }
                -- len;
            }
        }
    }
    // printf('finished!\n');
    return ans;
}