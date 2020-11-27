package runnoob.collection;

import java.util.ArrayList;
import java.util.List;

public class addAndToArrayOflist_11 {
    public static void main(String[] args)throws Exception{
        List<String> list = new ArrayList<String>();
        list.add("菜");
        list.add("鸟");
        list.add("教");
        list.add("程");
        list.add("www.runoob.com");
        System.out.println(list);
        String[] s1 = list.toArray(new String[0]);
        System.out.println(s1);
        for (int i = 0; i <s1.length ; i++) {
            String contents = s1[i];
            System.out.println(contents);
        }
    }
}
