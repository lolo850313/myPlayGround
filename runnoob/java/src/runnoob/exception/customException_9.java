package runnoob.exception;

class WrongInputException extends Exception{
    WrongInputException(String s) {
        super(s);
    }
}

class Input {
    void method()throws Exception {
        throw new WrongInputException("Wrong input");
    }
}

class customException_9 {
    public static void main(String[] args) {
        try {
            new Input().method();
            //使用以下则不报错
        } catch (Exception wie) {
//        } catch (WrongInputException wie) {
            System.out.println(wie.getMessage());
        }
    }
}
