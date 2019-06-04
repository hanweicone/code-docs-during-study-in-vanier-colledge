# JAVA基础之对象的初始化
本文主要记录JAVA中对象的初始化过程，包括实例变量的初始化和类变量的初始化以及 final 关键字对初始化的影响。另外，还讨论了由于继承原因，探讨了引用变量的编译时类型和运行时类型

 

## 一，实例变量的初始化

一共有三种方式对实例变量进行初始化：

①定义实例变量时指定初始值

②非静态初始化块中对实例变量进行初始化

③构造器中对实例变量进行初始化

当new对象 初始化时，①②要先于③执行。而①②的顺序则按照它们在源代码中定义的顺序来执行。

当实例变量使用了final关键字修饰时，如果是在定义该final实例变量时直接指定初始值进行的初始化(第①种方式)，则：该变量的初始值在编译时就被确定下来，那么该final变量就类似于“宏变量”，相当于JAVA中的直接常量。

```java
 1 public class Test {
 2     public static void main(String[] args) {
 3         final String str1 = "HelloWorld";
 4         final String str2 = "Hello" + "World";
 5         System.out.println(str1 == str2);//true
 6         
 7         final String str3 = "Hello" + String.valueOf("World");
 8         System.out.println(str1 == str3);//false
 9     }
10 }
```
第8行输出false，是因为：第7行中str3需要通过valueOf方法调用之后才能确定。而不是在编译时确定。

 

再来看一个示例：

```java
 1 public class Test {
 2     
 3     final String str1 = "HelloWorld";
 4     final String str2 = "Hello" + "World";
 5     final String str3;
 6     final String str4;
 7     {
 8         str3 = "HelloWorld";
 9     }
10     {
11         System.out.println(str1 == str2);//true
12         System.out.println(str1 == str3);//true
13 //        System.out.println(str1 == str4);//compile error
14     }
15     public Test() {
16         str4 = "HelloWorld";
17         System.out.println(str1 == str4);//true
18     }
19     
20     public static void main(String[] args) {
21         new Test();
22     }
23 }
```
把第13行的注释去掉，会报编译错误“The blank final field str4 may not have been initialized”

因为变量str4是在构造器中进行初始化的。而前面提到：①定义实例变量时直接指定初始值(str1 和 str2的初始化)、 ②非静态初始化块中对实例变量进行初始化（str3的初始化）要先于 ③构造器中对实例变量进行初始化。

 

另外，对于final修饰的实例变量必须显示地对它进行初始化，而不是通过构造器(<clinit>)对之进行默认初始化。

```java
1 public class Test {
2     final String str1;//compile error---没有显示的使用①②③中的方式进行初始化
3     String str2;
4 }
```
str2可以通过构造器对之进行默认的初始化，初始化为null。而对于final修饰的变量 str1，必须显示地使用 上面提到的三种方式进行初始化。如下面的这个Test.java（一共有22行的这个Test类）

 

```java
 1 public class Test {
 2     final String str1 = "Hello";//定义实例变量时指定初始值
 3     
 4     final String str2;//非静态初始化块中对实例变量进行初始化
 5     final String str3;//构造器中对实例变量进行初始化
 6     
 7     {
 8         str2 = "Hello";
 9     }
10     public Test() {
11         str3 = "Hello";
12     }
13     
14     public void show(){
15         System.out.println(str1 + str1 == "HelloHello");//true
16         System.out.println(str2 + str2 == "HelloHello");//false
17         System.out.println(str3 + str3 == "HelloHello");//false
18     }
19     public static void main(String[] args) {
20         new Test().show();
21     }
22 }
```
由于str1采用的是第①种方式进行的初始化，故在执行15行: str1+str1 连接操作时，str1其实相当于“宏变量”

而str2 和 str3 并不是“宏变量”，故16-17行输出false

 

在非静态初始化代码块中初始化变量和在构造器中初始化变量的一点小区别：因为构造器是可以重写的，比如你把某个实例变量放在无参的构造器中进行初始化，但是在 new 对象时却调用的是有参数的构造器，那就得注意该实例变量有没有正确得到初始化了。

而放在非静态初始化代码块中初始化变量时，不管是调用 有参的构造器还是无参的构造器，非静态初始化代码块都会执行。

 

## 二，类变量的初始化

