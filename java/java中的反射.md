<div id="post_detail">

<div class="post">

# [java中的反射](https://www.cnblogs.com/tech-bird/p/3525336.html)

<div id="cnblogs_post_body" class="blogpost-body">

主要介绍以下几方面内容

*   理解 Class 类
*   理解 Java 的类加载机制
*   学会使用 ClassLoader 进行类加载
*   理解反射的机制
*   掌握 Constructor、Method、Field 类的用法
*   理解并掌握动态代理

# **<span style="color: #3366ff;">1.理解Class类</span>**

<div class="O1">　　–对象照镜子后可以得到的信息：某个类的数据成员名、方法和构造器、某个类到底实现了哪些接口。对于每个类而言，JRE 都为其保留一个不变的 Class 类型的对象。一个 Class 对象包含了特定某个类的有关信息。</div>

<div class="O1">　　–Class 对象只能由系统建立对象</div>

<div class="O1">　　–一个类在 JVM 中只会有一个Class实例</div>

<div class="O1">　　–每个类的实例都会记得自己是由哪个 Class 实例所生成</div>

<div class="O1">      1：** Class是什么？**</div>

<div class="O1">      Class是一个类：</div>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">testClass() {
       Class clazz</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }
}</span> <span style="color: #008000;">//</span><span style="color: #008000;">Class的定义</span>
<span style="color: #0000ff;">public</span> <span style="color: #000000;">final</span> <span style="color: #0000ff;">class</span> Class<T> <span style="color: #000000;">implements java.io.Serializable,
                              java.lang.reflect.GenericDeclaration,
                              java.lang.reflect.Type,
                              java.lang.reflect.AnnotatedElement {

.....
.....
.....
}  
**<span style="color: #ff0000; font-family: Courier New; background-color: #f5f5f5;">//小写class表示是一个类类型，大写Class表示这个类的名称</span>**</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

      2：**Class这个类封装了什么信息？**

**<span style="color: #ff0000;">　　Class是一个类，封装了当前对象所对应的类的信息</span>**  
　　 一个类中有属性，方法，构造器等，比如说有一个Person类，一个Order类，一个Book类，这些都是不同的类，现在需要一个类，用来描述类，这就是Class，它应该有类名，属性，方法，构造器等。Class是用来描述类的类

　　Class类是一个对象照镜子的结果，对象可以看到自己有哪些属性，方法，构造器，实现了哪些接口等等

      3.对于每个类而言，JRE 都为其保留一个不变的 Class 类型的对象。一个 Class 对象包含了特定某个类的有关信息。  
 　  4.Class 对象只能由系统建立对象，一个类（而不是一个对象）在 JVM 中只会有一个Class实例

<div class="cnblogs_code" onclick="cnblogs_code_show('4360664b-cc3e-4728-9367-2d7bae470f9e')">![](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

<div id="cnblogs_code_open_4360664b-cc3e-4728-9367-2d7bae470f9e" class="cnblogs_code_hide">

<pre><span style="color: #0000ff;">package</span> <span style="color: #000000;">com.atguigu.java.fanshe;</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">Person {
    String name;</span> <span style="color: #0000ff;">private</span> <span style="color: #0000ff;">int</span> <span style="color: #000000;">age;</span> <span style="color: #0000ff;">public</span> <span style="color: #000000;">String getName() {</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">name;
    }</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">setName(String name) {</span> <span style="color: #0000ff;">this</span>.name = <span style="color: #000000;">name;
    }</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">int</span> <span style="color: #000000;">getAge() {</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">age;
    }</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> setAge(<span style="color: #0000ff;">int</span> <span style="color: #000000;">age) {</span> <span style="color: #0000ff;">this</span>.age = <span style="color: #000000;">age;
    }</span> <span style="color: #008000;">//</span><span style="color: #008000;">包含一个带参的构造器和一个不带参的构造器</span>
    <span style="color: #0000ff;">public</span> Person(String name, <span style="color: #0000ff;">int</span> <span style="color: #000000;">age) {</span> <span style="color: #0000ff;">super</span><span style="color: #000000;">();</span> <span style="color: #0000ff;">this</span>.name = <span style="color: #000000;">name;</span> <span style="color: #0000ff;">this</span>.age = <span style="color: #000000;">age;
    }</span> <span style="color: #0000ff;">public</span> <span style="color: #000000;">Person() {</span> <span style="color: #0000ff;">super</span><span style="color: #000000;">();
    }

}</span></pre>

</div>

<span class="cnblogs_code_collapse">定义一个Person类</span></div>

      通过Class类获取类对象

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">testClass() {
       Class clazz</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">1.得到Class对象</span>
       clazz = Person.<span style="color: #0000ff;">class</span><span style="color: #000000;">;

       System.out.println();</span> <span style="color: #008000;">//</span><span style="color: #008000;">插入断点</span>
 <span style="color: #000000;">}
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　在断点处就可以看到Class对像包含的信息  
![](https://images0.cnblogs.com/blog/534926/201401/181604215171.jpg)

　　同样，这些属性值是可以获取的

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">testClass() {
       Class clazz</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">1.得到Class对象</span>
       clazz = Person.<span style="color: #0000ff;">class</span><span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">2.返回字段的数组</span>
       Field[] fields = <span style="color: #000000;">clazz.getDeclaredFields();

       System.out.println();</span> <span style="color: #008000;">//</span><span style="color: #008000;">插入断点</span>
 <span style="color: #000000;">}
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

 　　查看fields的内容

![](https://images0.cnblogs.com/blog/534926/201401/181610008144.jpg)

　　<span style="font-size: 14pt;">**对象为什么需要照镜子呢？**</span>

　　　　1\. 有可能这个对象是别人传过来的

　　　　2\. 有可能没有对象，只有一个全类名 

　　通过反射，可以得到这个类里面的信息

## <span style="font-size: 18px;">**<span style="color: #3366ff;">获取Class对象的三种方式</span>**</span>

**　　1.通过类名获取      类名.class    **

**　　2.通过对象获取      对象名.getClass()**

**　　3.通过全类名获取    Class.forName(全类名)**

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testClass() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">ClassNotFoundException {
       Class clazz</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">1.通过类名</span>
       clazz = Person.<span style="color: #0000ff;">class</span><span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">2.通过对象名</span> <span style="color: #008000;">//</span><span style="color: #008000;">这种方式是用在传进来一个对象，却不知道对象类型的时候使用</span>
       Person person = <span style="color: #0000ff;">new</span> <span style="color: #000000;">Person();
       clazz</span> = <span style="color: #000000;">person.getClass();</span> <span style="color: #008000;">//</span><span style="color: #008000;">上面这个例子的意义不大，因为已经知道person类型是Person类，再这样写就没有必要了</span> <span style="color: #008000;">//</span><span style="color: #008000;">如果传进来是一个Object类，这种做法就是应该的</span>
       Object obj = <span style="color: #0000ff;">new</span> <span style="color: #000000;">Person();
       clazz</span> = <span style="color: #000000;">obj.getClass();</span> <span style="color: #008000;">//</span><span style="color: #008000;">3.通过全类名(会抛出异常)</span> <span style="color: #008000;">//</span><span style="color: #008000;">一般框架开发中这种用的比较多，因为配置文件中一般配的都是全类名，通过这种方式可以得到Class实例</span>
       String className=" com.atguigu.java.fanshe.Person"<span style="color: #000000;">;
       clazz</span> = <span style="color: #000000;">Class.forName(className);</span> <span style="color: #008000;">//</span><span style="color: #008000;">字符串的例子</span>
       clazz = String.<span style="color: #0000ff;">class</span><span style="color: #000000;">;

       clazz</span> = "javaTest"<span style="color: #000000;">.getClass();

       clazz</span> = Class.forName("java.lang.String"<span style="color: #000000;">);

       System.out.println(); 
    }
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

## **<span style="color: #3366ff;">Class类的常用方法</span>**

