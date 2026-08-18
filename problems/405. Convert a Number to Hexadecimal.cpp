/*
=== 405. Convert a Number to Hexadecimal ===

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
    1. All letters in hexadecimal (a-f) must be in lowercase.
    2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
    3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
    4. You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:
    Input:
    26
    Output:
    "1a"
Example 2:
    Input:
    -1
    Output:
    "ffffffff"
*/
char num2hex(int num){
    if(num < 10){
        return num + '0';
    }
    else{
        return num - 10 + 'a';
    }
}
// === 4ms(42.86%) && 6.9MB(100%) === //
char * toHex(int num){
    char* ans = (char*)malloc(10*sizeof(char));
    if(num == 0){
        ans[0] = '0';
        ans[1] = '\0';
        return ans;
    }
    unsigned int n = num;
    int i=0;
    while(n != 0){
        ans[i] = num2hex(n % 16);
        ++ i;
        n /= 16;
    }
    ans[i] = '\0';
    for(int j=0; j<i/2; ++j){
        char tmp = ans[j];
        ans[j] = ans[i-1-j];
        ans[i-1-j] = tmp;
    }
    return ans;
}

