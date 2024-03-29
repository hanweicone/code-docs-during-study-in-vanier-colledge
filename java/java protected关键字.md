<div id="content_views" class="markdown_views">
            <!-- flowchart 箭头图标 勿删 -->
            <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
              <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
            </svg>
            <p><strong>摘要：</strong></p>

<p>　　对于类的成员而言，其能否被其他类所访问，取决于该成员的修饰词；而对于一个类而言，其能否被其他类所访问，也取决于该类的修饰词。在Java中，类成员访问权限修饰词有四类：private，无（包访问权限），protected 和 public，而其中只有包访问权限和public才能修饰一个类（内部类除外）。特别地，很多Java书籍对protected可见性的介绍都比较笼统，本文重点说明了protected关键字的可见性内涵，并介绍了一些其他的修饰符。</p>

<hr>

<p><strong>版权声明：</strong></p>

<p>本文原创作者：<a href="http://my.csdn.net/justloveyou_" rel="nofollow" target="_blank">书呆子Rico</a> <br>
作者博客地址：<a href="http://blog.csdn.net/justloveyou_/" rel="nofollow" target="_blank">http://blog.csdn.net/justloveyou_/</a></p>

<hr>

<h2 id="一-package"><a name="t0"></a>一. Package</h2>

<p>　关于包的使用，只需注意一点：<font color="red">在一个项目中，不可以有相同的两个包名，也就是说，包名不能和项目中其他的包名重复，这里不但包括自定义包名也包括项目所引用的类库的包名。</font>看下面例子：</p>



<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-keyword">package</span> java.lang;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyObject</span> {</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String[] args) <span class="hljs-keyword">throws</span> CloneNotSupportedException {
        Object o = <span class="hljs-keyword">new</span> Object();
        System.out.println(o.hashCode());
    }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>

<p>　我们给自己的程序设置的包名是java.lang，事实上，java.lang是JDK使用的包名。这时，程序可以正常编译，但当我们运行程序时会有包冲突警告并抛出 “java.lang.SecurityException: Prohibited package name: java.lang”，如下图所示:</p>

<p>　　　　　　　<img src="http://static.zybuluo.com/Rico123/2y7noxdpq8q9tkajpqcj1ml3/%E5%8C%85%E5%86%B2%E7%AA%81.png" alt="包冲突.png-7kB" title=""></p>

<p>　　　　<img src="http://static.zybuluo.com/Rico123/mitxxpl6xijwgfsgfsbp0m9k/Package.png" alt="Package.png-46.2kB" title=""></p>

<p>　此外，我们需要注意：在程序中，package语句必须是文件中除注释外第一句程序代码，否则不能通过编译。</p>

<hr>

<h2 id="二-java访问权限概述"><a name="t1"></a>二. Java访问权限概述</h2>

<p>　　 对于一个类，其成员（包括成员变量和成员方法）能否被其他类所访问，取决于该成员的修饰词。在Java中，类成员的访问权限修饰词有四个：private，无（包访问权限），protected 和 public，其权限控制如下表所示：</p>

<p>　　　　　<img src="http://static.zybuluo.com/Rico123/mybpgsljdfu9hn5ojot0x66n/Java%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90%E6%8E%A7%E5%88%B6.png" alt="Java访问权限控制.png-10.7kB" title=""></p>

<p>　　特别要注意的是，不同于类成员的访问权限类别，对于非内部类而言，类的访问权限修饰词仅有public和包访问权限两种（内部类可以是private或protected的，关于内部类进一步了解请见我的博客<a href="http://blog.csdn.net/justloveyou_/article/details/53245561" rel="nofollow" target="_blank">《Java 内部类综述》</a>）。特别地，如果你不希望其他任何人对该类拥有访问权，你可以把所有的构造器都指定为private的，从而阻止任何人创建该类的对象。这个时候，该类的对象就只能在其static成员内部进行创建，这种情形有点像单例模式，例如像下面的例子那样：</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"> class Test {
       <span class="hljs-comment">// private Constructor!</span>
       <span class="hljs-keyword">private</span> <span class="hljs-title">Test</span>() {}
       <span class="hljs-comment">// Allow creation via static method:</span>
       <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Test <span class="hljs-title">getTest</span>() {
           <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Test();
       }
    }<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li></ul></pre>