<table style="width: 900px;" border="0" cellspacing="0" cellpadding="0"><colgroup><col width="351"> <col width="549"></colgroup>

<tbody>

<tr>

<td class="oa1" width="351" height="30">

<span style="font-size: 15px;">方法名</span>

</td>

<td class="oa2" width="549">

<span style="font-size: 15px;">功能说明</span>

</td>

</tr>

<tr>

<td class="oa3" width="351" height="40">

<span style="font-size: 15px;">static Class forName(String name)</span>

</td>

<td class="oa4" width="549">

<span style="font-size: 15px;">返回指定类名 name 的 Class 对象</span>

</td>

</tr>

<tr>

<td class="oa3" width="351" height="38">

<span style="font-size: 15px;">Object newInstance()</span>

</td>

<td class="oa4" width="549">

<span style="font-size: 15px;">调用缺省构造函数，返回该Class对象的一个实例</span>

</td>

</tr>

<tr>

<td class="oa3" width="351" height="45">

<span style="font-size: 15px;">Object newInstance(Object []args)</span>

</td>

<td class="oa4" width="549">

<span style="font-size: 15px;">调用当前格式构造函数，返回该Class对象的一个实例</span>

</td>

</tr>

<tr>

<td class="oa3" width="351" height="45">

<span style="font-size: 15px;">getName()</span>

</td>

<td class="oa4" width="549">

<span style="font-size: 15px;">返回此Class对象所表示的实体（类、接口、数组类、基本类型或void）名称</span>

</td>

</tr>

<tr>

<td class="oa3" width="351" height="38">

<span style="font-size: 15px;">Class getSuperClass()</span>

</td>

<td class="oa4" width="549">

<span style="font-size: 15px;">返回当前Class对象的父类的Class对象</span>

</td>

</tr>

<tr>

<td class="oa3" width="351" height="38">

<span style="font-size: 15px;">Class [] [getInterfaces](mk:@MSITStore:C:\ZOL\JDK%20150.chm::/jdk150/api/java/lang/Class.html)()</span>

</td>

<td class="oa4" width="549">

<span style="font-size: 15px;">获取当前Class对象的接口</span>

</td>

</tr>

<tr>

<td class="oa3" width="351" height="38">

<span style="font-size: 15px;">ClassLoader getClassLoader()</span>

</td>

<td class="oa4" width="549">

<span style="font-size: 15px;">返回该类的类加载器</span>

</td>

</tr>

<tr>

<td class="oa5" width="351" height="38">

<span style="font-size: 15px;">Class getSuperclass()</span>

</td>

<td class="oa6" width="549">

<span style="font-size: 15px;">返回表示此Class所表示的实体的超类的Class</span>

</td>

</tr>

</tbody>

</table>

　**<span style="color: #3366ff;">　Class类的newInstance（）方法</span>**

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre>    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testNewInstance() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">ClassNotFoundException, InstantiationException, IllegalAccessException{</span> <span style="color: #008000;">//</span><span style="color: #008000;">1.获取Class对象</span>
        String className="com.atguigu.java.fanshe.Person"<span style="color: #000000;">;
        Class clazz</span> = <span style="color: #000000;">Class.forName(className);</span> <span style="color: #008000;">//</span><span style="color: #008000;">利用Class对象的newInstance方法创建一个类的实例</span>
        Object obj = <span style="color: #000000;">clazz.newInstance();
        System.out.println(obj);
    }</span> <span style="color: #008000;"><a>//结果是：</a></span><a><span style="color: #008000;">com.atguigu.java.fanshe.Person@2866bb78</span></a>
    </pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　可以看出确实是创建了一个Person实例  
　　但是Person类有两个构造方法，到底是调用的哪一个构造方法呢

　　实际调用的是类的**<span style="color: #ff0000;">无参数的构造器</span>**。所以在我们在定义一个类的时候，定义一个有参数的构造器，作用是对属性进行初始化，还要写一个无参数的构造器，作用就是反射时候用。

　　**<span style="color: #ff0000;">一般地、一个类若声明一个带参的构造器，同时要声明一个无参数的构造器</span>**

# <span style="color: #0000ff;">**2.ClassLoader**</span>

 　　类装载器是用来把类(class)装载进 JVM 的。JVM 规范定义了两种类型的类装载器：启动类装载器(bootstrap)和用户自定义装载器(user-defined class loader)。 JVM在运行时会产生3个类加载器组成的初始化加载器层次结构 ，如下图所示：

![](https://images0.cnblogs.com/blog/534926/201401/181711178455.jpg)

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testClassLoader() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">ClassNotFoundException, FileNotFoundException{</span> <span style="color: #008000;">//</span><span style="color: #008000;">1\. 获取一个系统的类加载器(可以获取，当前这个类PeflectTest就是它加载的)</span>
        ClassLoader classLoader = <span style="color: #000000;">ClassLoader.getSystemClassLoader();
        System.out.println(classLoader);</span> <span style="color: #008000;">//</span><span style="color: #008000;">2\. 获取系统类加载器的父类加载器（扩展类加载器，可以获取）.</span> 
        classLoader = <span style="color: #000000;">classLoader.getParent();
        System.out.println(classLoader);</span> <span style="color: #008000;">//</span><span style="color: #008000;">3\. 获取扩展类加载器的父类加载器（引导类加载器，不可获取）.</span>
        classLoader = <span style="color: #000000;">classLoader.getParent();
        System.out.println(classLoader);</span> <span style="color: #008000;">//</span><span style="color: #008000;">4\. 测试当前类由哪个类加载器进行加载（系统类加载器）:</span> 
        classLoader = Class.forName("com.atguigu.java.fanshe.ReflectionTest"<span style="color: #000000;">)
             .getClassLoader();
        System.out.println(classLoader);</span> <span style="color: #008000;">//</span><span style="color: #008000;">5\. 测试 JDK 提供的 Object 类由哪个类加载器负责加载（引导类）</span>
        classLoader = Class.forName("java.lang.Object"<span style="color: #000000;">)
                 .getClassLoader();
        System.out.println(classLoader); 
    }
}</span> <span style="color: #008000;">//</span><span style="color: #008000;">结果：</span> <span style="color: #008000;">//</span><span style="color: #008000;">sun.misc.Launcher$AppClassLoader@5ffdfb42</span> <span style="color: #008000;">//</span><span style="color: #008000;">sun.misc.Launcher$ExtClassLoader@1b7adb4a</span> <span style="color: #008000;">//</span><span style="color: #008000;">null</span> <span style="color: #008000;">//</span><span style="color: #008000;">sun.misc.Launcher$AppClassLoader@5ffdfb42</span> <span style="color: #008000;">//</span><span style="color: #008000;">null</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　<span style="font-size: 16px;">**<span style="color: #3366ff;">使用类加载器获取当前类目录下的文件</span>**</span>

