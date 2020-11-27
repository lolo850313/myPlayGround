package runnoob.web;

import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class socket_2 {
    public static void main(String[] args){
        Socket Skt;
//        String host = "localhost";
        String host = "www.runoob.com";
        if (args.length > 0) {
            host = args[0];
        }
        for (int i = 0; i < 100; i++) {
            try {
                System.out.println("查看 " + i);
                Skt = new Socket(host, i);
                System.out.println("端口 " + i + "已被占用");
            } catch (UnknownHostException e) {
                System.out.println("Exception occured" + e);
                break;
            } catch (IOException e) {

            }
        }
    }
}
