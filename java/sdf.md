<div id="topics">

<div class="post">

# [详解Java的自动装箱与拆箱(Autoboxing and unboxing)](https://www.cnblogs.com/wang-yaz/p/8516151.html)

<div class="postBody">

<div id="cnblogs_post_body" class="blogpost-body">

一、什么是自动装箱拆箱   
很简单，下面两句代码就可以看到装箱和拆箱过程

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #008000;">//</span><span style="color: #008000;">自动装箱</span>
<span style="color: #008080;">2</span> Integer total = 99<span style="color: #000000;">;</span> <span style="color: #008080;">3</span> 
<span style="color: #008080;">4</span> <span style="color: #008000;">//</span><span style="color: #008000;">自定拆箱</span>
<span style="color: #008080;">5</span> <span style="color: #0000ff;">int</span> totalprim = total;</pre>

</div>

简单一点说，装箱就是自动将基本数据类型转换为包装器类型；拆箱就是自动将包装器类型转换为基本数据类型。

下面我们来看看需要装箱拆箱的类型有哪些：

![这里写图片描述](http://img.blog.csdn.net/20160329101454749)

![这里写图片描述](http://img.blog.csdn.net/20150922151443893)

这个过程是自动执行的，那么我们需要看看它的执行过程：

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008080;">1</span> <span style="color: #000000;">public class Main {</span> <span style="color: #008080;">2</span>     public static <span style="color: #0000ff;">void</span> <span style="color: #000000;">main(String[] args) {</span> <span style="color: #008080;">3</span>     <span style="color: #008000;">//</span><span style="color: #008000;">自动装箱</span>
<span style="color: #008080;">4</span>     Integer total = 99<span style="color: #000000;">;</span> <span style="color: #008080;">5</span> 
<span style="color: #008080;">6</span>     <span style="color: #008000;">//</span><span style="color: #008000;">自定拆箱</span>
<span style="color: #008080;">7</span>     <span style="color: #0000ff;">int</span> totalprim = <span style="color: #000000;">total;</span> <span style="color: #008080;">8</span> <span style="color: #000000;">}</span> <span style="color: #008080;">9</span> }</pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

反编译class文件之后得到如下内容：

 <span class="cnblogs_code"><span style="color: #008080;">1</span> javap -c StringTest</span> 