![](https://images0.cnblogs.com/blog/534926/201401/181739102057.jpg)

　　首先，系统类加载器可以加载当前项目src目录下面的所有类，如果文件也放在src下面，也可以用类加载器来加载

　　调用 <span style="color: #ff0000;">**getResourceAsStream**</span> 获取类路径下的文件对应的输入流.

![](https://images0.cnblogs.com/blog/534926/201401/181747533770.jpg)

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">、public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testClassLoader() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">FileNotFoundException{</span> <span style="color: #008000;">//</span><span style="color: #008000;">src目录下，直接加载</span>
        InputStream in1 = <span style="color: #0000ff;">null</span><span style="color: #000000;">;
        in1</span> = <span style="color: #0000ff;">this</span>.getClass().getClassLoader().getResourceAsStream("test1.txt"<span style="color: #000000;">);</span> <span style="color: #008000;">//</span><span style="color: #008000;">放在内部文件夹，要写全路径</span>
        InputStream in2 = <span style="color: #0000ff;">null</span><span style="color: #000000;">;
        in2</span> = <span style="color: #0000ff;">this</span>.getClass().getClassLoader().getResourceAsStream("com/atguigu/java/fanshe/test2.txt"<span style="color: #000000;">);
    }
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

# **<span style="color: #0000ff;">3.反射</span>**

## <span style="color: #3366ff;">反射概述</span>

     Reflection（反射）是Java被视为动态语言的关键，反射机制允许程序在执行期借助于Reflection API取得任何类的內部信息，并能直接操作任意对象的内部属性及方法。

　　Java反射机制主要提供了以下功能：

*   在运行时构造任意一个类的对象
*   在运行时获取任意一个类所具有的成员变量和方法
*   在运行时调用任意一个对象的方法（属性）
*   生成动态代理

<div class="O1">　　Class 是一个类; **<span style="color: #ff0000;">一个描述类的类.</span>**</div>

<div class="O1">　　封装了描述方法的 <span style="color: #ff0000;">Method</span>,</div>

<div class="O1">              描述字段的 <span style="color: #ff0000;">Filed</span>,</div>

<div class="O1">              描述构造器的 <span style="color: #ff0000;">Constructor</span> 等属性.</div>

## <span style="color: #3366ff;"> 3.1如何描述方法-Method</span>

<div class="O1">

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testMethod() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        Class clazz</span> = Class.forName("com.atguigu.java.fanshe.Person"<span style="color: #000000;">);</span> <span style="color: #008000;">//  
</span>        <span style="color: #008000;">//</span><span style="color: #008000;">1.<span style="font-size: 16px;">**<span style="color: #ff0000;">获取方法</span> **</span>//  1.1 获取取clazz对应类中的所有方法--方法数组（一）</span> <span style="color: #008000;">//</span> <span style="color: #008000;">不能获取private方法,且获取从父类继承来的所有方法</span>
        Method[] methods = <span style="color: #000000;">clazz.**<span style="color: #ff0000;">getMethods</span>**();</span> <span style="color: #0000ff;">for</span><span style="color: #000000;">(Method method:methods){
            System.out.print(</span>" "+<span style="color: #000000;">method.getName());
        }
        System.out.println();</span> <span style="color: #008000;">//</span>
        <span style="color: #008000;">//  1.</span><span style="color: #008000;">2.获取所有方法，包括私有方法 --方法数组（二）</span> <span style="color: #008000;">//</span> <span style="color: #008000;">所有声明的方法，都可以获取到，且只获取当前类的方法</span>
        methods = <span style="color: #000000;">clazz.**<span style="color: #ff0000;">getDeclaredMethods</span>**();</span> <span style="color: #0000ff;">for</span><span style="color: #000000;">(Method method:methods){
            System.out.print(</span>" "+<span style="color: #000000;">method.getName());
        }
        System.out.println();</span> <span style="color: #008000;">//</span>
        <span style="color: #008000;">//  1.</span><span style="color: #008000;">3.获取指定的方法</span> <span style="color: #008000;">//</span> <span style="color: #008000;">需要参数名称和参数列表，无参则不需要写</span> <span style="color: #008000;">//</span> <span style="color: #008000;">对于方法public void setName(String name) {  }</span>
        Method method = clazz.**<span style="color: #ff0000;">getDeclaredMethod</span>**("setName", String.<span style="color: #0000ff;">class</span><span style="color: #000000;">);
        System.out.println(method);</span> <span style="color: #008000;">//</span> <span style="color: #008000;">而对于方法public void setAge(int age) {  }</span>
        method = clazz.getDeclaredMethod("setAge", Integer.<span style="color: #0000ff;">class</span><span style="color: #000000;">);
        System.out.println(method);</span> <span style="color: #008000;">//</span> <span style="color: #008000;">这样写是获取不到的，如果方法的参数类型是int型</span> <span style="color: #008000;">//</span> <span style="color: #008000;">如果方法用于反射，**<span style="color: #ff0000;">那么要么int类型写成Integer</span>**： public void setAge(Integer age) {  }  
　　　　 //  要么获取方法的参数写成int.class</span> <span style="color: #008000;">//</span>
        <span style="color: #008000;">//2</span><span style="color: #008000;">.<span style="font-size: 16px;">**<span style="color: #ff0000;">执行方法</span> **</span></span><span style="color: #008000;">//</span> <span style="color: #008000;">invoke第一个参数表示执行哪个对象的方法，剩下的参数是执行方法时需要传入的参数</span>
        Object obje = <span style="color: #000000;">clazz.newInstance();
        method.**<span style="color: #ff0000;">invoke</span>**(obje,</span>2<span style="color: #000000;">);

　　　　//如果一个方法是私有方法，第三步是可以获取到的，但是这一步却不能执行  
　**<span style="color: #ff0000;">　　　//私有方法的执行，必须在调用invoke之前加上一句method.setAccessible（true）;</span>**  
    }
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　主要用到的两个方法

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008000;">/**</span> <span style="color: #008000;">*</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">name the name of the method
         *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">parameterTypes the list of parameters
         *</span> <span style="color: #808080;">@return</span> <span style="color: #008000;">the {</span><span style="color: #808080;">@code</span> <span style="color: #008000;">Method} object that matches the specified</span> <span style="color: #008000;">*/</span>
        <span style="color: #0000ff;">public</span> Method getMethod(String name, Class<?><span style="color: #000000;">... parameterTypes){

        }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">*</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">obj  the object the underlying method is invoked from
         *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">args the arguments used for the method call
         *</span> <span style="color: #808080;">@return</span> <span style="color: #008000;">the result of dispatching the method represented by</span> <span style="color: #008000;">*/</span>
        <span style="color: #0000ff;">public</span> <span style="color: #000000;">Object invoke(Object obj, Object... args){

        }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

<span style="font-size: 18px;">**<span style="color: #3366ff;">自定义工具方法</span>**</span>

　　自定义一个方法

             **<span style="color: #ff0000;">把类对象和类方法名作为参数，执行方法</span>**

**<span style="color: #ff0000;">             把全类名和方法名作为参数，执行方法</span>**

　　比如Person里有一个方法

<div class="cnblogs_code">

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">test(String name,Integer age){
        System.out.println(</span>"调用成功"<span style="color: #000000;">);
    }</span></pre>

</div>

　　那么我们自定义一个方法  
     <span style="color: #0000ff; font-size: 18px;">1. **把类对象和类方法名作为参数，执行方法**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008000;">/**</span> <span style="color: #008000;">* 
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">obj: 方法执行的那个对象. 
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">methodName: 类的一个方法的方法名. 该方法也可能是私有方法. 
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">args: 调用该方法需要传入的参数
     *</span> <span style="color: #808080;">@return</span><span style="color: #008000;">: 调用方法后的返回值
     *</span> <span style="color: #008000;">*/</span>
      <span style="color: #0000ff;">public</span> Object invoke(Object obj, String methodName, Object ... args) <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{</span> <span style="color: #008000;">//</span><span style="color: #008000;">1\. 获取 Method 对象</span> <span style="color: #008000;">//</span>** <span style="color: #ff0000;">因为getMethod的参数为Class列表类型，所以要把参数args转化为对应的Class类型。</span> ** <span style="color: #000000;">Class [] parameterTypes</span> = <span style="color: #0000ff;">new</span> <span style="color: #000000;">Class[args.length];</span> <span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">int</span> i = 0; i < args.length; i++<span style="color: #000000;">){
            parameterTypes[i]</span> = <span style="color: #000000;">args[i].getClass();
            System.out.println(parameterTypes[i]); 
        }

        Method method</span> = <span style="color: #000000;">obj.getClass().getDeclaredMethod(methodName, parameterTypes);</span> <span style="color: #008000;">//<span style="color: #ff0000;">**如果使用getDeclaredMethod，就不能获取父类方法，如果使用getMethod，就不能获取私有方法**</span>  

