package runnoob.directory;

import java.io.File;

public class mkdir_1 {
    public static void main(String[] args) {
        String directories = "/Users/hewenhao/python/runnoob/dirTest/dirTest1/dirTest2";
        File file = new File(directories);
        boolean result = file.mkdirs();
        System.out.println("status " + result);
    }
        }
