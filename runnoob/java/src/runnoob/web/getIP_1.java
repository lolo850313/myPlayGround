package runnoob.web;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class getIP_1 {
    public static void main(String[] args){
        InetAddress address = null;
        try {
            address = InetAddress.getByName("www.runoob.com");

        } catch (UnknownHostException e) {
            System.exit(2);
        }
        System.out.println(address.getHostName() + "=" + address.getHostAddress());
        System.exit(0);
    }
}