　　　　　//  
　　　　　//</span><span style="color: #008000;">2\. 执行 Method 方法</span> <span style="color: #008000;">//</span><span style="color: #008000;">3\. 返回方法的返回值</span>
        <span style="color: #0000ff;">return</span> <span style="color: #000000;">method.invoke(obj, args);
      }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　调用：

<div class="cnblogs_code">

<pre> <span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testInvoke() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
            Object obj</span> = <span style="color: #0000ff;">new</span> <span style="color: #000000;">Person();            
            invoke(obj,</span> "test", "wang", 1<span style="color: #000000;">);             
        }</span> </pre>

</div>

　　这样就通过对象名，方法名，方法参数执行了该方法

　<span style="font-size: 18px;">　**<span style="color: #0000ff;">2.把全类名和方法名作为参数，执行方法</span>**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008000;">/**</span> <span style="color: #008000;">*</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">className: 某个类的全类名
         *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">methodName: 类的一个方法的方法名. 该方法也可能是私有方法. 
         *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">args: 调用该方法需要传入的参数
         *</span> <span style="color: #808080;">@return</span><span style="color: #008000;">: 调用方法后的返回值</span> <span style="color: #008000;">*/</span>
        <span style="color: #0000ff;">public</span> <span style="color: #000000;">Object invoke(String className, String methodName, Object ... args){
            Object obj</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{
                obj</span> = <span style="color: #000000;">Class.forName(className).newInstance();</span> <span style="color: #008000;">//</span><span style="color: #008000;">调用上一个方法</span>
                <span style="color: #0000ff;">return</span> <span style="color: #000000;">invoke(obj, methodName, args);
            }</span><span style="color: #0000ff;">catch</span><span style="color: #000000;">(Exception e) {
                e.printStackTrace();
            }</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
        }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　调用

<div class="cnblogs_code">

<pre><span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testInvoke() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{</span><span style="color: #000000;">        
            invoke(</span>"com.atguigu.java.fanshe.Person"<span style="color: #000000;">,</span> "test", "zhagn", 12<span style="color: #000000;">);         
        }</span></pre>

</div>

　　使用系统方法（前提是此类<span style="color: #ff0000;">有一个无参的构造器</span>（查看API））

<div class="cnblogs_code">

<pre><span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testInvoke() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
            Object result</span> = <span style="color: #000000;">invoke(</span>"java.text.SimpleDateFormat", "format", <span style="color: #0000ff;">new</span> <span style="color: #000000;">Date());
            System.out.println(result);          
        }</span></pre>

</div>

　<span style="font-size: 16px;">**<span style="color: #ff0000;">　</span>**</span>

<span style="font-size: 16px;">**<span style="color: #ff0000;">　　这种反射实现的主要功能是可配置和低耦合。只需要类名和方法名，而不需要一个类对象就可以执行一个方法。如果我们把全类名和方法名放在一个配置文件中，就可以根据调用配置文件来执行方法</span>**</span>

**<span style="color: #0000ff; font-size: 18px;"> 如何获取父类定义的（私有）方法</span>**

　　前面说一般使用getDeclaredMethod获取方法（因为此方法可以获取类的私有方法，但是不能获取父类方法）

　　如何获取父类方法呢，上一个例子format方法其实就是父类的方法（获取的时候用到的是getMethod）

　　首先我们要知道，如何获取类的父亲：

　　比如有一个类，继承自Person

　　使用

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {
    @Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testGetSuperClass() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        String className</span> = "com.atguigu.java.fanshe.Student"<span style="color: #000000;">;

        Class clazz</span> = <span style="color: #000000;">Class.forName(className);
        Class superClazz</span> = <span style="color: #000000;">clazz.getSuperclass();

        System.out.println(superClazz); 
    }
}</span> <span style="color: #008000;">//</span><span style="color: #008000;">结果是 “ class com.atguigu.java.fanshe.Person ”</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　此时如果Student中有一个方法是私有方法method1(int age); Person中有一个私有方法method2();  
　　怎么调用

　　**<span style="color: #ff0000;">定义一个方法，不但能访问当前类的私有方法，还要能父类的私有方法</span>**

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008000;">/**</span> <span style="color: #008000;">* 
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">obj: 某个类的一个对象
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">methodName: 类的一个方法的方法名. 
     * 该方法也可能是私有方法, 还可能是该方法在父类中定义的(私有)方法
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">args: 调用该方法需要传入的参数
     *</span> <span style="color: #808080;">@return</span><span style="color: #008000;">: 调用方法后的返回值</span> <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #000000;">Object invoke2(Object obj, String methodName, 
            Object ... args){</span> <span style="color: #008000;">//</span><span style="color: #008000;">1\. 获取 Method 对象</span>
        Class [] parameterTypes = <span style="color: #0000ff;">new</span> <span style="color: #000000;">Class[args.length];</span> <span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">int</span> i = 0; i < args.length; i++<span style="color: #000000;">){
            parameterTypes[i]</span> = <span style="color: #000000;">args[i].getClass();
        }</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{
            Method method</span> = <span style="color: #000000;">getMethod(obj.getClass(), methodName, parameterTypes);
            method.setAccessible(</span><span style="color: #0000ff;">true</span><span style="color: #000000;">);</span> <span style="color: #008000;">//</span><span style="color: #008000;">2\. 执行 Method 方法</span> <span style="color: #008000;">//</span><span style="color: #008000;">3\. 返回方法的返回值</span>
            <span style="color: #0000ff;">return</span> <span style="color: #000000;">method.invoke(obj, args);
        }</span> <span style="color: #0000ff;">catch</span> <span style="color: #000000;">(Exception e) {
            e.printStackTrace();
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 获取 clazz 的 methodName 方法. 该方法可能是私有方法, 还可能在父类中(私有方法)
     * 如果在该类中找不到此方法，就向他的父类找，一直到Object类为止
　　　* **<span style="color: #ff0000;">这个方法的另一个作用是根据一个类名，一个方法名，追踪到并获得此方法</span>**  
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">clazz
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">methodName
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">parameterTypes
     *</span> <span style="color: #808080;">@return</span>
     <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #000000;">Method getMethod(Class clazz, String methodName, 
            Class ... parameterTypes){</span> <span style="color: #0000ff;">for</span>(;clazz != Object.<span style="color: #0000ff;">class</span>; clazz = <span style="color: #000000;">clazz.getSuperclass()){</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{
                Method method</span> = <span style="color: #000000;">clazz.getDeclaredMethod(methodName, parameterTypes);</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">method;
            }</span> <span style="color: #0000ff;">catch</span> <span style="color: #000000;">(Exception e) {}            
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

## <span style="color: #0000ff;">** 3.2 如何描述字段-Field**</span>  

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testField() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        String className</span> = "com.atguigu.java.fanshe.Person"<span style="color: #000000;">;        
        Class clazz</span> = <span style="color: #000000;">Class.forName(className);</span> <span style="color: #008000;">//</span><span style="font-size: 16px;">**<span style="color: #ff0000;">1.获取字段</span> **</span><span style="color: #008000;">//</span> <span style="color: #008000;">1.1 获取所有字段 -- 字段数组</span> <span style="color: #008000;">//</span> <span style="color: #ff0000;">可以获取公用和私有的所有字段，但不能获取父类字段</span>
        Field[] fields = <span style="color: #000000;">clazz.getDeclaredFields();</span> <span style="color: #0000ff;">for</span><span style="color: #000000;">(Field field: fields){
            System.out.print(</span>" "+ <span style="color: #000000;">field.getName());
        }
        System.out.println();</span> <span style="color: #008000;">//</span> <span style="color: #008000;">1.2获取指定字段</span>
        Field field = clazz.**<span style="color: #ff0000;">getDeclaredField</span>**("name"<span style="color: #000000;">);
        System.out.println(field.getName());

        Person person</span> = <span style="color: #0000ff;">new</span> Person("ABC",12<span style="color: #000000;">);</span> <span style="font-size: 16px;">**<span style="color: #ff0000;">//2.使用字段</span> **</span><span style="color: #008000;">//</span> <span style="color: #008000;">2.1获取指定对象的指定字段的值</span>
        Object val = <span style="color: #000000;">field.**<span style="color: #ff0000;">get</span>**(person);
        System.out.println(val);</span> <span style="color: #008000;">//</span> <span style="color: #008000;">2.2设置指定对象的指定对象Field值</span>
        field.**<span style="color: #ff0000;">set</span>**(person, "DEF"<span style="color: #000000;">);
        System.out.println(person.getName());</span> <span style="color: #008000;">//</span> <span style="color: #008000;">2.3如果字段是<span style="color: #ff0000;">私有的，不管是读值还是写值，都必须先调用setAccessible（true）方法</span></span><span style="color: #008000;">//</span> <span style="color: #008000;">比如Person类中，字段name字段是公用的，age是私有的</span>
        field = clazz.getDeclaredField("age"<span style="color: #000000;">);
        field.**<span style="color: #ff0000;">setAccessible</span>**(</span><span style="color: #0000ff;">true</span><span style="color: #000000;">);
        System.out.println(field.get(person));        
    }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　但是如果需要访问父类中的（私有）字段：

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008000;">/**</span> <span style="color: #008000;">* //创建 className 对应类的对象, 并为其 fieldName 赋值为 val</span> <span style="color: #008000;">* //Student继承自Person,age是Person类的私有字段/  
</span>     <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testClassField() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        String className</span> = "com.atguigu.java.fanshe.Student"<span style="color: #000000;">;
        String fieldName</span> = "age"; <span style="color: #008000;">//</span><span style="color: #008000;">可能为私有, 可能在其父类中.</span> 
        Object val = 20<span style="color: #000000;">;        

        Object obj</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">1.创建className 对应类的对象</span>
        Class clazz = <span style="color: #000000;">Class.forName(className);</span> <span style="color: #008000;">//</span><span style="color: #008000;">2.创建fieldName 对象字段的对象</span>
        Field field = <span style="color: #000000;">getField(clazz, fieldName);</span> <span style="color: #008000;">//</span><span style="color: #008000;">3.为此对象赋值</span>
        obj = <span style="color: #000000;">clazz.newInstance();
        setFieldValue(obj, field, val);</span> <span style="color: #008000;">//</span><span style="color: #008000;">4.获取此对象的值</span>
        Object value = <span style="color: #000000;">getFieldValue(obj,field);
    }</span> <span style="color: #0000ff;">public</span> Object getFieldValue(Object obj, Field field) <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        field.setAccessible(</span><span style="color: #0000ff;">true</span><span style="color: #000000;">);</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">field.get(obj);
    }</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> setFieldValue(Object obj, Field field, Object val) <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception {
        field.setAccessible(</span><span style="color: #0000ff;">true</span><span style="color: #000000;">);
        field.set(obj, val);
    }</span> <span style="color: #0000ff;">public</span> Field getField(Class clazz, String fieldName) <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception {
        Field field</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #0000ff;">for</span>(Class clazz2 = clazz; clazz2 != Object.<span style="color: #0000ff;">class</span>;clazz2 = <span style="color: #000000;">clazz2.getSuperclass()){        
                field</span> = <span style="color: #000000;">clazz2.getDeclaredField(fieldName);
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">field;
    }</span> </pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

