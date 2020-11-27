package runnoob.IO;

import java.io.*;

public class bufferWrite_4 {
    public static void main(String[] args)throws Exception {
        BufferedWriter out1 = new BufferedWriter(new FileWriter("srcfile.txt"));
        out1.write("string to be copied\n");
        out1.close();
        InputStream in = new FileInputStream(new File("srcfile.txt"));
        OutputStream out = new FileOutputStream(new File("destnfile.txt"));
        byte[] buf = new byte[1024];
        int len;
        while ((len = in.read(buf))>0) {
            out.write(buf, 0, len);
        }
        in.close();
        out.close();
        BufferedReader in1 = new BufferedReader(new FileReader("destnfile.txt"));
        String str;
        while ((str = in1.readLine()) != null) {
            System.out.println(str);
        }
        in1.close();
    }
}