![这里写图片描述](http://img.blog.csdn.net/20150922153411441)

Integer total = 99;   
执行上面那句代码的时候，系统为我们执行了：   
Integer total = Integer.valueOf(99);

int totalprim = total;   
执行上面那句代码的时候，系统为我们执行了：   
int totalprim = total.intValue();

我们现在就以Integer为例，来分析一下它的源码：   
1、首先来看看Integer.valueOf函数

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> Integer valueOf(<span style="color: #0000ff;">int</span> <span style="color: #000000;">i) {</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">return</span>  i >= 128 || i < -128 ? <span style="color: #0000ff;">new</span> Integer(i) : SMALL_VALUES[i + 128<span style="color: #000000;">];</span> <span style="color: #008080;">3</span> }</pre>

</div>

它会首先判断i的大小：如果i小于-128或者大于等于128，就创建一个Integer对象，否则执行SMALL_VALUES[i + 128]。

首先我们来看看Integer的构造函数：

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008080;">1</span> <span style="color: #0000ff;">private</span> <span style="color: #0000ff;">final</span> <span style="color: #0000ff;">int</span> <span style="color: #000000;">value;</span> <span style="color: #008080;">2</span> 
<span style="color: #008080;">3</span> <span style="color: #0000ff;">public</span> Integer(<span style="color: #0000ff;">int</span> <span style="color: #000000;">value) {</span> <span style="color: #008080;">4</span>     <span style="color: #0000ff;">this</span>.value = <span style="color: #000000;">value;</span> <span style="color: #008080;">5</span> <span style="color: #000000;">}</span> <span style="color: #008080;">6</span> 
<span style="color: #008080;">7</span> <span style="color: #0000ff;">public</span> Integer(String string) <span style="color: #0000ff;">throws</span> <span style="color: #000000;">NumberFormatException {</span> <span style="color: #008080;">8</span>     <span style="color: #0000ff;">this</span><span style="color: #000000;">(parseInt(string));</span> <span style="color: #008080;">9</span> }</pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

它里面定义了一个value变量，创建一个Integer对象，就会给这个变量初始化。第二个传入的是一个String变量，它会先把它转换成一个int值，然后进行初始化。

下面看看SMALL_VALUES[i + 128]是什么东西：

<pre name="code" class="prettyprint"> <span class="cnblogs_code"><span style="color: #008080;">1</span> <span style="color: #0000ff;">private</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">final</span> Integer[] SMALL_VALUES = <span style="color: #0000ff;">new</span> Integer[256];</span> </pre>

它是一个静态的Integer数组对象，也就是说最终valueOf返回的都是一个Integer对象。

所以我们这里可以总结一点：装箱的过程会创建对应的对象，这个会消耗内存，所以装箱的过程会增加内存的消耗，影响性能。

2、接着看看intValue函数

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #000000;">@Override</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">int</span> <span style="color: #000000;">intValue() {</span> <span style="color: #008080;">3</span>     <span style="color: #0000ff;">return</span> <span style="color: #000000;">value;</span> <span style="color: #008080;">4</span> }</pre>

</div>

这个很简单，直接返回value值即可。

二、相关问题   
上面我们看到在Integer的构造函数中，它分两种情况： 

1、i >= 128 || i < -128 =====> new Integer(i)   
2、i < 128 && i >= -128 =====> SMALL_VALUES[i + 128]

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #0000ff;">private</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">final</span> Integer[] SMALL_VALUES = <span style="color: #0000ff;">new</span> Integer[256];</pre>

</div>

SMALL_VALUES本来已经被创建好，也就是说在i >= 128 || i < -128是会创建不同的对象，在i < 128 && i >= -128会根据i的值返回已经创建好的指定的对象。

说这些可能还不是很明白，下面我们来举个例子吧：

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre> <span style="color: #008080;">1</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">Main {</span> <span style="color: #008080;">2</span>     <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">main(String[] args) {</span> <span style="color: #008080;">3</span> 
 <span style="color: #008080;">4</span>         Integer i1 = 100<span style="color: #000000;">;
</span> <span style="color: #008080;">5</span>         Integer i2 = 100<span style="color: #000000;">;
</span> <span style="color: #008080;">6</span>         Integer i3 = 200<span style="color: #000000;">;
</span> <span style="color: #008080;">7</span>         Integer i4 = 200<span style="color: #000000;">;
</span> <span style="color: #008080;">8</span> 
 <span style="color: #008080;">9</span>         System.out.println(i1==i2);  <span style="color: #008000;">//</span><span style="color: #008000;">true</span>
<span style="color: #008080;">10</span>         System.out.println(i3==i4);  <span style="color: #008000;">//</span><span style="color: #008000;">false</span>
<span style="color: #008080;">11</span> <span style="color: #000000;">}</span> <span style="color: #008080;">12</span> }</pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

代码的后面，我们可以看到它们的执行结果是不一样的，为什么，在看看我们上面的说明。   
1、i1和i2会进行自动装箱，执行了valueOf函数，它们的值在(-128,128]这个范围内，它们会拿到SMALL_VALUES数组里面的同一个对象SMALL_VALUES[228]，它们引用到了同一个Integer对象，所以它们肯定是相等的。

2、i3和i4也会进行自动装箱，执行了valueOf函数，它们的值大于128，所以会执行new Integer(200)，也就是说它们会分别创建两个不同的对象，所以它们肯定不等。

下面我们来看看另外一个例子：

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre> <span style="color: #008080;">1</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">Main {</span> <span style="color: #008080;">2</span>     <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">main(String[] args) {</span> <span style="color: #008080;">3</span> 
 <span style="color: #008080;">4</span>         Double i1 = 100.0<span style="color: #000000;">;
</span> <span style="color: #008080;">5</span>         Double i2 = 100.0<span style="color: #000000;">;
</span> <span style="color: #008080;">6</span>         Double i3 = 200.0<span style="color: #000000;">;
</span> <span style="color: #008080;">7</span>         Double i4 = 200.0<span style="color: #000000;">;
</span> <span style="color: #008080;">8</span> 
 <span style="color: #008080;">9</span>         System.out.println(i1==i2); <span style="color: #008000;">//</span><span style="color: #008000;">false</span>
