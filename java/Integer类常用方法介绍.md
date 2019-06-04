# Integer类常用方法介绍


 
　　在实际程序使用中，程序界面上用户输入的数据都是以字符串类型进行存储的。而程序开发中，我们需要把字符串数据根据需求转换成指定的基本数据类型，如年龄需要转换成int类型，考试成绩需要转换成double类型等。那么，想实现字符串与基本数据之间转换应该怎么办呢？接下来我们就一起学习一下Java的包装类吧。

 

一.基本类型包装类概述

　Java中提供了相应的对象来解决该问题，基本数据类型对象包装类：java将基础数据类型值封装成了对象。封装成对象有什么好处？当然是可以提供更多的操作基本数值的功能啦~



　　其中需要注意int对应的是Integer,char对应的Character，其它6个都是基本类型首字母大写即可。基本数据类型的特点是用于在基本数据和字符串之间进行转换。我们主要研究的类就是其中一个，即Integer，因为其它的类的方法跟它几乎一致。要学会举一反三哟~

 

二.Integer类常用方法

1>.ParseInt(String s)方法（将基本类型转换成字符串。)

a>.用于将字符串转换成基本数据类型(int)，要求字符串必须是数字格式。

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class ArrayListDemo {
10     public static void main(String[] args) {
11         String year = "2018";
12         int i = Integer.parseInt(year);
13         System.out.println(i/2);
14     }
15 }
16 
17 
18 /*
19 以上代码执行结果如下：
20 1009
21 */
复制代码
b>.parseInt(String s,int radix)方法

　　将字符串s按照radix进行转换相应的进制数，然后运行的结果都是以十进制的形式打印。

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class ArrayListDemo {
10     public static void main(String[] args) {
11         String year = "1110";
12         String age = "A";
13         //指定year的进制为2进制
14         int i = Integer.parseInt(year,2);
15         //指定age的进制为16进制
16         int i2 = Integer.parseInt(age,16);    
17         System.out.println(i);
18         System.out.println(i2);
19     }
20 }
21 
22 /*
23 以上代码执行结果如下：
24 14
25 10
26 */
复制代码
2>.基本数据类型int转换成字符串

a>.任何类型+"" 变成String类型(推荐使用)

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         int src = 3;
12         String dest = src + "";
13         System.out.println(dest+1);
14     }
15 }
16 
17 
18 
19 /*
20 31
21 */
复制代码
b>.Integer类中的静态方法toString()转换成字符串

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         int src = 50;
12         String dest = Integer.toString(src);
13         System.out.println(dest+1);
14     }
15 }
16 
17 
18 
19 /*
20 501
21 */
复制代码
c>.toString(int ,int 进制),将int整数转成指定的进制数

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         int src = 32;
12         //将int整数转换成指定的进制数
13         String dest = Integer.toString(src,2);    
14         System.out.println(dest);
15     }
16 }
17 
18 
19 
20 /*
21 100000
22 */
复制代码
 3>.Integer的两个静态成员变量

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         int max = Integer.MAX_VALUE;
12         int min = Integer.MIN_VALUE;
13         System.out.println("int最大值是："+max);
14         System.out.println("int最小值是："+min);
15         
16         //根据上面的估计你就会做出举一反三的动作，如下：
17         System.out.println("Long最大值是："+Long.MAX_VALUE);
18         System.out.println("Long最小值是："+Long.MIN_VALUE);
19         System.out.println("Double最大值是："+Double.MAX_VALUE);
20         System.out.println("Double最小值是："+Double.MIN_VALUE);
21     }
22 }
23 
24 
25 
26 /*
27 以上代码执行结果如下：
28 int最大值是：2147483647
29 int最小值是：-2147483648
30 Long最大值是：9223372036854775807
31 Long最小值是：-9223372036854775808
32 Double最大值是：1.7976931348623157E308
33 Double最小值是：4.9E-324
34 */
复制代码
4>.十进制转成不同的进制，三个静态方法的返回值都是以字符串的形式返回

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         int src = 1000;
12         String Binary = Integer.toBinaryString(src);
13         String OctalNumberSystem = Integer.toOctalString(src);
14         String Hexadecimal = Integer.toHexString(src);
15         System.out.printf("%d的二进制是：%s,八进制是:%s,十六进制是：%s\n",src,Binary,OctalNumberSystem,Hexadecimal);
16     }
17 }
18 
19 
20 
21 /*
22 以上代码执行结果如下：
23 int最大值是：2147483647
24 int最小值是：-2147483648
25 Long最大值是：9223372036854775807
26 Long最小值是：-9223372036854775808
27 Double最大值是：1.7976931348623157E308
28 Double最小值是：4.9E-324
29 */
复制代码
 

