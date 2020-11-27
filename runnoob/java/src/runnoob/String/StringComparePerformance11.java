package runnoob.String;

public class StringComparePerformance11 {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        for (int i = 0; i < 500000 ; i++) {
            String s1 = "hello";
            String s2 = "hello";
        }
        long endTime = System.nanoTime();
        System.out.println("通过String关键词创建字符串" + ":" + (endTime - startTime) + "纳秒");
        long startTime1 = System.nanoTime();
        for (int i = 0; i < 500000; i++) {
            String s3 = new String("hello");
            String s4 = new String("hello");
        }
        long endTime1 = System.nanoTime();
        System.out.println("通过String关键词创建字符串" + ":" + (endTime1 - startTime1) + "纳秒");

    }
}
