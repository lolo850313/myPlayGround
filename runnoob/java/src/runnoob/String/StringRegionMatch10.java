package runnoob.String;

public class StringRegionMatch10 {
    public static void main(String[] args) {
        String first_str = "Welcome to Microsoft";
        String second_str = "I work with microsoft";
        //regionMatches表示将first_str从第11个字符串开始，和second_str从
        //第12个字符串开始比较
        boolean match1 = first_str.
                regionMatches(11,second_str,12,9);

        //true表示忽略大小写
        boolean match2 = first_str.
                regionMatches(true,11,second_str,12,9);

        System.out.println("区分大小写返回值：" + match1);
        System.out.println("不区分大小写返回值：" + match2);
    }
}
