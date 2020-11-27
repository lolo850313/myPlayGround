package runnoob.directory;

import java.io.File;

public class curDir_14 {
    public static void main(String[] args) throws Exception {
        //user.dir是个特定参数，此处不需要输入任何路径
        String curDir = System.getProperty("user.dir");
        System.out.println("你当前的工作目录为：" + curDir);
    }
}