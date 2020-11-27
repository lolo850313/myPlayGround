package runnoob.array;
import java.util.Arrays;

public class PringArray1 {
    public static void main(String[] args) throws Exception{
        int array[] = {2,5,-2,6,-3,8,0,-7,-9,4};
        Arrays.sort(array);
        printArray("数组排序",array);
        int index = Arrays.binarySearch(array, 2);
        System.out.println("元素2所在位置（负数为不存在）：" + index);

    }
    public static void printArray(String message , int array[]) {
        System.out.println(message + ": [length:" + array.length + "]");
        for (int i = 0; i <array.length; i++) {
            if (i != 0) {
                System.out.println(",");
            }
            System.out.println(array[i]);
        }
        System.out.println();
    }

}
