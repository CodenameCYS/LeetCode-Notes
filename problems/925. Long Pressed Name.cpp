/*
=== 925. Long Pressed Name ===

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
    Input: name = "alex", typed = "aaleex"
    Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
    Input: name = "saeed", typed = "ssaaedd"
    Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
    Input: name = "leelee", typed = "lleeelee"
    Output: true

Example 4:
    Input: name = "laiden", typed = "laiden"
    Output: true
Explanation: It's not necessary to long press any character.
 
Note:
    1. name.length <= 1000
    2. typed.length <= 1000
    3. The characters of name and typed are lowercase letters.
*/
bool isLongPressedName(char* name, char* typed) {
    int i=0, j=0;
    while(name[i] != '\0'){
        while(name[i]!='\0' && name[i] == typed[j]){
            ++i;
            ++j;
        }
        if(name[i] =='\0' && typed[j] == '\0'){
            return true;
        }
        else if(typed[j] == '\0'){
            return false;
        }
        else{
            while(typed[j]!='\0' && typed[j] == name[i-1]){
                ++j;
            }
            if(name[i] =='\0' && typed[j] == '\0'){
                return true;
            }
            else if(typed[j] == '\0'){
                return false;
            }
            else if(typed[j] != name[i]){
                return false;
            }
        }
    }
    return true;
}