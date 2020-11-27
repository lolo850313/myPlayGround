package runnoob.array;

//数组初始化后对数组进行扩容
public class FindDupicateInArray_10 {
    public static void main(String[] args)  {
        int[] my_array = {1, 2, 5, 5, 6, 6, 7, 2, 9, 2};
        findDupicateInArray(my_array);
    }
    public static void findDupicateInArray(int[] a)  {
        int count = 0;
        for (int i = 0; i < a.length; i++) {
            for (int j = i+1; j < a.length; j++) {
                if (a[j] == a[i]){
                    count++;
                }
            }
            if (count > 1){
                System.out.println("重复元素" + a[i]);
                count = 0;
            }
        };



    }
}
