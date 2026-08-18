/*
=== 868. Binary Gap ===

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
If there aren't two consecutive 1's, return 0.


Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

Note:
1 <= N <= 10^9

*/

# include <stdio.h>
# include <stdlib.h>

bool dec2bin(int n, int bin[], int &len);
int binaryGap(int N);

int main(){
    int N = 25;
    int gap = binaryGap(N);
    
    int bin[30];
    int len = 0;
    dec2bin(N, bin, len);

    printf("The distance is %d!\n",gap);

    system("pause");
}

bool dec2bin(int n, int bin[], int &len){
    
    printf("%d's binary representation is: 0b" , n);

    int temp[30];

    len = 0;
    while(n != 0){
        temp[len] = n % 2;
        n = n / 2;
        ++ len;
    }

    for(int i=0; i<len; ++i){
        bin[i] = temp[len-1-i];
        printf("%d" , bin[i]);
    }
    printf("\n");

    return true;
}

int binaryGap(int N) {

    int max = 0;
    int distance = 0;
    int count = 0;
    while(N != 0){
        ++ distance;
        if(N % 2 == 1){
            ++ count;

            if(count != 1){
                max = max > distance?max:distance;
            }

            distance = 0;
        }
        N = N / 2;
    }

    return count == 1? 0 : max;
}