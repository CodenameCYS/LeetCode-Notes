/*
=== 809. Expressive Words ===

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.
For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
Given a list of query words, return the number of words that are stretchy. 

Example:
    Input: 
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    Output: 1
    Explanation: 
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 
Notes:
    1. 0 <= len(S) <= 100.
    2. 0 <= len(words) <= 100.
    3. 0 <= len(words[i]) <= 100.
    4. S and all words in words consist only of lowercase letters
*/
// === 4ms(63.33%) && 5.6MB(100%) === //
int expressiveWords(char * S, char ** words, int wordsSize){
    if(strlen(S) == 0){
        return 0;
    }
    char charlist[101];
    int charnum[101], size = 0;
    charlist[0] = S[0];
    size = 1;
    charnum[0] = 1;
    for(int i=1; S[i]; ++i){
        if(S[i] == charlist[size-1]){
            ++ charnum[size-1];
        }
        else{
            charlist[size] = S[i];
            charnum[size] = 1;
            ++ size;
        }
    }
    int ans = 0;
    for(int i=0; i<wordsSize; ++i){
        if(strlen(words[i]) == 0){
            continue;
        }
        char charlist2[101];
        int charnum2[101], wsize = 0;
        charlist2[0] = words[i][0];
        wsize = 1;
        charnum2[0] = 1;
        for(int j=1; words[i][j]; ++j){
            if(words[i][j] == charlist2[wsize-1]){
                ++ charnum2[wsize-1];
            }
            else{
                charlist2[wsize] = words[i][j];
                charnum2[wsize] = 1;
                ++ wsize;
            }
        }
        if(size != wsize){
            continue;
        }
        bool can_extend = true;
        for(int i=0; i<size; ++i){
            if(charlist[i] != charlist2[i] || (charnum[i] < 3 && charnum[i] != charnum2[i]) || charnum[i] < charnum2[i]){
                can_extend = false;
                break;
            }
        }
        if(can_extend){
            ++ ans;
        }
    }
    return ans;
}

