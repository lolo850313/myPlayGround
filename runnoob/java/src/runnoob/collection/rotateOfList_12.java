package runnoob.collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class rotateOfList_12 {
    public static void main(String[] args)throws Exception{
        List list = Arrays.asList("one two three four five six".split(" "));
        System.out.println("List" + list);
        Collections.rotate(list, 3);
        System.out.println("rotate: " + list);
    }
}
