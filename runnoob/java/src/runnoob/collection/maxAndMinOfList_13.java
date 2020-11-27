package runnoob.collection;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class maxAndMinOfList_13 {
    public static void main(String[] args)throws Exception{
        List list = Arrays.asList("one two three four five six".split(" "));
        System.out.println("List" + list);
        System.out.println("max: " + Collections.max(list));
        System.out.println("min: " + Collections.min(list));

    }
}