<span style="color: #008080;">10</span>         System.out.println(i3==i4); <span style="color: #008000;">//</span><span style="color: #008000;">false</span>
<span style="color: #008080;">11</span> <span style="color: #000000;">}</span> <span style="color: #008080;">12</span> }</pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

看看上面的执行结果，跟Integer不一样，这样也不必奇怪，因为它们的valueOf实现不一样，结果肯定不一样，那为什么它们不统一一下呢？   
这个很好理解，因为对于Integer，在(-128,128]之间只有固定的256个值，所以为了避免多次创建对象，我们事先就创建好一个大小为256的Integer数组SMALL_VALUES，所以如果值在这个范围内，就可以直接返回我们事先创建好的对象就可以了。

但是对于Double类型来说，我们就不能这样做，因为它在这个范围内个数是无限的。   
总结一句就是：在某个范围内的整型数值的个数是有限的，而浮点数却不是。

所以在Double里面的做法很直接，就是直接创建一个对象，所以每次创建的对象都不一样。

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> Double valueOf(<span style="color: #0000ff;">double</span> <span style="color: #000000;">d) {</span> <span style="color: #008080;">2</span>     <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">new</span> <span style="color: #000000;">Double(d);</span> <span style="color: #008080;">3</span> }</pre>

</div>

下面我们进行一个归类：   
Integer派别：Integer、Short、Byte、Character、Long这几个类的valueOf方法的实现是类似的。   
Double派别：Double、Float的valueOf方法的实现是类似的。每次都返回不同的对象。

下面对Integer派别进行一个总结，如下图：   
![这里写图片描述](http://img.blog.csdn.net/20150922153039509)

下面我们来看看另外一种情况：

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre> <span style="color: #008080;">1</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">Main {</span> <span style="color: #008080;">2</span>     <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">main(String[] args) {</span> <span style="color: #008080;">3</span> 
 <span style="color: #008080;">4</span>         Boolean i1 = <span style="color: #0000ff;">false</span><span style="color: #000000;">;
</span> <span style="color: #008080;">5</span>         Boolean i2 = <span style="color: #0000ff;">false</span><span style="color: #000000;">;
</span> <span style="color: #008080;">6</span>         Boolean i3 = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
</span> <span style="color: #008080;">7</span>         Boolean i4 = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
</span> <span style="color: #008080;">8</span> 
 <span style="color: #008080;">9</span>         System.out.println(i1==i2);<span style="color: #008000;">//</span><span style="color: #008000;">true</span>
<span style="color: #008080;">10</span>         System.out.println(i3==i4);<span style="color: #008000;">//</span><span style="color: #008000;">true</span>
<span style="color: #008080;">11</span> <span style="color: #000000;">}</span> <span style="color: #008080;">12</span> }</pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

可以看到返回的都是true，也就是它们执行valueOf返回的都是相同的对象。

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> Boolean valueOf(<span style="color: #0000ff;">boolean</span> <span style="color: #000000;">b) {</span> <span style="color: #008080;">2</span>     <span style="color: #0000ff;">return</span> b ? <span style="color: #000000;">Boolean.TRUE : Boolean.FALSE;</span> <span style="color: #008080;">3</span> }</pre>

</div>

可以看到它并没有创建对象，因为在内部已经提前创建好两个对象，因为它只有两种情况，这样也是为了避免重复创建太多的对象。

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">final</span> Boolean TRUE = <span style="color: #0000ff;">new</span> Boolean(<span style="color: #0000ff;">true</span><span style="color: #000000;">);</span> <span style="color: #008080;">2</span> 
<span style="color: #008080;">3</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">final</span> Boolean FALSE = <span style="color: #0000ff;">new</span> Boolean(<span style="color: #0000ff;">false</span>);</pre>

</div>

上面把几种情况都介绍到了，下面来进一步讨论其他情况。

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> Integer num1 = 400<span style="color: #000000;">;</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">int</span> num2 = 400<span style="color: #000000;">;</span> <span style="color: #008080;">3</span> System.out.println(num1 == num2); <span style="color: #008000;">//</span><span style="color: #008000;">true</span></pre>