三.Interger类构造方法

　　常用的构造方法Integer(String s)是将数字格式的字符串，传递到Integer类的构造方法中，创建Integer对象，包装的是一个字符串。将构造方法中的字符串转成基本数据类型，调用非静态方法。

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         String s1 = new String("1000");
12         Integer src = new Integer(s1);
13         int dest = src.intValue();
14         System.out.println(dest--);
15         System.out.println(--dest);
16     }
17 }
18 
19 
20 
21 /*
22 1000
23 998
24 */
复制代码
 

四.自动装箱和自动拆箱

　　从JDK1.5后出现的特性，即自动拆箱和自动装箱。自动装箱就是将基本数据类型直接变成Integer包装类。自动拆箱和装箱动作相反，即将对象中的数据变回基本数据类型。自动拆箱和装箱的好处就是基本类型和引用类型可以直接运算，代码如下：

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         Integer src = 100; //这里就是自动装箱的过程，相当于Integer src = new Integer(100);
12         
13         int dest = src + 5; //我们知道src本身是引用数据类型，不能直接跟基本数据类型运算，首先它会自动进行拆箱操作，相当于：int dest = src.intValue() + 5 ;
14         System.out.println(dest);
15         
16     }
17 }
18 
19 
20 
21 /*
22 以上代码执行结果如下：
23 105
24 */
复制代码
　　当然，一个事物都具有两面性，虽然说自动拆箱和自动装箱可以减少代码的书写量，还可以直接跟引用数据类型进行运算，但是它也存在一个弊端，即可能出现空指针异常。

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         Integer src = null;     //任何引用数据类型都可以指向空
12         src = src + 10;
13         System.out.println(src);
14     }
15 }
16 
17 
18 
19 /*
20 以上代码执行结果如下：
21 Exception in thread "main" java.lang.NullPointerException
22     at cn.org.yinzhengjie.demo.Demo1.main(Demo1.java:12)
23 */
复制代码
 

五.小试牛刀

复制代码
 1 /*
 2 @author :yinzhengjie
 3 Blog:http://www.cnblogs.com/yinzhengjie/tag/Java%E5%9F%BA%E7%A1%80/
 4 EMAIL:y1053419035@qq.com
 5 */
 6 
 7 package cn.org.yinzhengjie.demo;
 8 
 9 public class Demo1 {
10     public static void main(String[] args) {
11         Integer i = new Integer(100);
12         Integer j = new Integer(100);
13         System.out.println(i==j);            //false
14         System.out.println(i.equals(j));    //true
15         System.out.println("---------------");
16         
17         Integer a = 500;        //此时a进行了装箱操作
18         Integer b = 500;        //此时b也进行了装箱操作，两个数值上是相等的，但是并不是同一个对象。
19         System.out.println(a == b);            //false
20         System.out.println(a.equals(b));    //true
21         System.out.println("---------------");
22         
23         
24         //数据在byte范围内，JVM不会重新new对象。(可以查看源码)
25         Integer x = 127;
26         Integer y = 127;
27         System.out.println(x==y);            //true
28         System.out.println(x.equals(y));    //true
29         System.out.println("---------------");
30     }
31 }
32 
33 
34 
35 /*
36 以上代码执行结果如下：
37 false
38 true
39 ---------------
40 false
41 true
42 ---------------
43 true
44 true
45 ---------------
46 */
复制代码