<p>　　在上面所提到的四种修饰词中，除 protected 外都很好理解和掌握，在此略作简述：</p>

<ul>
<li><p>public ：被public修饰的类成员能被所有的类直接访问；</p></li>
<li><p>private：被public修饰的类成员只能在定义它的类中被访问，其他类都访问不到。特别地，我们一般建议将成员变量设为private的，并为外界提供 getter/setter 去对成员变量进行访问，这种做法充分体现了Java的封装思想；</p></li>
<li><p>包访问权限：包访问权限就是Java中的默认的权限，具有包访问权限的类成员只能被同一包中的类访问。</p>

<p>　　由于 protected 关键字的可见性内涵不太容易理解，我们在下一节专门进行介绍。</p></li>
</ul>

<hr>

<h2 id="三-protected-关键字的真正内涵"><a name="t2"></a>三. protected 关键字的真正内涵</h2>

<p>　　很多介绍Java语言的书籍(包括《Java编程思想》)都对protected介绍的比较的简单，基本都是一句话，就是:<font color="red">被protected修饰的成员对于本包和其子类可见。</font>这种说法有点太过含糊，常常会对大家造成误解。实际上，protected的可见性在于两点：</p>

<ul>
<li><p><font color="red">基类的protected成员是包内可见的，并且对子类可见；</font></p></li>
<li><p><font color="red">若子类与基类不在同一包中，那么在子类中，子类实例可以访问其从基类继承而来的protected方法，而不能访问基类实例的protected方法。</font></p></li>
</ul>

<p>我们可以通过以下几个关于protected方法可见性的例子来进一步掌握protected关键字。<font color="red"><b>在碰到涉及protected成员的调用时，首先要确定出该protected成员来自何方，其可见性范围是什么，然后就可以判断出当前用法是否可行了，</b></font>看下面七个例子：</p>

<hr>

<p>(1)、示例一</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-comment">//示例一</span>
<span class="hljs-keyword">package</span> p1;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Father1</span> {</span>
    <span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">f</span>() {}    <span class="hljs-comment">// 父类Father1中的protected方法</span>
}

<span class="hljs-keyword">package</span> p1;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son1</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Father1</span> {</span>}

<span class="hljs-keyword">package</span> p11;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Son11</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Father1</span>{</span>}

<span class="hljs-keyword">package</span> p1;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test1</span> {</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String[] args) {
        Son1 son1 = <span class="hljs-keyword">new</span> Son1();
        son1.f(); <span class="hljs-comment">// Compile OK     ----（1）</span>
        son1.clone(); <span class="hljs-comment">// Compile Error     ----（2）</span>

        Son11 son = <span class="hljs-keyword">new</span> Son11();    
        son11.f(); <span class="hljs-comment">// Compile OK     ----（3）</span>
        son11.clone(); <span class="hljs-comment">// Compile Error     ----（4）</span>
    }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li></ul></pre>

<p>　　对于上面的示例，首先看(1)(3)，其中的f()方法从类Father1继承而来，其可见性是包p1及其子类Son1和Son11，而由于调用f()方法的类Test1所在的包也是p1，因此（1）(3)处编译通过。其次看(2)(4)，其中的clone()方法的可见性是java.lang包及其所有子类，对于语句“son1.clone();”和“son11.clone();”，二者的clone()在类Son1、Son11中是可见的，但对Test1是不可见的，因此（1）(3)处编译不通过。</p>

<hr>

<p>(2)、示例二</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-comment">//示例二</span>
<span class="hljs-keyword">package</span> p2;
class MyObject2 {
    <span class="hljs-keyword">protected</span> Object <span class="hljs-title">clone</span>() <span class="hljs-keyword">throws</span> CloneNotSupportedException{
       <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.clone();
    }
}

