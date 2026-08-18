/*
=== 1190. Reverse Substrings Between Each Pair of Parentheses ===

Given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any bracket.

Example 1:
    Input: s = "(abcd)"
    Output: "dcba"
Example 2:
    Input: s = "(u(love)i)"
    Output: "iloveu"
Example 3:
    Input: s = "(ed(et(oc))el)"
    Output: "leetcode"
Example 4:
    Input: s = "a(bcdefghijkl(mno)p)q"
    Output: "apmnolkjihgfedcbq"

Constraints:
    1. 0 <= s.length <= 2000
    2. s only contains lower case English characters and parentheses.
    3. It's guaranteed that all parentheses are balanced.
*/
// === 0ms && 9.9MB === //
void fill(char* s, char* ans, int* flag_in, int* flag_out){
    char* tmp = (char *)malloc(2001 * sizeof(char));
    // char* tmp[2001]; 如果采用这种定义则会出错。
    int flag_tmp = 0;
    while(s[*flag_in] != ')' && s[*flag_out] != '\0'){
        if(s[*flag_in] == '('){
            ++ *flag_in;
            fill(s, tmp, flag_in, &flag_tmp);
        }
        else{
            tmp[flag_tmp] = s[*flag_in];
            ++ flag_tmp;
            ++ *flag_in;
        }
    }
    ++ *flag_in;
    for(int i=0; i<flag_tmp; ++i){
        ans[*flag_out] = tmp[flag_tmp-i-1];
        ++ *flag_out;
        // printf("%c", tmp[i]);
    }
    // printf("\n");
    free(tmp);
    return;
}
char * reverseParentheses(char * s){
    char* ans = (char *)malloc(2001 * sizeof(char));
    int flag_in = 0, flag_out = 0;
    int len = strlen(s);
    while(flag_in < len){
        if(s[flag_in] == ')'){
            ++ flag_in;
        }
        else if(s[flag_in] == '('){
            ++ flag_in;
            fill(s, ans, &flag_in, &flag_out);
        }
        else{
            ans[flag_out] = s[flag_in];
            ++ flag_out;
            ++ flag_in;
        }
    }
    ans[flag_out] = '\0';
    return ans;
}

