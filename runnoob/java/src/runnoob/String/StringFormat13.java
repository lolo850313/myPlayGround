package runnoob.String;
import java.util.Locale;

public class StringFormat13 {
    public static void main(String[] args) {
        double e = Math.E;
        System.out.format("%f%n", e);
        System.out.format(Locale.CHINA,"%-10.4f%n%n",e);
    }
}
