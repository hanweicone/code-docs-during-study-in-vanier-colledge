<div id="mainContent">

<div class="forFlow">

<div id="post_detail">

<div id="topics">

<div class="post">

# [浅析java中的语法糖](https://www.cnblogs.com/qingshanli/p/9375040.html)

<div class="postBody">

<div id="cnblogs_post_body" class="blogpost-body"><a name="_labelTop"></a>

<div id="navCategory">

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

</div>

<div style="text-align: right"><a name="_label0"></a></div>

## **<span style="font-size: 18px;">概述</span>**

编译器是一种计算机程序, 它主要的目的是将便于人编写、阅读、维护的高级计算机语言所写的源代码程序, 翻译为计算机能解读、运行的低阶机器语言的程序, 即可执行文件。而 javac 就是java语言中的编译器, 它用于将 .java 文件转换成JVM能识别的 .class 字节码文件, 反编译则是将 .class 文件转换成 .java 文件。

语法糖（Syntactic sugar），也译为糖衣语法，是由英国计算机科学家彼得·兰丁发明的一个术语，指计算机语言中添加的某种语法，这种语法对语言的功能没有影响，但是更方便程序员使用。语法糖让程序更加简洁，有更高的可读性。

java中的语法糖只存在于编译期, 在编译器将 .java 源文件编译成 .class 字节码时, 会进行解语法糖操作, 还原最原始的基础语法结构。这些语法糖包含条件编译、断言、Switch语句与枚举及字符串结合、可变参数、自动装箱/拆箱、枚举、内部类、泛型擦除、增强for循环、lambda表达式、try-with-resources语句、JDK10的局部变量类型推断等等。

关于反编译工具, 其实在JDK中自带了一个javap命令, 在以前的文章[JDK的命令行工具系列 (二) javap、jinfo、jmap](https://www.cnblogs.com/qingshanli/p/9315649.html)中也有提及到, 但是日常中很少会用到javap, 所以这次我们借助另一个[反编译工具 CFR](http://www.benf.org/other/cfr/) 来分析java中的语法糖, 这里我下载的是最新的<span style="color: #ff6600;">cfr_0_132.jar</span>。

<div style="text-align: right"><a name="_label1"></a></div>

## **<span style="font-size: 18px;">字符串拼接</span>**


命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --stringbuilder false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803120016044-486497178.png)从反编译后的代码中能看出, 当我们使用+号进行字符串拼接操作时, 编译时会自动创建一个<span style="color: #ff6600;">StringBuilder</span>对象。所以当在循环中拼接字符串时, 应避免使用+号操作, 否则每次循环都会创建一个<span style="color: #ff6600;">StringBuilder</span>对象再回收, 造成较大的开销。

<div style="text-align: right"><a name="_label2"></a></div>

## **<span style="font-size: 18px;">条件编译</span>**

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 条件编译
 * option: 不需要参数</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">ifCompilerTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">if</span></span><span class="pun">(</span><span style="color: #0000ff;"><span class="kwd">false</span></span><span style="color: #000000;"><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"false if"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span></span><span style="color: #0000ff;"><span class="kwd">else</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"true else"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

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
命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803142423489-682039451.png)

很明显, javac编译器在编译时期的解语法糖阶段, 会将条件分支不成立的代码进行消除。

<div style="text-align: right"><a name="_label3"></a></div>

## <span style="font-size: 18px;">**断言**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 断言, JDK1.4开始支持
 * option: --sugarasserts false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">assertTest</span><span class="pun">(</span><span class="typ">String</span> <span class="pln">s</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">assert</span></span> <span class="pln"></span> <span class="pun">(!</span><span class="pln">s</span><span class="pun">.</span><span class="pln">equals</span><span class="pun">(</span><span class="str">"Fred"</span><span style="color: #000000;"><span class="pun">));</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --sugarasserts false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803145913175-818304986.png)

如上, 当断言结果为true时, 程序继续正常执行, 当断言结果为false时, 则抛出AssertionError异常来打断程序的执行。

<div style="text-align: right"><a name="_label4"></a></div>

## <span style="font-size: 18px;">**枚举与Switch语句**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 枚举与Switch语句
 * option: --decodeenumswitch false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">int</span></span><span style="color: #000000;"> <span class="pln">switchEnumTest</span><span class="pun">(</span><span class="typ">EnumTest</span> <span class="pln">e</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">switch</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="pln">e</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span><span style="color: #000000;"> <span class="pln">FOO</span><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">1</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span><span style="color: #000000;"> <span class="pln">BAP</span><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">2</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">0</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 枚举, JDK1.5开始支持
 * option: --sugarenums false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">enum</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">EnumTest</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln">FOO</span><span class="pun">,</span> <span class="pln">BAR</span><span class="pun">,</span> <span class="pln">BAP</span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --decodeenumswitch false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803143426977-947258293.png)

