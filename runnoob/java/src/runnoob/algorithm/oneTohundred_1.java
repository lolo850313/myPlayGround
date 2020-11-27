package runnoob.algorithm;


public class oneTohundred_1 {
    public static void main(String[] args)  {
        int limit = 100;
        int sum = 0;
        int start = 1;
        do {
            sum = sum + start;
            start = start + 1;
        } while (
                start <= limit
        );
        System.out.println(sum);
    }

}
