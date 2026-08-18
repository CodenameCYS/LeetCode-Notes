/*
=== 1333. Filter Restaurants by Vegan-Friendly, Price and Distance ===

Given the array restaurants where  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.
The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition, you have the filters maxPrice and maxDistance which are the maximum value for price and distance of restaurants you should consider respectively.
Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.

Example 1:
    Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
    Output: [3,1,5] 
    - Explanation: 
    The restaurants are:
    Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
    Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
    Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
    Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
    Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
    After filter restaurants with veganFriendly = 1, maxPrice = 50 and maxDistance = 10 we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from highest to lowest). 
Example 2:
    Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
    Output: [4,3,2,1,5]
    - Explanation: The restaurants are the same as in example 1, but in this case the filter veganFriendly = 0, therefore all restaurants are considered.
Example 3:
    Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
    Output: [4,5]
 
Constraints:
    1. 1 <= restaurants.length <= 10^4
    2. restaurants[i].length == 5
    3. 1 <= idi, ratingi, pricei, distancei <= 10^5
    4. 1 <= maxPrice, maxDistance <= 10^5
    5. veganFriendlyi and veganFriendly are 0 or 1.
    6. All idi are distinct.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool is_larger(int* a, int* b){
    if(a[1] < b[1]){
        return false;
    }
    else if(a[1] == b[1]){
        return a[0] > b[0];
    }
    else{
        return true;
    }
}

void quick_sort(int** restaurants, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed;
    int* tmp = restaurants[st];
    while(i<j){
        while(i<j && is_larger(tmp, restaurants[j])){
            -- j;
        }
        if(i<j){
            restaurants[i] = restaurants[j];
            ++ i;
        }
        while(i<j && is_larger(restaurants[i] , tmp)){
            ++ i;
        }
        if(i<j){
            restaurants[j] = restaurants[i];
            -- j;
        }
    }
    restaurants[i] = tmp;
    quick_sort(restaurants, st, i-1);
    quick_sort(restaurants, i+1, ed);
}

void show(int** restaurants, int restaurantsSize){
    for(int i=0; i<restaurantsSize; ++i){
        printf("(%d, %d, %d, %d, %d)\t", restaurants[i][0], restaurants[i][1], restaurants[i][2], restaurants[i][3], restaurants[i][4]);
    }
    printf("\n");
}
// === 112ms && 12.8MB === //
int* filterRestaurants(int** restaurants, int restaurantsSize, int* restaurantsColSize, int veganFriendly, int maxPrice, int maxDistance, int* returnSize){
    quick_sort(restaurants, 0, restaurantsSize-1);
    //show(restaurants, restaurantsSize);
    
    int* ans = (int*)malloc(restaurantsSize*sizeof(int));
    *returnSize = 0;
    for(int i=0; i<restaurantsSize; ++i){
        if((veganFriendly == 0 ? true : restaurants[i][2] == veganFriendly) && restaurants[i][3] <= maxPrice && restaurants[i][4] <= maxDistance){
            ans[*returnSize] = restaurants[i][0];
            ++ *returnSize;
        }
    }
    return ans;
}