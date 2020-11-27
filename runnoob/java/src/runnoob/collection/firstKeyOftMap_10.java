package runnoob.collection;

import java.util.*;

public class firstKeyOftMap_10 {
    public static void main(String[] args)throws Exception{
        System.out.println("TreeMap 实例！ \n");
        TreeMap tMap = new TreeMap();
        tMap.put(1, "Sunday");
        tMap.put(2, "Monday");
        tMap.put(3, "Tuesday");
        tMap.put(4, "Wednesday");
        tMap.put(5, "Thursday");
        tMap.put(6, "Friday");
        tMap.put(7, "Saturday");
        System.out.println("TreeMap 键：" + tMap.keySet());
        System.out.println("TreeMap 值：" + tMap.values());
        System.out.println("TreeMap 键为5的值为：" + tMap.get(5));
        System.out.println("TreeMap 第一个键：" + tMap.firstKey() + " Value: " + tMap.get(tMap.firstKey()));
        System.out.println("TreeMap 最后一个值：" + tMap.lastKey()+ " Value: " + tMap.get(tMap.lastKey()));
        System.out.println("TreeMap 移除第一个数据：" + tMap.remove(tMap.firstKey()));
        System.out.println("现在TreeMap 键：" + tMap.keySet());
        System.out.println("现在TreeMap 值：" + tMap.values());
        System.out.println("TreeMap 移除最后一个数据：" + tMap.remove(tMap.lastKey()));
        System.out.println("现在TreeMap 键：：" + tMap.keySet());
        System.out.println("现在TreeMap 值：" + tMap.values());

    }
}
