/*
=== 1432. Max Difference You Can Get From Changing an Integer ===

You are given an integer num. You will apply the following steps exactly two times:
    - Pick a digit x (0 <= x <= 9).
    - Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
    - Replace all the occurrences of x in the decimal representation of num by y.
    - The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.
Return the max difference between a and b.

Example 1:
    Input: num = 555
    Output: 888
    Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
    The second time pick x = 5 and y = 1 and store the new integer in b.
    We have now a = 999 and b = 111 and max difference = 888
Example 2:
    Input: num = 9
    Output: 8
    Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
    The second time pick x = 9 and y = 1 and store the new integer in b.
    We have now a = 9 and b = 1 and max difference = 8
Example 3:
    Input: num = 123456
    Output: 820000
Example 4:
    Input: num = 10000
    Output: 80000
Example 5:
    Input: num = 9288
    Output: 8700
 
Constraints:
    1. 1 <= num <= 10^8
*/
int get_max(int num){
    int digits[9], size=0;
    num2digits(num, digits, &size);
    int src=digits[size-1], tgt=9;
    
    if(digits[size-1] == 9){
        src = 9;
        for(int i=size-1; i>=0; --i){
            if(digits[i] != 9){
                src = digits[i];
                break;
            }
        }
    }
    
    change_digit(digits, size, src, tgt);
    return digits2num(digits, size);
}
int get_min(int num){
    int digits[9], size=0;
    num2digits(num, digits, &size);
    int src=digits[size-1], tgt=1;
    
    if(digits[size-1] == 1){
        src = 1;
        for(int i=size-1; i>=0; --i){
            if(digits[i] > 1){
                src = digits[i];
                tgt = 0;
                break;
            }
        }
    }
    
    change_digit(digits, size, src, tgt);
    return digits2num(digits, size);
}
int change_digit(int* digits, int size, int src, int tgt){
    for(int i=0; i<size; ++i){
        if(digits[i] == src){
            digits[i] = tgt;
        }
    }
    return;
}
void num2digits(int num, int* digits, int* size){
    *size = 0;
    while(num != 0){
        digits[*size] = num % 10;
        num /= 10;
        ++ *size;
    }
    return;
}
int digits2num(int* digits, int size){
    int ans = 0;
    for(int i=size-1; i>=0; --i){
        ans = ans*10 + digits[i];
    }
    return ans;
}
// === 0ms && 5.2MB === //
int maxDiff(int num){
    int max = get_max(num);
    int min = get_min(num);
    return max-min;
}