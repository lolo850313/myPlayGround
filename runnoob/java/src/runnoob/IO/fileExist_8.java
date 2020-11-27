package runnoob.IO;

import java.io.File;

public class fileExist_8 {
    public static long getFileSize(String filename) {
        File file = new File(filename);
        if (!file.exists()) {
            System.out.println("文件不存在");
            return -1;
        }
        return file.length();
    }
    public static void main(String[] args)throws Exception {
        long size = getFileSize("/Users/hewenhao/python/runnoob/myJavaFile.txt");
        System.out.println("myJavaFile.txt 的大小为" + size);
    }
}
