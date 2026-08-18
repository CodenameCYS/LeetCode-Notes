/*
=== 948. Bag of Tokens ===

You have an initial power P, an initial score of 0 points, and a bag of tokens.
Each token can be used at most once, has a value token[i], and has potentially two ways to use it.
- If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
- If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
Return the largest number of points we can have after playing any number of tokens.

Example 1:
Input: tokens = [100], P = 50
Output: 0

Example 2:
Input: tokens = [100,200], P = 150
Output: 1

Example 3:
Input: tokens = [100,200,300,400], P = 200
Output: 2

Note:
1. tokens.length <= 1000
2. 0 <= tokens[i] < 10000
3. 0 <= P < 10000
*/
bool QuickSort(int* seq, int start, int end){
    if(end <= start){
        return true;
    }
    int i=start, j=end;
    int temp = seq[start];
    while(i < j){
        while(i<j && seq[j]>=temp){
            --j;
        }
        if(i<j){
            seq[i] = seq[j];
            ++i;
        }
        while(i<j && seq[i]<=temp){
            ++i;
        }
        if(i<j){
            seq[j] = seq[i];
            --j;
        }
    }
    seq[i] = temp;
    QuickSort(seq, start, i-1);
    QuickSort(seq, i+1, end);
    return true;
}

int bagOfTokensScore(int* tokens, int tokensSize, int P) {
    QuickSort(tokens, 0, tokensSize-1);

    int max_point = 0, point = 0;
    int first = 0, last = tokensSize - 1;
    while(first <= last && tokens[first] <= P){
        while(first <= last && P >= tokens[first]){
            P -= tokens[first];
            ++ first;
            ++ point;
            max_point = max_point >= point ? max_point : point;
        }
        if(first <= last && point > 0){
            P += tokens[last];
            -- last;
            -- point;
        }
    }
    return max_point;
}