package runnoob.web;

import runnoob.date.SimpleDateFormat_1;

import java.net.URL;
import java.net.URLConnection;
import java.text.SimpleDateFormat;
import java.util.Date;

public class lastModifiedTimeOfURL_6 {
    public static void main(String[] args)throws Exception{
        URL u = new URL("http://127.0.0.1/test/test.html");
        URLConnection uc = u.openConnection();
        SimpleDateFormat ft = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        uc.setUseCaches(false);
        long timeStamp = uc.getLastModified();
        System.out.println("test.html 文件最后修改时间： " + ft.format(new Date(timeStamp)));
    }
}
