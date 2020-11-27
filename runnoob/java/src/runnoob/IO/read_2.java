package runnoob.IO;

import java.io.*;

public class read_2 {
    public static void main(String[] args) {
        try {
            BufferedReader out = new BufferedReader(new FileReader("test.log"));
            String str;
            while ((str = out.readLine())!=null) {
                System.out.println(str);
            }
            System.out.println("@@@");
            System.out.println(str);
        }catch (IOException e) {

        }
    }
}
