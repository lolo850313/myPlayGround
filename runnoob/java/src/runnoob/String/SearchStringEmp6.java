package runnoob.String;

public class SearchStringEmp6 {
    public static void main(String[] args){
        String string = "Google Runnoob Taobao";
        int intIndex = string.indexOf("Runnoob");
        if (intIndex == -1){
            System.out.println("没有找到字符串 Runnoob");
        }else {
            System.out.println("Runnoob位置为" + intIndex);
        }
    }
}
