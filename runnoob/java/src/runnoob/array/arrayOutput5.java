package runnoob.array;

//将数组输出
public class arrayOutput5 {
    public static void main(String[] args) throws Exception{
        String[] runnoobs = new String[3];
        runnoobs[0] = "菜鸟教程";
        runnoobs[1] = "菜鸟工具";
        runnoobs[2] = "菜鸟笔记";
//        for (int i = 0; i < runnoobs.length; i++) {
//            System.out.println(runnoobs[i]);
//        }
        //使用for each便利输出
        for (String obj:runnoobs
             ) {
            System.out.println(obj);
        }
    }

}
