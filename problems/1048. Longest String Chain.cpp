/*
=== 1048. Longest String Chain ===

Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:
    Input: ["a","b","ba","bca","bda","bdca"]
    Output: 4
    - Explanation: one of the longest word chain is "a","ba","bda","bdca".
 
Note:
    1. 1 <= words.length <= 1000
    2. 1 <= words[i].length <= 16
    3. words[i] only consists of English lowercase letters.
*/
void QuickSort(char** words, int* nums, int st, int ed){
    if(st >= ed){
        return;
    }
    int i = st, j = ed;
    int temp = nums[st];
    char* tempw = words[st];
    while(i<j){
        while(i<j && nums[j] >= temp){
            --j;
        }
        if(i<j){
            nums[i] = nums[j];
            words[i] = words[j];
            ++i;
        }
        while(i<j && nums[i] <= temp){
            ++i;
        }
        if(i<j){
            nums[j] = nums[i];
            words[j] = words[i];
            --j;
        }
    }
    nums[i] = temp;
    words[i] = tempw;
    QuickSort(words, nums, st, i-1);
    QuickSort(words, nums, i+1, ed);
}
bool isPredecessor(char* str1, char* str2){
    int len = strlen(str1);
    int delta = 0;
    for(int i=0; i<len; ++i){
        if(str1[i] == str2[i+delta]){
            continue;
        }
        else{
            ++ delta;
            if(delta > 1 || str2[i+delta] != str1[i]){
                return false;
            }
        }
    }
    return true;
}
// === 40ms & 8.7MB === //
int longestStrChain(char ** words, int wordsSize){
    int len[wordsSize];
    int dp[wordsSize];
    for(int i=0; i<wordsSize; ++i){
        len[i] = strlen(words[i]);
        dp[i] = 1;
    }
    QuickSort(words, len, 0, wordsSize-1);
    
    int ans = 1;
    for(int i=wordsSize-2; i>=0; --i){
        for(int j=i+1; j<wordsSize; ++j){
            if(len[j] == len[i]){
                continue;
            }
            else if(len[j] == len[i] + 1){
                if(isPredecessor(words[i], words[j])){
                    dp[i] = dp[i] > 1+dp[j] ? dp[i] : 1+dp[j];
                }
            }
            else{
                break;
            }
        }
        ans = ans > dp[i] ? ans : dp[i];
    }
    return ans;
}