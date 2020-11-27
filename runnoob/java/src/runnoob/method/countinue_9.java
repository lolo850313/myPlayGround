package runnoob.method;


public class countinue_9 {
    public static void main(String[] args) {
        StringBuffer searchstr = new StringBuffer("hello how are you.");
        int searchstr_length = searchstr.length();
        int count = 0;
        for (int i = 0; i <searchstr_length ; i++) {
            if (searchstr.charAt(i) != 'h') {
                //continue直接跳到下依次循环中，即不执行下面的2句操作
                continue;
            }
            count++;
            searchstr.setCharAt(i,'q');
//            //以上语句相当于下面的
//            if (searchstr.charAt(i) == 'h') {
//                count++;
//                searchstr.setCharAt(i,'q');
//            }

        }
        System.out.println("发现" + count +" 个h 字符");
        System.out.println(searchstr);

    }
}
