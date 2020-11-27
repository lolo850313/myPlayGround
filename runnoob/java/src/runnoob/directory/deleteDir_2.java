package runnoob.directory;

import java.io.File;

public class deleteDir_2 {
    public static void main(String[] args) {
        deleteDir(new File("dirTest"));
    }
    public static boolean deleteDir(File dir){
        if (dir.isDirectory()) {
            String[] children = dir.list();
            for (int i = 0; i < children.length; i++) {
                boolean success;
                success = deleteDir(new File(dir, children[i]));
                if (!success) {
                    return false;
                }
            }
        }
        if (dir.delete()) {
            System.out.println("目录已经被删除");
            return true;
        } else {
            System.out.println("目录删除失败");
            return false;
        }

    }
}
