package runnoob.collection;

import java.lang.reflect.Array;
import java.util.*;

public class unmodifiableListOfCollection_9 {
    public static void main(String[] args)throws Exception{
        List stuff = Arrays.asList(new String[]{"a", "B"});
        List list = new ArrayList(stuff);
        list = Collections.unmodifiableList(list);
        try {
            list.set(0, "new Value");
        } catch (UnsupportedOperationException e) {
            System.out.println("oo");
        }
        System.out.println(list);
        for(Object value :list){
            System.out.println(value);
        }
        Set set = new HashSet(stuff);
        set = Collections.unmodifiableSet(set);
        Map map = new HashMap();
        map = Collections.unmodifiableMap(map);
        System.out.println("集合现在是只读");

    }
}
