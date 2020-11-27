package runnoob.exception;


class reload_7 {
    double method(int i) throws Exception{
        return i / 0;
    }
    boolean method(boolean b){
        return !b;
    }
    static double method(int x, double y)throws Exception{
        return x + y;
    }
    static double method(double x, double y){
        return x + y - 3;
    }
    public static void main(String[] args){
        reload_7 mn = new reload_7();
        try {
            System.out.println(method(10, 20.0));
            System.out.println(method(10.0, 20));
            System.out.println(method(10.0, 20.0));
            //静态方法不需要加类名
            //reload_7类中未被使用的方法则会是灰色，使用过的会被高亮。
//            System.out.println(mn.method(true));
            System.out.println(mn.method(10));
        } catch (Exception ex) {
            System.out.println("exception occure:" + ex);
        }
    }
}
