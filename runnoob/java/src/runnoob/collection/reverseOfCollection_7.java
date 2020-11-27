package runnoob.collection;

import java.util.*;

public class reverseOfCollection_7 {
    public static void main(String[] args){
        String[] coins = {"A", "B", "C", "D", "E"};
        List l = new ArrayList();
        for (int i = 0; i < coins.length; i++) {
            l.add(coins[i]);
        }
        ListIterator liter = l.listIterator();
        System.out.println("反转前");
        while (liter.hasNext()) {
            System.out.println(liter.next());
        }
        Collections.reverse(l);
        liter = l.listIterator();
        System.out.println("反转后");
        while (liter.hasNext()) {
            System.out.println(liter.next());
        }
    }
}
