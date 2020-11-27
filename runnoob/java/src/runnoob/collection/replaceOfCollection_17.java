package runnoob.collection;

import java.util.*;

public class replaceOfCollection_17 {
    public static void main(String[] args){
        List list = Arrays.asList("one Two three Four five six one three Four".split("  "));
        System.out.println("List" + list);
        Collections.replaceAll(list, "one", "hundred");
        System.out.println("replaceAll: " + list);
    }
}
