/*
=== 875. Koko Eating Bananas ===

Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.
Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
Return the minimum integer K such that she can eat all the bananas within H hours.

Example 1:
Input: piles = [3,6,7,11], H = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], H = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], H = 6
Output: 23

Note:
1. 1 <= piles.length <= 10^4
2. piles.length <= H <= 10^9
3. 1 <= piles[i] <= 10^9

*/
# include <stdio.h>
# include <stdlib.h>
# include <climits>

int minEatingSpeed(int* piles, int pilesSize, int H);
void QuickSort(int* nums, int start, int end);

int main(){

    system("pause");
    return 1;
}

void QuickSort(int *nums, int start, int end){
    if(start >= end){
        return;
    }

    int i = start, j = end;
    int temp = nums[i];
    while(i < j){
        while(i < j && nums[j] >= temp){
            --j;
        }
        if(i < j){
            nums[i] = nums[j];
            ++i;
        }
        while(i < j && nums[i] <= temp){
            ++i;
        }
        if(i < j){
            nums[j] = nums[i];
            --j;
        }
    }
    nums[i] = temp;
    QuickSort(nums, start, i-1);
    QuickSort(nums, i+1, end);

    return;
}

int minEatingSpeed(int* piles, int pilesSize, int H) {
    QuickSort(piles, 0, pilesSize-1);
    if(H == pilesSize){
        return piles[pilesSize-1];
    }
    int minspeed = (piles[pilesSize-1]-1)/(H-pilesSize+1) + 1;
    while(true){
        // printf("%d\t",minspeed);
        int time = 0;
        bool outrange = false;
        int gap = piles[pilesSize-1];
        for(int i=pilesSize-1; i>=0; --i){
            if(piles[i] <= minspeed){
                if(i+1 <= H - time){
                    time += i+1;
                }
                else{
                    outrange = true;
                }
                break;
            }
            else{
                int needtime = (piles[i]-1)/minspeed + 1;
                int speedgap = (piles[i]-1)/(needtime-1) + 1 - minspeed;
                gap = gap <= speedgap? gap : speedgap;
                if(needtime <= H - time){
                    time += needtime;
                }
                else{
                    outrange = true;
                }
            }
        }
        // printf("%d\n",time);
        if(time > H || outrange){
            minspeed += gap;
        }
        else{
            break;
        }
    }
    return minspeed;
}
