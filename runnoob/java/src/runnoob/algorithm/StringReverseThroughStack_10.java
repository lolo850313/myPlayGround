package runnoob.algorithm;


import java.io.IOException;

public class StringReverseThroughStack_10 {
    private String input;
    private String output;


    public StringReverseThroughStack_10(String in) {
        input = in;
    }

    //从栈顶弹出元素，并将元素合并到outout中输出
    public String doRev() {
        int stackSize = input.length();
        Stack theStack = new Stack(stackSize);
        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            theStack.push(ch);
        }
        output = "";
        while (!theStack.isEmpty()){
            char ch = theStack.pop();
            output = output + ch;
        }
        return output;
    }
    public static void main(String[] args)throws IOException {
        String input = "www.w3school.cc";
        String output;
        StringReverseThroughStack_10 theReverse = new StringReverseThroughStack_10(input);
        output = theReverse.doRev();
        System.out.println("翻转前" + input);
        System.out.println("翻转后" + output);
    }
    class Stack{
        private int maxSize;
        private char[] stackArray;
        private int top;
        public Stack(int max){
            maxSize = max;
            stackArray = new char[maxSize];
            top = -1;
        }
        public void push(char j){
            stackArray[++top] = j;
        }
        public char pop(){
            return stackArray[top--];
        }

        public char peek(){
            return stackArray[top];
        }

        public boolean isEmpty() {
            return top == -1;
        }
    }
}
