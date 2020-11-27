package runnoob.directory;

import java.io.File;

public class parentDirectory_7 {
    public static void main(String[] args)throws Exception {
        File file = new File("/Users/hewenhao/python/runnoob/src/runnoob/IO");
        String strParentDirectory = file.getParent();
        System.out.println("文件的上级目录为" + strParentDirectory);
    }
        }
