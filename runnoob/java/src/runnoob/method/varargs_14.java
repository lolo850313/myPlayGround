package runnoob.method;

public class varargs_14 {
    static int sumvarargs(int... intArrays){
        int sum, i;
        sum = 0;
        for (i = 0; i < intArrays.length; i++) {
            sum += intArrays[i];
        }
        return (sum);
    }

    public static void main(String a[]) {
        int sum = 0;
        sum = sumvarargs(new int[]{1, 2, 3,44});
        System.out.println("数字相加之和为: "+ sum);
    }
}
