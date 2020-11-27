package runnoob.date;

import java.text.SimpleDateFormat;
import java.util.Date;

public class fomatDate_2 {
    public static void main(String[] args){
        Date date = new Date();
        //HH则输出24小时制，hh则输出12小时制
        String strDateFormat = "yyyy-MM-dd hh:mm:ss HH a";
        SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
        //输入24小时制的时间
        System.out.println(sdf.format(date));
    }
}
