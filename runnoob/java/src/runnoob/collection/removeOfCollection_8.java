package runnoob.collection;

import java.util.*;

public class removeOfCollection_8 {
    public static void main(String[] args){
        System.out.println("集合实例!\n");
        int Size;
        HashSet collection = new HashSet();
        String str1 = "Yellow", str2 = "White", str3 = "Green", str4 = "Blue";
        Iterator iterator;
        collection.add(str1);
        collection.add(str2);
        collection.add(str3);
        collection.add(str4);
        System.out.println("集合数据： ");
        iterator = collection.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next() + " ");
        }
        System.out.println();
        collection.remove(str2);
        System.out.println("删除之后 [" + str2+ "]");
        System.out.println("现在集合的数据是： ");
        iterator = collection.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next() + " ");
        }
        System.out.println();
        int size = collection.size();
        System.out.println("集合大小： " + size + "\n");
    }
}
