package runnoob.method;
//此迭代思路是将碟子分为2部分，最下面一个为一部分，其他排好顺序的为一部分。
//即将N个碟子简化为2个碟子的情况。然后依次简化。
//详细过程为1.将排好顺序的碟子都放到inter柱子上，2.将最下面的一个碟子放到to柱子上。
//3.将拍好顺序N-1的碟子放到最后to柱子上。
//那么如何得到排好顺序的N-1个碟子呢？
//将排好顺序的N-2个碟子放到inter柱子上循环即可。
public class hanno_3 {
    public static void main(String [] args) {
        //其中ABC为3个柱子
        //nDisk表示在A柱子中一共有nDisks个碟子，其中最上面的碟子序号为1，最下
        //面的碟子序号为nDisks。
        int nDisks = 2;
        doTowers(nDisks, 'A', 'B', 'C');
    }

    public static void doTowers(int topN,char from, char inter ,char to) {
        //此方法为迭代思路
        //topN表示在from柱子有几个碟子
        //当from柱子只有一个碟子时，直接把此碟子放到to柱子中
        if (topN == 1) {
            System.out.println("Disk 1 from " + from + " to " + to);
        } else {
            //将from柱子上的topN-1个碟子移动到inter
            doTowers(topN -1 , from ,to,inter);
            //此处printf语句表示动作，即将from柱子上的一个圆盘移动到to柱子上
            System.out.println("Disk " + topN + " from " + from + " to " + to);
            //将inter上的topN-1个碟子移动到to
            doTowers(topN -1 ,inter, from ,to);
        }

    }
}
