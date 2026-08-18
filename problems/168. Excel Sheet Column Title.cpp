/*
=== 168. Excel Sheet Column Title ===

Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
*/
char* convertToTitle(int n) {
    char s[1000];
    int len = 0;
    while(n > 0){
        -- n;
        s[len] = n % 26 + 65;
        ++ len;
        n /= 26;
        if(n == 0){
            break;
        }
    }
    s[len] = '\0';
    ++ len;
    
    char* ans = (char*)malloc(len*sizeof(char));
    for(int i=0; i<len-1; ++i){
        ans[i] = s[len-2-i];
    }
    ans[len-1] = '\0';
    return ans;
}