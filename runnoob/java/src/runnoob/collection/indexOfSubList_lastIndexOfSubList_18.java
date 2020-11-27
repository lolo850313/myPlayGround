package runnoob.collection;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class indexOfSubList_lastIndexOfSubList_18 {
    public static void main(String[] args){
        List list = Arrays.asList("one Two three Four five six one three Four".split("  "));
        System.out.println("List" + list);
        List subList = Arrays.asList("three Four".split(" "));
        System.out.println("字列表： " + subList);
        System.out.println("indexOfSubList: " + Collections.indexOfSubList(list, subList));
        System.out.println("lastIndexOfSubList: " + Collections.lastIndexOfSubList(list, subList));

    }
}
