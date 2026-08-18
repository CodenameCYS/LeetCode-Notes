/*
=== 451. Sort Characters By Frequency ===

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
    Input:
    "tree"
    Output:
    "eert"
    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:
    Input:
    "cccaaa"
    Output:
    "cccaaa"
    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:
    Input:
    "Aabb"
    Output:
    "bbAa"
    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.
*/
void quick_sort(int* nums, int* index, int st, int ed){
    if(st >= ed){
        return;
    }
    int i=st, j=ed, tmp1=nums[st], tmp2=index[st];
    while(i<j){
        while(i < j && nums[j] <= tmp1){
            -- j;
        }
        if(i < j){
            nums[i] = nums[j];
            index[i] = index[j];
            ++ i;
        }
        while(i < j && nums[i] >= tmp1){
            ++ i;
        }
        if(i < j){
            nums[j] = nums[i];
            index[j] = index[i];
            -- j;
        }
    }
    nums[i] = tmp1;
    index[i] = tmp2;
    quick_sort(nums, index, st, i-1);
    quick_sort(nums, index, i+1, ed);
}

void show(int* alphabet, int* index){
    for(int i=0; i<256; ++i){
        if(alphabet[i] != 0){
            printf("%c:%d  ", index[i], alphabet[i]);
        }
    }
    printf("\n");
}
// === 8ms(63.64%) && 7.8MB(100%) === //
char * frequencySort(char * s){
    int alphabet[256] = {0};
    int index[256];
    for(int i=0; i<256; ++i){
        index[i] = i;
    }
    int len = 0;
    for(; s[len]; ++len){
        ++ alphabet[s[len]];
    }
    // show(alphabet, index);
    quick_sort(alphabet, index, 0, 255);
    // show(alphabet, index);
    char* ans = (char*)malloc((len+1)*sizeof(char));
    int flag = 0;
    for(int i=0; i<256; ++i){
        for(int j=0; j<alphabet[i]; ++j){
            ans[flag] = index[i];
            ++ flag;
        }
    }
    ans[flag] = '\0';
    return ans;
}

