package runnoob.algorithm;


import java.util.LinkedList;

public class clear_linkedList_5 {
    public static void main(String[] args)  {
        LinkedList<String> llist = new LinkedList<String>();
        llist.add("1");
        llist.add("2");
        llist.add("3");
        llist.add("4");
        llist.add("5");
        System.out.println(llist);
        System.out.println(llist.subList(2,4));
        llist.subList(2,4).clear();
        System.out.println(llist);
    }

}
