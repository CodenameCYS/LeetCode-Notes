/*
=== 645. Set Mismatch ===
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
*/
# include <stdio.h>
# include <stdlib.h>
# include <time.h>

int* findErrorNums(int* nums, int numsSize, int* returnSize);

int main(){
    srand((unsigned int)time(NULL));

    int len = 15;
    int a[len];
    for(int i=0; i<len; ++i){
        a[i] = i+1;
    }
    int loc = rand()/32767.0 * (len-1);
    int rep = rand()/32767.0 * (len-1) + 1;
    a[loc] = rep;
    for(int i=0; i<len; ++i){
        printf("%d\t", a[i]);
    }
    printf("\n");

    int returnSize;
    int *ans = findErrorNums(a, len, &returnSize);
    for(int i=0; i<returnSize; ++i){
        printf("%d\t", ans[i]);
    }
    printf("\n");

    system("pause");
    return 1;
}

int* findErrorNums(int* nums, int numsSize, int* returnSize) {

}