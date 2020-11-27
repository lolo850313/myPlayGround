package runnoob.String;
import java.util.Arrays;

public class sortAndFind2 {
    public static void main(String[] args) throws Exception{
        int array[] = {2,5,-2,6,-3,8,0,-7,-9,4};
        Arrays.sort(array);
        printArray("数组排序结果为",array);
        int index = Arrays.binarySearch(array, 2);
        System.out.println("元素2在第" + index + "个位置");
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
