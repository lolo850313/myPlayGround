package runnoob.directory;

import java.io.File;
import java.io.FileFilter;

public class fileList_10 {
    public static void main(String[] args) throws Exception {
        File dir = new File("/Users/hewenhao/python/runnoob");
        File[] files = dir.listFiles();
        FileFilter fileFilter = new FileFilter() {
            public boolean accept(File file){
                return file.isDirectory();
            }
        };
        files = dir.listFiles(fileFilter);
        System.out.println(files.length);
        if (files.length == 0) {
            System.out.println("目录不存在或者不是一个目录");
        } else {
            for (int i = 0; i < files.length; i++) {
                File filename = files[i];
                System.out.println(filename.toString());
            }
        }

    }
}