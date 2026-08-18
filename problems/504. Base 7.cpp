/*
=== 504. Base 7 ===

Given an integer, return its base 7 string representation.

Example 1:
    Input: 100
    Output: "202"
Example 2:
    Input: -7
    Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
*/
void to_base7(int num, char* ans){
    if(num == 0){
        ans[0] = '0', ans[1] = '\0';
        return ans;
    }
    int stack[10];
    int flag = 0;
    while(num != 0){
        stack[flag] = num % 7;
        num /= 7;
        ++ flag;
    }
    int loc = 0;
    for(int i=flag-1; i>=0; --i){
        ans[loc] = stack[i] + '0';
        ++ loc;
    }
    ans[flag] = '\0';
}
// === 4ms(66.67%) && 6.8MB(100%) === //
char * convertToBase7(int num){
    char* ans = (char*)malloc(11*sizeof(char));
    if(num < 0){
        ans[0] = '-';
        to_base7(-num, &ans[1]);
    }
    else{
        to_base7(num, ans);
    }
    return ans;
}

