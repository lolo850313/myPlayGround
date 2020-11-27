package runnoob.array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//将数组输出
public class arrayMerge_7 {
    public static void main(String[] args)  {
        String a[] = {"A", "E", "I"};
        String b[] = {"O", "U"};
        List list = new ArrayList(Arrays.asList(a));
        //list.addAll是 传入一个List，将此List中的所有元素加入到当前List中
        list.addAll(Arrays.asList(b));
        Object[] c = list.toArray();
        System.out.println(Arrays.toString(c));
        System.out.println(c);
    }
}
