/*
=== 171. Excel Sheet Column Number ===

Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
*/
int titleToNumber(char* s) {
    int ans = 0;
    int i = 0;
    while(s[i] != '\0'){
        ans = 26*ans + s[i] - 64;
        ++ i;
    }
    return ans;
}