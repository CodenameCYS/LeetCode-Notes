/*
=== 155. Min Stack ===

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    - push(x) -- Push element x onto stack.
    - pop() -- Removes the element on top of the stack.
    - top() -- Get the top element.
    - getMin() -- Retrieve the minimum element in the stack.
 
Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
*/
// =========================================================================================================== //
// === 24ms(90.96%) && 14.8MB(100%) === //
typedef struct {
    int min;
    int stack[100000];
    int size;
} MinStack;

/** initialize your data structure here. */

MinStack* minStackCreate() {
    MinStack* obj = (MinStack*)malloc(sizeof(MinStack));
    obj -> size = 0;
    return obj;
}

void minStackPush(MinStack* obj, int x) {
    if(obj -> size == 0 || x < obj -> min){
        obj -> min = x;
    }
    obj -> stack[obj -> size] = x;
    ++ obj -> size;
}

void minStackPop(MinStack* obj) {
    if(obj -> size == 0){
        return;
    }
    -- obj -> size;
    if(obj -> min < obj -> stack[obj -> size]){
        return;
    }
    obj -> min = obj -> stack[0];
    for(int i=1; i<obj->size; ++i){
        if(obj -> stack[i] < obj -> min){
            obj -> min = obj -> stack[i];
        }
    }
}

int minStackTop(MinStack* obj) {
    return obj -> stack[obj -> size - 1];
}

int minStackGetMin(MinStack* obj) {
    return obj -> min;
}

void minStackFree(MinStack* obj) {
    free(obj);
}
// =========================================================================================================== //
// === 20ms(98.31%) && 16MB(100%) === //
typedef struct {
    int min[100000];
    int stack[100000];
    int size;
} MinStack;

/** initialize your data structure here. */

MinStack* minStackCreate() {
    MinStack* obj = (MinStack*)malloc(sizeof(MinStack));
    obj -> size = 0;
    return obj;
}

void minStackPush(MinStack* obj, int x) {
    obj -> stack[obj -> size] = x;
    if(obj -> size == 0){
        obj -> min[obj -> size] = x;
    }
    else{
        obj -> min[obj -> size] = x < obj -> min[obj -> size - 1] ? x : obj -> min[obj -> size - 1];
    }
    ++ obj -> size;
}

void minStackPop(MinStack* obj) {
    -- obj -> size;
}

int minStackTop(MinStack* obj) {
    return obj -> stack[obj -> size - 1];
}

int minStackGetMin(MinStack* obj) {
    return obj -> min[obj -> size - 1];
}

void minStackFree(MinStack* obj) {
    free(obj);
}
// =========================================================================================================== //
/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, x);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/