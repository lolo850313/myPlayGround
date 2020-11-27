package runnoob.collection;

import java.io.IOException;
import java.util.*;

public class minAndMaxOfCollections_2 {
    public static void main(String[] args) throws IOException {
        String[] coins = {"Penny", "nickel", "dime", "Quarter", "dollar"};
        Set<String> set = new TreeSet<String>();
        for (int i = 0; i <coins.length ; i++) {
            set.add(coins[i]);
        }
        //找出set中的最小
        System.out.println(Collections.min(set));
        //将set中无视字母大小找出最小
        System.out.println(Collections.min(set, String.CASE_INSENSITIVE_ORDER));
        for (int i = 0; i <=10 ; i++) {
            System.out.print("-");
        }
        System.out.println("");
        System.out.println(Collections.max(set));
        //将set中无视字母大小找出最大
        System.out.println(Collections.max(set,String.CASE_INSENSITIVE_ORDER));
    }
}
