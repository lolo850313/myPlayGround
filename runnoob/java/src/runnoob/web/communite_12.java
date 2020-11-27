package runnoob.web;


import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URL;

public class communite_12 {
    public static void main(String[] args)throws Exception{
        try {
            ServerSocket ss = new ServerSocket(8888);
            System.out.println("启动服务器。。。。");
            Socket s = ss.accept();
            System.out.println("客户端" + s.getInetAddress().getLocalHost() + "已链接到服务器");
            BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));

            String mess = br.readLine();
            System.out.println("客户端" + mess);
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
            bw.write(mess + "\n");
            bw.flush();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
