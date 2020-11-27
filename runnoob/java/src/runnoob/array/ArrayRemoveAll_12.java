package runnoob.array;

import java.util.ArrayList;

//数组初始化后对数组进行扩容
public class ArrayRemoveAll_12 {
    public static void main(String[] args)  {
        ArrayList objArray = new ArrayList();
        ArrayList objArray2 = new ArrayList();
        objArray2.add(0,"common1");
        objArray2.add(1,"common2");
        objArray2.add(2,"notcommon1");
        objArray.add(0,"common1");
        objArray.add(1,"common2");
        objArray.add(2,"notcommon2");
        System.out.println("array1的元素" + objArray);
        System.out.println("array2的元素" + objArray2);
        objArray.removeAll(objArray2);
        System.out.println("array1 与 array2 数组差集为" + objArray);
    }

}
