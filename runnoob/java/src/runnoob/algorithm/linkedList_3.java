package runnoob.algorithm;


import java.util.LinkedList;

public class linkedList_3 {
    public static void main(String[] args)  {
        LinkedList<String> llist = new LinkedList<String>();
        llist.add("1");
        llist.add("2");
        llist.add("3");
        llist.add("4");
        llist.add("5");
        System.out.println(llist);
        llist.addFirst("0");
        System.out.println(llist);
        llist.addLast("6");
        System.out.println(llist);
    }

}
