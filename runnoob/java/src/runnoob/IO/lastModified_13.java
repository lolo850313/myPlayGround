package runnoob.IO;

import java.io.File;
import java.util.Date;

public class lastModified_13 {
    public static void main(String[] args){
        File file = new File("mainJava.java");
        Long lastModified = file.lastModified();
        Date date = new Date(lastModified);
        System.out.println(date);
    }
}
