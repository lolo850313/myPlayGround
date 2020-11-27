package runnoob.web;

import java.net.InetAddress;
import java.net.URL;
import java.net.URLConnection;

public class urlConnection_4 {
    public static void main(String[] args)throws Exception{
        int size;
        URL url = new URL("http://www.runoob.com/wp-content/themes/runoob/assets/img/newlogo.png");
        URLConnection conn = url.openConnection();
        size = conn.getContentLength();
        if (size < 0) {
            System.out.println("无法获取文件大小。");
        } else {
            System.out.println("文件大小为： " + size + " bytes");
        }
        conn.getInputStream();
    }
}
