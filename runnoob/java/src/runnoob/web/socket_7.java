package runnoob.web;

import java.net.InetAddress;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import java.text.SimpleDateFormat;
import java.util.Date;

public class socket_7 {
    public static void main(String[] args)throws Exception{
        try {
            InetAddress addr;
            Socket sock = new Socket("www.runoob.com", 80);
            addr = sock.getInetAddress();
            System.out.println("连接到" + addr);
            sock.close();
        } catch (java.io.IOException e) {
            System.out.println("无法链接" + args[0]);
            System.out.println(e);
        }
    }
}