类变量一共有两个地方对之进行初始化：

❶定义类变量时指定初始值

❷静态初始化代码块中进行初始化

不管new多少个对象，类变量的初始化只执行一次。

 

## 三，继承对初始化的影响

主要是理解编译时类型和运行时类型的不同，从这个不同中可以看出 this 关键字 和 super 关键字的一些本质区别。

```java
 1 class Fruit{
 2     String color = "unknow";
 3     public  Fruit getThis(){
 4         return this;
 5     }
 6     public void info(){
 7         System.out.println("fruit's method");
 8     }
 9 }
10 
11 public class Apple extends Fruit{
12 
13     String color = "red";//与父类同名的实例变量
14     
15     @Override
16     public void info() {
17         System.out.println("apple's method");
18     }
19     
20     public void accessFruitInfo(){
21         super.info();
22     }
23     public Fruit getSuper(){
24         return super.getThis();
25     }
26     
27     //for  test purpose
28     public static void main(String[] args) {
29         Apple a = new Apple();
30         Fruit f = a.getSuper();
31         
32         //Fruit f2 = a.getThis();
33         //System.out.println(f == f2);//true
34         
35         System.out.println(a == f);//true
36         System.out.println(a.color);//red
37         System.out.println(f.color);//unknow
38         
39         a.info();//"apple's method"
40         f.info();//"apple's method"
41         
42         a.accessFruitInfo();//"fruit's method"
43     }
44 }
```
值得注意的地方有以下几个：

⒈ 第35行 引用变量 a 和 f 都指向内存中的同一个对象，36-37行调用它们的属性时，a.color是red，而f.color是unknow

因为，f变量的声明类型(编译时类型)为Fruit，当访问属性时是由声明该变量的类型来决定的。

⒉ 第39-40行，a.info() 和 f.info()都输出“apple's method”

因为，f 变量的运行时类型为Apple，info()是Apple重载的父类的一个方法。调用方法时由变量的运行时类型来决定。

⒊ 关于 this 关键字

当在29行new一个Apple对象，在30行调用 getSuper()方法时，最终是执行到第4行的 return this

this 的解释是：返回调用本方法的对象。它返回的类型是Fruit类型(见getThis方法的返回值类型)，但实际上是Apple对象导致的getThis方法的调用。故，这里的this的声明类型是Fruit，而运行时类型是Apple

⒋ 关于 super 关键字

super 与 this 是有区别的。this可以用来代表“当前对象”，可用 return 返回。而对于super而言，没有 return super;这样的语句。

super 主要是为了：在子类中访问父类中的属性 或者 在子类中 调用父类中的方法 而引入的一个关键字。比如第24行。

⒌ 在父类的构造器中不要去调用被子类覆盖的方法(Override)，或者说在构造父类对象时，不要依赖于子类覆盖了父类的那些方法。这样很可能会导致初始化的失败(没有正确地初始化对象)

因为：前面第1点和第2点谈到了，对象(变量 )有 声明时类型(编译时类型)和运行时类型。而方法的调用取决于运行时类型。

当new子类对象时，会首先去初始化父类的属性，而此时对象的运行时类型是子类，因此父类的属性的赋值若依赖于子类中重载的方法，会导致父类属性得不到正确的初始化值。示例如下：

```java
 1     class Fruit{
 2         String color;
 3         
 4         public Fruit() {
 5             color = this.getColor();//父类color属性初始化依赖于重载的方法getColor
 6 //            color = getColor();
 7         }
 8         public String getColor(){
 9             return "unkonw";
10         }
11         
12         @Override
13         public String toString() {
14             return color;
15         }
16     }
17     
18     public class Apple extends Fruit{
19     
20         @Override
21         public String getColor() {
22             return "color: " + color;
23         }
24         
25 //        public Apple() {
26 //            color = "red";
27 //        }
28         
29         public static void main(String[] args) {
30             System.out.println(new Apple());//color: null
31         }
32     }
```
Fruit类的color属性 没有正确地被初始化为"unknow"，而是为 null

主要是因为第5行 this.getColor()调用的是Apple类的getColor方法，而此时Apple类的color属性是直接从Fruit类继承的。

 

四，参考资料

《疯狂JAVA突破程序员基本功16课》第二章

《Effective Java》第二版第17条

 
