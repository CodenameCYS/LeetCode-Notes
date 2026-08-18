/*
=== 957. Prison Cells After N Days ===

There are 8 prison cells in a row, and each cell is either occupied or vacant.
Each day, whether the cell is occupied or vacant changes according to the following rules:
    - If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    - Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:
    Input: cells = [0,1,0,1,1,0,0,1], N = 7
    Output: [0,0,1,1,0,0,0,0]
Explanation: 
    The following table summarizes the state of the prison on each day:
    Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
    Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
    Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
    Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
    Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
    Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
    Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
    Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 
Note:
    1. cells.length == 8
    2. cells[i] is in {0, 1}
    3. 1 <= N <= 10^9
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int update(int* src, int* tgt, int cellsSize){
    int id=0;
    for(int i=1; i<cellsSize-1; ++i){
        tgt[i] = (src[i-1] + src[i+1] + 1) % 2;
        id = 2*id + tgt[i];
    }
    tgt[0] = 0;
    tgt[cellsSize-1] = 0;
    return id;
}
int findAns(int* history, int len, int N){
    int st = -1;
    for(int i=0; i<len-1; ++i){
        if(history[i] == history[len-1]){
            st = i;
            break;
        }
    }
    if(st == -1){
        return st;
    }
    else{
        int looplen = len-1 - st;
        len = st + (N - len) % looplen;
        return len;
    }
}
    
int* prisonAfterNDays(int* cells, int cellsSize, int N, int* returnSize) {
    *returnSize = cellsSize;
    
    int cellgroup[64][cellsSize];
    int history[64];
    int ed = 0;
    
    history[ed] = update(cells, cellgroup[0], cellsSize);
    ++ ed;
    for(int i=1; i<N; ++i){
        history[ed] = update(cellgroup[i-1], cellgroup[i], cellsSize);
        ++ ed;
        
        int tgt = findAns(history, ed, N);
        if(tgt != -1){
            ed = tgt + 1;
            break;
        }
    }
    
    int* ans = (int*)malloc(cellsSize*sizeof(int));
    for(int i=0; i<cellsSize; ++i){
        ans[i] = cellgroup[ed-1][i];
    }
    return ans;
}