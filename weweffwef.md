<div class="blog-content-box">
  <div class="article-header-box">
    <div class="article-header">
      <div class="article-title-box">
        <span class="article-type type-2 float-left">转</span>        

# [java]static关键字的四种用法和void的用法

      </div>
      <div class="article-info-box">
        <div class="article-bar-top">
                                                  <span class="time">2018年05月30日 11:16:25</span>
          [xxm0720](https://me.csdn.net/xxm0720)
          <span class="read-count">阅读数：2121</span>
                  </div>
        <div class="operating">
                  </div>
      </div>
    </div>
  </div>
  <article class="baidu_pl">
    <div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post" style="height: 3126px; overflow: hidden;">
            <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">
                              <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">
          <div class="htmledit_views" id="content_views">

<span style="font-family:'-apple-system', 'SF UI Text', Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'WenQuanYi Micro Hei', sans-serif, SimHei, SimSun;background-color:rgb(255,255,255);">void关键字表示函数没有返回结果，是java中的一个关键字。</span>

<span style="font-family:'-apple-system', 'SF UI Text', Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'WenQuanYi Micro Hei', sans-serif, SimHei, SimSun;background-color:rgb(255,255,255);"><span style="font-family:'-apple-system', 'SF UI Text', Arial, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'WenQuanYi Micro Hei', sans-serif, SimHei, SimSun;background-color:rgb(255,255,255);">Void作为函数的返回结果表示函数返回null(除了null不能返回其它类型)。</span>
</span>

在java的关键字中，<span style="margin:0px;padding:0px;">static</span>和<span style="margin:0px;padding:0px;">final</span>是两个我们必须掌握的关键字。不同于其他关键字，他们都有多种用法，而且在一定环境下使用，可以提高程序的运行性能，优化程序的结构。下面我们先来了解一下static关键字及其用法。

## <a name="t0"></a>static关键字

### <a name="t1"></a>1.修饰成员变量

在我们平时的使用当中，static最常用的功能就是修饰类的属性和方法，让他们成为类的成员属性和方法，我们通常将用static修饰的成员称为类成员或者静态成员，这句话挺起来都点奇怪，其实这是相对于对象的属性和方法来说的。请看下面的例子：（未避免程序太过臃肿，暂时不管访问控制）
<pre><div class="hljs-button {2}" data-title="复制" onclick="hljs.copyCode(event)"></div></pre><pre class="java" name="code">`

1.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="1"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">public class Person {</div></div>
2.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="2"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    String name;</div></div>
3.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="3"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    int age;</div></div>
4.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="4"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
5.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="5"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    public String toString() {</div></div>
6.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="6"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        return "Name:" + name + ", Age:" + age;</div></div>
7.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="7"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
8.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="8"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
9.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="9"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    public static void main(String[] args) {</div></div>
10.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="10"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        Person p1 = new Person();</div></div>
11.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="11"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        p1.name = "zhangsan";</div></div>
12.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="12"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        p1.age = 10;</div></div>
13.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="13"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        Person p2 = new Person();</div></div>
14.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="14"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        p2.name = "lisi";</div></div>
15.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="15"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        p2.age = 12;</div></div>
16.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="16"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(p1);</div></div>
17.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="17"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(p2);</div></div>
18.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="18"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
19.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="19"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    /**Output</div></div>
20.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="20"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">     * Name:zhangsan, Age:10</div></div>
21.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="21"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">     * Name:lisi, Age:12</div></div>
22.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="22"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">     *///~</div></div>
23.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="23"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">}</div></div>`<div class="hljs-button {2}" data-title="复制" onclick="hljs.copyCode(event)"></div></pre>

<span style="color:rgb(0,0,0);font-family:Verdana, Arial, Helvetica, sans-serif;font-size:13px;text-align:left;background-color:rgb(254,254,242);">上面的代码我们很熟悉，根据Person构造出的每一个对象都是独立存在的，保存有自己独立的成员变量，相互不会影响，他们在内存中的示意如下:</span>

<span style="color:rgb(0,0,0);font-family:Verdana, Arial, Helvetica, sans-serif;font-size:13px;text-align:left;background-color:rgb(254,254,242);">![](https://images2015.cnblogs.com/blog/1055692/201701/1055692-20170128111659941-455494498.jpg)
</span>

<span style="color:rgb(0,0,0);font-family:Verdana, Arial, Helvetica, sans-serif;font-size:13px;text-align:left;background-color:rgb(254,254,242);"><span style="color:rgb(0,0,0);font-family:Verdana, Arial, Helvetica, sans-serif;font-size:13px;text-align:left;background-color:rgb(254,254,242);">从上图中可以看出，p1和p2两个变量引用的对象分别存储在内存中堆区域的不同地址中，所以他们之间相互不会干扰。但其实，在这当中，我们省略了一些重要信息，相信大家也都会想到，对象的成员属性都在这了，由每个对象自己保存，那么他们的方法呢？实际上，不论一个类创建了几个对象，他们的方法都是一样的：</span>![](https://images2015.cnblogs.com/blog/1055692/201701/1055692-20170129182729316-1860809324.jpg)
</span>

<span style="color:rgb(0,0,0);font-family:Verdana, Arial, Helvetica, sans-serif;font-size:13px;text-align:left;background-color:rgb(254,254,242);"></span>

从上面的图中我们可以看到，两个Person对象的方法实际上只是指向了同一个方法定义。这个方法定义是位于内存中的一块不变区域（由jvm划分），我们暂称它为静态存储区。这一块存储区不仅存放了方法的定义，实际上从更大的角度而言，它存放的是各种类的定义，当我们通过new来生成对象时，会根据这里定义的类的定义去创建对象。多个对象仅会对应同一个方法，这里有一个让我们充分信服的理由，那就是不管多少的对象，他们的方法总是相同的，尽管最后的输出会有所不同，但是方法总是会按照我们预想的结果去操作，即不同的对象去调用同一个方法，结果会不尽相同。

我们知道，static关键字可以修饰成员变量和方法，来让它们变成类的所属，而不是对象的所属，比如我们将Person的age属性用static进行修饰，结果会是什么样呢？请看下面的例子：

<pre>`

1.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="1"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>{</div></div>
2.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="2"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    String name;</div></div>
3.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="3"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span> age;</div></div>
4.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="4"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
5.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="5"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-comment">/* 其余代码不变... */</span></div></div>
6.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="6"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"> </div></div>
7.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="7"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-comment"><span class="hljs-comment">/**Output</span></span></div></div>
8.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="8"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * Name:zhangsan, Age:12</span></div></div>
9.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="9"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * Name:lisi, Age:12</span></div></div>
10.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="10"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     */</span><span class="hljs-comment">//~</span></div></div>
11.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="11"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">}</div></div>`<div class="hljs-button {2}" data-title="复制" onclick="hljs.copyCode(event)"></div></pre>

<span style="color:rgb(0,0,0);font-family:Verdana, Arial, Helvetica, sans-serif;font-size:13px;text-align:left;background-color:rgb(254,254,242);">我们发现，结果发生了一点变化，在给p2的age属性赋值时，干扰了p1的age属性，这是为什么呢？我们还是来看他们在内存中的示意：</span>![](https://images2015.cnblogs.com/blog/1055692/201701/1055692-20170129182741362-1771285007.jpg)

我们发现，给age属性加了<span style="margin:0px;padding:0px;">static</span>关键字之后，Person对象就不再拥有age属性了，age属性会统一交给Person类去管理，即多个Person对象只会对应一个age属性，一个对象如果对age属性做了改变，其他的对象都会受到影响。我们看到此时的age和toString()方法一样，都是交由类去管理。

虽然我们看到static可以让对象共享属性，但是实际中我们很少这么用，也不推荐这么使用。因为这样会让该属性变得难以控制，因为它在任何地方都有可能被改变。如果我们想共享属性，一般我们会采用其他的办法：
<pre style="margin-bottom:0px;padding-right:0px;padding-left:0px;white-space:pre-wrap;text-align:left;font-family:'Courier New';"><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">class</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person {
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">private</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">int</span> count = 0<span style="margin:0px;padding:0px;line-height:1.5;">;
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">int</span><span style="margin:0px;padding:0px;line-height:1.5;"> id;
    String name;
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">int</span><span style="margin:0px;padding:0px;line-height:1.5;"> age;

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person() {
        id </span>= ++count<span style="margin:0px;padding:0px;line-height:1.5;">;
    }

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span><span style="margin:0px;padding:0px;line-height:1.5;"> String toString() {
        </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">return</span> "Id:" + id + ", Name:" + name + ", Age:" +<span style="margin:0px;padding:0px;line-height:1.5;"> age;
    }

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">void</span><span style="margin:0px;padding:0px;line-height:1.5;"> main(String[] args) {
        Person p1 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person();
        p1.name </span>= "zhangsan"<span style="margin:0px;padding:0px;line-height:1.5;">;
        p1.age </span>= 10<span style="margin:0px;padding:0px;line-height:1.5;">;
        Person p2 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person();
        p2.name </span>= "lisi"<span style="margin:0px;padding:0px;line-height:1.5;">;
        p2.age </span>= 12<span style="margin:0px;padding:0px;line-height:1.5;">;
        System.out.println(p1);
        System.out.println(p2);
    }
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">/**</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">Output
     * Id:1, Name:zhangsan, Age:10
     * Id:2, Name:lisi, Age:12
     </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">*///</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">~</span>
}</pre>

上面的代码起到了给Person的对象创建一个唯一id以及记录总数的作用，其中count由static修饰，是Person类的成员属性，每次创建一个Person对象，就会使该属性自加1然后赋给对象的id属性，这样，count属性记录了创建Person对象的总数，由于count使用了private修饰，所以从类外面无法随意改变。

### <a name="t2"></a>2.修饰成员方法

static的另一个作用，就是修饰成员方法。相比于修饰成员属性，修饰成员方法对于数据的存储上面并没有多大的变化，因为我们从上面可以看出，方法本来就是存放在类的定义当中的。static修饰成员方法最大的作用，就是可以使用"<span style="margin:0px;padding:0px;">类名.方法名</span>"的方式操作方法，避免了先要new出对象的繁琐和资源消耗，我们可能会经常在帮助类中看到它的使用：

<pre>`

1.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="1"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrintHelper</span> </span>{</div></div>
2.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="2"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"> </div></div>
3.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="3"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">print</span><span class="hljs-params">(Object o)</span></span>{</div></div>
4.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="4"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(o);</div></div>
5.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="5"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
6.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="6"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
7.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="7"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>{</div></div>
8.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="8"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        PrintHelper.print(<span class="hljs-string">"Hello world"</span>);</div></div>
9.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="9"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
10.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="10"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">}</div></div>`<div class="hljs-button {2}" data-title="复制" onclick="hljs.copyCode(event)"></div></pre>

上面便是一个例子（现在还不太实用），但是我们可以看到它的作用，使得static修饰的方法成为类的方法，使用时通过“<span style="margin:0px;padding:0px;">类名.方法名</span>”的方式就可以方便的使用了，相当于定义了一个全局的函数（只要导入该类所在的包即可）。不过它也有使用的局限，一个static修饰的类中，不能使用非static修饰的成员变量和方法，这很好理解，因为static修饰的方法是属于类的，如果去直接使用对象的成员变量，它会不知所措（不知该使用哪一个对象的属性）。

### <a name="t3"></a>3.静态块

在说明static关键字的第三个用法时，我们有必要重新梳理一下一个对象的初始化过程。以下面的代码为例：
<pre>
<div class="cnblogs_code" style="margin:5px 0px;padding:5px;background-color:rgb(245,245,245);border:1px solid rgb(204,204,204);color:rgb(0,0,0);text-align:left;font-family:'Courier New';font-size:12px;"><pre style="margin-bottom:0px;padding-right:0px;padding-left:0px;white-space:pre-wrap;font-family:'Courier New';"><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">package</span><span style="margin:0px;padding:0px;line-height:1.5;"> com.dotgua.study;

</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">class</span><span style="margin:0px;padding:0px;line-height:1.5;"> Book{
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span><span style="margin:0px;padding:0px;line-height:1.5;"> Book(String msg) {
        System.out.println(msg);
    }
}

</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">class</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person {

    Book book1 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("book1成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> Book book2 = <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("static成员book2成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person(String msg) {
        System.out.println(msg);
    }

    Book book3 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("book3成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> Book book4 = <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("static成员book4成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">void</span><span style="margin:0px;padding:0px;line-height:1.5;"> main(String[] args) {
        Person p1 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Person("p1初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);
    }
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">/**</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">Output
     * static成员book2成员变量初始化
     * static成员book4成员变量初始化
     * book1成员变量初始化
     * book3成员变量初始化
     * p1初始化
     </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">*///</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">~</span>
}</pre></div>

&nbsp;上面的例子中，Person类中组合了四个Book成员变量，两个是普通成员，两个是static修饰的类成员。我们可以看到，当我们new一个Person对象时，static修饰的成员变量首先被初始化，随后是普通成员，最后调用Person类的构造方法完成初始化。也就是说，在创建对象时，static修饰的成员会首先被初始化，而且我们还可以看到，如果有多个static修饰的成员，那么会按照他们的先后位置进行初始化。

实际上，static修饰的成员的初始化可以更早的进行，请看下面的例子：
<div class="cnblogs_code" style="margin:5px 0px;padding:5px;background-color:rgb(245,245,245);border:1px solid rgb(204,204,204);color:rgb(0,0,0);text-align:left;font-family:'Courier New';font-size:12px;"><div class="cnblogs_code_toolbar" style="margin:5px 0px 0px;padding:0px;">
</div><pre style="margin-bottom:0px;padding-right:0px;padding-left:0px;white-space:pre-wrap;font-family:'Courier New';"><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">class</span><span style="margin:0px;padding:0px;line-height:1.5;"> Book{
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span><span style="margin:0px;padding:0px;line-height:1.5;"> Book(String msg) {
        System.out.println(msg);
    }
}

</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">class</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person {

    Book book1 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("book1成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> Book book2 = <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("static成员book2成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span><span style="margin:0px;padding:0px;line-height:1.5;"> Person(String msg) {
        System.out.println(msg);
    }

    Book book3 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("book3成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> Book book4 = <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Book("static成员book4成员变量初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">void</span><span style="margin:0px;padding:0px;line-height:1.5;"> funStatic() {
        System.out.println(</span>"static修饰的funStatic方法"<span style="margin:0px;padding:0px;line-height:1.5;">);
    }

    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">public</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">static</span> <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">void</span><span style="margin:0px;padding:0px;line-height:1.5;"> main(String[] args) {
        Person.funStatic();
        System.out.println(</span>"****************"<span style="margin:0px;padding:0px;line-height:1.5;">);
        Person p1 </span>= <span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,0,255);">new</span> Person("p1初始化"<span style="margin:0px;padding:0px;line-height:1.5;">);
    }
    </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">/**</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">Output
     * static成员book2成员变量初始化
     * static成员book4成员变量初始化
     * static修饰的funStatic方法
     * ***************
     * book1成员变量初始化
     * book3成员变量初始化
     * p1初始化
     </span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">*///</span><span style="margin:0px;padding:0px;line-height:1.5;color:rgb(0,128,0);">~</span>
}</pre></div>

