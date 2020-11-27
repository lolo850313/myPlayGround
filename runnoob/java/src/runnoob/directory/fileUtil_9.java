package runnoob.directory;

import java.io.File;
import java.io.IOException;

public class fileUtil_9 {
    public static void main(String[] args) throws Exception {
        showDir(1,new File("/Users/hewenhao/python/runnoob/src/runnoob/directory"));
    }

    static void showDir(int indent, File file)throws Exception {
        for (int i = 0; i < indent; i++) {
            System.out.print("-");
        }
        System.out.println(file.getName());
        if (file.isDirectory()) {
            File[] files = file.listFiles();
            for (int i = 0; i < files.length; i++) {
                showDir(indent+4,files[i]);
            }
        }
    }
}