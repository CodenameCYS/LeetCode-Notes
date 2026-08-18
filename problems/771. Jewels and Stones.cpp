/*
=== 771. Jewels and Stones ===

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: J = "aA", S = "aAAbbbb"
    Output: 3
Example 2:
    Input: J = "z", S = "ZZ"
    Output: 0

Note:
    1. S and J will consist of letters and have length at most 50.
    2. The characters in J are distinct.
*/
// === 0ms(100%) && 5.2MB(100%) === //
int numJewelsInStones(char * J, char * S){
    int alphabet[256] = {0};
    for(int i=0; J[i]; ++i){
        alphabet[J[i]] = 1;
    }
    int ans = 0;
    for(int i=0; S[i]; ++i){
        if(alphabet[S[i]] == 1){
            ++ ans;
        }
    }
    return ans;
}

