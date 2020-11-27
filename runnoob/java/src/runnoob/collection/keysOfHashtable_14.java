package runnoob.collection;

import java.util.*;

public class keysOfHashtable_14 {
    public static void main(String[] args)throws Exception{
        Hashtable ht = new Hashtable();
        ht.put("1", "One");
        ht.put("2", "Two");
        ht.put("3", "Three");
        Enumeration e = ht.keys();
        while (e.hasMoreElements()) {
            System.out.println(e.nextElement());
        }
    }
}
