package runnoob.collection;

import java.io.IOException;
import java.util.*;

public class forAndIterator_6 {
    public static void main(String[] args){
        //list集合的遍历
        listTest();
        //Set集合的遍历;
        setTest();
    }

    private static void setTest() {
        Set<String> set = new HashSet<String>();
        set.add("Java");
        set.add("C");
        set.add("C++");
        //重复数据添加失败
        set.add("Java");
        set.add("JavaScript");

        Iterator<String> it = set.iterator();
        while (it.hasNext()) {
            String value = it.next();
            System.out.println(value);
        }

        for (String s : set) {
            System.out.println(s);
        }
    }

    private static void listTest() {
        List<String> list = new ArrayList<String>();
        list.add("菜");
        list.add("鸟");
        list.add("教");
        list.add("程");
        list.add("www.runoob.com");

        Iterator<String> it = list.iterator();
        while (it.hasNext()) {
            String value = it.next();
            System.out.println(value);
        }

        for (int i = 0,size = list.size(); i < size; i++) {
            String value = list.get(i);
            System.out.println(value);
        }
        for (String value : list) {
            System.out.println(value);
        }
    }
}