<span style="font-size: 14pt;">**<span style="color: #0000ff;">3.3如何描述构造器-Constructor</span>**</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testConstructor() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        String className</span> = "com.atguigu.java.fanshe.Person"<span style="color: #000000;">;
        Class</span><Person> clazz = (Class<Person><span style="color: #000000;">) Class.forName(className);</span> <span style="color: #008000;">//</span><span style="color: #008000;">1\. 获取 Constructor 对象</span> <span style="color: #008000;">//</span> <span style="color: #008000;">1.1 获取全部</span>
        Constructor<Person> [] constructors = <span style="color: #000000;">(Constructor</span><Person><span style="color: #000000;">[]) Class.forName(className).getConstructors();</span> <span style="color: #0000ff;">for</span>(Constructor<Person> <span style="color: #000000;">constructor: constructors){
            System.out.println(constructor); 
        }</span> <span style="color: #008000;">//</span> <span style="color: #008000;">1.2获取某一个，需要参数列表</span>
        Constructor<Person> constructor = clazz.getConstructor(String.<span style="color: #0000ff;">class</span>, <span style="color: #0000ff;">int</span>.<span style="color: #0000ff;">class</span><span style="color: #000000;">);
        System.out.println(constructor);</span> <span style="color: #008000;">//</span><span style="color: #008000;">2\. 调用构造器的 newInstance() 方法创建对象</span>
        Object obj = constructor.newInstance("zhagn", 1<span style="color: #000000;">);                
    }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

**<span style="color: #0000ff; font-size: 14pt;">3.4 如何描述注解 -- Annotation</span>**

　　定义一个Annotation

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.annotation.ElementType;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.annotation.Retention;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.annotation.RetentionPolicy;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(value</span>=<span style="color: #000000;">{ElementType.METHOD})</span> <span style="color: #0000ff;">public</span> @<span style="color: #0000ff;">interface</span> <span style="color: #000000;">AgeValidator {</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">int</span> <span style="color: #000000;">min();</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">int</span> <span style="color: #000000;">max();
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　此注解只能用在方法上

<div class="cnblogs_code">

<pre>@AgeValidator(min=18,max=35<span style="color: #000000;">)</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> setAge(<span style="color: #0000ff;">int</span> <span style="color: #000000;">age) {</span> <span style="color: #0000ff;">this</span>.age = <span style="color: #000000;">age;
    }</span></pre>

</div>

　　那么我们在给Person类对象的age赋值时，是感觉不到注解的存在的

<div class="cnblogs_code">

<pre><span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testAnnotation() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        Person person</span> = <span style="color: #0000ff;">new</span> <span style="color: #000000;">Person();    
        person.setAge(</span>10<span style="color: #000000;">);
    }</span></pre>

</div>

　　必须通过反射的方式为属性赋值，才能获取到注解

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #008000;">/**</span> <span style="color: #008000;">Annotation 和 反射:
         * 1\. 获取 Annotation
         * 
         * getAnnotation(Class<T> annotationClass) 
         * getDeclaredAnnotations() 
         *</span> <span style="color: #008000;">*/</span> <span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testAnnotation() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
        String className</span> = "com.atguigu.java.fanshe.Person"<span style="color: #000000;">;

        Class clazz</span> = <span style="color: #000000;">Class.forName(className);
        Object obj</span> = <span style="color: #000000;">clazz.newInstance();    

        Method method</span> = clazz.getDeclaredMethod("setAge", <span style="color: #0000ff;">int</span>.<span style="color: #0000ff;">class</span><span style="color: #000000;">);</span> <span style="color: #0000ff;">int</span> val = 6<span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">获取指定名称的注解</span>
        Annotation annotation = method.getAnnotation(AgeValidator.<span style="color: #0000ff;">class</span><span style="color: #000000;">);</span> <span style="color: #0000ff;">if</span>(annotation != <span style="color: #0000ff;">null</span><span style="color: #000000;">){</span> <span style="color: #0000ff;">if</span>(annotation <span style="color: #0000ff;">instanceof</span> <span style="color: #000000;">AgeValidator){
                AgeValidator ageValidator</span> = <span style="color: #000000;">(AgeValidator) annotation;</span> <span style="color: #0000ff;">if</span>(val < ageValidator.min() || val > <span style="color: #000000;">ageValidator.max()){</span> <span style="color: #0000ff;">throw</span> <span style="color: #0000ff;">new</span> RuntimeException("年龄非法"<span style="color: #000000;">);
                }
            }
        }        
        method.invoke(obj,</span> 20<span style="color: #000000;">);
        System.out.println(obj);          
    }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　**<span style="color: #ff0000;">如果在程序中要获取注解，然后获取注解的值进而判断我们赋值是否合法，那么类对象的创建和方法的创建必须是通过反射而来的</span>**

