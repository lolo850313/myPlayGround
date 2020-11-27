package runnoob.web;


import java.net.URL;
import java.net.URLConnection;
import java.util.Map;
import java.util.Set;

public class header_10 {
    public static void main(String[] args)throws Exception{
        URL url = new URL("http://www.runoob.com");
        URLConnection conn = url.openConnection();
        Map headers = conn.getHeaderFields();
        Set<String> keys = headers.keySet();
        for (String key : keys) {
            String val = conn.getHeaderField(key);
            System.out.println(key + "   " + val);
        }
        System.out.println(conn.getLastModified());
    }
}