switch支持枚举是通过调用枚举类默认继承的父类Enum中的<span style="color: #ff6600;">ordinal()</span>方法来实现的, 这个方法会返回枚举常量的序数。由于笔者的经验尚浅, 具体的实现细节还不是很清楚(比如枚举常量FOO的序数是0, 而case FOO语句编译后的 case 1, 这个1是什么? 另外switchEnumTest()方法传入一个FOO, 调用ordinal()方法得到的序数为0, 那么他又是如何与case 1进行匹配的呢?), 欢迎读者在留言区一起讨论。

<div style="text-align: right"><a name="_label5"></a></div>

## <span style="font-size: 18px;">**字符串与Switch语句**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 字符串与Switch语句
 * option: --decodestringswitch false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">int</span></span><span style="color: #000000;"> <span class="pln">switchStringTest</span><span class="pun">(</span><span class="typ">String</span> <span class="pln">s</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">switch</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="pln">s</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">default</span></span><span style="color: #000000;"><span class="pun">:</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"Test"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">break</span></span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span> <span class="pln"></span> <span class="str">"BB"</span><span class="pun">:</span> <span class="pln"></span> <span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"> <span class="com">BB and Aa have the same hashcode.</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">12</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span> <span class="pln"></span> <span class="str">"Aa"</span><span style="color: #000000;"><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span> <span class="pln"></span> <span class="str">"FRED"</span><span style="color: #000000;"><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">13</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"Here"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">0</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --decodestringswitch false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803143605821-951143227.png)

switch支持字符串是通过<span style="color: #ff6600;">hashCode()</span>和<span style="color: #ff6600;">equals()</span>方法来实现的, 先通过<span style="color: #ff6600;">hashCode()</span>返回的哈希值进行switch, 然后通过<span style="color: #ff6600;">equals()</span>方法比较进行安全检查, 调用<span style="color: #ff6600;">equals()</span>是为了防止可能发生的哈希碰撞。

另外switch还支持<span style="color: #ff6600;">byte</span>、<span style="color: #ff6600;">short</span>、<span style="color: #ff6600;">int</span>、<span style="color: #ff6600;">char</span>这几种基本数据类型, 其中支持<span style="color: #ff6600;">char</span>类型是通过比较它们的ascii码(ascii码是整型)来实现的。所以switch其实只支持一种数据类型, 也就是整型, 其他诸如String、枚举类型都是转换成整型之后再使用switch的。

<div style="text-align: right"><a name="_label6"></a></div>

## <span style="font-size: 18px;">**可变参数**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 可变参数
 * option: --arrayiter false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">varargsTest</span><span class="pun">(</span><span class="typ">String</span> <span class="pln"></span> <span class="pun">...</span> <span class="pln">arr</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">for</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="typ">String</span> <span class="pln">s</span> <span class="pun">:</span> <span class="pln">arr</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --arrayiter false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803143827363-1860208236.png)

可变参数其实就是一个不定长度的数组, 数组长度随传入方法的对应参数个数来决定。可变参数只能在参数列表的末位使用。

<div style="text-align: right"><a name="_label7"></a></div>

## <span style="font-size: 18px;">**自动装箱/拆箱**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 自动装箱/拆箱
 * option: --sugarboxing false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">Double</span> <span class="pln">autoBoxingTest</span><span class="pun">(</span><span class="typ">Integer</span> <span class="pln">i</span><span class="pun">,</span> <span class="pln"></span> <span class="typ">Double</span> <span class="pln">d</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln">d</span> <span class="pun">+</span><span style="color: #000000;"> <span class="pln">i</span><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --sugarboxing false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803144041276-2054980101.png)

首先我们知道, 基本类型与包装类型在某些操作符的作用下, 包装类型调用`valueOf()`方法的过程叫做装箱, 调用`xxxValue()方法`的过程叫做拆箱。所以上面的结果很容易看出, 先对两个包装类进行拆箱, 再对运算结果进行装箱。

<div style="text-align: right"><a name="_label8"></a></div>

## <span style="font-size: 18px;">**枚举**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 枚举, JDK1.5开始支持
 * option: --sugarenums false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">enum</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">EnumTest</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln">FOO</span><span class="pun">,</span> <span class="pln">BAR</span><span class="pun">,</span> <span class="pln">BAP</span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --sugarenums false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803144547865-634089140.png)

当我们自定义一个枚举类型时, 编译器会自动创建一个被final修饰的枚举类来继承<span style="color: #ff6600;">Enum</span>, 所以自定义枚举类型是无法继承和被继承的。当枚举类初始化时, 枚举字段引用该枚举类的一个静态常量对象, 并且所有的枚举字段都用常量数组<span style="color: #ff6600;">$VALUES</span>来存储。<span style="color: #ff6600;">values()</span>方法内则调用Object的<span style="color: #ff6600;">clone()</span>方法, 参照<span style="color: #ff6600;">$VALUES</span>数组对象复制一个新的数组, 新数组会有所有的枚举字段。

<div style="text-align: right"><a name="_label9"></a></div>

