package runnoob.method.overLoading_1;

class Myclass{
    int height;
    Myclass(){
        System.out.println("无参数构造函数");
        height = 4;
    }
    Myclass(int i){
        System.out.println("房子高度为" + i + "米");
        height = i;
    }
    void info(){
        System.out.println("房子高度为" + height + "米");
    }
    void info(String s){
        System.out.println(s + ": 房子高度为" + height + " 米");
    }
}
public class overLoading_1 {
    public static void main(String[] args){
        Myclass t = new Myclass(3);
        t.info();
        t.info("重载方法");
        new Myclass();
    }
}
