package runnoob.algorithm;


import java.util.LinkedList;

public class getFirst_linkedList_4 {
    public static void main(String[] args)  {
        LinkedList<String> llist = new LinkedList<String>();
        llist.add("1");
        llist.add("2");
        llist.add("3");
        llist.add("4");
        llist.add("5");
        System.out.println("链表第一个元素是： " + llist.getFirst());
        System.out.println("链表第一个元素是： " + llist.getLast());
    }

}
