package runnoob.IO;

import java.io.*;

public class delete_3 {
    public static void main(String[] args) {
        try {
            File file = new File("runoob.txt");
            if (file.delete()) {
                System.out.println(file.getName() + " 文件已经被删除");
            } else {
                System.out.println("文件删除失败");
            }
        }catch (Exception e) {
            //在命令行打印异常信息在程序中出错的位置和原因
            e.printStackTrace();
        }
    }
}
