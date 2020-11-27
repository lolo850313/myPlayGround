package runnoob.collection;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class arrayToCollection_1 {
    public static void main(String[] args) throws IOException {
        int n = 5;
        String[] name = new String[n];
        for (int i = 0; i < n; i++) {
            name[i] = String.valueOf(i);
        }
        System.out.println(name);
        //Arrays.asList(name)将数组转换为集合
        List<String> list = Arrays.asList(name);
        System.out.println(list);
        System.out.println();
        for (String li : list) {
            String str = li;
            System.out.println(str + " ");

        }
    }
}
