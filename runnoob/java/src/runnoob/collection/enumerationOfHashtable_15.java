package runnoob.collection;

import java.util.Enumeration;
import java.util.Hashtable;

public class enumerationOfHashtable_15 {
    public static void main(String[] args)throws Exception{
        Hashtable ht = new Hashtable();
        ht.put("1", "One");
        ht.put("2", "Two");
        ht.put("3", "Three");
        Enumeration e = ht.elements();
        while (e.hasMoreElements()) {
            System.out.println(e.nextElement());
        }
    }
}
