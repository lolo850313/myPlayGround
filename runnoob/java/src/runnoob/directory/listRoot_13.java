package runnoob.directory;

import java.io.File;
import java.io.FilenameFilter;

public class listRoot_13 {
    public static void main(String[] args) throws Exception {
        File[] roots = File.listRoots();
        System.out.println("系统所有根目录：");
        for (int i = 0; i < roots.length; i++) {
            System.out.println(roots[i].toString());
        }
    }
}