package runnoob.IO;

import java.io.File;
import java.io.IOException;

public class compareTo_15 {
    public static void main(String[] args){
        File file1 = new File("/Users/hewenhao/python/runnoob/demo1.txt");
        File file2 = new File("/Users/hewenhao/python/runnoob/dd/demo1.txt");
        if (file1.compareTo(file2) == 0) {
            System.out.println("文件路径一致");
        } else {
            System.out.println("文件路径不一致");
        }
    }
}
