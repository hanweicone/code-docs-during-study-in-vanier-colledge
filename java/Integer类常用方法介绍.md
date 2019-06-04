# Integer类常用方法介绍

在实际程序使用中，程序界面上用户输入的数据都是以字符串类型进行存储的。而程序开发中，我们需要把字符串数据根据需求转换成指定的基本数据类型，如年龄需要转换成int类型，考试成绩需要转换成double类型等。那么，想实现字符串与基本数据之间转换应该怎么办呢？接下来我们就一起学习一下Java的包装类吧。

## 一.基本类型包装类概述

Java中提供了相应的对象来解决该问题，基本数据类型对象包装类：java将基础数据类型值封装成了对象。封装成对象有什么好处？当然是可以提供更多的操作基本数值的功能啦~

![](https://github.com/hanweicone/test1/blob/master/img/boxing.png)


其中需要注意int对应的是Integer,char对应的Character，其它6个都是基本类型首字母大写即可。基本数据类型的特点是用于在基本数据和字符串之间进行转换。我们主要研究的类就是其中一个，即Integer，因为其它的类的方法跟它几乎一致。要学会举一反三哟~


## 二.Integer类常用方法

### 1>.ParseInt(String s)方法（将基本类型转换成字符串。)

#### a>.用于将字符串转换成基本数据类型(int)，要求字符串必须是数字格式。

      public class ArrayListDemo {
         public static void main(String[] args) {
             String year = "2018";
             int i = Integer.parseInt(year);
             System.out.println(i/2);
         }
     }
     
     
     /*
     以上代码执行结果如下：
     1009
     */

#### b>.parseInt(String s,int radix)方法

　　将字符串s按照radix进行转换相应的进制数，然后运行的结果都是以十进制的形式打印。

      public class ArrayListDemo {
         public static void main(String[] args) {
             String year = "1110";
             String age = "A";
             //指定year的进制为2进制
             int i = Integer.parseInt(year,2);
             //指定age的进制为16进制
             int i2 = Integer.parseInt(age,16);    
             System.out.println(i);
             System.out.println(i2);
         }
     }
     
     /*
     以上代码执行结果如下：
     14
     10
     */

### 2>.基本数据类型int转换成字符串

#### a>.任何类型+"" 变成String类型(推荐使用)

      public class Demo1 {
         public static void main(String[] args) {
             int src = 3;
             String dest = src + "";
             System.out.println(dest+1);
         }
     }
     
     
     
     /*
     31
     */
    
#### b>.Integer类中的静态方法toString()转换成字符串

      public class Demo1 {
         public static void main(String[] args) {
             int src = 50;
             String dest = Integer.toString(src);
             System.out.println(dest+1);
         }
     }
     
     
     
     /*
     501
     */
    
#### c>.toString(int ,int 进制),将int整数转成指定的进制数

      public class Demo1 {
         public static void main(String[] args) {
             int src = 32;
             //将int整数转换成指定的进制数
             String dest = Integer.toString(src,2);    
             System.out.println(dest);
         }
     }
     
     
     
     /*
     100000
     */
    
 ### 3>.Integer的两个静态成员变量
 
      public class Demo1 {
         public static void main(String[] args) {
             int max = Integer.MAX_VALUE;
             int min = Integer.MIN_VALUE;
             System.out.println("int最大值是："+max);
             System.out.println("int最小值是："+min);
             
             //根据上面的估计你就会做出举一反三的动作，如下：
             System.out.println("Long最大值是："+Long.MAX_VALUE);
             System.out.println("Long最小值是："+Long.MIN_VALUE);
             System.out.println("Double最大值是："+Double.MAX_VALUE);
             System.out.println("Double最小值是："+Double.MIN_VALUE);
         }
     }
     
     
     
     /*
     以上代码执行结果如下：
     int最大值是：2147483647
     int最小值是：-2147483648
     Long最大值是：9223372036854775807
     Long最小值是：-9223372036854775808
     Double最大值是：1.7976931348623157E308
     Double最小值是：4.9E-324
     */
    
### 4>.十进制转成不同的进制，三个静态方法的返回值都是以字符串的形式返回

      public class Demo1 {
         public static void main(String[] args) {
             int src = 1000;
             String Binary = Integer.toBinaryString(src);
             String OctalNumberSystem = Integer.toOctalString(src);
             String Hexadecimal = Integer.toHexString(src);
             System.out.printf("%d的二进制是：%s,八进制是:%s,十六进制是：%s\n",src,Binary,OctalNumberSystem,Hexadecimal);
         }
     }
      
     /*
     以上代码执行结果如下：
     int最大值是：2147483647
     int最小值是：-2147483648
     Long最大值是：9223372036854775807
     Long最小值是：-9223372036854775808
     Double最大值是：1.7976931348623157E308
     Double最小值是：4.9E-324
     */
 
## 三.Interger类构造方法

常用的构造方法Integer(String s)是将数字格式的字符串，传递到Integer类的构造方法中，创建Integer对象，包装的是一个字符串。将构造方法中的字符串转成基本数据类型，调用非静态方法。

      public class Demo1 {
         public static void main(String[] args) {
             String s1 = new String("1000");
             Integer src = new Integer(s1);
             int dest = src.intValue();
             System.out.println(dest--);
             System.out.println(--dest);
         }
     }
    
     
     
     /*
     1000
     998
     */
    
## 四.自动装箱和自动拆箱

从JDK1.5后出现的特性，即自动拆箱和自动装箱。自动装箱就是将基本数据类型直接变成Integer包装类。自动拆箱和装箱动作相反，即将对象中的数据变回基本数据类型。自动拆箱和装箱的好处就是基本类型和引用类型可以直接运算，代码如下：

    
      public class Demo1 {
         public static void main(String[] args) {
             Integer src = 100; //这里就是自动装箱的过程，相当于Integer src = new Integer(100);
             
             int dest = src + 5; //我们知道src本身是引用数据类型，不能直接跟基本数据类型运算，首先它会自动进行拆箱操作，相当于：int dest = src.intValue() + 5 ;
             System.out.println(dest);
             
         }
     }
     
     
     
     /*
     以上代码执行结果如下：
     105
     */
    
当然，一个事物都具有两面性，虽然说自动拆箱和自动装箱可以减少代码的书写量，还可以直接跟引用数据类型进行运算，但是它也存在一个弊端，即可能出现空指针异常。

      public class Demo1 {
         public static void main(String[] args) {
             Integer src = null;     //任何引用数据类型都可以指向空
             src = src + 10;
             System.out.println(src);
         }
     }
     
     
     
     /*
     以上代码执行结果如下：
     Exception in thread "main" java.lang.NullPointerException
         at cn.org.yinzhengjie.demo.Demo1.main(Demo1.java:12)
     */
    
 

## 五.小试牛刀

      public class Demo1 {
         public static void main(String[] args) {
             Integer i = new Integer(100);
             Integer j = new Integer(100);
             System.out.println(i==j);            //false
             System.out.println(i.equals(j));    //true
             System.out.println("---------------");
             
             Integer a = 500;        //此时a进行了装箱操作
             Integer b = 500;        //此时b也进行了装箱操作，两个数值上是相等的，但是并不是同一个对象。
             System.out.println(a == b);            //false
             System.out.println(a.equals(b));    //true
             System.out.println("---------------");
             
             
             //数据在byte范围内，JVM不会重新new对象。(可以查看源码)
             Integer x = 127;
             Integer y = 127;
             System.out.println(x==y);            //true
             System.out.println(x.equals(y));    //true
             System.out.println("---------------");
         }
     }
     
     
     
     /*
     以上代码执行结果如下：
     false
     true
     ---------------
     false
     true
     ---------------
     true
     true
     ---------------
     */
    
