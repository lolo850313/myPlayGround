package runnoob.algorithm;


import java.util.Collections;
import java.util.LinkedList;
import java.util.Vector;

public class addAndSetOfLinkedList_13 {
    public static void main(String[] args) {
        LinkedList officers = new LinkedList();
        officers.add("B");
        officers.add("B");
        officers.add("T");
        officers.add("H");
        officers.add("P");
        System.out.println(officers);
        officers.set(2, "M");
        System.out.println(officers);
    }
}
