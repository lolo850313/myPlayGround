package runnoob.array;
import java.util.Arrays;

public class insertElement2 {
    public static void main(String[] args) throws Exception{
        int array[] = {2,5,-2,6,-3,8,0,-7,-9,4};
        Arrays.sort(array);
        printArray("数组排序",array);
        int index = Arrays.binarySearch(array, 1);
        System.out.println("元素1所在位置（负数为不存在）：" + index);
        int newIndex = -index - 1;
        array = insertElement(array, 1, newIndex);
        printArray("数组添加元素1",array);
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
    public static int[] insertElement(int original[],int element, int index) {
        int length = original.length;
        int destination[] = new int[length + 1];
        System.arraycopy(original,0,destination,0,index);
        //将index前的元素拷贝到目标列表中
        for (int i = 0; i < destination.length; i++) {
            System.out.println(destination[i]);
        }
        //将列表的index位置设置为需要插入的数值
        destination[index] = element;
        for (int i = 0; i < destination.length; i++) {
            System.out.println(destination[i]);
        }
        //将index+1后的元素拷贝到目标数组中
        System.arraycopy(original,index,destination,index +1,length-index);
        return destination;
    }
}
