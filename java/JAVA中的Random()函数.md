# JAVA中的Random()函数

Java中存在着两种Random函数：

## 一、java.lang.Math.Random;

调用这个Math.Random()函数能够返回带正号的double值，该值大于等于0.0且小于1.0，即取值范围是[0.0,1.0)的左闭右开区间，返回值是一个伪随机选择的数，在该范围内（近似）均匀分布。例子如下：

    复制代码
    package IO;
    import java.util.Random;

    public class TestRandom {

        public static void main(String[] args) {
            // 案例1
            System.out.println("Math.random()=" + Math.random());// 结果是个double类型的值，区间为[0.0,1.0）
            int num = (int) (Math.random() * 3); // 注意不要写成(int)Math.random()*3，这个结果为0，因为先执行了强制转换
            System.out.println("num=" + num);
            /**
             * 输出结果为：
             * 
             * Math.random()=0.02909671613289655
             * num=0
             * 
             */
      }
    }
    复制代码
## 二、java.util.Random

下面Random()的两种构造方法：

Random()：创建一个新的随机数生成器。

Random(long seed)：使用单个 long 种子创建一个新的随机数生成器。

我们可以在构造Random对象的时候指定种子（这里指定种子有何作用，请接着往下看），如：Random r1 = new Random(20);

或者默认当前系统时间的毫秒数作为种子数:Random r1 = new Random();

需要说明的是：你在创建一个Random对象的时候可以给定任意一个合法的种子数，种子数只是随机算法的起源数字，和生成的随机数的区间没有任何关系。如下面的Java代码：

    Random rand =new Random(25);
    int i;
    i=rand.nextInt(100);
初始化时25并没有起直接作用（注意：不是没有起作用）,rand.nextInt(100);中的100是随机数的上限,产生的随机数为0-100的整数,不包括100。

具体用法如下例：

    复制代码
    package IO;

    import java.util.ArrayList;
    import java.util.Random;

    public class TestRandom {

        public static void main(String[] args) {

            // 案例2
            // 对于种子相同的Random对象，生成的随机数序列是一样的。
            Random ran1 = new Random(10);
            System.out.println("使用种子为10的Random对象生成[0,10)内随机整数序列: ");
            for (int i = 0; i < 10; i++) {
                System.out.print(ran1.nextInt(10) + " ");
            }
            System.out.println();
            Random ran2 = new Random(10);
            System.out.println("使用另一个种子为10的Random对象生成[0,10)内随机整数序列: ");
            for (int i = 0; i < 10; i++) {
                System.out.print(ran2.nextInt(10) + " ");
            }
            /**
             * 输出结果为：
             * 
             * 使用种子为10的Random对象生成[0,10)内随机整数序列: 
             * 3 0 3 0 6 6 7 8 1 4 
             * 使用另一个种子为10的Random对象生成[0,10)内随机整数序列: 
             * 3 0 3 0 6 6 7 8 1 4 
             * 
             */

            // 案例3
            // 在没带参数构造函数生成的Random对象的种子缺省是当前系统时间的毫秒数。
            Random r3 = new Random();
            System.out.println();
            System.out.println("使用种子缺省是当前系统时间的毫秒数的Random对象生成[0,10)内随机整数序列");
            for (int i = 0; i < 10; i++) {
                System.out.print(r3.nextInt(10)+" ");
            }
            /**
             * 输出结果为：
             * 
             * 使用种子缺省是当前系统时间的毫秒数的Random对象生成[0,10)内随机整数序列
             * 1 1 0 4 4 2 3 8 8 4
             *  
             */

            // 另外，直接使用Random无法避免生成重复的数字，如果需要生成不重复的随机数序列，需要借助数组和集合类
            ArrayList list=new TestRandom().getDiffNO(10);
            System.out.println();
            System.out.println("产生的n个不同的随机数："+list);
        }

        /**
         * 生成n个不同的随机数，且随机数区间为[0,10)
         * @param n
         * @return
         */
        public ArrayList getDiffNO(int n){
            // 生成 [0-n) 个不重复的随机数
            // list 用来保存这些随机数
            ArrayList list = new ArrayList();
            Random rand = new Random();
            boolean[] bool = new boolean[n];
            int num = 0;
            for (int i = 0; i < n; i++) {
                do {
                    // 如果产生的数相同继续循环
                    num = rand.nextInt(n);
                } while (bool[num]);
                bool[num] = true;
                list.add(num);
            }
            return list;
        }


    }
    复制代码
备注：下面是Java.util.Random()方法摘要：

protected int next(int bits)：生成下一个伪随机数。
boolean nextBoolean()：返回下一个伪随机数，它是取自此随机数生成器序列的均匀分布的boolean值。
void nextBytes(byte[] bytes)：生成随机字节并将其置于用户提供的 byte 数组中。
double nextDouble()：返回下一个伪随机数，它是取自此随机数生成器序列的、在0.0和1.0之间均匀分布的 double值。
float nextFloat()：返回下一个伪随机数，它是取自此随机数生成器序列的、在0.0和1.0之间均匀分布float值。
double nextGaussian()：返回下一个伪随机数，它是取自此随机数生成器序列的、呈高斯（“正态”）分布的double值，其平均值是0.0标准差是1.0。
int nextInt()：返回下一个伪随机数，它是此随机数生成器的序列中均匀分布的 int 值。
int nextInt(int n)：返回一个伪随机数，它是取自此随机数生成器序列的、在（包括和指定值（不包括）之间均匀分布的int值。
long nextLong()：返回下一个伪随机数，它是取自此随机数生成器序列的均匀分布的 long 值。
void setSeed(long seed)：使用单个 long 种子设置此随机数生成器的种子。
下面给几个例子：

    生成[0,1.0)区间的小数：double d1 = r.nextDouble();
    生成[0,5.0)区间的小数：double d2 = r.nextDouble() * 5;
    生成[1,2.5)区间的小数：double d3 = r.nextDouble() * 1.5 + 1;
    生成-231到231-1之间的整数：int n = r.nextInt();
    生成[0,10)区间的整数：
        int n2 = r.nextInt(10);//方法一

        n2 = Math.abs(r.nextInt() % 10);//方法二

 

参考资料：

http://blog.sina.com.cn/s/blog_93dc666c0101h3gd.html

http://blog.csdn.net/wpjava/article/details/6004492

