package runnoob.directory;

import java.io.File;
import java.io.FileFilter;

public class allFile_11 {
    public static void main(String[] args) throws Exception {
        File dir = new File("/Users/hewenhao/python/runnoob");
        String[] children = dir.list();
        if (children==null){
            System.out.println("目录不存在或者不是一个目录");
        }else{
            for (int i = 0; i < children.length; i++) {
                String filename = children[i];
                System.out.println(filename);
            }
        }
    }
}