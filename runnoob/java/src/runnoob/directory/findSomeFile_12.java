package runnoob.directory;

import java.io.File;
import java.io.FileFilter;
import java.io.FilenameFilter;

public class findSomeFile_12 {
    public static void main(String[] args) throws Exception {
        File dir = new File("/Users/hewenhao/python/runnoob");
        FilenameFilter filter = new FilenameFilter() {
            public boolean accept(File dir, String name) {
                return name.startsWith("d");
            }
        };
        String[] children = dir.list(filter);
        if (children == null) {
            System.out.println("目录不存在或者不是一个目录");
        }else{
            for (int i = 0; i < children.length; i++) {
                String filename = children[i];
                System.out.println(filename);
            }
        }
    }
}