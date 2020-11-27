package runnoob.String;

public class JavaStringSplitEmp7 {
    public static void main(String[] args){
        String string = "www-runnoob-com";
        String[] temp;
        String delimeter = "-";
        temp = string.split(delimeter);

        for (int i = 0; i < temp.length; i++) {
            System.out.println(temp[i]);
            System.out.println("");
        }
        System.out.println("------java for each循环输出的方法-----");
        String str1 = "www.runnoob.com";
        String[] temp1;
        String delimeter1 = "\\.";
        temp1 = str1.split(delimeter1);
        for (String x: temp1
             ) {
            System.out.println(x);
            System.out.println("");
        }
    }
}
