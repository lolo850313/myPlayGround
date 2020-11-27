package runnoob.array;

import java.util.HashSet;
import java.util.Set;

//计算2个数组的交集
public class ArrayUnion_16 {
    public static void main(String[] args)  {
        String[] arr1 = {"1","2","3"};
        String[] arr2 = {"4","5","6"};
        String[] result = union(arr1, arr2);
        System.out.println("并集结果如下：" );
        for (String str: result
             ) {
            System.out.println(str);
        }
  }
    public static String[] union(String[] arr1,String[] arr2)  {
        Set<String> setAll = new HashSet<String >();
        for (String str:arr1
             ) {
            setAll.add(str);
        }
        for (String str:arr2
        ) {
            setAll.add(str);
        }
        String[] result = {};

        return setAll.toArray(result);

            }
}
