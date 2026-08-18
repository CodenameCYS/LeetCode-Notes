/*
=== 672. Bulb Switcher II ===

There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.
Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:
    1. Flip all the lights.
    2. Flip lights with even numbers.
    3. Flip lights with odd numbers.
    4. Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
 
Example 1:
    Input: n = 1, m = 1.
    Output: 2
    Explanation: Status can be: [on], [off]
Example 2:
    Input: n = 2, m = 1.
    Output: 3
    Explanation: Status can be: [on, off], [off, on], [off, off]
Example 3:
    Input: n = 3, m = 1.
    Output: 4
    Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
 
- Note: n and m both fit in range [0, 1000].
*/
int analyse_mode(int m){
    if(m <= 4){
        return m;
    }
    else{
        return m % 2 == 0 ? 4 : 3;
    }
}
int analyse_status(int n, int mode){
    if(n == 0 || mode == 0){
        return 1;
    }
    else if(n == 1){
        return 2;
    }
    else if(n == 2){
        if(mode == 1){
            return 3;
        }
        else{
            return 4;
        }
    }
    else{
        if(mode == 1){
            return 4;
        }
        else if(mode == 2){
            return 7;
        }
        else{
            return 8;
        }
    }
}
// === 0ms(100%) && 5MB(100%) === //
int flipLights(int n, int m){
    int mode = analyse_mode(m);
    return analyse_status(n, mode);
}