# <span style="color: #0000ff;">**4.反射与泛型**</span>

　　定义一个泛型类

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> DAO<T> <span style="color: #000000;">{</span> <span style="color: #008000;">//</span><span style="color: #008000;">根据id获取一个对象</span>
 <span style="color: #000000;">T get(Integer id){</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }</span> <span style="color: #008000;">//</span><span style="color: #008000;">保存一个对象</span>
    <span style="color: #0000ff;">void</span> <span style="color: #000000;">save(T entity){

    }
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

<span style="color: #000000;">　　再定义一个子类，继承这个泛型类：</span>

<div class="cnblogs_code">

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> PersonDAO <span style="color: #0000ff;">extends</span> DAO<Person> <span style="color: #000000;">{

}</span></pre>

</div>

<span style="color: #000000;">　　父类中的泛型T，就相当于一个参数，当子类继承这个类时，就要给这个参数赋值，这里是把Person类型传给了父类</span>

<span style="color: #000000;">　　或者还有一种做法</span>

<div class="cnblogs_code">

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> PersonDAO<T> <span style="color: #0000ff;">extends</span> DAO<T> <span style="color: #000000;">{

}</span></pre>

</div>

<span style="color: #000000;">　　然后进行测试</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> testAnnotation() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
       PersonDAO personDAO</span> = <span style="color: #0000ff;">new</span> <span style="color: #000000;">PersonDAO();
       Person entity</span> = <span style="color: #0000ff;">new</span> <span style="color: #000000;">Person();</span> <span style="color: #008000;">//</span><span style="color: #008000;">调用父类的save方法，同时也把Person这个“实参”传给了父类的T</span>
 <span style="color: #000000;">personDAO.save(entity);</span> <span style="color: #008000;">//</span><span style="color: #008000;">这句的本意是要返回一个Person类型的对象</span>
       Person result = personDAO.get(1<span style="color: #000000;">); 
       System.out.print(result);
    }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

<span style="color: #000000;">　　问题出来了。这里的get方法是父类的get方法，对于父类而言，方法返回值是一个T类型，当T的值为Person时，本该返回一个Person类型，但是必须用反射来创建这个对象（泛型方法返回一个对象），方法无非就是clazz.newInstance(); 所以关键点就是根据T得到其对于的Class对象。</span>

<span style="color: #000000;">　　那么首先，在父类中定义一个字段，表示T所对应的Class，然后想办法得到这个clazz的值</span>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> DAO<T> <span style="color: #000000;">{</span> <span style="color: #0000ff;">private</span> Class<T> <span style="color: #000000;">clazz;

    T get(Integer id){</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

     如何获得这个clazz呢？

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #000000;">@Test</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">void</span> test() <span style="color: #0000ff;">throws</span> <span style="color: #000000;">Exception{
       PersonDAO personDAO</span> = <span style="color: #0000ff;">new</span> <span style="color: #000000;">PersonDAO();

       Person result</span> = personDAO.get(1<span style="color: #000000;">); 
       System.out.print(result);
    }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #000000;">DAO(){</span> <span style="color: #008000;">//</span><span style="color: #008000;">1.</span>
        System.out.println("DAO's Constrctor..."<span style="color: #000000;">);
        System.out.println(</span><span style="color: #0000ff;">this</span>);           <span style="color: #008000;">//</span><span style="color: #008000;">结果是：com.atguigu.java.fanshe.PersonDAO@66588ec0</span> <span style="color: #008000;">//</span><span style="color: #008000;">this：父类构造方法中的this指的是子类对象，因为此时是PersonDAO对象在调用</span>
        System.out.println(<span style="color: #0000ff;">this</span>.getClass()); <span style="color: #008000;">//</span><span style="color: #008000;">结果是：class com.atguigu.java.fanshe.PersonDAO</span> <span style="color: #008000;">//</span><span style="color: #008000;">2.</span> <span style="color: #008000;">//</span><span style="color: #008000;">获取DAO子类的父类</span>
        Class class1 = <span style="color: #0000ff;">this</span><span style="color: #000000;">.getClass().getSuperclass();
        System.out.println(class1);</span> <span style="color: #008000;">//</span><span style="color: #008000;">结果是：class com.atguigu.java.fanshe.DAO</span> <span style="color: #008000;">//</span><span style="color: #008000;">此时只能获的父类的类型名称，却不可以获得父类的泛型参数</span> <span style="color: #008000;">//</span><span style="color: #008000;">3.</span> <span style="color: #008000;">//</span><span style="color: #008000;">获取DAO子类带泛型参数的子类</span>
        Type type=<span style="color: #0000ff;">this</span><span style="color: #000000;">.getClass().getGenericSuperclass();
        System.out.println(type);</span> <span style="color: #008000;">//</span><span style="color: #008000;">结果是：com.atguigu.java.fanshe.DAO<com.atguigu.java.fanshe.Person></span> <span style="color: #008000;">//</span><span style="color: #008000;">此时获得了泛型参数，然后就是把它提取出来</span> <span style="color: #008000;">//</span><span style="color: #008000;">4.</span> <span style="color: #008000;">//</span><span style="color: #008000;">获取具体的泛型参数 DAO<T></span> <span style="color: #008000;">//</span><span style="color: #008000;">注意Type是一个空的接口，这里使用它的子类ParameterizedType，表示带参数的类类型（即泛型）</span>
        <span style="color: #0000ff;">if</span>(type <span style="color: #0000ff;">instanceof</span> <span style="color: #000000;">ParameterizedType){
            ParameterizedType parameterizedType</span> = <span style="color: #000000;">(ParameterizedType) type;
            Type [] arges</span> = <span style="color: #000000;">parameterizedType.getActualTypeArguments();
            System.out.println(Arrays.asList(arges));</span> <span style="color: #008000;">//</span><span style="color: #008000;">结果是：[class com.atguigu.java.fanshe.Person]</span> <span style="color: #008000;">//</span><span style="color: #008000;">得到的是一个数组，因为可能父类是多个泛型参数public class DAO<T,PK>{}</span>
            <span style="color: #0000ff;">if</span>(arges != <span style="color: #0000ff;">null</span> && arges.length >0<span style="color: #000000;">){
                Type arg</span> = arges[0<span style="color: #000000;">];
                System.out.println(arg);</span> <span style="color: #008000;">//</span><span style="color: #008000;">结果是：class com.atguigu.java.fanshe.Person</span> <span style="color: #008000;">//</span><span style="color: #008000;">获得第一个参数</span>
                <span style="color: #0000ff;">if</span>(arg <span style="color: #0000ff;">instanceof</span> <span style="color: #000000;">Class){
                    clazz</span> = (Class<T><span style="color: #000000;">) arg;</span> <span style="color: #008000;">//</span><span style="color: #008000;">把值赋给clazz字段</span>
 <span style="color: #000000;">}
            }
        }        
    }</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

　　所以就定义一个方法，**<span style="color: #ff0000;">获得 Class 定义中声明的父类的泛型参数类型 </span>**

<div class="cnblogs_code">

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

