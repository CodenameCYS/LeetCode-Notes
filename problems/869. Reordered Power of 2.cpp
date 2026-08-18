/*
=== 869. Reordered Power of 2 ===

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.
Return true if and only if we can do this in a way such that the resulting number is a power of 2.


Example 1:
Input: 1
Output: true

Example 2:
Input: 10
Output: false

Example 3:
Input: 16
Output: true

Example 4:
Input: 24
Output: false

Example 5:
Input: 46
Output: true
 

Note:
1 <= N <= 10^9
*/

# include <stdio.h>
# include <stdlib.h>

bool reorderedPowerOf2(int N);
bool isPowerOf2(int n);
bool CheckEachNum(int* digits, bool* tag, int len, int currentnum, int left);

int main(){
    //printf("%d\n",10*9*8*7*6*5*4*3*2);

    int n = 124;
    if(reorderedPowerOf2(n)){
        printf("true!\n");
    }
    else{
        printf("false!\n");
    }

    system("pause");
}

bool isPowerOf2(int n){
    while(n % 2 == 0){
        n = n / 2;
    }

    if(n == 1){
        return true;
    }
    else{
        return false;
    }
}

bool CheckEachNum(int* digits, bool* tag, int len, int currentnum, int left){
    if(left == 0){
        /*
        printf("%d\t", currentnum);
        if(isPowerOf2(currentnum)){
            printf("true\n");
        }
        else{
            printf("false\n");
        }
        */
        return isPowerOf2(currentnum);
    }
    else if(left == len){
        bool ans = false;
        for(int i=0; i<len; ++i){
            if(digits[i] == 0){
                continue;
            }
            else{
                tag[i] = true;
                ans = CheckEachNum(digits, tag, len, 10 * currentnum + digits[i], left - 1);
                tag[i] = false;

                if(ans){
                    //printf("final true\n");
                    return true;
                }
            }
        }
        //printf("final false\n");
        return false;
    }
    else{
        bool ans = false;
        for(int i=0; i<len; ++i){
            if(!tag[i]){
                tag[i] = true;
                ans = CheckEachNum(digits, tag, len, 10 * currentnum + digits[i], left-1);
                tag[i] = false;

                if(ans){
                    return true;
                }
            }
        }
        return false;
    }
}

bool reorderedPowerOf2(int N) {

    int len = 0;
    int digits[10];
    while(N != 0){
        digits[len] = N % 10;
        N = N / 10;
        ++ len;
    }

    bool tag[len];
    for(int i=0; i<len; ++i){
        tag[i] = false;
    }

    return CheckEachNum(digits, tag, len, 0, len);
}