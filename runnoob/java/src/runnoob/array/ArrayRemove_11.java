package runnoob.array;

import java.util.ArrayList;

public class ArrayRemove_11 {
    public static void main(String[] args)  {
        ArrayList<String> objArray  = new ArrayList<String >();
        objArray.clear();
        objArray.add(0,"第0个元素");
        objArray.add(1,"第1个元素");
        objArray.add(2,"第2个元素");
        System.out.println("数组删除元素前" + objArray);
        objArray.remove(1);
        objArray.remove("第0个元素");
        System.out.println("数组删除元素前" + objArray);
    }

}
