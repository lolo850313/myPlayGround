package runnoob.algorithm;


import java.util.LinkedList;

public class topAndPop_linkedList_6 {
    private LinkedList list = new LinkedList();

    public void push(Object v) {
        list.addFirst(v);
    }

    public Object top() {
        return list.getFirst();
    }

    public Object pop() {
        return list.removeFirst();
    }
    public static void main(String[] args)  {
        topAndPop_linkedList_6 stack = new topAndPop_linkedList_6();
        for (int i = 0; i < 40; i++) {
            stack.push(i);
        }
        System.out.println(stack.top());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }

}
