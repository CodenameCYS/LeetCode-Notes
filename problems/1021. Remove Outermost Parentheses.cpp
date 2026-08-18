/*
=== 1021. Remove Outermost Parentheses ===

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:
    Input: "(()())(())"
    Output: "()()()"
    - Explanation: 
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:
    Input: "(()())(())(()(()))"
    Output: "()()()()(())"
    - Explanation: 
    The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:
    Input: "()()"
    Output: ""
    - Explanation: 
    The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".
 
Note:
    1. S.length <= 10000
    2. S[i] is "(" or ")"
    3. S is a valid parentheses string
*/
// === 4ms & 7.1MB === //
char* removeOuterParentheses(char* S) {
    int len = strlen(S);
    char* ans = (char*)malloc((len+1)*sizeof(char));
    char temp[len], mystack[len];
    int loc = 0;
    int slen = 0, tlen = 0;
    for(int i=0; S[i]!='\0'; ++i){
        if(S[i] == '('){
            mystack[slen] = S[i];
            ++slen;
        }
        else{
            --slen;
        }
        temp[tlen] = S[i];
        ++tlen;
        if(slen == 0){
            for(int j=1; j<tlen-1; ++j){
                ans[loc] = temp[j];
                ++loc;
            }
            tlen = 0;
        }
    }
    ans[loc] = '\0';
    return ans;
}