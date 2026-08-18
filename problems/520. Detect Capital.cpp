/*
=== 520. Detect Capital ===

Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
    1. All letters in this word are capitals, like "USA".
    2. All letters in this word are not capitals, like "leetcode".
    3. Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 
Example 1:
    Input: "USA"
    Output: True
Example 2:
    Input: "FlaG"
    Output: False
 
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
*/
// === 0ms(100%) && 5MB(100%) === //
bool is_all_lower(char* word){
    for(int i=0; word[i]; ++i){
        if(word[i] < 'a' || word[i] > 'z'){
            return false;
        }
    }
    return true;
}
bool is_all_upper(char* word){
    for(int i=0; word[i]; ++i){
        if(word[i] < 'A' || word[i] > 'Z'){
            return false;
        }
    }
    return true;
}
bool detectCapitalUse(char * word){
    if(word[0] >= 'a' && word[0] <= 'z'){
        return is_all_lower(&word[1]);
    }
    else if(word[0] >= 'A' && word[0] <= 'Z'){
        return is_all_lower(&word[1]) || is_all_upper(&word[1]);
    }
    return false;
}

