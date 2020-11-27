package runnoob.directory;

import java.io.File;

public class dirList_6 {
    public static void main(String[] args)throws Exception {
        File dir = new File("dirTest");
        String[] children = dir.list();
        if (children == null) {
            System.out.println("该目录不存在");
        } else {
            for (int i = 0; i <children.length; i++) {
                String fileName = children[i];
                System.out.println(fileName);
            }
        }
    }
        }
