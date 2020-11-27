package runnoob.algorithm;


import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class queue_11 {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();
        //添加元素
        queue.offer("a");
        queue.offer("b");
        queue.offer("c");
        queue.offer("d");
        queue.offer("e");
        for (String q : queue) {
            System.out.println(q);
        }
        System.out.println("===");
        //返回第一个元素，并在队列中删除
        System.out.println("poll=" + queue.poll());
        for (String q : queue) {
            System.out.println(q);
        }

        //element,peek都是查询队列的头部元素，但队列为空时，element抛出一个异常，peek返回null
        System.out.println("===");
        //返回第一个元素
        System.out.println("element=" + queue.element());
        for (String q : queue) {
            System.out.println(q);
        }
        System.out.println("===");
        //返回第一个元素
        System.out.println("peek=" + queue.peek());
        for (String q : queue) {
            System.out.println(q);
        }
    }


}
