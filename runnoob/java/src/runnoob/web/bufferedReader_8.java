package runnoob.web;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.Socket;
import java.net.URL;

public class bufferedReader_8 {
    public static void main(String[] args)throws Exception{
        URL url = new URL("http://www.runoob.com");
        BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()));
        BufferedWriter writer = new BufferedWriter(new FileWriter("date.html"));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
            writer.write(line);
            writer.newLine();
        }
        reader.close();
        writer.close();
    }
}
