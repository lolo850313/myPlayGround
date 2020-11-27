package runnoob.IO;

import java.io.File;

public class exist_11 {
    public static void main(String[] args){
        File file = new File("/Users/hewenhao/python/runnoob/new_myJavaFile.txt");
        System.out.println(file.exists());
    }
}
