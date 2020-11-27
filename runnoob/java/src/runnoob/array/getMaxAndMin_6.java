package runnoob.array;

import java.util.Arrays;
import java.util.Collections;

//将数组输出
public class getMaxAndMin_6 {
    public static void main(String[] args) throws Exception {
        Integer[] numbers = {8, 2, 7, 1, 4, 9, 5};
        //Arrays.asList将数组转化为list
        //Collections.min返回给定collection的最小元素
        int min = (int) Collections.min(Arrays.asList(numbers));
        int max = (int) Collections.max(Arrays.asList(numbers));
        System.out.println("最小值" + min);
        System.out.println("最大值" + max);

    }
}
