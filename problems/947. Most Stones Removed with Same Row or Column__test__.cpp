/*
=== 947. Most Stones Removed with Same Row or Column === // this version exceed time limit

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
What is the largest possible number of moves we can make?

Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:
Input: stones = [[0,0]]
Output: 0

Note:
1. 1 <= stones.length <= 1000
2. 0 <= stones[i][j] < 10000
*/
int* createStateInfo(int stonesRowSize){
    int* state = (int*)malloc(stonesRowSize * sizeof(int));
    for(int i=0; i<stonesRowSize; ++i){
        state[i] = 0;
    }
    return state;
}
int cleanStones(int** stones, int stonesRowSize, int *stonesColSizes, int* state){
    int effetive_stone_num = 0;
    for(int i=0; i<stonesRowSize; ++i){
        bool is_isolated = true;
        for(int j=0; j<stonesRowSize; ++j){
            if(i == j){
                continue;
            }
            if(stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]){
                is_isolated = false;
                break;
            }
        }
        if(is_isolated){
            state[i] = -1;
        }
        else{
            ++ effetive_stone_num;
        }
    }
    return effetive_stone_num;
}
void removeOneMoreStone(int** stones, int stonesRowSize, int *stonesColSizes, int* state, int* stone_num, int effetive_stone_num){
    if(*stone_num == effetive_stone_num-1){
        return;
    }
    int loc = 0;
    bool finished = true;
    for(; loc<stonesRowSize; ++loc){
        if(state[loc] == 1 || state[loc] == -1){
            continue;
        }
        for(int i=0; i<stonesRowSize; ++i){
            if(state[i] == 1 || state[i] == -1 || loc == i){
                continue;
            }
            if(stones[loc][0] == stones[i][0] || stones[loc][1] == stones[i][1]){
                state[loc] = 1;
                finished = false;
                removeOneMoreStone(stones, stonesRowSize, stonesColSizes, state, stone_num, effetive_stone_num);
                state[loc] = 0;
            }
        }
    }
    if(finished){
        int points = 0;
        for(int i=0; i<stonesRowSize; ++i){
            if(state[i] == 1){
                ++ points;
            }
        }
        *stone_num = *stone_num >= points? *stone_num : points;
    }
}
int removeStones(int** stones, int stonesRowSize, int *stonesColSizes) {
    int* state = createStateInfo(stonesRowSize);
    int effetive_stone_num = cleanStones(stones, stonesRowSize, stonesColSizes, state);
    
    int ans = 0;
    removeOneMoreStone(stones, stonesRowSize, stonesColSizes, state, &ans, effetive_stone_num);
    free(state);
    return ans;
}