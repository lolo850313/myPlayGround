package runnoob.web;


import java.net.URL;

public class analyseURL_11 {
    public static void main(String[] args)throws Exception{
        URL url = new URL("http://www.runoob.com/html/html-tutorial.html");
        System.out.println("URL是： " + url.toString());
        System.out.println("协议是： " + url.getProtocol());
        System.out.println("文件名： " + url.getFile());
        System.out.println("主机： " + url.getHost());
        System.out.println("路径： " + url.toString());
        System.out.println("端口号： " + url.toString());
        System.out.println("默认端口： " + url.toString());
    }
}
