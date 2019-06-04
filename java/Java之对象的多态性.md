<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">

<div class="article-copyright">版权声明：本文为博主原创文章，未经博主允许不得转载。 https://blog.csdn.net/qq_19782019/article/details/79788326</div>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css"> <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">

<div class="htmledit_views" id="content_views">

# <a name="t0"></a><span style="color:#000000;">Java之对象的多态性</span>

# <a name="t1"></a>多态概念 （Java）

<span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">    多态</span><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">（</span><span class="LangWithName" style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">英语：<span lang="en" xml:lang="en">polymorphism</span></span><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">），是指</span>[计算机程序](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F "计算机程序")<span style="font-family:sans-serif;font-size:15.008px;"><span style="color:#222222;">运行时</span><span style="color:#ff0000;">，**相同的消息**</span><span style="color:#222222;">可能会送给</span>**<span style="color:#ff0000;">多个不同的类别之</span>**</span>[**<span style="color:#ff0000;">对象</span>**](https://zh.wikipedia.org/wiki/%E5%AF%B9%E8%B1%A1_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6) "对象 (计算机科学)")<span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">，而**系统可依据对象所属类别，引发对应类别的方法，而有不同的行为。**简单来说，所谓</span><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">多态意指相同的消息给予不同的对象会引发不同的动作称之</span><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">。</span>

<span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;"><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">多态也可定义为“一种将不同的特殊行为和单个泛化记号相关联的能力”。</span>  
</span>

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;"><span style="color:#222222;">多态可分为变量多态与函数多态。变量多态是指：</span><span style="color:rgb(34,34,34);">基类型的变量（对于C++是引用或指针）可以被赋值基类型对象，也可以被赋值派生类型的对象。</span><span style="color:#222222;">函数多态是指，</span><u><span style="color:#222222;">相同的函数调用界面（函数名与实参表），传送给一个对象变量，可以有不同的行为，</span><span style="color:#000000;">这视该对象变量所指向的对象类型而定。</span></u><span style="color:#222222;">因此，变量多态是函数多态的基础。</span></span>  
</span></span>

<span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;"><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;"><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">  
</span></span></span>

<span style="font-family:sans-serif;"><span style="font-family:sans-serif;"><span style="font-family:sans-serif;"></span></span></span>

## <a name="t2"></a><span class="mw-headline">例子</span>

<span style="color:#222222;">    比如有动物（Animal）之</span>[类别](https://zh.wikipedia.org/wiki/%E7%B1%BB_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6) "类 (计算机科学)")<span style="color:#222222;">（Class），而且由动物</span>[继承](https://zh.wikipedia.org/wiki/%E7%BB%A7%E6%89%BF_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6) "继承 (计算机科学)")<span style="color:#222222;">出类别鸡（Chicken）和类别狗（Dog），并对</span>**<span style="color:#ff0000;">同一源自类别动物</span>**<span style="color:#222222;">（父类别）之一消息</span><span style="color:#ff0000;">**有不同、的响应**</span><span style="color:#222222;">，如类别动物有“叫()”之动作，而类别鸡会“啼叫()”，类别狗则会“吠叫()”，则称之为多态。</span>

## <a name="t3"></a>概括

<span style="color:#222222;">    上面关于多态的概念看起来有那么一点难以理解，但是我们可以把上述一大段话给归纳成为一句话就是：</span><span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;"><span style="color:#ff0000;">**相同的消息**</span><span style="color:#222222;">可能会送给</span>**<span style="color:#ff0000;">多个不同的类别之</span>**</span>[**<span style="color:#ff0000;">对象</span>**](https://zh.wikipedia.org/wiki/%E5%AF%B9%E8%B1%A1_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6) "对象 (计算机科学)")<span style="font-family:sans-serif;font-size:15.008px;"><span style="color:#222222;">，而</span>**<span style="color:#ff0000;">系统可依据对象所属类别，引发对应类别的方法，而有不同的行为</span><span style="color:#222222;">。</span>**</span>  

<span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">**例如：<span style="color:#222222;font-family:sans-serif;font-size:15.008px;">比如有动物（Animal）之</span>[类别](https://zh.wikipedia.org/wiki/%E7%B1%BB_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6) "类 (计算机科学)")<span style="color:#222222;font-family:sans-serif;font-size:15.008px;">（Class），而且由动物</span>[继承](https://zh.wikipedia.org/wiki/%E7%BB%A7%E6%89%BF_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6) "继承 (计算机科学)")<span style="color:#222222;font-family:sans-serif;font-size:15.008px;">出类别鸡（Chicken）和类别狗（Dog），并对</span><span style="font-family:sans-serif;font-size:15.008px;"><span style="color:#ff0000;">同一源自类别动物</span></span><span style="color:#222222;font-family:sans-serif;font-size:15.008px;">（父类别）之一消息</span><span style="color:#ff0000;font-family:sans-serif;font-size:15.008px;">**有不同的响应。**</span>**</span>

<span style="color:rgb(34,34,34);font-family:sans-serif;font-size:15.008px;">**<span style="color:#ff0000;font-family:sans-serif;font-size:15.008px;"></span>**</span>

<span style="font-size:15.008px;font-family:sans-serif;"><span style="font-family:sans-serif;font-size:15.008px;"></span></span>

## <a name="t4"></a>解释

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;"> 方法的覆盖特性是Java在运行时支持的多态性之一。系统动态的调度方法是由调用一个被覆盖的方法引起的，该调用机制发生在运行时，而不是编译时。</span></span>

<span style="font-size:15.008px;font-family:sans-serif;"><span style="font-family:sans-serif;font-size:15.008px;"></span></span>

*   当一个被覆盖的方法通过一个父类引用调用时，Java决定执行哪个版本的方法（父类的方法或者被子类覆盖的方法）取决于方法调用发生时，被引用的对象的类型。因此，这一决定实在运行期间做出来的。
*   在运行期间，哪个版本的被覆盖的方法将会被执行是由被引用的对象的类型决定的而不是引用的类型（值）。
*   一个父类的引用可以引用一个子类的对象，这也是一些人口中所说的“向上转型”，Java用这个方法来解决程序运行时覆盖方法被调用的问题。  

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;">![](https://img-blog.csdn.net/20180402142139362?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)</span></span>

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;">  
</span></span>

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;">    因此，如果一个父类包含了一个被子类覆盖的方法，接下来通过一个父类的引用值来引用其不同的子类对象，父类引用调用被覆盖的方法时，不同版本的被覆盖的方法将会执行。下面是一个例子，简单的阐述一下这种动态方法分配机制：  
</span></span>

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;">![](https://img-blog.csdn.net/20180402142549939?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span></span>

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;">![](https://img-blog.csdn.net/20180402143211497?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span></span>

<span style="font-family:sans-serif;"><span style="font-family:sans-serif;"><span style="font-size:32px;">OUTPUT(输出）:</span></span></span>

<span style="font-family:sans-serif;font-size:15.008px;"><span style="font-family:sans-serif;font-size:15.008px;">![](https://img-blog.csdn.net/20180402143244973?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span></span>

<span style="font-family:sans-serif;"><span style="font-family:sans-serif;"></span></span>

## <a name="t5"></a>程序详解

    上面的这个程序创建了一个名为<span style="color:#ff0000;">**A的父类**</span>以及两个分别名为<span><span style="color:#ff0000;">B，C的子类</span></span>。这**<span style="color:#ff0000;">两个子类都覆盖了父类A类的m1方法</span>**。

1.在main（）方法里面的Dispatch类中，首先声明了A类，B类，C类的三个对象。

![](https://img-blog.csdn.net/20180402174811170?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

    此时的引用及对象之间的关系如下图所示：

![](https://img-blog.csdn.net/20180402174859909?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

    其中，A类引用指向了一个A类对象，B类引用指向了一个B类对象，B类对象内包含了一个从A类中继承下来的m1（）方法以及自己覆盖m1的方法；C类引用指向了一个C类对象，C类对象内也包含了一个从A类中继承下来的m1（）方法以及自己覆盖m1的方法；

2.现在声明一个名为ref的A类的引用，起初它将会指向一个空指针。

![](https://img-blog.csdn.net/20180402175407368?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

3.接下来我们将用A类引用来一个一个地指向每一种对象（A类B类或者C类），并且通过这个A类引用ref来调用m1（）方法。正如输出所显示的那样，到底执行哪一个版本的m1（）方法是由此时引用指向的对象的类型所决定的。

![](https://img-blog.csdn.net/20180402180210908?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-blog.csdn.net/20180402180231457?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-blog.csdn.net/20180402180506718?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-blog.csdn.net/2018040218062783?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-blog.csdn.net/20180402180751481?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

![](https://img-blog.csdn.net/20180402180801165?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

## <a name="t6"></a>亲自动手验证

<span style="font-size:15.008px;">     </span>

<span style="font-size:15.008px;">           有兴趣的同学可以</span>**<u><span style="font-size:16px;">[<span style="color:#ff0000;">点击此处</span><span style="color:#ff0000;">进行试验</span>](https://ide.geeksforgeeks.org/V7f6B9P9g3)</span></u>**<span style="font-size:15.008px;">去这个在线IDE平台自己试一下这串代码，亲自动手验证一下上面这个例子。</span>

<span style="font-size:15.008px;">  
</span>

<span style="font-size:15.008px;font-family:sans-serif;"><span style="font-family:sans-serif;font-size:15.008px;"></span></span>

![](https://img-blog.csdn.net/20180402181313698?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

## <a name="t7"></a>运行时成员变量的多态性

    在Java中，我们只能够覆盖父类的方法，却不能覆盖父类的成员变量。

所以运行时，成员变量无法实现多态性。举一个例子：

![](https://img-blog.csdn.net/20180402182050514?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

    在上面这个例子中，子类B类虽然覆盖了父类A类的成员变量X，然而通过A类引用去调用B类对象的X时返回的并不是B类中已经覆盖了A类的那个X的值，返回的仍然是父类A类中的X值，也就是说，成员变量覆盖无法实现像方法覆盖那样的多态性。虽然A类（父类）和B类（子类）都有一个公共的变量x,我们实例化一个B类对象并用一个A类引用a指向它。因为变量没有被覆盖，所以“a.x”这一句话总是代表父类的数据成员。

# <a name="t8"></a>OUTPUT（输出）：

![](https://img-blog.csdn.net/20180402182456476?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## <a name="t9"></a>亲自试一试

    有兴趣的同学可以[**<u><span style="font-size:16px;color:#ff0000;">点击此处</span></u>**](https://ide.geeksforgeeks.org/livUNpux83)通过在线IDE平台亲自实验一下，更好的理解这个例子。  

## <a name="t10"></a>静态VS动态绑定

    1.静态绑定发生在程序的编译期间，而动态绑定发生在程序的运行期间。

    2.private,final,static方法以及变量通过编译器实现静态绑定，同时覆盖方法与运行时运行的对象类型所绑定。

## <a name="t11"></a>对于多态的通俗理解

        其实，对于引用的理解，我们可以简单的理解其为一个“遥控器”，每个“遥控器”可以与一个对象进行“配对”，并通过遥控器来控制对象的“行为”。例如，按下空调遥控器的开关键，空调就会开启。就好比调用 空调遥控器.开机（）方法使得空调遥控器指向的空调对象执行开机（）方法一样。

![](https://img-blog.csdn.net/20180402212912294?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  

## <a name="t12"></a>多态的误区点

  其中，<span><span style="color:#ff0000;">**对象能够执行哪些方法是由引用的类型所决定的，而对象具体怎样去执行某个方法，却是由对象自己决定的。**</span></span>

<span>**<span style="color:#ff0000;"></span> <span style="color:#000000;"></span> **<span style="color:#000000;">例如下面这段程序：</span></span>

    class A {    public void fun1() {        System.out.println("A-->public void fun1(){}");    }     public void fun2() {        this.fun1();    }} class B extends A {    public void fun1() {        System.out.println("B-->public void fun1(){}");    }     public void fun3() {        System.out.println("B-->public void fun3(){}");    }} public class JavaExample {    public static void main(String[] args) {        A a = new B();        a.fun1();    }} 

执行结果为：B-->public void fun1(){};

 上面的程序中，定义了父类为A类，子类为B类，子类B覆盖了父类的fun1（）方法，添加了自己的fun3()类，这是一个对象向上转型的关系，**<span style="color:#ff0000;">但是A类型的引用a虽然可以调用fun1()方法，但是不能通过A类引用a调用子类对象独有的fun3（）方法！！！</span>**

<span style="color:#000000;">因此，我们可以得出下面这个结论：</span>

<span style="color:#000000;">   </span>** <span style="color:#ff0000;">引用所能够调用的方法取决于引用的类型，而如何具体的实现该方法取决于对象的类型。</span>**  

<span style="color:#000000;">引用a为A类型，所以通过引用a只能调用A类型中包含的方法（ fun1()和fun2()），而</span>**<span style="color:#ff0000;">不</span><span style="color:#ff0000;">能调用B类中的fun3（</span><span style="color:#ff0000;">）</span>**<span style="color:#000000;">。也就是说A类引用只能向指向的对象发送A类中包含的方法，具体的实现由指向的对象的类型来决定。</span>

  <span><span style="color:#ff0000;"> </span></span>

<span><span style="color:#ff0000;"><span style="font-size:16px;">[**                    <span style="color:#ff0000;"><u>点击此处</u></span>**](https://ide.geeksforgeeks.org/2lroXOFAuB)</span></span></span>进入在线IDE实验本案例。  

我们可以在上面的实验中，执行a.fun3（）,将会提示找不到fun3（）方法。

## <a name="t13"></a>向下转型的要求

    还是上面的这一串代码,我们只更改其main()函数中的代码：  

    public class JavaExample {    public static void main(String[] args) {       A a=new B();       B b=(B)a;       b.fun1();       b.fun2();       b.fun3();    }} 

    B类为A类的子类，上面的a首先被声明为一个A类型的引用，并指向一个B类型的对象，接下来把A类引用通过向下转型变成一个B类引用，从而有权利去调用B类中非共有的方法。

    然而，在看下面这一段代码,还是只更改main（）函数中的代码：

    public class JavaExample {    public static void main(String[] args) {       A a=new A();       B b=(B)a;       b.fun1();       b.fun2();       b.fun3();    }

    上面的这一段代码也实现了向下转型，然而运行时却报错了：

Exception in thread "main" java.lang.ClassCastException: A cannot be cast to B  

<span></span>at JavaExample.main(JavaExample.java:26)

错误提示说A类引用无法被转换成B类引用，这又是怎么回事呢？

我们发现两端代码的不同之处就在于第一段代码中是

     A a=new B();

而第二段代码中是：

      A a=new A();

    初始化的对象不同而已，**<span style="color:#ff0000;">因为在对象进行向下转型时，必须首先发生对象向上转型，否则将出现对象转换异常。</span>**

<span><span style="color:#000000;">第二段代码中，</span>**<span style="color:#ff0000;">A类型引用指向的是一个A类对象，把A类引用转换成B类引用，此时就可以发送调用B类方法的命令给指向的对象，而指向的对象为A类对象却并不含B类中非共有的方法，对象根本就没有实现这个方法，怎么去执行方法呢？</span>**<span style="color:#000000;">因此就会产生错误。</span></span>

<span><span style="color:#000000;"> 可以用上述遥控器的例子来简单的理解一下这个问题：</span></span>  

<span><span style="color:#000000;"><span style="color:rgb(0,0,0);">      假设最开始只有一个老式遥控器，遥控器只有1.打开空调，2.关闭空调，3.制冷三个功能，遥控器向空调发送相应的命令，空调收到命令后执行相应的动作。</span>  
</span></span>

<span>**<span style="color:#33cc00;">    此时类似于执行语句 A a=new A( );</span>**</span>

<span><span style="color:#000000;">![](https://img-blog.csdn.net/20180403122128253?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span></span>

<span><span style="color:#000000;">    
</span></span>

<span><span style="color:#000000;">    接下来，老式空调太旧了，空调厂商在老式空调的基础上，开发了一款新式空调，不仅有老式空调的三个功能，而且还加入了1.制热功能和2.加湿功能这两个功能。  
</span></span>

<span><span style="color:#000000;">   </span>** <span style="color:#33cc00;">此时类似于语句 class B extend A;</span>**  
</span>

<span><span style="color:#000000;">![](https://img-blog.csdn.net/20180403123050632?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span></span>

<span><span style="color:#000000;">    然而，我们此时只有老式空调的遥控器，但是我们还是可以用老式空调的遥控器与操作新式空调，</span>**<span style="color:#33cc00;">类似于A a=new B( )这个操作</span>**<span style="color:#000000;">，因为新式空调是继承与老式空调改造而来的，我们仍然能够使用老式空调的遥控去操控新式空调，只不过老式空调上只有最基础的三个功能，不能操纵新式空调执行其新添加的加热和加湿功能，但是仍然还是可以使用的。</span>  
</span>

<span><span style="color:#000000;">![](https://img-blog.csdn.net/20180403123521811?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span></span>

<span><span style="color:#000000;">        如果，我们需要使用新式空调的新增的加热和加湿功能，那么我们理应更换新式空调对应的遥控器就好了。  
</span></span>

<span>**<span style="color:#33cc00;">此时类似于 B b=(B) a；</span>**</span>

<span>**<span style="color:#33cc00;">    ![](https://img-blog.csdn.net/20180403124010699?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span>**</span>

<span><span><span style="color:#33cc00;"></span><span style="color:#33cc00;">**此时的情况就类似于调用b.makeCold( )方法了。**</span></span></span><span style="color:#33cc00;">  
</span>

<span><span style="font-weight:bold;"><span><span style="color:#33cc00;"> </span><span style="color:#ff0000;">   上面是正常的向下转型，然而，如果我们不向上转型而直接向下转型会发生什么样的情况呢？</span></span></span></span>

<span><span><span><span style="color:rgb(255,0,0);"></span> <span style="color:#000000;">例如：A a=new A( );  
</span></span></span></span>

<span><span><span><span style="color:#000000;">                B b=(B)a;</span></span></span></span>

<span><span><span><span style="color:#000000;">            就发生了下面这种情况：</span>  
</span></span></span>

<span><span><span><span style="color:#000000;">![](https://img-blog.csdn.net/20180403124522645?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzE5NzgyMDE5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
</span></span></span></span>

<span><span><span><span style="color:#000000;">  
</span></span></span></span>

<span><span style="color:#000000;">    此时，如果新式空调遥控器向老式空调发送一个加热的指令，然而老式空调收到指令后却发现并没有加热的功能，此时就会发生系统故障。  
</span></span>

<span><span style="color:#000000;">        所以，总结而之一句话：<span style="color:rgb(255,0,0);font-weight:700;">在对象进行向下转型时，必须首先发生对象向上转型，否则将出现对象转换异常。</span>  
</span></span>

<span><span style="color:#000000;"><span style="color:rgb(255,0,0);font-weight:700;">  
</span></span></span>

<span><span style="color:#000000;"></span></span>

## <a name="t14"></a>参考资料

<span><span style="color:#000000;">    1.维基百科-多态</span></span>

<span><span style="color:#000000;">    2.https://www.geeksforgeeks.org/dynamic-method-dispatch-runtime-polymorphism-java  
</span></span>

<span><span style="color:#000000;">        作者：<span style="border:0px;font-size:15px;vertical-align:baseline;color:rgb(0,0,0);font-family:'Open Sans', Helvetica, Arial, Verdana, sans-serif;">Gaurav Miglani   翻译：刘扬俊</span>  
</span></span>

<span><span style="color:#000000;"><span style="border:0px;font-size:15px;vertical-align:baseline;color:rgb(0,0,0);font-family:'Open Sans', Helvetica, Arial, Verdana, sans-serif;">    3.《<span style="color:rgb(0,0,0);font-family:'Open Sans', Helvetica, Arial, Verdana, sans-serif;font-size:15px;">Java开发实战经典</span>》 李兴华著  清华大学出版社</span></span></span>

<span><span style="color:#000000;"><span style="border:0px;font-size:15px;vertical-align:baseline;color:rgb(0,0,0);font-family:'Open Sans', Helvetica, Arial, Verdana, sans-serif;">  
</span></span></span>

<span><span style="color:#000000;"><span style="border:0px;font-size:15px;vertical-align:baseline;color:rgb(0,0,0);font-family:'Open Sans', Helvetica, Arial, Verdana, sans-serif;"></span></span></span>

# <a name="t15"></a>博客文章版权说明

<span style="color:rgb(51,51,51);">第一条</span><span style="color:rgb(51,51,51);"> </span><span style="color:rgb(51,51,51);">本博客文章仅代表作者本人的观点，不保证文章等内容的有效性。</span>

<span style="color:rgb(51,51,51);">第二条</span><span style="color:rgb(51,51,51);"> </span><span style="color:rgb(51,51,51);">本博客部分内容转载于合作站点或摘录于部分书籍，但都会注明作</span><span style="color:rgb(51,51,51);">/</span><span style="color:rgb(51,51,51);">译者和原出处。如有不妥之处，敬请指出。</span>

<span style="color:rgb(51,51,51);">第三条</span><span style="color:rgb(51,51,51);"> </span><span style="color:rgb(51,51,51);">在</span><span style="font-weight:700;"><span style="color:rgb(255,0,0);">征得本博客作者同意的情况下</span></span><span style="color:rgb(51,51,51);">，本博客的作品</span><span style="font-weight:700;"><span style="color:rgb(255,0,0);">允许非盈利性引用，并请注明出处：</span><span style="color:rgb(255,0,0);">“作者：____转载自____”</span><span style="color:rgb(255,0,0);">字样，以尊重作者的劳动成果</span></span><span style="color:rgb(51,51,51);">。版权归原作</span><span style="color:rgb(51,51,51);">/</span><span style="color:rgb(51,51,51);">译者所有。</span><span style="color:rgb(255,0,0);"><span style="font-weight:700;">未经允许，严禁转载</span></span><span style="color:rgb(51,51,51);">。</span>

<span style="color:rgb(51,51,51);">第四条 </span><span style="font-weight:700;"><span style="color:rgb(255,0,0);">对非法转载者，“扬俊的小屋”和作/</span><span style="color:rgb(255,0,0);">译者保留采用法律手段追究的权利</span></span><span style="color:rgb(51,51,51);">。</span>

<span style="color:rgb(51,51,51);">第五条</span><span style="color:rgb(51,51,51);"> </span><span style="color:rgb(51,51,51);">本博客之声明以及其修改权、更新权及最终解释权均属“扬俊的小屋”。</span>

<span style="color:rgb(51,51,51);">第六条 </span><span style="color:rgb(51,51,51);">以上声明的解释权归</span><span style="color:rgb(51,51,51);">“</span><span style="color:rgb(51,51,51);">扬俊的小屋</span><span style="color:rgb(51,51,51);">”</span><span style="color:rgb(51,51,51);">所有。</span>

</div>

</div>

</article>
