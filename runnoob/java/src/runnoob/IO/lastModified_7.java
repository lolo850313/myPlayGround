package runnoob.IO;

import java.io.File;
import java.util.Date;


public class lastModified_7 {
    public static void main(String[] args)throws Exception {
        File fileToChange = new File("/Users/hewenhao/python/runnoob/myJavaFile.txt");
        fileToChange.createNewFile();
        Date fileTime = new Date(fileToChange.lastModified());
        System.out.println(fileTime.toString());
        System.out.println(fileToChange.setLastModified(System.currentTimeMillis()));
        fileTime = new Date(fileToChange.lastModified());
        System.out.println(fileTime.toString());

    }
}
