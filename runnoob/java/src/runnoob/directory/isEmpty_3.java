package runnoob.directory;

import java.io.File;

public class isEmpty_3 {
    public static void main(String[] args) {
        File file = new File("dirTest");
        if (file.isDirectory()) {
            if (file.list().length > 0) {
                System.out.println("目录不为空");
            } else {
                System.out.println("目录为空");
            }
        } else {
            System.out.println("这不是一个目录");
        }
    }
}
