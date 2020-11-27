package runnoob.IO;

import java.io.File;

public class setReadOnly_10 {
    public static void main(String[] args){
        File file = new File("/Users/hewenhao/python/runnoob/new_myJavaFile.txt");
        System.out.println(file.setReadOnly());
        System.out.println(file.canWrite());
    }
}