## <span style="font-size: 18px;">**内部类**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #0000ff;"><span class="kwd">import</span></span> <span class="pln">java</span><span class="pun">.</span><span class="pln">util</span><span class="pun">.*</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">import</span></span> <span class="pln">java</span><span class="pun">.</span><span class="pln">io</span><span class="pun">.*</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">class</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">CFRDecompilerDemo</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">int</span></span> <span class="pln">x</span> <span class="pun">=</span> <span class="pln"></span> <span class="lit">3</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 内部类
     * option: --removeinnerclasssynthetics false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">innerClassTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">new</span></span> <span class="pln"></span> <span class="typ">InnerClass</span><span class="pun">().</span><span class="pln">getSum</span><span class="pun">(</span><span class="lit">6</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">class</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">InnerClass</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">int</span></span> <span class="pln">getSum</span><span class="pun">(</span><span style="color: #0000ff;"><span class="kwd">int</span></span><span style="color: #000000;"> <span class="pln">y</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln">x</span> </span><span class="pun">+=</span><span style="color: #000000;"> <span class="pln">y</span><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span><span style="color: #000000;"> <span class="pln">x</span><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行:<span style="color: #ff6600;"> java -jar cfr_0_132.jar CFRDecompilerDemo.class --removeinnerclasssynthetics false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803150827020-401588426.png)

首先我们要明确, 上述innerClassTest()方法中的<span style="color: #ff6600;">this</span>是外部类当前对象的引用, 而InnerClass类中的<span style="color: #ff6600;">this</span>则是内部类当前对象的引用。编译过程中, 编译器会自动在内部类定义一个外部类的常量引用<span style="color: #ff6600;">this$0</span>, 并且在内部类的构造器中初始化<span style="color: #ff6600;">this$0</span>, 当外部类访问内部类时, 会把当前外部类的对象引用<span style="color: #ff6600;">this</span>传给内部类的构造器用于初始化, 这样内部类就能通过所持有的外部类的对象引用, 来访问外部类的所有公有及私有成员。

<div style="text-align: right"><a name="_label10"></a></div>

## <span style="font-size: 18px;">**泛型擦除**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 泛型擦除
 * option:</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">genericEraseTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">List</span></span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span> <span class="pln">list</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span> <span class="pln"></span> <span class="typ">ArrayList</span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span><span style="color: #000000;"><span class="pun">();</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803145253168-1402875032.png)

在JVM中没有泛型这一概念,  只有普通方法和普通类, 所有泛型类的泛型参数都会在编译时期被擦除, 所以泛型类并没有自己独有的Class类对象比如List<Integer>.class, 而只有<span style="color: #ff6600;">List.class</span>对象。

<div style="text-align: right"><a name="_label11"></a></div>

## **<span style="font-size: 18px;">增强for循环</span>**

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 增强for循环
 * option: --collectioniter false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">forLoopTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">String</span><span class="pun">[]</span> <span class="pln">qingshanli</span> </span><span class="pun">=</span> <span class="pln"></span> <span class="pun">{</span><span class="str">"haha"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"qingshan"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"helloworld"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"ceshi"</span><span style="color: #000000;"><span class="pun">};</span> <span class="pln"></span> <span class="typ">List</span></span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span> <span class="pln">list</span> <span class="pun">=</span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">Arrays</span><span class="pun">.</span><span class="pln">asList</span><span class="pun">(</span><span class="pln">qingshanli</span><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">for</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="typ">Object</span> <span class="pln">s</span> <span class="pun">:</span> <span class="pln">list</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --collectioniter false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803151155842-1294559378.png)

很明显, 增强for循环的底层其实还是通过迭代器来实现的, 这也就解释了为什么增强for循环中不能进行增删改操作。

<div style="text-align: right"><a name="_label12"></a></div>

## <span style="font-size: 18px;">**lambda表达式**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* lambda表达式
 * option: --decodelambdas false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">lambdaTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">String</span><span class="pun">[]</span> <span class="pln">qingshanli</span> </span><span class="pun">=</span> <span class="pln"></span> <span class="pun">{</span><span class="str">"haha"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"qingshan"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"helloworld"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"ceshi"</span><span style="color: #000000;"><span class="pun">};</span> <span class="pln"></span> <span class="typ">List</span></span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span> <span class="pln">list</span> <span class="pun">=</span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">Arrays</span><span class="pun">.</span><span class="pln">asList</span><span class="pun">(</span><span class="pln">qingshanli</span><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"> <span class="com">使用lambda表达式以及函数操作</span></span> <span class="pln">list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">((</span><span class="pln">str</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">-></span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="kwd">print</span><span class="pun">(</span><span class="pln">str</span> <span class="pun">+</span> <span class="pln"></span> <span class="str">"; "</span><span style="color: #000000;"><span class="pun">));</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"> <span class="com">在JDK8中使用双冒号操作符</span></span> <span class="pln"></span><span style="color: #000000;"> <span class="pln">list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">::</span><span class="pln">println</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行:<span style="color: #ff6600;"> java -jar cfr_0_132.jar CFRDecompilerDemo.class --decodelambdas false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803160951039-1629659950.png)

