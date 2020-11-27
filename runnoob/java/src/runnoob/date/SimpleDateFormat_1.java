package runnoob.date;
import java.util.Date;
import java.text.SimpleDateFormat;

public class SimpleDateFormat_1 {
    public static void main(String[] args){
        Date date = new Date();
        String strDateFormat = "yyyy-MM-dd:hh:mm:ss";
        SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
        System.out.println(sdf.format(date));
    }
}