<span class="hljs-keyword">package</span> p22;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test2</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">MyObject2</span> {</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String args[]) {
       MyObject2 obj = <span class="hljs-keyword">new</span> MyObject2();
       obj.clone(); <span class="hljs-comment">// Compile Error         ----（1）</span>

       Test2 tobj = <span class="hljs-keyword">new</span> Test2();
       tobj.clone(); <span class="hljs-comment">// Complie OK         ----（2）</span>
    }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li></ul></pre>

<p>　　对于(1)而言，clone()方法来自于类MyObject2本身，因此其可见性为包p2及MyObject2的子类，虽然Test2是MyObject2的子类，但在Test2中不能访问基类MyObject2的protected方法clone()，因此编译不通过;对于(2)而言，由于在Test2中访问的是其本身实例的从基类MyObject2继承来的的clone()，因此编译通过。</p>

<hr>

<p>(3)、示例三</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-comment">//示例三</span>
<span class="hljs-keyword">package</span> p3;
class MyObject3 extends Test3 {
}

<span class="hljs-keyword">package</span> p33;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test3</span> {</span>
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String args[]) {
    MyObject3 obj = <span class="hljs-keyword">new</span> MyObject3();
    obj.clone();   <span class="hljs-comment">// Compile OK     ------（1）</span>
  }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>

<p>　　对于(1)而言，clone()方法来自于类Test3，因此其可见性为包p33及其子类MyObject3，而（1）正是在p33的类Test3中调用，属于同一包，编译通过。</p>

<hr>

<p>(4)、示例四</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-comment">//示例四</span>
<span class="hljs-keyword">package</span> p4;
class MyObject4 extends Test4 {
  <span class="hljs-keyword">protected</span> Object <span class="hljs-title">clone</span>() <span class="hljs-keyword">throws</span> CloneNotSupportedException {
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.clone();
  }
}

<span class="hljs-keyword">package</span> p44;
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test4</span> {</span>
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String args[]) {
    MyObject4 obj = <span class="hljs-keyword">new</span> MyObject4();
    obj.clone(); <span class="hljs-comment">// Compile Error      -----（1）</span>
  }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li></ul></pre>

<p>　　对于(1)而言，clone()方法来自于类MyObject4，因此其可见性为包p4及其子类(此处没有子类)，而类Test4却在包p44中，因此不满足可见性，编译不通过。</p>

<hr>

<p>(5)、示例五</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-comment">//示例五</span>
<span class="hljs-keyword">package</span> p5;

class MyObject5 {
    <span class="hljs-keyword">protected</span> Object <span class="hljs-title">clone</span>() <span class="hljs-keyword">throws</span> CloneNotSupportedException{
       <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.clone();
    }
}
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test5</span> {</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String[] args) <span class="hljs-keyword">throws</span> CloneNotSupportedException {
       MyObject5 obj = <span class="hljs-keyword">new</span> MyObject5();
       obj.clone(); <span class="hljs-comment">// Compile OK        ----(1)</span>
    }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li></ul></pre>

<p>　　对于(1)而言，clone()方法来自于类MyObject5，因此其可见性为包p5及其子类(此处没有子类)，而类Test5也在包p5中，因此满足可见性，编译通过。</p>

<hr>

<p>(6)、示例六</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-comment">//示例六</span>
<span class="hljs-keyword">package</span> p6;

class MyObject6 extends Test6{}
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test6</span> {</span>
  <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String[] args) {
    MyObject6 obj = <span class="hljs-keyword">new</span> MyObject6();
    obj.clone();        <span class="hljs-comment">// Compile OK   -------（1）</span>
  }
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li></ul></pre>

<p>　　对于(1)而言，clone()方法来自于类Test6，因此其可见性为包p6及其子类MyObject6，而类Test6也在包p6中，因此满足可见性，编译通过。</p>

<hr>

<p>(7)、示例七</p>

