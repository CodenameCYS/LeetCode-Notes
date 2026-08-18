/*
=== 1052. Grumpy Bookstore Owner ===

Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
    Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
    Output: 16
    - Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
    The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 
Note:
    1. 1 <= X <= customers.length == grumpy.length <= 20000
    2. 0 <= customers[i] <= 1000
    3. 0 <= grumpy[i] <= 1
*/
// === 36ms(50%) && 8.9MB === //
int maxSatisfied(int* customers, int customersSize, int* grumpy, int grumpySize, int X){
    int csum[customersSize], gsum[customersSize];
    csum[0] = customers[0];
    gsum[0] = (1-grumpy[0])*customers[0];
    for(int i=1; i<customersSize; ++i){
        csum[i] = csum[i-1] + customers[i];
        gsum[i] = gsum[i-1] + (1-grumpy[i])*customers[i];
    }
    
    int ans = csum[X-1] + gsum[grumpySize-1] - gsum[X-1];
    for(int i=1; i<customersSize; ++i){
        int temp;
        if(X-1+i < grumpySize){
            temp = gsum[i-1] + csum[i+X-1] - csum[i-1] + gsum[grumpySize-1] - gsum[X-1+i];
        }
        else{
            temp = gsum[i-1] + csum[customersSize-1] - csum[i-1];
        }
        ans = ans > temp ? ans : temp;
    }
    return ans;
}

