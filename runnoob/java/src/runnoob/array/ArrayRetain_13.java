package runnoob.array;

import java.util.ArrayList;

//计算2个数组的交集
public class ArrayRetain_13 {
    public static void main(String[] args)  {
        ArrayList objArray = new ArrayList();
        ArrayList objArray2 = new ArrayList();
        objArray2.add(0,"common1");
        objArray2.add(1,"common2");
        objArray2.add(2,"notcommon");
        objArray2.add(3,"notcommon1");
        objArray.add(0,"common1");
        objArray.add(1,"common2");
        objArray.add(2,"notcommon2");
        System.out.println("array1的元素" + objArray);
        System.out.println("array2的元素" + objArray2);
        objArray.retainAll(objArray2);
        System.out.println("array1 与 array2 数组交集为" + objArray);
    }

}