这里笔者经验尚浅, 关于lambda表达式的实现原理暂不做阐述, 以免误人子弟, 欢迎有兴趣的读者在留言区一起讨论。

<div style="text-align: right"><a name="_label13"></a></div>

## <span style="font-size: 18px;">**try-with-resources语句**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* try-with-resources语句
 * option: --tryresources false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span> <span class="pln">tryWithResourcesTest</span><span class="pun">()</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">throws</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">IOException</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">try</span></span> <span class="pln"></span> <span class="pun">(</span><span style="color: #0000ff;"><span class="kwd">final</span></span> <span class="pln"></span> <span class="typ">StringWriter</span> <span class="pln">writer</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">StringWriter</span><span class="pun">();</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">final</span></span> <span class="pln"></span> <span class="typ">StringWriter</span> <span class="pln">writer2</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">StringWriter</span><span class="pun">())</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln">writer</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span></span><span class="str">"This is qingshanli1"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln">writer2</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span></span><span class="str">"this is qingshanli2"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

命令行:<span style="color: #ff6600;"> java -jar cfr_0_132.jar CFRDecompilerDemo.class --tryresources false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803152324539-1851079267.png)

在JDK7之前, 如IO流、数据库连接等资源用完后, 都是通过finally代码块来释放资源。而try-with-resources语法糖则帮我们省去了释放资源这一操作, 编译器在解语法糖阶段时会将它还原成原始的语法结构。

<div style="text-align: right"><a name="_label14"></a></div>

## <span style="font-size: 18px;">**JDK10的局部变量类型推断**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 局部变量类型推断, JDK10开始支持
 * option: 不需要参数</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">varTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">初始化局部变量</span> </span><span class="pln"></span> <span class="kwd">var</span> <span class="pln"></span> <span class="kwd">string</span> <span class="pln"></span> <span class="pun">=</span> <span class="pln"></span> <span class="str">"qingshanli"</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">初始化局部变量</span> </span><span class="pln"></span> <span class="kwd">var</span> <span class="pln">stringList</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span> <span class="pln"></span> <span class="typ">ArrayList</span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span><span style="color: #000000;"><span class="pun">();</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span></span><span class="str">"九幽阴灵，诸天神魔，以我血躯，奉为牺牲。"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span></span><span class="str">"三生七世，永堕阎罗，只为情故，虽死不悔！"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span></span><span class="str">"blog:http://www.cnblogs.com/qingshanli/"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">增强for循环的索引</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">for</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="kwd">var</span> <span class="pln">s</span> <span class="pun">:</span> <span class="pln">stringList</span><span class="pun">){</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">传统for循环的局部变量定义</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">for</span></span> <span class="pln"></span> <span class="pun">(</span><span class="kwd">var</span> <span class="pln">i</span> <span class="pun">=</span> <span class="pln"></span> <span class="lit">0</span><span class="pun">;</span> <span class="pln">i</span> <span class="pun"><</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">size</span><span class="pun">();</span> <span class="pln">i</span><span class="pun">++</span><span style="color: #000000;"><span class="pun">){</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">stringList</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="pln">i</span><span class="pun">));</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

JDK10环境下编译:<span style="color: #ff6600;"> /home/qingshanli/Downloads/jdk-10.0.2/bin/javac CFRDecompilerDemo.java</span>

命令行: <span style="color: #ff6600;">java -jar cfr_0_132.jar CFRDecompilerDemo.class --collectioniter false</span>

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180803153228437-1297024872.png)

可以看出, 局部变量类型推断其实也是一个语法糖。在编译过程的解语法糖阶段, 会使用变量真正的类型来替代var类型。所以java由始至终是一种强类型语言, java中的var和弱类型语言JavaScript中的var是完全不一样的, 例如下图 <span style="color: #ff6600;">var i = "10" - 6</span> 这样的语法运算在JavaScript中可以的, 而在Java语言中则不被允许。

