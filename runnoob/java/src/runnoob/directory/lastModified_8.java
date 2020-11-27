package runnoob.directory;

import java.io.File;
import java.util.Date;

public class lastModified_8 {
    public static void main(String[] args) throws Exception {
        File file = new File("filename");
        System.out.println("最后的修改时间"+ new Date(file.lastModified()));
    }
}