在上面的例子中我们可以发现两个有意思的地方，第一个是当我们没有创建对象，而是通过类去调用类方法时，尽管该方法没有使用到任何的类成员，类成员还是在方法调用之前就初始化了，这说明，当我们第一次去使用一个类时，就会触发该类的成员初始化。第二个是当我们使用了类方法，完成类的成员的初始化后，再new该类的对象时，static修饰的类成员没有再次初始化，这说明，static修饰的类成员，在程序运行过程中，只需要初始化一次即可，不会进行多次的初始化。

回顾了对象的初始化以后，我们再来看static的第三个作用就非常简单了，那就是当我们初始化static修饰的成员时，可以将他们统一放在一个以static开始，用花括号包裹起来的块状语句中：
<pre>`

1.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="1"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Book</span></span>{</div></div>
2.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="2"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Book</span><span class="hljs-params">(String msg)</span> </span>{</div></div>
3.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="3"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(msg);</div></div>
4.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="4"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
5.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="5"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">}</div></div>
6.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="6"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"> </div></div>
7.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="7"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>{</div></div>
8.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="8"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"> </div></div>
9.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="9"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    Book book1 = <span class="hljs-keyword">new</span> Book(<span class="hljs-string">"book1成员变量初始化"</span>);</div></div>
10.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="10"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-keyword">static</span> Book book2;</div></div>
11.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="11"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
12.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="12"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-keyword">static</span> {</div></div>
13.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="13"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        book2 = <span class="hljs-keyword">new</span> Book(<span class="hljs-string">"static成员book2成员变量初始化"</span>);</div></div>
14.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="14"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        book4 = <span class="hljs-keyword">new</span> Book(<span class="hljs-string">"static成员book4成员变量初始化"</span>);</div></div>
15.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="15"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
16.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="16"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
17.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="17"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Person</span><span class="hljs-params">(String msg)</span> </span>{</div></div>
18.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="18"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(msg);</div></div>
19.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="19"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
20.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="20"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
21.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="21"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    Book book3 = <span class="hljs-keyword">new</span> Book(<span class="hljs-string">"book3成员变量初始化"</span>);</div></div>
22.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="22"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-keyword">static</span> Book book4;</div></div>
23.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="23"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
24.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="24"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">funStatic</span><span class="hljs-params">()</span> </span>{</div></div>
25.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="25"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(<span class="hljs-string">"static修饰的funStatic方法"</span>);</div></div>
26.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="26"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
27.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="27"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    </div></div>
28.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="28"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>{</div></div>
29.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="29"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        Person.funStatic();</div></div>
30.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="30"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(<span class="hljs-string">"****************"</span>);</div></div>
31.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="31"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        Person p1 = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"p1初始化"</span>);</div></div>
32.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="32"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
33.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="33"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-comment"><span class="hljs-comment">/**Output</span></span></div></div>
34.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="34"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * static成员book2成员变量初始化</span></div></div>
35.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="35"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * static成员book4成员变量初始化</span></div></div>
36.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="36"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * static修饰的funStatic方法</span></div></div>
37.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="37"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * ***************</span></div></div>
38.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="38"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * book1成员变量初始化</span></div></div>
39.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="39"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * book3成员变量初始化</span></div></div>
40.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="40"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * p1初始化</span></div></div>
41.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="41"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     */</span><span class="hljs-comment">//~</span></div></div>
42.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="42"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">}</div></div>`<div class="hljs-button {2}" data-title="复制" onclick="hljs.copyCode(event)"></div></pre>

