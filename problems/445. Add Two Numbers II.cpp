/*
=== 445. Add Two Numbers II ===

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
- What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void list2num(struct ListNode* l, int* num, int* len){
    while(l){
        num[*len] = l->val;
        ++ *len;
        l = l->next;
    }
}

void add_num(int* num1, int l1, int* num2, int l2, int* sum, int* len){
    int carry = 0;
    while(l1>0 && l2>0){
        int digit = num1[l1-1] + num2[l2-1] + carry;
        sum[*len] = digit % 10;
        carry = digit / 10;
        ++ *len;
        -- l1;
        -- l2;
    }
    while(l1 > 0){
        int digit = num1[l1-1] + carry;
        sum[*len] = digit % 10;
        carry = digit / 10;
        ++ *len;
        -- l1;
    }
    while(l2 > 0){
        int digit = num2[l2-1] + carry;
        sum[*len] = digit % 10;
        carry = digit / 10;
        ++ *len;
        -- l2;
    }
    if(carry != 0){
        sum[*len] = carry;
        ++ *len;
    }
}

struct ListNode* num2list(int* num, int len){
    struct ListNode* head = NULL;
    for(int i=0; i<len; ++i){
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node -> val = num[i];
        node -> next = head;
        head = node;
    }
    return head;
}

void show(int* num, int len){
    for(int i=0; i<len; ++i){
        printf("%d", num[i]);
    }
    printf("\n");
}
// === 12ms(89.74%) && 9.1MB(100%) === //
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int num1[500], num2[500], sum[500];
    int len1=0, len2=0,  len=0;
    list2num(l1, num1, &len1);
    // show(num1, len1);
    list2num(l2, num2, &len2);
    // show(num2, len2);
    add_num(num1, len1, num2, len2, sum, &len);
    // show(sum, len);
    return num2list(sum, len);
}

