package runnoob.collection;

import java.util.*;

public class mutilElementOfList_16 {
    public static void main(String[] args){
        List lnkLst = new LinkedList();
        lnkLst.add("element1");
        lnkLst.add("element2");
        lnkLst.add("element3");
        lnkLst.add("element4");
        displayAll(lnkLst);

        List aryLst = new ArrayList();
        aryLst.add("x");
        aryLst.add("y");
        aryLst.add("z");
        aryLst.add("W");
        displayAll(aryLst);

        Set hashSet = new HashSet();
        hashSet.add("set1");
        hashSet.add("set2");
        hashSet.add("set3");
        hashSet.add("set4");
        displayAll(hashSet);

        SortedSet treeSet = new TreeSet();
        treeSet.add("1");
        treeSet.add("2");
        treeSet.add("3");
        treeSet.add("4");
        displayAll(treeSet);

        LinkedHashSet lnkHashSet = new LinkedHashSet();
        lnkHashSet.add("one");
        lnkHashSet.add("two");
        lnkHashSet.add("three");
        lnkHashSet.add("four");
        displayAll(lnkHashSet);

        Map map1 = new HashMap();
        map1.put("key1", "j");
        map1.put("key2", "k");
        map1.put("key3", "l");
        map1.put("key4", "m");
        displayAll(map1.keySet());
        displayAll(map1.values());

        SortedMap map2 = new TreeMap();
        map2.put("key1", "jj");
        map2.put("key2", "kk");
        map2.put("key3", "ll");
        map2.put("key4", "mm");
        displayAll(map2.keySet());
        displayAll(map2.values());

        LinkedHashMap map3 = new LinkedHashMap();
        map3.put("key1", "jjj");
        map3.put("key2", "kkk");
        map3.put("key3", "lll");
        map3.put("key4", "mmm");
        displayAll(map3.keySet());
        displayAll(map3.values());
    }

    static void displayAll(Collection col) {
        Iterator itr = col.iterator();
        while (itr.hasNext()) {
            String str = (String) itr.next();
            System.out.print(str + " ");

        }
        System.out.println();
    }
}
