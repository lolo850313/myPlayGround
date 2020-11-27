package runnoob.String;
import java.util.Locale;
//通过+操作符和stringbuffer.append方法来连接字符串，并比较性能
public class StringConcatenate14 {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        for (int i = 0; i < 5000; i++) {
            String result = "This is" + "testing the" + "difference"
                    +"between" + "String" + "and" + "StringBuffer";
        }
        long endTime = System.nanoTime();
        System.out.println("字符串连接" + " - 使用 + 操作符：" + (endTime - startTime) + "ms");
        long startTime1 = System.nanoTime();
        for (int i = 0; i < 5000; i++) {
            StringBuffer result = new StringBuffer();
            result.append("This is");
            result.append("testing the");
            result.append("difference");
            result.append("between");
            result.append("String");
            result.append("and");
            result.append("StringBuffer");
        }
        long endTime1 = System.nanoTime();
        System.out.println("字符串连接" + " - 使用 StringBuffer操作符：" + (endTime1 - startTime1) + "ms");
    }
}
