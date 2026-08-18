/*
=== 917. reverse-only-letters ===

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 
Note:
1. S.length <= 100
2. 33 <= S[i].ASCIIcode <= 122 
3. S doesn't contain \ or "
*/
bool isLetter(char c){
    if((c >= 65 && c <= 90) || (c >= 97 && c <= 122)){
        return true;
    }
    else{
        return false;
    }
}
char* reverseOnlyLetters(char* S) {
    int len = strlen(S);
    char* ans = (char*)malloc((len+1)*sizeof(char));
    ans[len] = '\0';
    int i = 0;
    int j = len - 1;
    while(i <= j){
        if(isLetter(S[i]) && isLetter(S[j])){
            ans[i] = S[j];
            ans[j] = S[i];
            ++i;
            --j;
        }
        else if(isLetter(S[i])){
            ans[j] = S[j];
            --j;
        }
        else if(isLetter(S[j])){
            ans[i] = S[i];
            ++i;
        }
        else{
            ans[i] = S[i];
            ans[j] = S[j];
            ++i;
            --j;
        }
    }
    return ans;
}