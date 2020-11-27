package runnoob.method;

public class varargs_15 {
    static void vaTest(int ... no){
        System.out.print("vaTest(int...): " + "参数个数：" + no.length +
                "内容： ");
        for (int n :no
             ) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
    static void vaTest(String msg,int ... no){
        System.out.print("vaTest(String, int ...): " +msg+ " 参数个数：" + no.length +
                "内容： ");
        for (int n :no
        ) {
            System.out.print(n + " ");

        }
        System.out.println();
    }
    static void vaTest(boolean ... no){
        System.out.print("vaTest(boolean ...): " + "参数个数：" + no.length +
                "内容： ");
        for (boolean n :no
        ) {
            System.out.print(n + " ");
        }
        System.out.println();
    }
    public static void main(String a[]) {
        vaTest(1,2,3);
        vaTest("测试:",1,2,3);
        vaTest(true,false,true);
    }
}