<pre><span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionTest {</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 通过反射, 获得定义 Class 时声明的父类的泛型参数的类型
     * 如: public EmployeeDao extends BaseDao<Employee, String>
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">clazz: 子类对应的 Class 对象
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">index: 子类继承父类时传入的泛型的索引. 从 0 开始
     *</span> <span style="color: #808080;">@return</span>
     <span style="color: #008000;">*/</span> <span style="color: #000000;">@SuppressWarnings(</span>"unchecked"<span style="color: #000000;">)</span> <span style="color: #0000ff;">public</span>  Class getSuperClassGenricType(Class clazz, <span style="color: #0000ff;">int</span> <span style="color: #000000;">index){

        Type type</span> = <span style="color: #000000;">clazz.getGenericSuperclass();</span> <span style="color: #0000ff;">if</span>(!(type <span style="color: #0000ff;">instanceof</span> <span style="color: #000000;">ParameterizedType)){</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
        }

        ParameterizedType parameterizedType</span> = <span style="color: #000000;">(ParameterizedType) type;

        Type [] args</span> = <span style="color: #000000;">parameterizedType.getActualTypeArguments();</span> <span style="color: #0000ff;">if</span>(args == <span style="color: #0000ff;">null</span><span style="color: #000000;">){</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
        }</span> <span style="color: #0000ff;">if</span>(index < 0 || index > args.length - 1<span style="color: #000000;">){</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
        }

        Type arg</span> = <span style="color: #000000;">args[index];</span> <span style="color: #0000ff;">if</span>(arg <span style="color: #0000ff;">instanceof</span> <span style="color: #000000;">Class){</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">(Class) arg;
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }

    @SuppressWarnings(</span>"unchecked"<span style="color: #000000;">)</span> <span style="color: #0000ff;">public</span> <span style="color: #000000;">Class getSuperGenericType(Class clazz){</span> <span style="color: #0000ff;">return</span> getSuperClassGenricType(clazz, 0<span style="color: #000000;">);
    }

    @Test</span> <span style="color: #0000ff;">public</span>  <span style="color: #0000ff;">void</span> <span style="color: #000000;">testGetSuperClassGenricType(){
        Class clazz</span> = PersonDAO.<span style="color: #0000ff;">class</span><span style="color: #000000;">;</span> <span style="color: #008000;">//</span><span style="color: #008000;">PersonDAO.class</span>
        Class argClazz = getSuperClassGenricType(clazz, 0<span style="color: #000000;">);
        System.out.println(argClazz);</span> <span style="color: #008000;">//</span><span style="color: #008000;">结果是class com.atguigu.java.fanshe.Person</span> 
 <span style="color: #000000;">}
}</span></pre>

<div class="cnblogs_code_toolbar"><span class="cnblogs_code_copy">[![复制代码](//common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")</span></div>

</div>

## **<span style="color: #0000ff;">反射小结</span>**

 1\. Class: 是一个类; 一个描述类的类.

　　封装了描述方法的 Method,

　　　　   描述字段的 Filed,

              描述构造器的 Constructor 等属性.  

 2\. 如何得到 Class 对象:  
  　　2.1 Person.class  
  　　2.2 person.getClass()  
  　　2.3 Class.forName("com.atguigu.javase.Person")  

 3\. 关于 Method:  
  　　3.1 如何获取 Method:  
  　　　　1). getDeclaredMethods: 得到 Method 的数组.  
  　　　　2). getDeclaredMethod(String methondName, Class ... parameterTypes)  

  　　3.2 如何调用 Method  
  　　　　1). 如果方法时 private 修饰的, 需要先调用 Method 的　setAccessible(true), 使其变为可访问  
  　　　　2). method.invoke(obj, Object ... args);  

  4\. 关于 Field:  
  　　4.1 如何获取 Field: getField(String fieldName)  
  　　4.2 如何获取 Field 的值:   
  　　　　1). setAccessible(true)  
  　　　　2). field.get(Object obj)  
  　　4.3 如何设置 Field 的值:  
  　　　　field.set(Obejct obj, Object val)  

  5\. 了解 Constructor 和 Annotation   

  6\. 反射和泛型.  
  　　6.1 getGenericSuperClass: 获取带泛型参数的父类, 返回值为: BaseDao<Employee, String>  
  　　6.2 Type 的子接口: ParameterizedType  
  　　6.3 可以调用 ParameterizedType 的 Type[] getActualTypeArguments() 获取泛型参数的数组.