</div>

<pre name="code" class="prettyprint">说明num1 == num2进行了拆箱操作</pre>

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> Integer num1 = 100<span style="color: #000000;">;</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">int</span> num2 = 100<span style="color: #000000;">;</span> <span style="color: #008080;">3</span> System.out.println(num1.equals(num2));  <span style="color: #008000;">//</span><span style="color: #008000;">true</span></pre>

</div>

我们先来看看equals源码：

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #000000;">@Override</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">boolean</span> <span style="color: #000000;">equals(Object o) {</span> <span style="color: #008080;">3</span>     <span style="color: #0000ff;">return</span> (o <span style="color: #0000ff;">instanceof</span> Integer) && (((Integer) o).value == <span style="color: #000000;">value);</span> <span style="color: #008080;">4</span> }</pre>

</div>

我们指定equal比较的是内容本身，并且我们也可以看到equal的参数是一个Object对象，我们传入的是一个int类型，所以首先会进行装箱，然后比较，之所以返回true，是由于它比较的是对象里面的value值。

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> Integer num1 = 100<span style="color: #000000;">;</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">int</span> num2 = 100<span style="color: #000000;">;</span> <span style="color: #008080;">3</span> Long num3 = 200l<span style="color: #000000;">;</span> <span style="color: #008080;">4</span> System.out.println(num1 + num2);  <span style="color: #008000;">//</span><span style="color: #008000;">200</span>
<span style="color: #008080;">5</span> System.out.println(num3 == (num1 + num2));  <span style="color: #008000;">//</span><span style="color: #008000;">true</span>
<span style="color: #008080;">6</span> System.out.println(num3.equals(num1 + num2));  <span style="color: #008000;">//</span><span style="color: #008000;">false</span></pre>

</div>

1、当一个基础数据类型与封装类进行==、+、-、*、/运算时，会将封装类进行拆箱，对基础数据类型进行运算。   
2、对于num3.equals(num1 + num2)为false的原因很简单，我们还是根据代码实现来说明：

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #000000;">@Override</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">boolean</span> <span style="color: #000000;">equals(Object o) {</span> <span style="color: #008080;">3</span>     <span style="color: #0000ff;">return</span> (o <span style="color: #0000ff;">instanceof</span> Long) && (((Long) o).value == <span style="color: #000000;">value);</span> <span style="color: #008080;">4</span> }</pre>

</div>

它必须满足两个条件才为true：   
1、类型相同   
2、内容相同   
上面返回false的原因就是类型不同。

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> Integer num1 = 100<span style="color: #000000;">;</span> <span style="color: #008080;">2</span> Ingeger num2 = 200<span style="color: #000000;">;</span> <span style="color: #008080;">3</span> Long num3 = 300l<span style="color: #000000;">;</span> <span style="color: #008080;">4</span> System.out.println(num3 == (num1 + num2)); <span style="color: #008000;">//</span><span style="color: #008000;">true</span></pre>

</div>

