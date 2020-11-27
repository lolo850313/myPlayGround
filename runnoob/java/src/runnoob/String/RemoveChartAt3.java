package runnoob.String;

public class RemoveChartAt3 {
    public static void main(String[] args) throws Exception{
        String str = "this is java";
        System.out.println(removeChartAt(str, 4));
    }
    public static String removeChartAt(String s , int pos) {
        return s.substring(0, pos) + s.substring(pos + 1);
    }
}
