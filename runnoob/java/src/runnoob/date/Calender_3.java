package runnoob.date;

import java.util.Calendar;

public class Calender_3 {
    public static void main(String[] args){
        Calendar cal = Calendar.getInstance();

        int day = cal.get(Calendar.DATE);
        int month = cal.get(Calendar.MONDAY) + 1;
        int year = cal.get(Calendar.YEAR);
        int dow = cal.get(Calendar.DAY_OF_WEEK);
        int dom = cal.get(Calendar.DAY_OF_MONTH);
        int doy = cal.get(Calendar.DAY_OF_YEAR);

        System.out.println("当前日期" + cal.getTime());
        System.out.println("日期" + day);
        System.out.println("月份" + month);
        System.out.println("年份" + year);
        System.out.println("周的第几天" + dow);
        System.out.println("月的第几天" + dom);
        System.out.println("年的第几天" + doy);
    }
}
