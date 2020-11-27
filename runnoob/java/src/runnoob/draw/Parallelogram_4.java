package runnoob.draw;


public class Parallelogram_4 {
    public static void main(String[] args) {
        print(5);//输出5行菱形
    }

    public static void print(int size) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j<size-i ; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j<2*(size)-1 ; j++) {
                System.out.print("-");
            }
            System.out.println();
        }

    }
}