我们将上一个例子稍微做了一下修改，可以看到，结果没有二致。

### <a name="t4"></a>4.静态导包

&nbsp;相比于上面的三种用途，第四种用途可能了解的人就比较少了，但是实际上它很简单，而且在调用类方法时会更方便。以上面的“PrintHelper”的例子为例，做一下稍微的变化，即可使用静态导包带给我们的方便：<a title="复制代码" style="background-color:rgb(245,245,245);font-family:'Courier New';font-size:12px;margin:0px;padding:0px;color:rgb(7,93,179);border:none;" target="_blank"></a>
<pre>`

1.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="1"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">/* PrintHelper.java文件 */</span></div></div>
2.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="2"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-keyword">package</span> com.dotgua.study;</div></div>
3.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="3"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"> </div></div>
4.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="4"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PrintHelper</span> </span>{</div></div>
5.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="5"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"> </div></div>
6.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="6"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">print</span><span class="hljs-params">(Object o)</span></span>{</div></div>
7.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="7"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        System.out.println(o);</div></div>
8.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="8"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
9.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="9"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">}</div></div>`<div class="hljs-button {2}" data-title="复制" onclick="hljs.copyCode(event)"></div></pre><div class="cnblogs_code" style="margin:5px 0px;padding:5px;background-color:rgb(245,245,245);border:1px solid rgb(204,204,204);color:rgb(0,0,0);text-align:left;font-family:'Courier New';font-size:12px;"><div class="cnblogs_code_toolbar" style="margin:5px 0px 0px;padding:0px;"><span class="cnblogs_code_copy" style="margin:0px;padding:0px 5px 0px 0px;line-height:1.5;"><a title="复制代码" style="margin:0px;padding:0px;color:rgb(7,93,179);border:none;" target="_blank"></a></span><pre>`

1.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="1"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span style="color:rgb(0,0,0);font-family:Consolas, Inconsolata, Courier, monospace;font-size:12px;white-space:pre;background-color:rgb(240,240,240);"><span class="hljs-comment">/* App.java文件 */</span></span></div></div>
2.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="2"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-keyword">import</span> <span class="hljs-keyword">static</span> com.dotgua.study.PrintHelper.*;</div></div>
3.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="3"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"> </div></div>
4.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="4"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> </span></div></div>
5.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="5"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">{</div></div>
6.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="6"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">( String[] args )</span></span></div></div>
7.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="7"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    {</div></div>
8.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="8"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">        print(<span class="hljs-string">"Hello World!"</span>);</div></div>
9.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="9"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    }</div></div>
10.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="10"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">    <span class="hljs-comment"><span class="hljs-comment">/**Output</span></span></div></div>
11.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="11"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     * Hello World!</span></div></div>
12.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="12"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line"><span class="hljs-comment">     */</span><span class="hljs-comment">//~</span></div></div>
13.  <div class="hljs-ln-numbers"><div class="hljs-ln-line hljs-ln-n" data-line-number="13"></div></div><div class="hljs-ln-code"><div class="hljs-ln-line">}</div></div>`<div class="hljs-button {2}" data-title="复制" onclick="hljs.copyCode(event)"></div></pre>

