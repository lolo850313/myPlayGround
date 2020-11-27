package runnoob.draw;

public class MutiplicationTable_2 {
//    public static void main(String[] args){
//        for (int i = 1; i < 10; i++) {
//            for (int j = 1; j < 10; j++) {
//                System.out.println(i + "*"+j + "="+ i*j);
//            }
//        }
//    }
    public static void main(String[] args){
        for (int i = 1; i < 10; i++) {
            for (int j = 1; j < i+1; j++) {
                System.out.print(i + "*"+j + "="+ i*j + "\t");
            }
            System.out.println();
        }
    }
}
