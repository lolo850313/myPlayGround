package runnoob.IO;

import java.io.File;
import java.io.IOException;

public class createNewFile_14 {
    public static void main(String[] args){
        try {
            File file = new File("/Users/hewenhao/python/runnoob/myFile.txt");
            if (file.createNewFile()) {
                System.out.println("文件创建成功");
            } else {
                System.out.println("文件创建失败");
            }
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}