</div></div>

上面的代码来自于两个java文件，其中的PrintHelper很简单，包含了一个用于打印的static方法。而在App.java文件中，我们首先将PrintHelper类导入，这里在导入时，我们使用了static关键字，而且在引入类的最后还加上了<span style="margin:0px;padding:0px;">“.*”</span>，它的作用就是将PrintHelper类中的所有类方法直接导入。不同于非static导入，采用static导入包后，在不与当前类的方法名冲突的情况下，无需使用“<span style="margin:0px;padding:0px;">类名.方法名</span>”的方法去调用类方法了，直接可以采用"<span style="margin:0px;padding:0px;">方法名</span>"去调用类方法，就好像是该类自己的方法一样使用即可。

## <a name="t5"></a>总结

static是java中非常重要的一个关键字，而且它的用法也很丰富，主要有四种用法：

1.  用来修饰成员变量，将其变为类的成员，从而实现所有对象对于该成员的共享；
2.  用来修饰成员方法，将其变为类方法，可以直接使用<span style="margin:0px;padding:0px;">“类名.方法名”</span>的方式调用，常用于工具类；
3.  静态块用法，将多个类成员放在一起初始化，使得程序更加规整，其中理解对象的初始化过程非常关键；
4.  静态导包用法，将类的方法直接导入到当前类中，从而直接使用<span style="margin:0px;padding:0px;">“方法名”</span>即可调用类方法，更加方便。
          </div>
                  </div>
  </article>
</div>