![](https://images2018.cnblogs.com/blog/1278884/201808/1278884-20180804004353391-1540412177.png)

另外目前已知的允许使用var声明变量的几个场景有初始化局部变量、增强for循环的索引、传统for循环的局部变量定义。而诸如方法的形参、构造器的形参、方法的返回值类型、对象的成员变量、只进行定义而不初始化的变量等则不支持这种用法。对于后面的几种不支持, 我的猜想是因为它们会被外部访问而导致充满了不确定性, 举个栗子, 比如对象的成员变量X, 被对象A访问并赋值ArrayList类型, 被对象B访问并赋值HashMap类型, 那么问题来了, 对象A和对象B都是同一个类的实例, 这就产生了冲突, 此时虚拟机又如何区分这个对象的成员变量X到底是什么类型呢? 

<div style="text-align: right"><a name="_label15"></a></div>

## <span style="font-size: 18px;">**源代码**</span>

<div class="cnblogs_code" onclick="cnblogs_code_show('723b83fa-810c-482c-a015-dbb56bd5bf80')">![](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

<div id="cnblogs_code_open_723b83fa-810c-482c-a015-dbb56bd5bf80" class="cnblogs_code_hide" style="display: block;">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre class="prettyprint prettyprinted" style=""><span style="color: #0000ff;"><span class="kwd">import</span></span> <span class="pln">java</span><span class="pun">.</span><span class="pln">util</span><span class="pun">.*</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">import</span></span> <span class="pln">java</span><span class="pun">.</span><span class="pln">io</span><span class="pun">.*</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">class</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">CFRDecompilerDemo</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">int</span></span> <span class="pln">x</span> <span class="pun">=</span> <span class="pln"></span> <span class="lit">3</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 字符串拼接
     * option: --stringbuilder false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span> <span class="pln">stringBuilderTest</span><span class="pun">(</span><span style="color: #0000ff;"><span class="kwd">int</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="kwd">end</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">char</span></span><span class="pun">[]</span> <span class="pln">foo</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">char</span></span><span class="pun">[]{</span><span class="str">'@'</span><span class="pun">,</span> <span class="pln"></span> <span class="str">'a'</span><span class="pun">,</span> <span class="pln"></span> <span class="str">'*'</span><span style="color: #000000;"><span class="pun">};</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">char</span></span><span style="color: #000000;"> <span class="pln">ch</span><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">int</span></span> <span class="pln">x</span> <span class="pun">=</span> <span class="pln"></span> <span class="lit">0</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">while</span></span> <span class="pln"></span> <span class="pun">((</span><span class="pln">ch</span> <span class="pun">=</span> <span class="pln">foo</span><span class="pun">[++</span><span class="pln">x</span><span class="pun">])</span> <span class="pln"></span> <span class="pun">!=</span> <span class="pln"></span> <span class="str">'*'</span><span style="color: #000000;"><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">""</span> <span class="pln"></span> <span class="pun">+</span> <span class="pln">x</span> <span class="pun">+</span> <span class="pln"></span> <span class="str">": "</span> <span class="pln"></span> <span class="pun">+</span><span style="color: #000000;"> <span class="pln">ch</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 条件编译
     * option: 不需要参数</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">ifCompilerTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">if</span></span><span class="pun">(</span><span style="color: #0000ff;"><span class="kwd">false</span></span><span style="color: #000000;"><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"false if"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span></span><span style="color: #0000ff;"><span class="kwd">else</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"true else"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 断言, JDK1.4开始支持
     * option: --sugarasserts false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">assertTest</span><span class="pun">(</span><span class="typ">String</span> <span class="pln">s</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">assert</span></span> <span class="pln"></span> <span class="pun">(!</span><span class="pln">s</span><span class="pun">.</span><span class="pln">equals</span><span class="pun">(</span><span class="str">"Fred"</span><span style="color: #000000;"><span class="pun">));</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 枚举与Switch语句
     * option: --decodeenumswitch false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">int</span></span><span style="color: #000000;"> <span class="pln">switchEnumTest</span><span class="pun">(</span><span class="typ">EnumTest</span> <span class="pln">e</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">switch</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="pln">e</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span><span style="color: #000000;"> <span class="pln">FOO</span><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">1</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span><span style="color: #000000;"> <span class="pln">BAP</span><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">2</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">0</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 字符串与Switch语句
     * option: --decodestringswitch false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">int</span></span><span style="color: #000000;"> <span class="pln">switchStringTest</span><span class="pun">(</span><span class="typ">String</span> <span class="pln">s</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">switch</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="pln">s</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">default</span></span><span style="color: #000000;"><span class="pun">:</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"Test"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">break</span></span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span> <span class="pln"></span> <span class="str">"BB"</span><span class="pun">:</span> <span class="pln"></span> <span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"> <span class="com">BB and Aa have the same hashcode.</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">12</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span> <span class="pln"></span> <span class="str">"Aa"</span><span style="color: #000000;"><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">case</span></span> <span class="pln"></span> <span class="str">"FRED"</span><span style="color: #000000;"><span class="pun">:</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">13</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span></span><span class="str">"Here"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln"></span> <span class="lit">0</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 可变参数
     * option: --arrayiter false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">varargsTest</span><span class="pun">(</span><span class="typ">String</span> <span class="pln"></span> <span class="pun">...</span> <span class="pln">arr</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">for</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="typ">String</span> <span class="pln">s</span> <span class="pun">:</span> <span class="pln">arr</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 自动装箱/拆箱
     * option: --sugarboxing false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">Double</span> <span class="pln">autoBoxingTest</span><span class="pun">(</span><span class="typ">Integer</span> <span class="pln">i</span><span class="pun">,</span> <span class="pln"></span> <span class="typ">Double</span> <span class="pln">d</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span> <span class="pln">d</span> <span class="pun">+</span><span style="color: #000000;"> <span class="pln">i</span><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 枚举, JDK1.5开始支持
     * option: --sugarenums false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">enum</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">EnumTest</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln">FOO</span><span class="pun">,</span> <span class="pln">BAR</span><span class="pun">,</span> <span class="pln">BAP</span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 内部类
     * option: --removeinnerclasssynthetics false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">innerClassTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">new</span></span> <span class="pln"></span> <span class="typ">InnerClass</span><span class="pun">().</span><span class="pln">getSum</span><span class="pun">(</span><span class="lit">6</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">class</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">InnerClass</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">int</span></span> <span class="pln">getSum</span><span class="pun">(</span><span style="color: #0000ff;"><span class="kwd">int</span></span><span style="color: #000000;"> <span class="pln">y</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln">x</span> </span><span class="pun">+=</span><span style="color: #000000;"> <span class="pln">y</span><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">return</span></span><span style="color: #000000;"> <span class="pln">x</span><span class="pun">;</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 泛型擦除
     * option:</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">genericEraseTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">List</span></span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span> <span class="pln">list</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span> <span class="pln"></span> <span class="typ">ArrayList</span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span><span style="color: #000000;"><span class="pun">();</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 增强for循环
     * option: --collectioniter false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">forLoopTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">String</span><span class="pun">[]</span> <span class="pln">qingshanli</span> </span><span class="pun">=</span> <span class="pln"></span> <span class="pun">{</span><span class="str">"haha"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"qingshan"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"helloworld"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"ceshi"</span><span style="color: #000000;"><span class="pun">};</span> <span class="pln"></span> <span class="typ">List</span></span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span> <span class="pln">list</span> <span class="pun">=</span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">Arrays</span><span class="pun">.</span><span class="pln">asList</span><span class="pun">(</span><span class="pln">qingshanli</span><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">for</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="typ">Object</span> <span class="pln">s</span> <span class="pun">:</span> <span class="pln">list</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* lambda表达式
     * option: --decodelambdas false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">lambdaTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> <span class="typ">String</span><span class="pun">[]</span> <span class="pln">qingshanli</span> </span><span class="pun">=</span> <span class="pln"></span> <span class="pun">{</span><span class="str">"haha"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"qingshan"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"helloworld"</span><span class="pun">,</span> <span class="pln"></span> <span class="str">"ceshi"</span><span style="color: #000000;"><span class="pun">};</span> <span class="pln"></span> <span class="typ">List</span></span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span> <span class="pln">list</span> <span class="pun">=</span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">Arrays</span><span class="pun">.</span><span class="pln">asList</span><span class="pun">(</span><span class="pln">qingshanli</span><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"> <span class="com">使用lambda表达式以及函数操作</span></span> <span class="pln">list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">((</span><span class="pln">str</span><span class="pun">)</span> <span class="pln"></span> <span class="pun">-></span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="kwd">print</span><span class="pun">(</span><span class="pln">str</span> <span class="pun">+</span> <span class="pln"></span> <span class="str">"; "</span><span style="color: #000000;"><span class="pun">));</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"> <span class="com">在JDK8中使用双冒号操作符</span></span> <span class="pln"></span><span style="color: #000000;"> <span class="pln">list</span><span class="pun">.</span><span class="pln">forEach</span><span class="pun">(</span><span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">::</span><span class="pln">println</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* try-with-resources语句
     * option: --tryresources false</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span> <span class="pln">tryWithResourcesTest</span><span class="pun">()</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">throws</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">IOException</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">try</span></span> <span class="pln"></span> <span class="pun">(</span><span style="color: #0000ff;"><span class="kwd">final</span></span> <span class="pln"></span> <span class="typ">StringWriter</span> <span class="pln">writer</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">StringWriter</span><span class="pun">();</span> <span class="pln"></span> </span><span style="color: #0000ff;"><span class="kwd">final</span></span> <span class="pln"></span> <span class="typ">StringWriter</span> <span class="pln">writer2</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="typ">StringWriter</span><span class="pun">())</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln">writer</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span></span><span class="str">"This is qingshanli1"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln">writer2</span><span class="pun">.</span><span class="pln">write</span><span class="pun">(</span></span><span class="str">"this is qingshanli2"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">/**</span></span><span style="color: #008000;"> <span class="com">* 局部变量类型推断, JDK10开始支持
     * option: 不需要参数</span> </span><span style="color: #008000;"><span class="com">*/</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">public</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">void</span></span><span style="color: #000000;"> <span class="pln">varTest</span><span class="pun">()</span> <span class="pln"></span> <span class="pun">{</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">初始化局部变量</span> </span><span class="pln"></span> <span class="kwd">var</span> <span class="pln"></span> <span class="kwd">string</span> <span class="pln"></span> <span class="pun">=</span> <span class="pln"></span> <span class="str">"qingshanli"</span><span style="color: #000000;"><span class="pun">;</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">初始化局部变量</span> </span><span class="pln"></span> <span class="kwd">var</span> <span class="pln">stringList</span> <span class="pun">=</span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">new</span></span> <span class="pln"></span> <span class="typ">ArrayList</span><span class="pun"><</span><span class="typ">String</span><span class="pun">></span><span style="color: #000000;"><span class="pun">();</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span></span><span class="str">"九幽阴灵，诸天神魔，以我血躯，奉为牺牲。"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span></span><span class="str">"三生七世，永堕阎罗，只为情故，虽死不悔！"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">add</span><span class="pun">(</span></span><span class="str">"blog:http://www.cnblogs.com/qingshanli/"</span><span style="color: #000000;"><span class="pun">);</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">增强for循环的索引</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">for</span></span><span style="color: #000000;"> <span class="pln"></span> <span class="pun">(</span><span class="kwd">var</span> <span class="pln">s</span> <span class="pun">:</span> <span class="pln">stringList</span><span class="pun">){</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">s</span><span class="pun">);</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> </span><span style="color: #008000;"><span class="com">//</span></span><span style="color: #008000;"><span class="com">传统for循环的局部变量定义</span></span> <span class="pln"></span> <span style="color: #0000ff;"><span class="kwd">for</span></span> <span class="pln"></span> <span class="pun">(</span><span class="kwd">var</span> <span class="pln">i</span> <span class="pun">=</span> <span class="pln"></span> <span class="lit">0</span><span class="pun">;</span> <span class="pln">i</span> <span class="pun"><</span> <span class="pln">stringList</span><span class="pun">.</span><span class="pln">size</span><span class="pun">();</span> <span class="pln">i</span><span class="pun">++</span><span style="color: #000000;"><span class="pun">){</span> <span class="pln"></span> <span class="typ">System</span><span class="pun">.</span><span class="kwd">out</span><span class="pun">.</span><span class="pln">println</span><span class="pun">(</span><span class="pln">stringList</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="pln">i</span><span class="pun">));</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span> <span class="pln"></span> <span class="pun">}</span></span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

<span class="cnblogs_code_collapse" style="display: none;">View Code</span></div>

<div style="text-align: right"><a name="_label16"></a></div>

## <span style="font-size: 18px;">**参数资料**</span>

[Java的编译原理](https://www.cnblogs.com/qingshanli/p/9281760.html)

[Java代码的编译与反编译那些事儿-HollisChuang's Blog](http://www.hollischuang.com/archives/58 "Java代码的编译与反编译那些事儿-HollisChuang's Blog")

[我反编译了Java 10的本地变量类型推断-HollisChuang's Blog](http://www.hollischuang.com/archives/2187 "我反编译了Java 10的本地变量类型推断-HollisChuang's Blog")

[Java中的Switch对整型、字符型、字符串型的具体实现细节-HollisChuang's Blo...](http://www.hollischuang.com/archives/61 "Java中的Switch对整型、字符型、字符串型的具体实现细节-HollisChuang's Blo...")

[一些防止java代码被反编译的方法](https://blog.csdn.net/qq_35038153/article/details/78054085)

</div>

<div id="blog_post_info_block">

<div id="BlogPostCategory">分类: [JVM虚拟机](https://www.cnblogs.com/qingshanli/category/1223757.html)</div>

<div id="EntryTag">标签: [JVM学习总结](https://www.cnblogs.com/qingshanli/tag/JVM%E5%AD%A6%E4%B9%A0%E6%80%BB%E7%BB%93/)</div>

<div id="blog_post_info">

<div id="green_channel">[好文要顶](javascript:void(0);) [关注我](javascript:void(0);) [收藏该文](javascript:void(0);) [![](//common.cnblogs.com/images/icon_weibo_24.png)](javascript:void(0); "分享至新浪微博") [![](//common.cnblogs.com/images/wechat.png)](javascript:void(0); "分享至微信")</div>

<div id="author_profile">

<div id="author_profile_info" class="author_profile_info">[![](//pic.cnblogs.com/face/1278884/20180718101838.png)](https://home.cnblogs.com/u/qingshanli/)

<div id="author_profile_detail" class="author_profile_info">[qingshanli](https://home.cnblogs.com/u/qingshanli/)  
[关注 - 19](https://home.cnblogs.com/u/qingshanli/followees)  
[粉丝 - 13](https://home.cnblogs.com/u/qingshanli/followers)</div>

</div>

<div id="author_profile_follow">[+加关注](javascript:void(0);)</div>

</div>

<div id="div_digg">

<div class="diggit" onclick="votePost(9375040,'Digg')" title="支持"><span class="diggnum" id="digg_count">2</span></div>

<div class="buryit" onclick="votePost(9375040,'Bury')" title="反对"><span class="burynum" id="bury_count">0</span></div>

</div>

<script type="text/javascript">currentDiggType = 0;</script></div>

<div id="post_next_prev">[«](https://www.cnblogs.com/qingshanli/p/9321175.html) 上一篇：[关于赞赏](https://www.cnblogs.com/qingshanli/p/9321175.html "发布于2018-07-30 23:46")  
[»](https://www.cnblogs.com/qingshanli/p/9439987.html) 下一篇：[左耳听风专栏学习总结](https://www.cnblogs.com/qingshanli/p/9439987.html "发布于2018-08-07 22:42")  
</div>

</div>

</div>

<div class="postDesc">posted @ <span id="post-date">2018-08-04 01:37</span> [qingshanli](https://www.cnblogs.com/qingshanli/) 阅读(<span id="post_view_count">1491</span>) 评论(<span id="post_comment_count">1</span>) [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=9375040) [收藏](#)</div>

</div>

<script type="text/javascript">var allowComments=true,cb_blogId=434237,cb_entryId=9375040,cb_blogApp=currentBlogApp,cb_blogUserGuid='a6083e56-ad3e-4b2f-c17b-08d523685c8c',cb_entryCreatedDate='2018/8/4 1:37:00';loadViewCount(cb_entryId);var cb_postType=1;var isMarkdown=false;</script></div>

</div>

<a name="!comments"></a>

<div id="blog-comments-placeholder">  

<div class="feedback_area_title">评论列表</div>

<div class="feedbackItem">

<div class="feedbackListSubtitle">

<div class="feedbackManage">  <span class="comment_actions"></span></div>

[#1楼](#4035280)<a name="4035280" id="comment_anchor_4035280"></a><span id="comment-maxId" style="display:none;">4035280</span><span id="comment-maxDate" style="display:none;">2018/8/4 8:25:43</span> <span class="comment_date">2018-08-04 08:25</span> [Dream_saddle](https://www.cnblogs.com/dream-saddle/) [ ](http://msg.cnblogs.com/send/Dream_saddle "发送站内短消息")</div>

<div class="feedbackCon">![](http://pic.cnblogs.com/face/1226851/20180828223755.png)

<div id="comment_body_4035280" class="blog_comment_body">凡瑶大旗用不倒</div>

<div class="comment_vote">[支持(1)](javascript:void(0);)[反对(0)](javascript:void(0);)</div>

<span id="comment_4035280_avatar" style="display:none;">http://pic.cnblogs.com/face/1226851/20180828223755.png</span></div>

</div>

</div>

<script type="text/javascript">var commentManager = new blogCommentManager();commentManager.renderComments(0);</script>

<div id="comment_form" class="commentform"><a name="commentform"></a>

<div id="comment_nav"><span id="span_refresh_tips"></span>[刷新评论](javascript:void(0);)[刷新页面](#)[返回顶部](#top)</div>

<div id="comment_form_container">

<div class="login_tips">注册用户登录后才能发表评论，请 [登录](javascript:void(0);) 或 [注册](javascript:void(0);)，[访问](http://www.cnblogs.com)网站首页。</div>

</div>

<div id="ad_t2">[【推荐】超50万C++/C#源码: 大型实时仿真组态图形源码](http://www.ucancode.com/index.htm)  
[【前端】SpreadJS表格控件，可嵌入系统开发的在线Excel](https://www.grapecity.com.cn/developer/spreadjs?utm_source=cnblogs&utm_medium=blogpage&utm_term=bottom&utm_content=SpreadJS&utm_campaign=community)  
[【推荐】程序员问答平台，解决您开发中遇到的技术难题](https://q.cnblogs.com/)  
</div>

<script>var googletag = googletag || {}; googletag.cmd = googletag.cmd || [];</script> <script>googletag.cmd.push(function() { googletag.defineSlot('/1090369/C1', [300, 250], 'div-gpt-ad-1546353474406-0').addService(googletag.pubads()); googletag.defineSlot('/1090369/C2', [468, 60], 'div-gpt-ad-1539008685004-0').addService(googletag.pubads()); googletag.pubads().enableSingleRequest(); googletag.enableServices(); });</script>

<div id="cnblogs_c1" class="c_ad_block" style="">

<div id="div-gpt-ad-1546353474406-0" style="height:250px; width:300px;" data-google-query-id="CJrd9emn0eICFUtgwQodqOAACg">

<div id="google_ads_iframe_/1090369/C1_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1090369/C1_0" title="3rd party ad content" name="google_ads_iframe_/1090369/C1_0" width="300" height="250" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" srcdoc="" data-google-container-id="1" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div>

</div>

</div>

<div id="cnblogs_c2" class="c_ad_block" style="">

<div id="div-gpt-ad-1539008685004-0" style="height:60px; width:468px;" data-google-query-id="CPK8-Omn0eICFUtgwQodqOAACg">

<div id="google_ads_iframe_/1090369/C2_0__container__" style="border: 0pt none;"><iframe id="google_ads_iframe_/1090369/C2_0" title="3rd party ad content" name="google_ads_iframe_/1090369/C2_0" width="468" height="60" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" srcdoc="" data-google-container-id="2" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div>

</div>

</div>

<script type="text/javascript">if(enablePostBottom()) { codeHighlight(); fixPostBody(); setTimeout(function () { incrementViewCount(cb_entryId); }, 50); deliverT2(); deliverC1(); deliverC2(); loadNewsAndKb(); loadBlogSignature(); LoadPostInfoBlock(cb_blogId, cb_entryId, cb_blogApp, cb_blogUserGuid); GetPrevNextPost(cb_entryId, cb_blogId, cb_entryCreatedDate, cb_postType); loadOptUnderPost(); GetHistoryToday(cb_blogId, cb_blogApp, cb_entryCreatedDate); }</script></div>

</div>

</div>
