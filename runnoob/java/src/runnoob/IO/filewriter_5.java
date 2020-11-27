package runnoob.IO;

import java.io.*;

public class filewriter_5 {
    public static void main(String[] args)throws Exception {
        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(("filename")));
            out.write("aString1\n");
            out.close();
            out = new BufferedWriter(new FileWriter("filename", true));
            out.write("aString2\n");
            out.close();
            BufferedReader in = new BufferedReader(new FileReader("filename"));
            String str;
            while ((str = in.readLine()) != null) {
                System.out.println(str);
            }
            in.close();
        } catch (IOException e) {
            System.out.println("exception occured" + e);
        }
    }
}
