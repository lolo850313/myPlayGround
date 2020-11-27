package runnoob.method;

public class factorial_5 {
    public static void main(String[] args) {
        for (int counter = 0; counter <=10 ; counter++) {
            System.out.printf("%d = %d\n",
                    counter, factorial(counter));
        }
    }
    public static long factorial(long number) {
        if ((number == 0) || (number == 1)) {
            return 1;
        } else {
            return factorial(number - 1)*number;
        }
    }
}