我们来反编译一些这个class文件：javap -c StringTest   
![这里写图片描述](http://img.blog.csdn.net/20150922153446481)

可以看到运算的时候首先对num3进行拆箱（执行num3的longValue得到基础类型为long的值300），然后对num1和mum2进行拆箱（分别执行了num1和num2的intValue得到基础类型为int的值100和200），然后进行相关的基础运算。

我们来对基础类型进行一个测试：

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span> <span style="color: #0000ff;">int</span> num1 = 100<span style="color: #000000;">;</span> <span style="color: #008080;">2</span> <span style="color: #0000ff;">int</span> num2 = 200<span style="color: #000000;">;</span> <span style="color: #008080;">3</span> <span style="color: #0000ff;">long</span> mum3 = 300<span style="color: #000000;">;</span> <span style="color: #008080;">4</span> System.out.println(num3 == (num1 + num2)); <span style="color: #008000;">//</span><span style="color: #008000;">true</span></pre>

</div>

就说明了为什么最上面会返回true.

所以，当 “==”运算符的两个操作数都是 包装器类型的引用，则是比较指向的是否是同一个对象，而如果其中有一个操作数是表达式（即包含算术运算）则比较的是数值（即会触发自动拆箱的过程）。

陷阱1：

<div class="cnblogs_code">

<pre><span style="color: #008080;">1</span>  Integer integer100=<span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #008080;">2</span>  <span style="color: #0000ff;">int</span> int100=integer100;</pre>

</div>

这两行代码是完全合法的，完全能够通过编译的，但是在运行时，就会抛出空指针异常。其中，integer100为Integer类型的对象，它当然可以指向null。但在第二行时，就会对integer100进行拆箱，也就是对一个null对象执行intValue()方法，当然会抛出空指针异常。所以，有拆箱操作时一定要特别注意封装类对象是否为null。

总结：   
1、需要知道什么时候会引发装箱和拆箱   
2、装箱操作会创建对象，频繁的装箱操作会消耗许多内存，影响性能，所以可以避免装箱的时候应该尽量避免。

3、equals(Object o) 因为原equals方法中的参数类型是封装类型，所传入的参数类型（a）是原始数据类型，所以会自动对其装箱，反之，会对其进行拆箱

4、当两种不同类型用==比较时，包装器类的需要拆箱， 当同种类型用==比较时，会自动拆箱或者装箱

</div>

<div id="MySignature" style="display: block;">hello world!!!</div>

<div id="blog_post_info_block">

<div id="BlogPostCategory">分类: [JAVA](https://www.cnblogs.com/wang-yaz/category/1157139.html)</div>

<div id="EntryTag">标签: [Java](https://www.cnblogs.com/wang-yaz/tag/Java/)</div>

<div id="blog_post_info">

<div id="green_channel">[好文要顶](javascript:void(0);) [关注我](javascript:void(0);) [收藏该文](javascript:void(0);) [![](//common.cnblogs.com/images/icon_weibo_24.png)](javascript:void(0); "分享至新浪微博") [![](//common.cnblogs.com/images/wechat.png)](javascript:void(0); "分享至微信")</div>

<div id="author_profile">

<div id="author_profile_info" class="author_profile_info">[![](//pic.cnblogs.com/face/1327924/20180131113602.png)](https://home.cnblogs.com/u/wang-yaz/)

<div id="author_profile_detail" class="author_profile_info">[低调的小白](https://home.cnblogs.com/u/wang-yaz/)  
[关注 - 10](https://home.cnblogs.com/u/wang-yaz/followees)  
[粉丝 - 34](https://home.cnblogs.com/u/wang-yaz/followers)</div>

</div>

<div id="author_profile_follow">[+加关注](javascript:void(0);)</div>

</div>

<div id="div_digg">

<div class="diggit" onclick="votePost(8516151,'Digg')"><span class="diggnum" id="digg_count">13</span></div>

<div class="buryit" onclick="votePost(8516151,'Bury')"><span class="burynum" id="bury_count">0</span></div>

</div>

<script type="text/javascript">currentDiggType = 0;</script></div>

<div id="post_next_prev">[«](https://www.cnblogs.com/wang-yaz/p/8467130.html) 上一篇：[Spring bean的生命周期详解](https://www.cnblogs.com/wang-yaz/p/8467130.html "发布于2018-02-24 17:38")  
[»](https://www.cnblogs.com/wang-yaz/p/8560054.html) 下一篇：[Java 多线程异步处理demo](https://www.cnblogs.com/wang-yaz/p/8560054.html "发布于2018-03-13 18:24")  
</div>

</div>

</div>

<div class="postDesc">posted @ <span id="post-date">2018-03-07 11:57</span> [低调的小白](https://www.cnblogs.com/wang-yaz/) 阅读(<span id="post_view_count">18821</span>) 评论(<span id="post_comment_count">6</span>) [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=8516151) [收藏](#)</div>

</div>

<script type="text/javascript">var allowComments=true,cb_blogId=409715,cb_entryId=8516151,cb_blogApp=currentBlogApp,cb_blogUserGuid='ebae133e-7e69-46bf-391f-08d54dbac325',cb_entryCreatedDate='2018/3/7 11:57:00';loadViewCount(cb_entryId);var cb_postType=1;var isMarkdown=false;</script></div>
