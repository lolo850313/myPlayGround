package runnoob.array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//将数组输出
public class FillTest_8 {
    public static void main(String[] args)  {
        int array[] = new int[6];
        //将array用100填满
        Arrays.fill(array,100);
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
        System.out.println();
        //将array用50填充，起始位置为3，结束位置为6
        Arrays.fill(array,3,6,50);
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
        }
    }
}
