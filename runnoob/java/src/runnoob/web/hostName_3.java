package runnoob.web;

import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class hostName_3 {
    public static void main(String[] args)throws Exception{
        InetAddress addr = InetAddress.getLocalHost();
        System.out.println("Local HostAddress: " + addr.getHostAddress());
        String hostname = addr.getHostName();
        System.out.println("Local host name " + hostname);
    }
}
