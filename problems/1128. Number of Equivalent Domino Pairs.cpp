/*
=== 5130. Number of Equivalent Domino Pairs ===

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
    Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1
 
Constraints:
    1. 1 <= dominoes.length <= 40000
    2. 1 <= dominoes[i][j] <= 9
*/
void QuickSort(int** dominoes, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed;
    int tmp[2] = {dominoes[st][0], dominoes[st][1]};
    while(i < j){
        while(i < j && dominoes[j][0] >= tmp[0]){
            --j;
        }
        if(i < j){
            dominoes[i][0] = dominoes[j][0];
            dominoes[i][1] = dominoes[j][1];
            ++i;
        }
        while(i < j && dominoes[i][0] <= tmp[0]){
            ++i;
        }
        if(i < j){
            dominoes[j][0] = dominoes[i][0];
            dominoes[j][1] = dominoes[i][1];
            --j;
        }
    }
    dominoes[i][0] = tmp[0];
    dominoes[i][1] = tmp[1];
    QuickSort(dominoes, st, i-1);
    QuickSort(dominoes, i+1, ed);
    return;
}
// === 1100ms && 13MB === //
int numEquivDominoPairs(int** dominoes, int dominoesSize, int* dominoesColSize){
    for(int i=0; i<dominoesSize; ++i){
        if(dominoes[i][0] > dominoes[i][1]){
            int tmp = dominoes[i][0];
            dominoes[i][0] = dominoes[i][1];
            dominoes[i][1] = tmp;
        }
    }
    QuickSort(dominoes, 0, dominoesSize-1);
    int ans = 0;
    for(int i=0; i<dominoesSize-1; ++i){
        for(int j=i+1; j<dominoesSize; ++j){
            if(dominoes[j][0] != dominoes[i][0]){
                break;
            }
            if(dominoes[j][1] == dominoes[i][1]){
                ++ans;
            }
        }
    }
    return ans;
}

