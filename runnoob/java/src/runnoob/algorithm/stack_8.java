package runnoob.algorithm;


public class stack_8 {
    private int maxSize;
    private long[] stackArray;
    private int top;
    public stack_8(int s){
        maxSize = s;
//        栈的最大长度
        stackArray = new long[maxSize];
        //栈顶初始位置
        top = -1;
    }
    public void push(long j){
//        栈顶位置自加1
//        栈顶位置的值为j
        stackArray[++top] = j;
    }
    public long pop(){
        //返回栈顶元素
        //栈顶位置自减1
        return stackArray[top--];
    }

    public long peek() {
//        返回栈顶值
        return stackArray[top];
    }

    public boolean isEmpty() {
//        判断栈的top是否为-1，是则表明栈是空栈。
        return (top == -1);
    }

    public boolean isFull() {
        return (top == maxSize - 1);
    }

    public static void main(String[] args) {
        stack_8 theStack = new stack_8(10);
        theStack.push(10);
        theStack.push(20);
        theStack.push(30);
        theStack.push(40);
        System.out.println(theStack.pop());
        theStack.push(50);
        theStack.isEmpty();
        while (!theStack.isEmpty()) {
            long value = theStack.pop();
            System.out.print(value);
            System.out.print(" ");
        }
        System.out.println(theStack.isEmpty());

    }
}
