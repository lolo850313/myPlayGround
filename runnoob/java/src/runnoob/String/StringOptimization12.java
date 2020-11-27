package runnoob.String;

//使用intern（），可以重用String对象，节省内存消耗。同时速度会变慢。
public class StringOptimization12 {
    public static void main(String[] args) {
        String variables[] = new String[50000];
        for (int i = 0; i < 50000; i++) {
            variables[i] = "s" + i;
        }
        long startTime0 = System.nanoTime();
        for (int i = 0; i < 50000 ; i++) {
            variables[i] = "hello";
        }
        long endTime0 = System.nanoTime();
        System.out.println("直接使用字符串" + ":" + (endTime0 - startTime0) + "纳秒");
        long startTime1 = System.nanoTime();
        for (int i = 0; i < 50000; i++) {
            variables[i] = new String("hello");
        }
        long endTime1 = System.nanoTime();
        System.out.println("通过new关键词创建字符串" + ":" + (endTime1 - startTime1) + "纳秒");
        long startTime2 = System.nanoTime();
        for (int i = 0; i < 50000; i++) {
            variables[i] = new String("hello");
            variables[i] = variables[i].intern();
        }
        long endTime2 = System.nanoTime();
        System.out.println("使用字符串对象的intern()" + ":" + (endTime2 - startTime2) + "纳秒");

    }
}
