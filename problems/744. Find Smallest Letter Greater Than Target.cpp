/*
=== 744. Find Smallest Letter Greater Than Target ===

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
    Input:
    letters = ["c", "f", "j"]
    target = "a"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "c"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "d"
    Output: "f"

    Input:
    letters = ["c", "f", "j"]
    target = "g"
    Output: "j"

    Input:
    letters = ["c", "f", "j"]
    target = "j"
    Output: "c"

    Input:
    letters = ["c", "f", "j"]
    target = "k"
    Output: "c"

Note:
    1. letters has a length in range [2, 10000].
    2. letters consists of lowercase letters, and contains at least 2 unique letters.
    3. target is a lowercase letter.
*/
// === 8ms(94.12%) && 5.9MB(100%) === //
char nextGreatestLetter(char* letters, int lettersSize, char target){
    char min='z', ans='z' + 1;
    for(int i=0; i<lettersSize; ++i){
        if(letters[i] > target){
            ans = ans < letters[i] ? ans : letters[i];
        }
        min = min < letters[i] ? min : letters[i];
    }
    return ans == 'z' + 1 ? min : ans;
}