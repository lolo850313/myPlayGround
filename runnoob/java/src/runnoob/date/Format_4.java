package runnoob.date;

import java.util.Date;
import java.text.SimpleDateFormat;

public class Format_4 {
    public static void main(String[] args){
        Long timeStamp = System.currentTimeMillis();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String sd = sdf.format(new Date(Long.parseLong(String.valueOf(timeStamp))));
        System.out.println("格式化的结果" + sd);
        SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy年MM月dd日 HH 时 mm 分 ss 秒");
        String sd2 = sdf2.format(new Date(Long.parseLong(String.valueOf(timeStamp))));
        System.out.println("格式化的结果" + sd2);


    }
}
