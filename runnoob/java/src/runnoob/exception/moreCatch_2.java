package runnoob.exception;


class Demo {
    int div(int a,int b)throws ArithmeticException,ArrayIndexOutOfBoundsException{
        int[] arr = new int[a];
        //制造第一出异常
        System.out.println(arr[4]);
        //制造第二处异常
        return a / b;
    }
}

class moreCatch_2{
    public static void main(String[] args) {
        Demo d = new Demo();
        try {
//            int x = d.div(4, 0);
            int x = d.div(5, 0);
//            int x = d.div(4, 1);
            System.out.println("x = " + x);;
        }catch (ArithmeticException e){
            System.out.println(e.toString());
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e.toString());
        }catch (Exception e)//父类，写在此处是为了捕捉其他没预料到的异常，只能
        //写在子类异常代码的后面，不过一般是不写的
        {
            System.out.println(e.toString());
        }
        System.out.println("Over");
    }
}
