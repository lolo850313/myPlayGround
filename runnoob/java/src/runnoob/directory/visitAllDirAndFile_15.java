package runnoob.directory;

import java.io.File;

public class visitAllDirAndFile_15 {
    public static void main(String[] args) throws Exception {
        System.out.println("遍历目录");
        File dir = new File("/Users/hewenhao/python/runnoob");
        visitAlldirsAndFiles(dir);
    }

    public static void visitAlldirsAndFiles(File dir) {
        System.out.println(dir);
        if (dir.isDirectory()){
            String [] children = dir.list();
            for (int i = 0; i < children.length; i++) {
                visitAlldirsAndFiles(new File(dir,children[i]));
            }
        }
    }
}