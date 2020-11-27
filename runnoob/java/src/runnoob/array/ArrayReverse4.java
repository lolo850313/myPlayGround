package runnoob.array;

import java.util.ArrayList;
import java.util.Collections;
//将数组反转
public class ArrayReverse4 {
    public static void main(String[] args) throws Exception{
        ArrayList<String> arrayList = new ArrayList<String >();
        arrayList.add("A");
        arrayList.add("B");
        arrayList.add("C");
        arrayList.add("D");
        arrayList.add("E");
        System.out.println("反转前" + arrayList);
        Collections.reverse(arrayList);
        System.out.println("反转后" + arrayList);

    }

}
