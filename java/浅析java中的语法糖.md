

# [浅析java中的语法糖](https://www.cnblogs.com/qingshanli/p/9375040.html)



**目录**

*   [概述](#_label0)
*   [字符串拼接](#_label1)
*   [条件编译](#_label2)
*   [断言](#_label3)
*   [枚举与Switch语句](#_label4)
*   [字符串与Switch语句](#_label5)
*   [可变参数](#_label6)
*   [自动装箱/拆箱](#_label7)
*   [枚举](#_label8)
*   [内部类](#_label9)
*   [泛型擦除](#_label10)
*   [增强for循环](#_label11)
*   [lambda表达式](#_label12)
*   [try-with-resources语句](#_label13)
*   [JDK10的局部变量类型推断](#_label14)
*   [源代码](#_label15)
*   [参数资料](#_label16)





## **<span style="font-size: 18px;">概述</span>**

编译器是一种计算机程序, 它主要的目的是将便于人编写、阅读、维护的高级计算机语言所写的源代码程序, 翻译为计算机能解读、运行的低阶机器语言的程序, 即可执行文件。而 javac 就是java语言中的编译器, 它用于将 .java 文件转换成JVM能识别的 .class 字节码文件, 反编译则是将 .class 文件转换成 .java 文件。

语法糖（Syntactic sugar），也译为糖衣语法，是由英国计算机科学家彼得·兰丁发明的一个术语，指计算机语言中添加的某种语法，这种语法对语言的功能没有影响，但是更方便程序员使用。语法糖让程序更加简洁，有更高的可读性。

java中的语法糖只存在于编译期, 在编译器将 .java 源文件编译成 .class 字节码时, 会进行解语法糖操作, 还原最原始的基础语法结构。这些语法糖包含条件编译、断言、Switch语句与枚举及字符串结合、可变参数、自动装箱/拆箱、枚举、内部类、泛型擦除、增强for循环、lambda表达式、try-with-resources语句、JDK10的局部变量类型推断等等。

关于反编译工具, 其实在JDK中自带了一个javap命令, 在以前的文章[JDK的命令行工具系列 (二) javap、jinfo、jmap](https://www.cnblogs.com/qingshanli/p/9315649.html)中也有提及到, 但是日常中很少会用到javap, 所以这次我们借助另一个[反编译工具 CFR](http://www.benf.org/other/cfr/) 来分析java中的语法糖, 这里我下载的是最新的<span style="color: #ff6600;">cfr_0_132.jar</span>。

<div style="text-align: right"><a name="_label1"></a></div>

## **<span style="font-size: 18px;">字符串拼接</span>**

```java
/**
 * 字符串拼接
 * option: --stringbuilder false
 */
public void stringBuilderTest(int end) {
    char[] foo = new char[]{'@', 'a', '*'};
    char ch;
    int x = 0;
    while ((ch = foo[++x]) != '*') {
        System.out.println("" + x + ": " + ch);
    }
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --stringbuilder false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803120016044-486497178.png)从反编译后的代码中能看出, 当我们使用+号进行字符串拼接操作时, 编译时会自动创建一个<span style="color: #ff6600;">StringBuilder</span>对象。所以当在循环中拼接字符串时, 应避免使用+号操作, 否则每次循环都会创建一个<span style="color: #ff6600;">StringBuilder</span>对象再回收, 造成较大的开销。

<div style="text-align: right"><a name="_label2"></a></div>

## **<span style="font-size: 18px;">条件编译</span>**

```java
/**
 * 条件编译
 * option: 不需要参数
 */
public void ifCompilerTest() {
    if(false) {
        System.out.println("false if");
    }else {
        System.out.println("true else");
    }
}

```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803142423489-682039451.png)

很明显, javac编译器在编译时期的解语法糖阶段, 会将条件分支不成立的代码进行消除。

<div style="text-align: right"><a name="_label3"></a></div>

## 断言

```java
/**
 * 断言, JDK1.4开始支持
 * option: --sugarasserts false
 */
public void assertTest(String s) {
    assert (!s.equals("Fred"));
    System.out.println(s);
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --sugarasserts false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803145913175-818304986.png)

如上, 当断言结果为true时, 程序继续正常执行, 当断言结果为false时, 则抛出AssertionError异常来打断程序的执行。



## **<span style="font-size: 18px;">枚举与Switch语句</span>**


    public int switchEnumTest(EnumTest e) {
        switch (e) {
            case FOO:
                return 1;
            case BAP:
                return 2;
        }
        return 0;
    }


    public enum EnumTest {
        FOO,
        BAR,
        BAP
    }


命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --decodeenumswitch false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803143426977-947258293.png)

switch支持枚举是通过调用枚举类默认继承的父类Enum中的<span style="color: #ff6600;">ordinal()</span>方法来实现的, 这个方法会返回枚举常量的序数。由于笔者的经验尚浅, 具体的实现细节还不是很清楚(比如枚举常量FOO的序数是0, 而case FOO语句编译后的 case 1, 这个1是什么? 另外switchEnumTest()方法传入一个FOO, 调用ordinal()方法得到的序数为0, 那么他又是如何与case 1进行匹配的呢?), 欢迎读者在留言区一起讨论。

<div style="text-align: right"><a name="_label5"></a></div>

## <span style="font-size: 18px;">**字符串与Switch语句**</span>

```java
/** 
 * 字符串与Switch语句
 * option: --decodestringswitch false
 */
public int switchStringTest(String s) {
    switch (s) {
        default:
            System.out.println("Test");
            break;
        case "BB":  // BB and Aa have the same hashcode.
            return 12;
        case "Aa":
        case "FRED":
            return 13;
    }
    System.out.println("Here");
    return 0;
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --decodestringswitch false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803143605821-951143227.png)

switch支持字符串是通过<span style="color: #ff6600;">hashCode()</span>和<span style="color: #ff6600;">equals()</span>方法来实现的, 先通过<span style="color: #ff6600;">hashCode()</span>返回的哈希值进行switch, 然后通过<span style="color: #ff6600;">equals()</span>方法比较进行安全检查, 调用<span style="color: #ff6600;">equals()</span>是为了防止可能发生的哈希碰撞。

另外switch还支持<span style="color: #ff6600;">byte</span>、<span style="color: #ff6600;">short</span>、<span style="color: #ff6600;">int</span>、<span style="color: #ff6600;">char</span>这几种基本数据类型, 其中支持<span style="color: #ff6600;">char</span>类型是通过比较它们的ascii码(ascii码是整型)来实现的。所以switch其实只支持一种数据类型, 也就是整型, 其他诸如String、枚举类型都是转换成整型之后再使用switch的。

<div style="text-align: right"><a name="_label6"></a></div>

## <span style="font-size: 18px;">**可变参数**</span>

```java
/**
 * 可变参数
 * option: --arrayiter false
 */
public void varargsTest(String ... arr) {
    for (String s : arr) {
        System.out.println(s);
    }
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --arrayiter false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803143827363-1860208236.png)

可变参数其实就是一个不定长度的数组, 数组长度随传入方法的对应参数个数来决定。可变参数只能在参数列表的末位使用。

<div style="text-align: right"><a name="_label7"></a></div>

## <span style="font-size: 18px;">**自动装箱/拆箱**</span>

```java
/**
 * 自动装箱/拆箱
 * option: --sugarboxing false
 */
public Double autoBoxingTest(Integer i, Double d) {
    return d + i;
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --sugarboxing false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803144041276-2054980101.png)

首先我们知道, 基本类型与包装类型在某些操作符的作用下, 包装类型调用`valueOf()`方法的过程叫做装箱, 调用`xxxValue()方法`的过程叫做拆箱。所以上面的结果很容易看出, 先对两个包装类进行拆箱, 再对运算结果进行装箱。

<div style="text-align: right"><a name="_label8"></a></div>

## <span style="font-size: 18px;">**枚举**</span>

```java
/**
 * 枚举, JDK1.5开始支持
 * option: --sugarenums false
 */
public enum EnumTest {
    FOO,
    BAR,
    BAP
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --sugarenums false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803144547865-634089140.png)

当我们自定义一个枚举类型时, 编译器会自动创建一个被final修饰的枚举类来继承<span style="color: #ff6600;">Enum</span>, 所以自定义枚举类型是无法继承和被继承的。当枚举类初始化时, 枚举字段引用该枚举类的一个静态常量对象, 并且所有的枚举字段都用常量数组<span style="color: #ff6600;">$VALUES</span>来存储。<span style="color: #ff6600;">values()</span>方法内则调用Object的<span style="color: #ff6600;">clone()</span>方法, 参照<span style="color: #ff6600;">$VALUES</span>数组对象复制一个新的数组, 新数组会有所有的枚举字段。

<div style="text-align: right"><a name="_label9"></a></div>

## <span style="font-size: 18px;">**内部类**</span>

```java
import java.util.*;
import java.io.*;

public class CFRDecompilerDemo {

    int x = 3;

    /**
     * 内部类
     * option: --removeinnerclasssynthetics false
     */
    public void innerClassTest() {
        new InnerClass().getSum(6);
    }

    public class InnerClass {
        public int getSum(int y) {
            x += y;
            return x;
        }
    }    
}
```
命令行:<span style="color: #ff6600;"> java -jar cfr_0_132.jar CFRDecompilerDemo.class --removeinnerclasssynthetics false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803150827020-401588426.png)

首先我们要明确, 上述innerClassTest()方法中的<span style="color: #ff6600;">this</span>是外部类当前对象的引用, 而InnerClass类中的<span style="color: #ff6600;">this</span>则是内部类当前对象的引用。编译过程中, 编译器会自动在内部类定义一个外部类的常量引用<span style="color: #ff6600;">this$0</span>, 并且在内部类的构造器中初始化<span style="color: #ff6600;">this$0</span>, 当外部类访问内部类时, 会把当前外部类的对象引用<span style="color: #ff6600;">this</span>传给内部类的构造器用于初始化, 这样内部类就能通过所持有的外部类的对象引用, 来访问外部类的所有公有及私有成员。

<div style="text-align: right"><a name="_label10"></a></div>

## <span style="font-size: 18px;">**泛型擦除**</span>

```java
/**
 * 泛型擦除
 * option: 
 */
public void genericEraseTest() {
    List<String> list =  new ArrayList<String>();
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803145253168-1402875032.png)

在JVM中没有泛型这一概念,  只有普通方法和普通类, 所有泛型类的泛型参数都会在编译时期被擦除, 所以泛型类并没有自己独有的Class类对象比如List<Integer>.class, 而只有<span style="color: #ff6600;">List.class</span>对象。

<div style="text-align: right"><a name="_label11"></a></div>

## **<span style="font-size: 18px;">增强for循环</span>**

```java
/**
 * 增强for循环
 * option: --collectioniter false
 */
public void forLoopTest() {
    String[] qingshanli = {"haha", "qingshan", "helloworld", "ceshi"};  
    List<String> list =  Arrays.asList(qingshanli);
    for (Object s : list) {
        System.out.println(s);
    }
}
```
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --collectioniter false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803151155842-1294559378.png)

很明显, 增强for循环的底层其实还是通过迭代器来实现的, 这也就解释了为什么增强for循环中不能进行增删改操作。

<div style="text-align: right"><a name="_label12"></a></div>

## <span style="font-size: 18px;">**lambda表达式**</span>

```java
/**
 * lambda表达式
 * option: --decodelambdas false
 */
public void lambdaTest() {
    String[] qingshanli = {"haha", "qingshan", "helloworld", "ceshi"};  
    List<String> list =  Arrays.asList(qingshanli);
    // 使用lambda表达式以及函数操作
    list.forEach((str) -> System.out.print(str + "; "));
    // 在JDK8中使用双冒号操作符
    list.forEach(System.out::println);  
}
```
命令行:<span style="color: #ff6600;"> java -jar cfr_0_132.jar CFRDecompilerDemo.class --decodelambdas false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803160951039-1629659950.png)

这里笔者经验尚浅, 关于lambda表达式的实现原理暂不做阐述, 以免误人子弟, 欢迎有兴趣的读者在留言区一起讨论。

<div style="text-align: right"><a name="_label13"></a></div>

## <span style="font-size: 18px;">**try-with-resources语句**</span>

```java
/**
 * try-with-resources语句
 * option: --tryresources false
 */
public void tryWithResourcesTest() throws IOException {
    try (final StringWriter writer = new StringWriter();
         final StringWriter writer2 = new StringWriter()) {
        writer.write("This is qingshanli1");
        writer2.write("this is qingshanli2");
    }
}
```
命令行:<span style="color: #ff6600;"> java -jar cfr_0_132.jar CFRDecompilerDemo.class --tryresources false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803152324539-1851079267.png)

在JDK7之前, 如IO流、数据库连接等资源用完后, 都是通过finally代码块来释放资源。而try-with-resources语法糖则帮我们省去了释放资源这一操作, 编译器在解语法糖阶段时会将它还原成原始的语法结构。

<div style="text-align: right"><a name="_label14"></a></div>

## <span style="font-size: 18px;">**JDK10的局部变量类型推断**</span>

```java
/**
 * 局部变量类型推断, JDK10开始支持
 * option: 不需要参数
 */
public void varTest() {
    //初始化局部变量  
    var string = "qingshanli";
    //初始化局部变量  
    var stringList = new ArrayList<String>();
    stringList.add("九幽阴灵，诸天神魔，以我血躯，奉为牺牲。");
    stringList.add("三生七世，永堕阎罗，只为情故，虽死不悔！");
    stringList.add("blog:http://www.cnblogs.com/qingshanli/");
    //增强for循环的索引
    for (var s : stringList){
        System.out.println(s);
    }
    //传统for循环的局部变量定义
    for (var i = 0; i < stringList.size(); i++){
        System.out.println(stringList.get(i));
    }
}
```
JDK10环境下编译:<span style="color: #ff6600;"> /home/qingshanli/Downloads/jdk-10.0.2/bin/javac CFRDecompilerDemo.java</span>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --collectioniter false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803153228437-1297024872.png)

可以看出, 局部变量类型推断其实也是一个语法糖。在编译过程的解语法糖阶段, 会使用变量真正的类型来替代var类型。所以java由始至终是一种强类型语言, java中的var和弱类型语言JavaScript中的var是完全不一样的, 例如下图 <span style="color: #ff6600;">var i = "10" - 6</span> 这样的语法运算在JavaScript中可以的, 而在Java语言中则不被允许。

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180804004353391-1540412177.png)

另外目前已知的允许使用var声明变量的几个场景有初始化局部变量、增强for循环的索引、传统for循环的局部变量定义。而诸如方法的形参、构造器的形参、方法的返回值类型、对象的成员变量、只进行定义而不初始化的变量等则不支持这种用法。对于后面的几种不支持, 我的猜想是因为它们会被外部访问而导致充满了不确定性, 举个栗子, 比如对象的成员变量X, 被对象A访问并赋值ArrayList类型, 被对象B访问并赋值HashMap类型, 那么问题来了, 对象A和对象B都是同一个类的实例, 这就产生了冲突, 此时虚拟机又如何区分这个对象的成员变量X到底是什么类型呢? 

<div style="text-align: right"><a name="_label15"></a></div>

## <span style="font-size: 18px;">**源代码**</span>

```java
import java.util.*;
import java.io.*;

public class CFRDecompilerDemo {

    int x = 3;

    /**
     * 字符串拼接
     * option: --stringbuilder false
     */
    public void stringBuilderTest(int end) {
        char[] foo = new char[]{'@', 'a', '*'};
        char ch;
        int x = 0;
        while ((ch = foo[++x]) != '*') {
            System.out.println("" + x + ": " + ch);
        }
    }
    
    /**
     * 条件编译
     * option: 不需要参数
     */
    public void ifCompilerTest() {
        if(false) {
            System.out.println("false if");
        }else {
            System.out.println("true else");
        }
    }
    
    /**
     * 断言, JDK1.4开始支持
     * option: --sugarasserts false
     */
    public void assertTest(String s) {
        assert (!s.equals("Fred"));
        System.out.println(s);
    }
    
    /**
     * 枚举与Switch语句
     * option: --decodeenumswitch false
     */
    public int switchEnumTest(EnumTest e) {
        switch (e) {
            case FOO:
                return 1;
            case BAP:
                return 2;
        }
        return 0;
    }
    
    /** 
     * 字符串与Switch语句
     * option: --decodestringswitch false
     */
   public int switchStringTest(String s) {
        switch (s) {
            default:
                System.out.println("Test");
                break;
            case "BB":  // BB and Aa have the same hashcode.
                return 12;
            case "Aa":
            case "FRED":
                return 13;
        }
        System.out.println("Here");
        return 0;
    }
    
    /**
     * 可变参数
     * option: --arrayiter false
     */
    public void varargsTest(String ... arr) {
        for (String s : arr) {
            System.out.println(s);
        }
    }
    
    /**
     * 自动装箱/拆箱
     * option: --sugarboxing false
     */
    public Double autoBoxingTest(Integer i, Double d) {
        return d + i;
    }
    
    /**
     * 枚举, JDK1.5开始支持
     * option: --sugarenums false
     */
    public enum EnumTest {
        FOO,
        BAR,
        BAP
    }
    
    /**
     * 内部类
     * option: --removeinnerclasssynthetics false
     */
    public void innerClassTest() {
        new InnerClass().getSum(6);
    }
    
    public class InnerClass {
        public int getSum(int y) {
            x += y;
            return x;
        }
    }
    
    /**
     * 泛型擦除
     * option: 
     */
    public void genericEraseTest() {
        List<String> list =  new ArrayList<String>();
    }
    
    /**
     * 增强for循环
     * option: --collectioniter false
     */
    public void forLoopTest() {
        String[] qingshanli = {"haha", "qingshan", "helloworld", "ceshi"};  
        List<String> list =  Arrays.asList(qingshanli);
        for (Object s : list) {
            System.out.println(s);
        }
    }
    
    /**
     * lambda表达式
     * option: --decodelambdas false
     */
    public void lambdaTest() {
        String[] qingshanli = {"haha", "qingshan", "helloworld", "ceshi"};  
        List<String> list =  Arrays.asList(qingshanli);
        // 使用lambda表达式以及函数操作
        list.forEach((str) -> System.out.print(str + "; "));
        // 在JDK8中使用双冒号操作符
        list.forEach(System.out::println);  
    }
    
    /**
     * try-with-resources语句
     * option: --tryresources false
     */
    public void tryWithResourcesTest() throws IOException {
        try (final StringWriter writer = new StringWriter();
             final StringWriter writer2 = new StringWriter()) {
            writer.write("This is qingshanli1");
            writer2.write("this is qingshanli2");
        }
    }
    
    /**
     * 局部变量类型推断, JDK10开始支持
     * option: 不需要参数
     */
    public void varTest() {
        //初始化局部变量  
        var string = "qingshanli";
        //初始化局部变量  
        var stringList = new ArrayList<String>();
        stringList.add("九幽阴灵，诸天神魔，以我血躯，奉为牺牲。");
        stringList.add("三生七世，永堕阎罗，只为情故，虽死不悔！");
        stringList.add("blog:http://www.cnblogs.com/qingshanli/");
        //增强for循环的索引
        for (var s : stringList){
            System.out.println(s);
        }
        //传统for循环的局部变量定义
        for (var i = 0; i < stringList.size(); i++){
            System.out.println(stringList.get(i));
        }
    }
}
```

## <span style="font-size: 18px;">**参数资料**</span>

[Java的编译原理](https://www.cnblogs.com/qingshanli/p/9281760.html)

[Java代码的编译与反编译那些事儿-HollisChuang's Blog](http://www.hollischuang.com/archives/58 "Java代码的编译与反编译那些事儿-HollisChuang's Blog")

[我反编译了Java 10的本地变量类型推断-HollisChuang's Blog](http://www.hollischuang.com/archives/2187 "我反编译了Java 10的本地变量类型推断-HollisChuang's Blog")

[Java中的Switch对整型、字符型、字符串型的具体实现细节-HollisChuang's Blo...](http://www.hollischuang.com/archives/61 "Java中的Switch对整型、字符型、字符串型的具体实现细节-HollisChuang's Blo...")

[一些防止java代码被反编译的方法](https://blog.csdn.net/qq_35038153/article/details/78054085)



