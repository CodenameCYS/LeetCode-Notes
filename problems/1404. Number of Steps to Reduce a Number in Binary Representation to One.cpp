/*
=== 1404. Number of Steps to Reduce a Number in Binary Representation to One ===

Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:
    - If the current number is even, you have to divide it by 2.
    - If the current number is odd, you have to add 1 to it.
It's guaranteed that you can always reach to one for all testcases.

Example 1:
    Input: s = "1101"
    Output: 6
    Explanation: "1101" corressponds to number 13 in their decimal representation.
    Step 1) 13 is odd, add 1 and obtain 14. 
    Step 2) 14 is even, divide by 2 and obtain 7.
    Step 3) 7 is odd, add 1 and obtain 8.
    Step 4) 8 is even, divide by 2 and obtain 4.  
    Step 5) 4 is even, divide by 2 and obtain 2. 
    Step 6) 2 is even, divide by 2 and obtain 1.  
Example 2:
    Input: s = "10"
    Output: 1
    Explanation: "10" corressponds to number 2 in their decimal representation.
    Step 1) 2 is even, divide by 2 and obtain 1.  
Example 3:
    Input: s = "1"
    Output: 0
 
Constraints:
    1. 1 <= s.length <= 500
    2. s consists of characters '0' or '1'
    3. s[0] == '1'
*/
void show(int* digits, int size){
    for(int i=0; i<size; ++i){
        printf("%d", digits[i]);
    }
    printf("\n");
}
// === 4ms(63.64%) && 5.4MB === //
int numSteps(char * s){
    int digits[501]={0}, size = 0, l=strlen(s);
    for(int i=l-1; i>=0; --i){
        digits[size] = s[i] - '0';
        ++ size;
    }
    
    // show(digits, size);
    
    int ans = 0;
    for(int i=0; i<size-1; ++i){
        if(digits[i] == 1){
            int j=i+1;
            while(j<size && digits[j]==1){
                digits[j] = 0;
                ++ j;
            }
            digits[j] = 1;
            if(j == size){
                ++ size;
            }
            ans += 2;
        }
        else{
            ++ ans;
        }
        // show(digits, size);
    }
    return ans;
}