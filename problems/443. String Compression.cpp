/*
=== 443. String Compression ===

Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Follow up:
- Could you solve it using only O(1) extra space?

Example 1:
    Input:
    ["a","a","b","b","c","c","c"]
    Output:
    Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation:
    "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
    Input:
    ["a"]
    Output:
    Return 1, and the first 1 characters of the input array should be: ["a"]
    Explanation:
    Nothing is replaced.
Example 3:
    Input:
    ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    Output:
    Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation:
    Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
    Notice each digit has it's own entry in the array.
 
Note:
    1. All characters have an ASCII value in [35, 126].
    2. 1 <= len(chars) <= 1000.
*/
int my_compress(char* chars, int charsSize, int index, char tmp, int count){
    chars[index] = tmp;
    ++ index;
    if(count == 1){
        return index;
    }
    int digits = 0;
    while(count != 0){
        chars[index + digits] = count % 10 + '0';
        count /= 10;
        ++ digits;
    }
    for(int i=0; i<digits/2; ++i){
        char temp = chars[index + i];
        chars[index + i] = chars[index + digits-1-i];
        chars[index + digits-1-i] = temp;
    }
    return index + digits;
}
// === 8ms(87.10%) && 7.7MB(100%) === //
int compress(char* chars, int charsSize){
    if(charsSize == 0){
        return 0;
    }
    char tmp = chars[0];
    int count = 1;
    int index = 0;
    for(int i=1; i<charsSize; ++i){
        if(chars[i] == tmp){
            ++ count;
        }
        else{
            index = my_compress(chars, charsSize, index, tmp, count);
            tmp = chars[i];
            count = 1;
        }
    }
    index = my_compress(chars, charsSize, index, tmp, count);
    return index;
}