<pre class="prettyprint" name="code"><code class="language-java hljs  has-numbering" onclick="mdcp.signin(event)"><span class="hljs-comment">//示例七</span>
<span class="hljs-keyword">package</span> p7;

class MyObject7 extends Test7 {
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String[] args) {
        Test7 test = <span class="hljs-keyword">new</span> Test7();
        test.clone(); <span class="hljs-comment">// Compile Error   ----- (1)</span>
  }
}

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test7</span> {</span>
}<div class="hljs-button signin" data-title="登录后复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li></ul></pre>

<p>　　对于(1)而言，clone()方法来自于类Object，因此该clone()方法可见性为包java.lang及其子类Test7，由于类MyObject7不在此范围内，因此不满足可见性，编译不通过。</p>

<hr>

<h2 id="四-其他的修饰符"><a name="t3"></a>四. 其他的修饰符</h2>

<p>　　static：修饰变量和内部类(不能修饰常规类)，其中所修饰变量称为类变量或静态变量。静态变量是和类层次的变量,每个实例共享这个静态变量，在类加载时初始化。</p>

<p>　　final：被声明为final的变量必须在声明时给定初值（当然，空白final可以延迟到构造器中赋值），而且被修饰的变量不能修改值。当修饰类时，该类不能派生出子类；修饰方法时，该方法不能被子类覆盖。若读者想对final关键字有一个更深刻的了解，请移步我的博文 <a href="http://blog.csdn.net/justloveyou_/article/details/52798666" rel="nofollow" target="_blank">《Java 继承、多态与类的复用》</a>。</p>

<p>　　abstract：修饰类和方法。当修饰类时，该类不能创建对象；修饰方法时，为抽象方法。类只要有一个abstract方法，类就必须定义为abstract，但abstract类不一定非要有abstract方法不可。</p>

<hr>



<h2 id="五-总结"><a name="t4"></a>五. 总结</h2>

<p>　　protected是最难理解的一种Java类成员访问权限修饰词。在编程中，碰到涉及protected的调用时，首先要确定出该protected成员来自何方，其可见性范围是什么，然后就正确无误的使用了。</p>

<hr>



<h2 id="六-说明"><a name="t5"></a>六. 说明</h2>

<p>　　在综述《Java 访问权限控制：你真的了解 protected 关键字吗？》的过程中，我们涉及到了很多知识点，其中有一些我们已经在其他博文中专门提到过，因此没有作更多详细的阐述，这里给出对应的链接：</p>

<p>　若读者想深入了解 Java 内部类，请移步我的博文<a href="http://blog.csdn.net/justloveyou_/article/details/53245561" rel="nofollow" target="_blank">《Java 内部类综述》</a>； <br>
　若读者想深入了解 final关键字，请移步我的博文<a href="http://blog.csdn.net/justloveyou_/article/details/52798666" rel="nofollow" target="_blank">《Java 继承、多态与类的复用》</a>。 <br>
　若读者想深入了解 Java 克隆，请移步我的博文<a href="http://blog.csdn.net/justloveyou_/article/details/60983034" rel="nofollow" target="_blank">《 Java String 综述(下篇)》</a>，本文用一个小节专门阐述了在Java中克隆的原理和使用方式，并揭示了String对象在克隆过程中的特殊性。</p>

<hr>

<blockquote>
  <h2 id="引用"><a name="t6"></a>引用</h2>
  
  <p><a href="http://blog.csdn.net/ciawow/article/details/8262609" rel="nofollow" target="_blank">JAVA中的protected（详解），以及和clone（）方法有关的一些问题</a> <br>
  <a href="http://www.cnblogs.com/0201zcr/p/4852272.html" rel="nofollow" target="_blank">java的访问权限</a> <br>
  <a href="http://www.cnblogs.com/ldq2016/p/5261345.html" rel="nofollow" target="_blank">Java基础详解 （一）Java的类成员访问权限修饰词（以及类访问权限）</a></p>
</blockquote>          </div>
