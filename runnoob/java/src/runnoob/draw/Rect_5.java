package runnoob.draw;


public class Rect_5 {
    public static void main(String[] args) {
        print(5);//输出5行菱形
    }

    public static void print(int size) {
        for (int i = 0; i < size; i++) {
            for (int j = 0; j<2*(size)-1 ; j++) {
                System.out.print("-");
            }
            System.out.println();
        }

    }
}
