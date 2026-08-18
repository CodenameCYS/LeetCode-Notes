/*
=== 709. To Lower Case ===

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
    Input: "Hello"
    Output: "hello"
Example 2:
    Input: "here"
    Output: "here"
Example 3:
    Input: "LOVELY"
    Output: "lovely"
*/
// === 0ms(100%) && 5MB(100%) === //
char * toLowerCase(char * str){
    for(int i=0; str[i]; ++i){
        if(str[i] >= 'A' && str[i] <= 'Z'){
            str[i] += ('a'-'A');
        }
    }
    return str;
}

