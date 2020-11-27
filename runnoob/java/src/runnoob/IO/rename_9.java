package runnoob.IO;

import java.io.File;

public class rename_9 {
    public static void main(String[] args){
        File oldName = new File("/Users/hewenhao/python/runnoob/myJavaFile.txt");
        File newName = new File("/Users/hewenhao/python/runnoob/new_myJavaFile.txt");
        if (oldName.renameTo(newName)) {
            System.out.println("已重命名");
        } else {
            System.out.println("Error");
        }
    }
}
