package runnoob.String;

public class StringReverseEmp5 {
    public static void main(String[] args){
        String string = "runnoob";
        String reverse = new StringBuffer(string).reverse().toString();
        System.out.println("字符串反转前" + string);
        System.out.println("字符串反转后" + reverse);
    }
}