<div class="cnblogs_code" onclick="cnblogs_code_show('0b35af8a-a1f4-4b5f-a71e-88b3fe5a80b4')">![](https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![](https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)

<div id="cnblogs_code_open_0b35af8a-a1f4-4b5f-a71e-88b3fe5a80b4" class="cnblogs_code_hide">

<pre><span style="color: #0000ff;">package</span> <span style="color: #000000;">com.atguigu.javase.lesson12;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.reflect.Field;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.reflect.InvocationTargetException;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.reflect.Method;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.reflect.Modifier;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.reflect.ParameterizedType;</span> <span style="color: #0000ff;">import</span> <span style="color: #000000;">java.lang.reflect.Type;</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 反射的 Utils 函数集合
 * 提供访问私有变量, 获取泛型类型 Class, 提取集合中元素属性等 Utils 函数
 *</span> <span style="color: #808080;">@author</span> <span style="color: #008000;">Administrator
 *</span> <span style="color: #008000;">*/</span>
<span style="color: #0000ff;">public</span> <span style="color: #0000ff;">class</span> <span style="color: #000000;">ReflectionUtils {</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 通过反射, 获得定义 Class 时声明的父类的泛型参数的类型
     * 如: public EmployeeDao extends BaseDao<Employee, String>
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">clazz
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">index
     *</span> <span style="color: #808080;">@return</span>
     <span style="color: #008000;">*/</span> <span style="color: #000000;">@SuppressWarnings(</span>"unchecked"<span style="color: #000000;">)</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> Class getSuperClassGenricType(Class clazz, <span style="color: #0000ff;">int</span> <span style="color: #000000;">index){
        Type genType</span> = <span style="color: #000000;">clazz.getGenericSuperclass();</span> <span style="color: #0000ff;">if</span>(!(genType <span style="color: #0000ff;">instanceof</span> <span style="color: #000000;">ParameterizedType)){</span> <span style="color: #0000ff;">return</span> Object.<span style="color: #0000ff;">class</span><span style="color: #000000;">;
        }

        Type [] params</span> = <span style="color: #000000;">((ParameterizedType)genType).getActualTypeArguments();</span> <span style="color: #0000ff;">if</span>(index >= params.length || index < 0<span style="color: #000000;">){</span> <span style="color: #0000ff;">return</span> Object.<span style="color: #0000ff;">class</span><span style="color: #000000;">;
        }</span> <span style="color: #0000ff;">if</span>(!(params[index] <span style="color: #0000ff;">instanceof</span> <span style="color: #000000;">Class)){</span> <span style="color: #0000ff;">return</span> Object.<span style="color: #0000ff;">class</span><span style="color: #000000;">;
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">(Class) params[index];
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 通过反射, 获得 Class 定义中声明的父类的泛型参数类型
     * 如: public EmployeeDao extends BaseDao<Employee, String>
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;"><T>
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">clazz
     *</span> <span style="color: #808080;">@return</span>
     <span style="color: #008000;">*/</span> <span style="color: #000000;">@SuppressWarnings(</span>"unchecked"<span style="color: #000000;">)</span> <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span><T> Class<T> <span style="color: #000000;">getSuperGenericType(Class clazz){</span> <span style="color: #0000ff;">return</span> getSuperClassGenricType(clazz, 0<span style="color: #000000;">);
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 循环向上转型, 获取对象的 DeclaredMethod
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">object
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">methodName
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">parameterTypes
     *</span> <span style="color: #808080;">@return</span>
     <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> Method getDeclaredMethod(Object object, String methodName, Class<?><span style="color: #000000;">[] parameterTypes){</span> <span style="color: #0000ff;">for</span>(Class<?> superClass = object.getClass(); superClass != Object.<span style="color: #0000ff;">class</span>; superClass = <span style="color: #000000;">superClass.getSuperclass()){</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{</span> <span style="color: #008000;">//</span><span style="color: #008000;">superClass.getMethod(methodName, parameterTypes);</span>
                <span style="color: #0000ff;">return</span> <span style="color: #000000;">superClass.getDeclaredMethod(methodName, parameterTypes);
            }</span> <span style="color: #0000ff;">catch</span> <span style="color: #000000;">(NoSuchMethodException e) {</span> <span style="color: #008000;">//</span><span style="color: #008000;">Method 不在当前类定义, 继续向上转型</span>
 <span style="color: #000000;">}</span> <span style="color: #008000;">//</span><span style="color: #008000;">..</span>
 <span style="color: #000000;">}</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 使 filed 变为可访问
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">field</span> <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">makeAccessible(Field field){</span> <span style="color: #0000ff;">if</span>(!<span style="color: #000000;">Modifier.isPublic(field.getModifiers())){
            field.setAccessible(</span><span style="color: #0000ff;">true</span><span style="color: #000000;">);
        }
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 循环向上转型, 获取对象的 DeclaredField
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">object
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">filedName
     *</span> <span style="color: #808080;">@return</span>
     <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #000000;">Field getDeclaredField(Object object, String filedName){</span> <span style="color: #0000ff;">for</span>(Class<?> superClass = object.getClass(); superClass != Object.<span style="color: #0000ff;">class</span>; superClass = <span style="color: #000000;">superClass.getSuperclass()){</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">superClass.getDeclaredField(filedName);
            }</span> <span style="color: #0000ff;">catch</span> <span style="color: #000000;">(NoSuchFieldException e) {</span> <span style="color: #008000;">//</span><span style="color: #008000;">Field 不在当前类定义, 继续向上转型</span>
 <span style="color: #000000;">}
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 直接调用对象方法, 而忽略修饰符(private, protected)
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">object
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">methodName
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">parameterTypes
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">parameters
     *</span> <span style="color: #808080;">@return</span> <span style="color: #008000;">*</span> <span style="color: #808080;">@throws</span> <span style="color: #008000;">InvocationTargetException 
     *</span> <span style="color: #808080;">@throws</span> <span style="color: #008000;">IllegalArgumentException</span> <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> Object invokeMethod(Object object, String methodName, Class<?> <span style="color: #000000;">[] parameterTypes,
            Object [] parameters)</span> <span style="color: #0000ff;">throws</span> <span style="color: #000000;">InvocationTargetException{

        Method method</span> = <span style="color: #000000;">getDeclaredMethod(object, methodName, parameterTypes);</span> <span style="color: #0000ff;">if</span>(method == <span style="color: #0000ff;">null</span><span style="color: #000000;">){</span> <span style="color: #0000ff;">throw</span> <span style="color: #0000ff;">new</span> IllegalArgumentException("Could not find method [" + methodName + "] on target [" + object + "]"<span style="color: #000000;">);
        }

        method.setAccessible(</span><span style="color: #0000ff;">true</span><span style="color: #000000;">);</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">method.invoke(object, parameters);
        }</span> <span style="color: #0000ff;">catch</span><span style="color: #000000;">(IllegalAccessException e) {
            System.out.println(</span>"不可能抛出的异常"<span style="color: #000000;">);
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">null</span><span style="color: #000000;">;
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 直接设置对象属性值, 忽略 private/protected 修饰符, 也不经过 setter
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">object
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">fieldName
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">value</span> <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #0000ff;">void</span> <span style="color: #000000;">setFieldValue(Object object, String fieldName, Object value){
        Field field</span> = <span style="color: #000000;">getDeclaredField(object, fieldName);</span> <span style="color: #0000ff;">if</span> (field == <span style="color: #0000ff;">null</span><span style="color: #000000;">)</span> <span style="color: #0000ff;">throw</span> <span style="color: #0000ff;">new</span> IllegalArgumentException("Could not find field [" + fieldName + "] on target [" + object + "]"<span style="color: #000000;">);

        makeAccessible(field);</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{
            field.set(object, value);
        }</span> <span style="color: #0000ff;">catch</span> <span style="color: #000000;">(IllegalAccessException e) {
            System.out.println(</span>"不可能抛出的异常"<span style="color: #000000;">);
        }
    }</span> <span style="color: #008000;">/**</span> <span style="color: #008000;">* 直接读取对象的属性值, 忽略 private/protected 修饰符, 也不经过 getter
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">object
     *</span> <span style="color: #808080;">@param</span> <span style="color: #008000;">fieldName
     *</span> <span style="color: #808080;">@return</span>
     <span style="color: #008000;">*/</span>
    <span style="color: #0000ff;">public</span> <span style="color: #0000ff;">static</span> <span style="color: #000000;">Object getFieldValue(Object object, String fieldName){
        Field field</span> = <span style="color: #000000;">getDeclaredField(object, fieldName);</span> <span style="color: #0000ff;">if</span> (field == <span style="color: #0000ff;">null</span><span style="color: #000000;">)</span> <span style="color: #0000ff;">throw</span> <span style="color: #0000ff;">new</span> IllegalArgumentException("Could not find field [" + fieldName + "] on target [" + object + "]"<span style="color: #000000;">);

        makeAccessible(field);

        Object result</span> = <span style="color: #0000ff;">null</span><span style="color: #000000;">;</span> <span style="color: #0000ff;">try</span> <span style="color: #000000;">{
            result</span> = <span style="color: #000000;">field.get(object);
        }</span> <span style="color: #0000ff;">catch</span> <span style="color: #000000;">(IllegalAccessException e) {
            System.out.println(</span>"不可能抛出的异常"<span style="color: #000000;">);
        }</span> <span style="color: #0000ff;">return</span> <span style="color: #000000;">result;
    }
}</span></pre>

</div>

<span class="cnblogs_code_collapse">反射的 Utils 函数集合</span></div>

</div>

</div>

<div id="blog_post_info_block">

<div id="BlogPostCategory">分类: [Java](https://www.cnblogs.com/tech-bird/category/545825.html)</div>

<div id="EntryTag">标签: [反射](https://www.cnblogs.com/tech-bird/tag/%E5%8F%8D%E5%B0%84/)</div>

<div id="blog_post_info">

<div id="green_channel">[好文要顶](javascript:void(0);) [关注我](javascript:void(0);) [收藏该文](javascript:void(0);) [![](//common.cnblogs.com/images/icon_weibo_24.png)](javascript:void(0); "分享至新浪微博") [![](//common.cnblogs.com/images/wechat.png)](javascript:void(0); "分享至微信")</div>

<div id="author_profile">

<div id="author_profile_info" class="author_profile_info">[![](//pic.cnblogs.com/face/534926/20131020130509.png)](https://home.cnblogs.com/u/tech-bird/)

<div id="author_profile_detail" class="author_profile_info">[飞鸟快跑](https://home.cnblogs.com/u/tech-bird/)  
[关注 - 9](https://home.cnblogs.com/u/tech-bird/followees)  
[粉丝 - 33](https://home.cnblogs.com/u/tech-bird/followers)</div>

</div>

<div id="author_profile_follow">[+加关注](javascript:void(0);)</div>

</div>

<div id="div_digg">

<div class="diggit" onclick="votePost(3525336,'Digg')"><span class="diggnum" id="digg_count">17</span></div>

<div class="buryit" onclick="votePost(3525336,'Bury')"><span class="burynum" id="bury_count">0</span></div>

</div>

<script type="text/javascript">currentDiggType = 0;</script></div>

</div>

<div class="postDesc">posted on <span id="post-date">2014-01-18 18:04</span> [飞鸟快跑](https://www.cnblogs.com/tech-bird/) 阅读(<span id="post_view_count">53406</span>) 评论(<span id="post_comment_count">9</span>) [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=3525336) [收藏](#)</div>

</div>

<script type="text/javascript">var allowComments=true,cb_blogId=166421,cb_entryId=3525336,cb_blogApp=currentBlogApp,cb_blogUserGuid='3e774b29-35cb-e211-8d02-90b11c0b17d6',cb_entryCreatedDate='2014/1/18 18:04:00';loadViewCount(cb_entryId);var cb_postType=1;var isMarkdown=false;</script></div>
