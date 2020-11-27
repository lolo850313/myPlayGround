package runnoob.method;


public class break_8 {
    public static void main(String[] args) {
        int[] intary = {99, 12, 22, 34, 45, 67, 5678, 8900};
        int no = 5678;
        boolean found = false;
        for (int j = 0; j <intary.length; j++) {
            if (intary[j] == no) {
                found = true;
                break;
            }
        }
        if (found) {
            System.out.println(no + " 元素的索引位置在： " );
        } else {
            System.out.println(no + " 元素不再数组中");
        }
    }
}
