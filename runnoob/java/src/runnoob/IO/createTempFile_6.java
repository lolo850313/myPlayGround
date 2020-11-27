package runnoob.IO;

import java.io.*;

//public class createTempFile_6 {
//    public static void main(String[] args)throws Exception {
//        File temp = File.createTempFile("testRunnoobimp", "txt");
//        System.out.println("文件路径" + temp.getAbsolutePath());
//        //临时文件退出时删除
//        temp.deleteOnExit();
//        BufferedWriter out = new BufferedWriter(new FileWriter(temp));
//        out.write("aString");
//        System.out.println("临时文件已创建");
//        out.close();
//    }
//}

//使用createFile()中的directory参数来指定临时文件的目录
public class createTempFile_6 {
    public static void main(String[] args)throws Exception {
        File f = null;
        try {
            f = File.createTempFile("temp", ".txt", new File("/Users/hewenhao/测试"));
            System.out.println("File path" + f.getAbsolutePath());
            f.deleteOnExit();
            f = File.createTempFile("temp", ".txt", new File("/Users/hewenhao"));
            System.out.print("File path" + f.getAbsolutePath());
            f.deleteOnExit();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
