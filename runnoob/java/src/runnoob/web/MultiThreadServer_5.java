package runnoob.web;

import java.io.IOException;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;

//定义一个类实现Runnable接口，重写接口中的run()方法。在run()方法中加入具体的任务代码或处理逻辑。
//(2).创建Runnable接口实现类的对象。
//(3).创建一个Thread类的对象，需要封装前面Runnable接口实现类的对象。（接口可以实现多继承）
//(4).调用Thread对象的start()方法，启动线程
public class MultiThreadServer_5 implements Runnable{
    Socket csocket;

    MultiThreadServer_5(Socket csocket) {
        this.csocket = csocket;
    }
    public static void main(String[] args)throws Exception{
        ServerSocket ssock = new ServerSocket(1234);
        System.out.println("Listening");
        while (true) {
            Socket sock = ssock.accept();
            System.out.println("Connected");
            new Thread(new MultiThreadServer_5(sock)).start();
        }

    }

    public void run() {
        try {
            PrintStream pstream = new PrintStream(csocket.getOutputStream());
            for (int i = 100; i >=0; i--) {
                pstream.println(i+" bottles of beer on the wall");
                pstream.close();
                csocket.close();
            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
