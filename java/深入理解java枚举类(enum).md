<main>

<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-1 float-left">原</span>

# 深入理解Java枚举类型(enum)

</div>

<div class="article-info-box">

<div class="article-bar-top"><span class="time">2017年05月13日 18:27:14</span> [zejian_](https://me.csdn.net/javazejian) <span class="read-count">阅读数：241974</span></div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">

<div class="article-copyright">版权声明：本文为博主原创文章，请尊重原创，未经博主允许禁止转载，保留追究权 https://blog.csdn.net/javazejian/article/details/71333103</div>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">

<div id="content_views" class="markdown_views">

> <font size="4" color="#D90E0E">【版权申明】未经博主同意，谢绝转载！（请尊重原创，博主保留追究权）  
> [http://blog.csdn.net/javazejian/article/details/71333103](http://blog.csdn.net/javazejian/article/details/71333103)  
> 出自[【zejian的博客】](http://blog.csdn.net/javazejian)</font>

关联文章：

[深入理解Java类型信息(Class对象)与反射机制](http://blog.csdn.net/javazejian/article/details/70768369)

[深入理解Java枚举类型(enum)](http://blog.csdn.net/javazejian/article/details/71333103)

[深入理解Java注解类型(@Annotation)](http://blog.csdn.net/javazejian/article/details/71860633)

[深入理解Java并发之synchronized实现原理](http://blog.csdn.net/javazejian/article/details/72828483)

[深入理解Java内存模型(JMM)及volatile关键字](http://blog.csdn.net/javazejian/article/details/72772461)

[深入理解Java类加载器(ClassLoader)](http://blog.csdn.net/javazejian/article/details/73413292)

本篇主要是深入对Java中枚举类型进行分析，主要内容如下：

<div class="toc">

*   [理解枚举类型](#理解枚举类型)
    *   [枚举的定义](#枚举的定义)
    *   [枚举实现原理](#枚举实现原理)
    *   [枚举的常见方法](#枚举的常见方法)
        *   [Enum抽象类常见方法](#enum抽象类常见方法)
        *   [编译器生成的Values方法与ValueOf方法](#编译器生成的values方法与valueof方法)
*   [枚举与Class对象](#枚举与class对象)
*   [枚举的进阶用法](#枚举的进阶用法)
    *   [向enum类添加方法与自定义构造函数](#向enum类添加方法与自定义构造函数)
    *   [关于覆盖enum类方法](#关于覆盖enum类方法)
    *   [enum类中定义抽象方法](#enum类中定义抽象方法)
    *   [enum类与接口](#enum类与接口)
*   [枚举与switch](#枚举与switch)
*   [枚举与单例模式](#枚举与单例模式)
*   [EnumMap](#enummap)
    *   [EnumMap基本用法](#enummap基本用法)
    *   [EnumMap实现原理剖析](#enummap实现原理剖析)
*   [EnumSet](#enumset)
    *   [EnumSet用法](#enumset用法)
    *   [EnumSet实现原理剖析](#enumset实现原理剖析)
        *   [理解位向量](#理解位向量)
        *   [EnumSet原理](#enumset原理)

</div>

# <a name="t0"></a><font color="#BE1921">理解枚举类型</font>

枚举类型是Java 5中新增特性的一部分，它是一种特殊的数据类型，之所以特殊是因为它既是一种类(class)类型却又比类类型多了些特殊的约束，但是这些约束的存在也造就了枚举类型的简洁性、安全性以及便捷性。下面先来看看什么是枚举？如何定义枚举？

## <a name="t1"></a><font color="#BE1921">枚举的定义</font>

回忆一下下面的程序，这是在没有枚举类型时定义常量常见的方式

    /**
     * Created by zejian on 2017/5/7.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     * 使用普通方式定义日期常量
     */
    public class DayDemo {

        public static final int MONDAY =1;

        public static final int TUESDAY=2;

        public static final int WEDNESDAY=3;

        public static final int THURSDAY=4;

        public static final int FRIDAY=5;

        public static final int SATURDAY=6;

        public static final int SUNDAY=7;

    }

上述的常量定义常量的方式称为int枚举模式，这样的定义方式并没有什么错，但它存在许多不足，如在类型安全和使用方便性上并没有多少好处，如果存在定义int值相同的变量，混淆的几率还是很大的，编译器也不会提出任何警告，因此这种方式在枚举出现后并不提倡，现在我们利用枚举类型来重新定义上述的常量，同时也感受一把枚举定义的方式，如下定义周一到周日的常量

    //枚举类型，使用关键字enum
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY,
        THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }

相当简洁，在定义枚举类型时我们使用的关键字是enum，与class关键字类似，只不过前者是定义枚举类型，后者是定义类类型。枚举类型Day中分别定义了从周一到周日的值，这里要注意，值一般是大写的字母，多个值之间以逗号分隔。同时我们应该知道的是枚举类型可以像类(class)类型一样，定义为一个单独的文件，当然也可以定义在其他类内部，更重要的是枚举常量在类型安全性和便捷性都很有保证，如果出现类型问题编译器也会提示我们改进，但务必记住枚举表示的类型其取值是必须有限的，也就是说每个值都是可以枚举出来的，比如上述描述的一周共有七天。那么该如何使用呢？如下：

    /**
     * Created by zejian on 2017/5/7.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */
    public class EnumDemo {

        public static void main(String[] args){
            //直接引用
            Day day =Day.MONDAY;
        }

    }
    //定义枚举类型
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY,
        THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }

就像上述代码那样，直接引用枚举的值即可，这便是枚举类型的最简单模型。

## <a name="t2"></a><font color="#BE1921">枚举实现原理</font>

我们大概了解了枚举类型的定义与简单使用后，现在有必要来了解一下枚举类型的基本实现原理。实际上在使用关键字enum创建枚举类型并编译后，编译器会为我们生成一个相关的类，这个类继承了Java API中的java.lang.Enum类，也就是说通过关键字enum创建枚举类型在编译后事实上也是一个类类型而且该类继承自java.lang.Enum类。下面我们编译前面定义的EnumDemo.java并查看生成的class文件来验证这个结论：

    //查看目录下的java文件
    zejian@zejiandeMBP enumdemo$ ls
    EnumDemo.java
    //利用javac命令编译EnumDemo.java
    zejian@zejiandeMBP enumdemo$ javac EnumDemo.java 
    //查看生成的class文件，注意有Day.class和EnumDemo.class 两个
    zejian@zejiandeMBP enumdemo$ ls
    Day.class  EnumDemo.class  EnumDemo.java

利用javac编译前面定义的EnumDemo.java文件后分别生成了Day.class和EnumDemo.class文件，而Day.class就是枚举类型，这也就验证前面所说的使用关键字enum定义枚举类型并编译后，编译器会自动帮助我们生成一个与枚举相关的类。我们再来看看反编译Day.class文件：

    //反编译Day.class
    final class Day extends Enum
    {
        //编译器为我们添加的静态的values()方法
        public static Day[] values()
        {
            return (Day[])$VALUES.clone();
        }
        //编译器为我们添加的静态的valueOf()方法，注意间接调用了Enum也类的valueOf方法
        public static Day valueOf(String s)
        {
            return (Day)Enum.valueOf(com/zejian/enumdemo/Day, s);
        }
        //私有构造函数
        private Day(String s, int i)
        {
            super(s, i);
        }
         //前面定义的7种枚举实例
        public static final Day MONDAY;
        public static final Day TUESDAY;
        public static final Day WEDNESDAY;
        public static final Day THURSDAY;
        public static final Day FRIDAY;
        public static final Day SATURDAY;
        public static final Day SUNDAY;
        private static final Day $VALUES[];

        static 
        {    
            //实例化枚举实例
            MONDAY = new Day("MONDAY", 0);
            TUESDAY = new Day("TUESDAY", 1);
            WEDNESDAY = new Day("WEDNESDAY", 2);
            THURSDAY = new Day("THURSDAY", 3);
            FRIDAY = new Day("FRIDAY", 4);
            SATURDAY = new Day("SATURDAY", 5);
            SUNDAY = new Day("SUNDAY", 6);
            $VALUES = (new Day[] {
                MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
            });
        }
    }

从反编译的代码可以看出编译器确实帮助我们生成了一个Day类(注意该类是final类型的，将无法被继承)而且该类继承自java.lang.Enum类，该类是一个抽象类(稍后我们会分析该类中的主要方法)，除此之外，编译器还帮助我们生成了7个Day类型的实例对象分别对应枚举中定义的7个日期，这也充分说明了我们前面使用关键字enum定义的Day类型中的每种日期枚举常量也是实实在在的Day实例对象，只不过代表的内容不一样而已。注意编译器还为我们生成了两个静态方法，分别是values()和 valueOf()，稍后会分析它们的用法，到此我们也就明白了，使用关键字enum定义的枚举类型，在编译期后，也将转换成为一个实实在在的类，而在该类中，会存在每个在枚举类型中定义好变量的对应实例对象，如上述的MONDAY枚举类型对应`public static final Day MONDAY;`，同时编译器会为该类创建两个方法，分别是values()和valueOf()。ok~，到此相信我们对枚举的实现原理也比较清晰，下面我们深入了解一下java.lang.Enum类以及values()和valueOf()的用途。

## <a name="t3"></a><font color="#BE1921">枚举的常见方法</font>

### <a name="t4"></a><font color="#BE1921">Enum抽象类常见方法</font>

Enum是所有 Java 语言枚举类型的公共基本类（注意Enum是抽象类），以下是它的常见方法：

<div class="table-box">

<table>

<thead>

<tr>

<th align="center">返回类型</th>

<th align="center">方法名称</th>

<th>方法说明</th>

</tr>

</thead>

<tbody>

<tr>

<td align="center">`int`</td>

<td align="center">`compareTo(E o)`</td>

<td>比较此枚举与指定对象的顺序</td>

</tr>

<tr>

<td align="center">`boolean`</td>

<td align="center">`equals(Object other)`</td>

<td>当指定对象等于此枚举常量时，返回 true。</td>

</tr>

<tr>

<td align="center">`Class<?>`</td>

<td align="center">`getDeclaringClass()`</td>

<td>返回与此枚举常量的枚举类型相对应的 Class 对象</td>

</tr>

<tr>

<td align="center">`String`</td>

<td align="center">`name()`</td>

<td>返回此枚举常量的名称，在其枚举声明中对其进行声明</td>

</tr>

<tr>

<td align="center">`int`</td>

<td align="center">`ordinal()`</td>

<td>返回枚举常量的序数（它在枚举声明中的位置，其中初始常量序数为零）</td>

</tr>

<tr>

<td align="center">`String`</td>

<td align="center">`toString()`</td>

<td>返回枚举常量的名称，它包含在声明中</td>

</tr>

<tr>

<td align="center">`static<T extends Enum<T>> T`</td>

<td align="center">`static valueOf(Class<T> enumType, String name)`</td>

<td>`返回带指定名称的指定枚举类型的枚举常量。`</td>

</tr>

</tbody>

</table>

</div>

这里主要说明一下`ordinal()`方法，该方法获取的是枚举变量在枚举类中声明的顺序，下标从0开始，如日期中的MONDAY在第一个位置，那么MONDAY的ordinal值就是0，如果MONDAY的声明位置发生变化，那么ordinal方法获取到的值也随之变化，注意在大多数情况下我们都不应该首先使用该方法，毕竟它总是变幻莫测的。`compareTo(E o)`方法则是比较枚举的大小，注意其内部实现是根据每个枚举的ordinal值大小进行比较的。`name()`方法与`toString()`几乎是等同的，都是输出变量的字符串形式。至于`valueOf(Class<T> enumType, String name)`方法则是根据枚举类的Class对象和枚举名称获取枚举常量，注意该方法是静态的，后面在枚举单例时，我们还会详细分析该方法，下面的代码演示了上述方法：

    package com.zejian.enumdemo;

    /**
     * Created by zejian on 2017/5/7.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */
    public class EnumDemo {

        public static void main(String[] args){

            //创建枚举数组
            Day[] days=new Day[]{Day.MONDAY, Day.TUESDAY, Day.WEDNESDAY,
                    Day.THURSDAY, Day.FRIDAY, Day.SATURDAY, Day.SUNDAY};

            for (int i = 0; i <days.length ; i++) {
                System.out.println("day["+i+"].ordinal():"+days[i].ordinal());
            }

            System.out.println("-------------------------------------");
            //通过compareTo方法比较,实际上其内部是通过ordinal()值比较的
            System.out.println("days[0].compareTo(days[1]):"+days[0].compareTo(days[1]));
            System.out.println("days[0].compareTo(days[1]):"+days[0].compareTo(days[2]));

            //获取该枚举对象的Class对象引用,当然也可以通过getClass方法
            Class<?> clazz = days[0].getDeclaringClass();
            System.out.println("clazz:"+clazz);

            System.out.println("-------------------------------------");

            //name()
            System.out.println("days[0].name():"+days[0].name());
            System.out.println("days[1].name():"+days[1].name());
            System.out.println("days[2].name():"+days[2].name());
            System.out.println("days[3].name():"+days[3].name());

            System.out.println("-------------------------------------");

            System.out.println("days[0].toString():"+days[0].toString());
            System.out.println("days[1].toString():"+days[1].toString());
            System.out.println("days[2].toString():"+days[2].toString());
            System.out.println("days[3].toString():"+days[3].toString());

            System.out.println("-------------------------------------");

            Day d=Enum.valueOf(Day.class,days[0].name());
            Day d2=Day.valueOf(Day.class,days[0].name());
            System.out.println("d:"+d);
            System.out.println("d2:"+d2);
        }
     /**
     执行结果:
       day[0].ordinal():0
       day[1].ordinal():1
       day[2].ordinal():2
       day[3].ordinal():3
       day[4].ordinal():4
       day[5].ordinal():5
       day[6].ordinal():6
       -------------------------------------
       days[0].compareTo(days[1]):-1
       days[0].compareTo(days[1]):-2
       clazz:class com.zejian.enumdemo.Day
       -------------------------------------
       days[0].name():MONDAY
       days[1].name():TUESDAY
       days[2].name():WEDNESDAY
       days[3].name():THURSDAY
       -------------------------------------
       days[0].toString():MONDAY
       days[1].toString():TUESDAY
       days[2].toString():WEDNESDAY
       days[3].toString():THURSDAY
       -------------------------------------
       d:MONDAY
       d2:MONDAY
       */

    }
    enum Day {
        MONDAY, TUESDAY, WEDNESDAY,
        THURSDAY, FRIDAY, SATURDAY, SUNDAY
    }

到此对于抽象类Enum类的基本内容就介绍完了，这里提醒大家一点，Enum类内部会有一个构造函数，该构造函数只能有编译器调用，我们是无法手动操作的，不妨看看Enum类的主要源码：

    //实现了Comparable
    public abstract class Enum<E extends Enum<E>>
            implements Comparable<E>, Serializable {

        private final String name; //枚举字符串名称

        public final String name() {
            return name;
        }

        private final int ordinal;//枚举顺序值

        public final int ordinal() {
            return ordinal;
        }

        //枚举的构造方法，只能由编译器调用
        protected Enum(String name, int ordinal) {
            this.name = name;
            this.ordinal = ordinal;
        }

        public String toString() {
            return name;
        }

        public final boolean equals(Object other) {
            return this==other;
        }

        //比较的是ordinal值
        public final int compareTo(E o) {
            Enum<?> other = (Enum<?>)o;
            Enum<E> self = this;
            if (self.getClass() != other.getClass() && // optimization
                self.getDeclaringClass() != other.getDeclaringClass())
                throw new ClassCastException();
            return self.ordinal - other.ordinal;//根据ordinal值比较大小
        }

        @SuppressWarnings("unchecked")
        public final Class<E> getDeclaringClass() {
            //获取class对象引用，getClass()是Object的方法
            Class<?> clazz = getClass();
            //获取父类Class对象引用
            Class<?> zuper = clazz.getSuperclass();
            return (zuper == Enum.class) ? (Class<E>)clazz : (Class<E>)zuper;
        }

        public static <T extends Enum<T>> T valueOf(Class<T> enumType,
                                                    String name) {
            //enumType.enumConstantDirectory()获取到的是一个map集合，key值就是name值，value则是枚举变量值   
            //enumConstantDirectory是class对象内部的方法，根据class对象获取一个map集合的值       
            T result = enumType.enumConstantDirectory().get(name);
            if (result != null)
                return result;
            if (name == null)
                throw new NullPointerException("Name is null");
            throw new IllegalArgumentException(
                "No enum constant " + enumType.getCanonicalName() + "." + name);
        }

        //.....省略其他没用的方法
    }

通过Enum源码，可以知道，Enum实现了Comparable接口，这也是可以使用compareTo比较的原因，当然Enum构造函数也是存在的，该函数只能由编译器调用，毕竟我们只能使用enum关键字定义枚举，其他事情就放心交给编译器吧。

    //由编译器调用
    protected Enum(String name, int ordinal) {
            this.name = name;
            this.ordinal = ordinal;
        }

### <a name="t5"></a><font color="#BE1921">编译器生成的Values方法与ValueOf方法</font>

values()方法和valueOf(String name)方法是编译器生成的static方法，因此从前面的分析中，在Enum类中并没出现values()方法，但valueOf()方法还是有出现的，只不过编译器生成的valueOf()方法需传递一个name参数，而Enum自带的静态方法valueOf()则需要传递两个方法，从前面反编译后的代码可以看出，编译器生成的valueOf方法最终还是调用了Enum类的valueOf方法，下面通过代码来演示这两个方法的作用：

    Day[] days2 = Day.values();
    System.out.println("day2:"+Arrays.toString(days2));
    Day day = Day.valueOf("MONDAY");
    System.out.println("day:"+day);

    /**
     输出结果:
     day2:[MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]
     day:MONDAY
     */

从结果可知道，values()方法的作用就是获取枚举类中的所有变量，并作为数组返回，而valueOf(String name)方法与Enum类中的valueOf方法的作用类似根据名称获取枚举变量，只不过编译器生成的valueOf方法更简洁些只需传递一个参数。这里我们还必须注意到，由于values()方法是由编译器插入到枚举类中的static方法，所以如果我们将枚举实例向上转型为Enum，那么values()方法将无法被调用，因为Enum类中并没有values()方法，valueOf()方法也是同样的道理，注意是一个参数的。

     //正常使用
    Day[] ds=Day.values();
    //向上转型Enum
    Enum e = Day.MONDAY;
    //无法调用,没有此方法
    //e.values();

# <a name="t6"></a><font color="#BE1921">枚举与Class对象</font>

上述我们提到当枚举实例向上转型为Enum类型后，values()方法将会失效，也就无法一次性获取所有枚举实例变量，但是由于Class对象的存在，即使不使用values()方法，还是有可能一次获取到所有枚举实例变量的，在Class对象中存在如下方法：

<div class="table-box">

<table>

<thead>

<tr>

<th align="center">返回类型</th>

<th align="center">方法名称</th>

<th>方法说明</th>

</tr>

</thead>

<tbody>

<tr>

<td align="center">`T[]`</td>

<td align="center">`getEnumConstants()`</td>

<td>返回该枚举类型的所有元素，如果Class对象不是枚举类型，则返回null。</td>

</tr>

<tr>

<td align="center">`boolean`</td>

<td align="center">`isEnum()`</td>

<td>当且仅当该类声明为源代码中的枚举时返回 true</td>

</tr>

</tbody>

</table>

</div>

因此通过getEnumConstants()方法，同样可以轻而易举地获取所有枚举实例变量下面通过代码来演示这个功能：

    //正常使用
    Day[] ds=Day.values();
    //向上转型Enum
    Enum e = Day.MONDAY;
    //无法调用,没有此方法
    //e.values();
    //获取class对象引用
    Class<?> clasz = e.getDeclaringClass();
    if(clasz.isEnum()) {
        Day[] dsz = (Day[]) clasz.getEnumConstants();
        System.out.println("dsz:"+Arrays.toString(dsz));
    }

    /**
       输出结果:
       dsz:[MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]
     */

正如上述代码所展示，通过Enum的class对象的getEnumConstants方法，我们仍能一次性获取所有的枚举实例常量。

# <a name="t7"></a><font color="#BE1921">枚举的进阶用法</font>

在前面的分析中，我们都是基于简单枚举类型的定义，也就是在定义枚举时只定义了枚举实例类型，并没定义方法或者成员变量，实际上使用关键字enum定义的枚举类，除了不能使用继承(因为编译器会自动为我们继承Enum抽象类而Java只支持单继承，因此枚举类是无法手动实现继承的)，可以把enum类当成常规类，也就是说我们可以向enum类中添加方法和变量，甚至是mian方法，下面就来感受一把。

## <a name="t8"></a><font color="#BE1921">向enum类添加方法与自定义构造函数</font>

重新定义一个日期枚举类，带有desc成员变量描述该日期的对于中文描述，同时定义一个getDesc方法，返回中文描述内容，自定义私有构造函数，在声明枚举实例时传入对应的中文描述，代码如下：

    package com.zejian.enumdemo;

    /**
     * Created by zejian on 2017/5/8.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */
    public enum Day2 {
        MONDAY("星期一"),
        TUESDAY("星期二"),
        WEDNESDAY("星期三"),
        THURSDAY("星期四"),
        FRIDAY("星期五"),
        SATURDAY("星期六"),
        SUNDAY("星期日");//记住要用分号结束

        private String desc;//中文描述

        /**
         * 私有构造,防止被外部调用
         * @param desc
         */
        private Day2(String desc){
            this.desc=desc;
        }

        /**
         * 定义方法,返回描述,跟常规类的定义没区别
         * @return
         */
        public String getDesc(){
            return desc;
        }

        public static void main(String[] args){
            for (Day2 day:Day2.values()) {
                System.out.println("name:"+day.name()+
                        ",desc:"+day.getDesc());
            }
        }

        /**
         输出结果:
         name:MONDAY,desc:星期一
         name:TUESDAY,desc:星期二
         name:WEDNESDAY,desc:星期三
         name:THURSDAY,desc:星期四
         name:FRIDAY,desc:星期五
         name:SATURDAY,desc:星期六
         name:SUNDAY,desc:星期日
         */
    }

从上述代码可知，在enum类中确实可以像定义常规类一样声明变量或者成员方法。但是我们必须注意到，如果打算在enum类中定义方法，务必在声明完枚举实例后使用分号分开，倘若在枚举实例前定义任何方法，编译器都将会报错，无法编译通过，同时即使自定义了构造函数且enum的定义结束，我们也永远无法手动调用构造函数创建枚举实例，毕竟这事只能由编译器执行。

## <a name="t9"></a><font color="#BE1921">关于覆盖enum类方法</font>

既然enum类跟常规类的定义没什么区别（实际上enum还是有些约束的），那么覆盖父类的方法也不会是什么难说，可惜的是父类Enum中的定义的方法只有toString方法没有使用final修饰，因此只能覆盖toString方法，如下通过覆盖toString省去了getDesc方法：

    package com.zejian.enumdemo;

    /**
     * Created by zejian on 2017/5/8.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */
    public enum Day2 {
        MONDAY("星期一"),
        TUESDAY("星期二"),
        WEDNESDAY("星期三"),
        THURSDAY("星期四"),
        FRIDAY("星期五"),
        SATURDAY("星期六"),
        SUNDAY("星期日");//记住要用分号结束

        private String desc;//中文描述

        /**
         * 私有构造,防止被外部调用
         * @param desc
         */
        private Day2(String desc){
            this.desc=desc;
        }

        /**
         * 覆盖
         * @return
         */
        @Override
        public String toString() {
            return desc;
        }

        public static void main(String[] args){
            for (Day2 day:Day2.values()) {
                System.out.println("name:"+day.name()+
                        ",desc:"+day.toString());
            }
        }

        /**
         输出结果:
         name:MONDAY,desc:星期一
         name:TUESDAY,desc:星期二
         name:WEDNESDAY,desc:星期三
         name:THURSDAY,desc:星期四
         name:FRIDAY,desc:星期五
         name:SATURDAY,desc:星期六
         name:SUNDAY,desc:星期日
         */
    }

## <a name="t10"></a><font color="#BE1921">enum类中定义抽象方法</font>

与常规抽象类一样，enum类允许我们为其定义抽象方法，然后使每个枚举实例都实现该方法，以便产生不同的行为方式，注意abstract关键字对于枚举类来说并不是必须的如下：

    package com.zejian.enumdemo;

    /**
     * Created by zejian on 2017/5/9.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */
    public enum EnumDemo3 {

        FIRST{
            @Override
            public String getInfo() {
                return "FIRST TIME";
            }
        },
        SECOND{
            @Override
            public String getInfo() {
                return "SECOND TIME";
            }
        }

        ;

        /**
         * 定义抽象方法
         * @return
         */
        public abstract String getInfo();

        //测试
        public static void main(String[] args){
            System.out.println("F:"+EnumDemo3.FIRST.getInfo());
            System.out.println("S:"+EnumDemo3.SECOND.getInfo());
            /**
             输出结果:
             F:FIRST TIME
             S:SECOND TIME
             */
        }
    }

通过这种方式就可以轻而易举地定义每个枚举实例的不同行为方式。我们可能注意到，enum类的实例似乎表现出了多态的特性，可惜的是枚举类型的实例终究不能作为类型传递使用，就像下面的使用方式，编译器是不可能答应的：

    //无法通过编译,毕竟EnumDemo3.FIRST是个实例对象
     public void text(EnumDemo3.FIRST instance){ }

在枚举实例常量中定义抽象方法

## <a name="t11"></a><font color="#BE1921">enum类与接口</font>

由于Java单继承的原因，enum类并不能再继承其它类，但并不妨碍它实现接口，因此enum类同样是可以实现多接口的，如下：

    package com.zejian.enumdemo;

    /**
     * Created by zejian on 2017/5/8.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */

    interface food{
        void eat();
    }

    interface sport{
        void run();
    }

    public enum EnumDemo2 implements food ,sport{
        FOOD,
        SPORT,
        ; //分号分隔

        @Override
        public void eat() {
            System.out.println("eat.....");
        }

        @Override
        public void run() {
            System.out.println("run.....");
        }
    }

有时候，我们可能需要对一组数据进行分类，比如进行食物菜单分类而且希望这些菜单都属于food类型，appetizer(开胃菜)、mainCourse(主菜)、dessert(点心)、Coffee等，每种分类下有多种具体的菜式或食品，此时可以利用接口来组织，如下(代码引用自Thinking in Java)：

    public interface Food {
      enum Appetizer implements Food {
        SALAD, SOUP, SPRING_ROLLS;
      }
      enum MainCourse implements Food {
        LASAGNE, BURRITO, PAD_THAI,
        LENTILS, HUMMOUS, VINDALOO;
      }
      enum Dessert implements Food {
        TIRAMISU, GELATO, BLACK_FOREST_CAKE,
        FRUIT, CREME_CARAMEL;
      }
      enum Coffee implements Food {
        BLACK_COFFEE, DECAF_COFFEE, ESPRESSO,
        LATTE, CAPPUCCINO, TEA, HERB_TEA;
      }
    }

    public class TypeOfFood {
      public static void main(String[] args) {
        Food food = Appetizer.SALAD;
        food = MainCourse.LASAGNE;
        food = Dessert.GELATO;
        food = Coffee.CAPPUCCINO;
      }
    } 

通过这种方式可以很方便组织上述的情景，同时确保每种具体类型的食物也属于Food，现在我们利用一个枚举嵌套枚举的方式，把前面定义的菜谱存放到一个Meal菜单中，通过这种方式就可以统一管理菜单的数据了。

    public enum Meal{
      APPETIZER(Food.Appetizer.class),
      MAINCOURSE(Food.MainCourse.class),
      DESSERT(Food.Dessert.class),
      COFFEE(Food.Coffee.class);
      private Food[] values;
      private Meal(Class<? extends Food> kind) {
        //通过class对象获取枚举实例
        values = kind.getEnumConstants();
      }
      public interface Food {
        enum Appetizer implements Food {
          SALAD, SOUP, SPRING_ROLLS;
        }
        enum MainCourse implements Food {
          LASAGNE, BURRITO, PAD_THAI,
          LENTILS, HUMMOUS, VINDALOO;
        }
        enum Dessert implements Food {
          TIRAMISU, GELATO, BLACK_FOREST_CAKE,
          FRUIT, CREME_CARAMEL;
        }
        enum Coffee implements Food {
          BLACK_COFFEE, DECAF_COFFEE, ESPRESSO,
          LATTE, CAPPUCCINO, TEA, HERB_TEA;
        }
      }
    } 

# <a name="t12"></a><font color="#BE1921">枚举与switch</font>

关于枚举与switch是个比较简单的话题，使用switch进行条件判断时，条件参数一般只能是整型，字符型。而枚举型确实也被switch所支持，在java 1.7后switch也对字符串进行了支持。这里我们简单看一下switch与枚举类型的使用：

    /**
     * Created by zejian on 2017/5/9.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */

    enum Color {GREEN,RED,BLUE}

    public class EnumDemo4 {

        public static void printName(Color color){
            switch (color){
                case BLUE: //无需使用Color进行引用
                    System.out.println("蓝色");
                    break;
                case RED:
                    System.out.println("红色");
                    break;
                case GREEN:
                    System.out.println("绿色");
                    break;
            }
        }

        public static void main(String[] args){
            printName(Color.BLUE);
            printName(Color.RED);
            printName(Color.GREEN);

            //蓝色
            //红色
            //绿色
        }
    }

需要注意的是使用在于switch条件进行结合使用时，无需使用Color引用。

# <a name="t13"></a><font color="#BE1921">枚举与单例模式</font>

单例模式可以说是最常使用的设计模式了，它的作用是确保某个类只有一个实例，自行实例化并向整个系统提供这个实例。在实际应用中，线程池、缓存、日志对象、对话框对象常被设计成单例，总之，选择单例模式就是为了避免不一致状态，下面我们将会简单说明单例模式的几种主要编写方式，从而对比出使用枚举实现单例模式的优点。首先看看饿汉式的单例模式：

    /**
     * Created by wuzejian on 2017/5/9.
     * 饿汉式（基于classloder机制避免了多线程的同步问题）
     */
    public class SingletonHungry {

        private static SingletonHungry instance = new SingletonHungry();

        private SingletonHungry() {
        }

        public static SingletonHungry getInstance() {
            return instance;
        }
    }

显然这种写法比较简单，但问题是无法做到延迟创建对象，事实上如果该单例类涉及资源较多，创建比较耗时间时，我们更希望它可以尽可能地延迟加载，从而减小初始化的负载，于是便有了如下的懒汉式单例：

    /**
     * Created by wuzejian on 2017/5/9..
     * 懒汉式单例模式（适合多线程安全）
     */
    public class SingletonLazy {

        private static volatile SingletonLazy instance;

        private SingletonLazy() {
        }

        public static synchronized SingletonLazy getInstance() {
            if (instance == null) {
                instance = new SingletonLazy();
            }
            return instance;
        }
    }

这种写法能够在多线程中很好的工作避免同步问题，同时也具备lazy loading机制，遗憾的是，由于synchronized的存在，效率很低，在单线程的情景下，完全可以去掉synchronized，为了兼顾效率与性能问题，改进后代码如下：

    public class Singleton {
        private static volatile Singleton singleton = null;

        private Singleton(){}

        public static Singleton getSingleton(){
            if(singleton == null){
                synchronized (Singleton.class){
                    if(singleton == null){
                        singleton = new Singleton();
                    }
                }
            }
            return singleton;
        }    
    }

这种编写方式被称为“双重检查锁”，主要在getSingleton()方法中，进行两次null检查。这样可以极大提升并发度，进而提升性能。毕竟在单例中new的情况非常少，绝大多数都是可以并行的读操作，因此在加锁前多进行一次null检查就可以减少绝大多数的加锁操作，也就提高了执行效率。但是必须注意的是volatile关键字，该关键字有两层语义。第一层语义是可见性，可见性是指在一个线程中对该变量的修改会马上由工作内存（Work Memory）写回主内存（Main Memory），所以其它线程会马上读取到已修改的值，关于工作内存和主内存可简单理解为高速缓存（直接与CPU打交道）和主存（日常所说的内存条），注意工作内存是线程独享的，主存是线程共享的。volatile的第二层语义是禁止指令重排序优化，我们写的代码（特别是多线程代码），由于编译器优化，在实际执行的时候可能与我们编写的顺序不同。编译器只保证程序执行结果与源代码相同，却不保证实际指令的顺序与源代码相同，这在单线程并没什么问题，然而一旦引入多线程环境，这种乱序就可能导致严重问题。volatile关键字就可以从语义上解决这个问题，值得关注的是volatile的禁止指令重排序优化功能在Java 1.5后才得以实现，因此1.5前的版本仍然是不安全的，即使使用了volatile关键字。或许我们可以利用静态内部类来实现更安全的机制，静态内部类单例模式如下：

    /**
     * Created by wuzejian on 2017/5/9.
     * 静态内部类
     */
    public class SingletonInner {
        private static class Holder {
            private static SingletonInner singleton = new SingletonInner();
        }

        private SingletonInner(){}

        public static SingletonInner getSingleton(){
            return Holder.singleton;
        }
    }

正如上述代码所展示的，我们把Singleton实例放到一个静态内部类中，这样可以避免了静态实例在Singleton类的加载阶段（类加载过程的其中一个阶段的，此时只创建了Class对象，关于Class对象可以看博主另外一篇博文， [深入理解Java类型信息(Class对象)与反射机制](http://blog.csdn.net/javazejian/article/details/70768369)）就创建对象，毕竟静态变量初始化是在SingletonInner类初始化时触发的，并且由于静态内部类只会被加载一次，所以这种写法也是线程安全的。从上述4种单例模式的写法中，似乎也解决了效率与懒加载的问题，但是它们都有两个共同的缺点：

*   序列化可能会破坏单例模式，比较每次反序列化一个序列化的对象实例时都会创建一个新的实例，解决方案如下：

        //测试例子(四种写解决方式雷同)
        public class Singleton implements java.io.Serializable {     
           public static Singleton INSTANCE = new Singleton();     

           protected Singleton() {     
           }  

           //反序列时直接返回当前INSTANCE
           private Object readResolve() {     
                    return INSTANCE;     
              }    
        }   

*   使用反射强行调用私有构造器，解决方式可以修改构造器，让它在创建第二个实例的时候抛异常，如下：

        public static Singleton INSTANCE = new Singleton();     
        private static volatile  boolean  flag = true;
        private Singleton(){
            if(flag){
            flag = false;   
            }else{
                throw new RuntimeException("The instance  already exists ！");
            }
        }

如上所述，问题确实也得到了解决，但问题是我们为此付出了不少努力，即添加了不少代码，还应该注意到如果单例类维持了其他对象的状态时还需要使他们成为transient的对象，这种就更复杂了，那有没有更简单更高效的呢？当然是有的，那就是枚举单例了，先来看看如何实现：

    /**
     * Created by wuzejian on 2017/5/9.
     * 枚举单利
     */
    public enum  SingletonEnum {
        INSTANCE;
        private String name;
        public String getName(){
            return name;
        }
        public void setName(String name){
            this.name = name;
        }
    }

代码相当简洁，我们也可以像常规类一样编写enum类，为其添加变量和方法，访问方式也更简单，使用`SingletonEnum.INSTANCE`进行访问，这样也就避免调用getInstance方法，更重要的是使用枚举单例的写法，我们完全不用考虑序列化和反射的问题。枚举序列化是由jvm保证的，每一个枚举类型和定义的枚举变量在JVM中都是唯一的，在枚举类型的序列化和反序列化上，Java做了特殊的规定：在序列化时Java仅仅是将枚举对象的name属性输出到结果中，反序列化的时候则是通过java.lang.Enum的valueOf方法来根据名字查找枚举对象。同时，编译器是不允许任何对这种序列化机制的定制的并禁用了writeObject、readObject、readObjectNoData、writeReplace和readResolve等方法，从而保证了枚举实例的唯一性，这里我们不妨再次看看Enum类的valueOf方法：

    public static <T extends Enum<T>> T valueOf(Class<T> enumType,
                                                  String name) {
          T result = enumType.enumConstantDirectory().get(name);
          if (result != null)
              return result;
          if (name == null)
              throw new NullPointerException("Name is null");
          throw new IllegalArgumentException(
              "No enum constant " + enumType.getCanonicalName() + "." + name);
      }

实际上通过调用enumType(Class对象的引用)的enumConstantDirectory方法获取到的是一个Map集合，在该集合中存放了以枚举name为key和以枚举实例变量为value的Key&Value数据，因此通过name的值就可以获取到枚举实例，看看enumConstantDirectory方法源码：

    Map<String, T> enumConstantDirectory() {
            if (enumConstantDirectory == null) {
                //getEnumConstantsShared最终通过反射调用枚举类的values方法
                T[] universe = getEnumConstantsShared();
                if (universe == null)
                    throw new IllegalArgumentException(
                        getName() + " is not an enum type");
                Map<String, T> m = new HashMap<>(2 * universe.length);
                //map存放了当前enum类的所有枚举实例变量，以name为key值
                for (T constant : universe)
                    m.put(((Enum<?>)constant).name(), constant);
                enumConstantDirectory = m;
            }
            return enumConstantDirectory;
        }
        private volatile transient Map<String, T> enumConstantDirectory = null;

到这里我们也就可以看出枚举序列化确实不会重新创建新实例，jvm保证了每个枚举实例变量的唯一性。再来看看反射到底能不能创建枚举，下面试图通过反射获取构造器并创建枚举

    public static void main(String[] args) throws IllegalAccessException, InvocationTargetException, InstantiationException, NoSuchMethodException {
      //获取枚举类的构造函数(前面的源码已分析过)
       Constructor<SingletonEnum> constructor=SingletonEnum.class.getDeclaredConstructor(String.class,int.class);
       constructor.setAccessible(true);
       //创建枚举
       SingletonEnum singleton=constructor.newInstance("otherInstance",9);
      }

执行报错

    Exception in thread "main" java.lang.IllegalArgumentException: Cannot reflectively create enum objects
        at java.lang.reflect.Constructor.newInstance(Constructor.java:417)
        at zejian.SingletonEnum.main(SingletonEnum.java:38)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:498)
        at com.intellij.rt.execution.application.AppMain.main(AppMain.java:144)

显然告诉我们不能使用反射创建枚举类，这是为什么呢？不妨看看newInstance方法源码：

     public T newInstance(Object ... initargs)
            throws InstantiationException, IllegalAccessException,
                   IllegalArgumentException, InvocationTargetException
        {
            if (!override) {
                if (!Reflection.quickCheckMemberAccess(clazz, modifiers)) {
                    Class<?> caller = Reflection.getCallerClass();
                    checkAccess(caller, clazz, null, modifiers);
                }
            }
            //这里判断Modifier.ENUM是不是枚举修饰符，如果是就抛异常
            if ((clazz.getModifiers() & Modifier.ENUM) != 0)
                throw new IllegalArgumentException("Cannot reflectively create enum objects");
            ConstructorAccessor ca = constructorAccessor;   // read volatile
            if (ca == null) {
                ca = acquireConstructorAccessor();
            }
            @SuppressWarnings("unchecked")
            T inst = (T) ca.newInstance(initargs);
            return inst;
        }

源码很了然，确实无法使用反射创建枚举实例，也就是说明了创建枚举实例只有编译器能够做到而已。显然枚举单例模式确实是很不错的选择，因此我们推荐使用它。但是这总不是万能的，对于android平台这个可能未必是最好的选择，在android开发中，内存优化是个大块头，而使用枚举时占用的内存常常是静态变量的两倍还多，因此android官方在内存优化方面给出的建议是尽量避免在android中使用enum。但是不管如何，关于单例，我们总是应该记住：线程安全，延迟加载，序列化与反序列化安全，反射安全是很重重要的。

# <a name="t14"></a><font color="#BE1921">EnumMap</font>

## <a name="t15"></a><font color="#BE1921">EnumMap基本用法</font>

先思考这样一个问题，现在我们有一堆size大小相同而颜色不同的数据，需要统计出每种颜色的数量是多少以便将数据录入仓库，定义如下枚举用于表示颜色Color:

    enum Color {
        GREEN,RED,BLUE,YELLOW
    }

我们有如下解决方案，使用Map集合来统计，key值作为颜色名称，value代表衣服数量，如下：

    package com.zejian.enumdemo;

    import java.util.*;

    /**
     * Created by zejian on 2017/5/10.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     */
    public class EnumMapDemo {
        public static void main(String[] args){
            List<Clothes> list = new ArrayList<>();
            list.add(new Clothes("C001",Color.BLUE));
            list.add(new Clothes("C002",Color.YELLOW));
            list.add(new Clothes("C003",Color.RED));
            list.add(new Clothes("C004",Color.GREEN));
            list.add(new Clothes("C005",Color.BLUE));
            list.add(new Clothes("C006",Color.BLUE));
            list.add(new Clothes("C007",Color.RED));
            list.add(new Clothes("C008",Color.YELLOW));
            list.add(new Clothes("C009",Color.YELLOW));
            list.add(new Clothes("C010",Color.GREEN));
            //方案1:使用HashMap
            Map<String,Integer> map = new HashMap<>();
            for (Clothes clothes:list){
               String colorName=clothes.getColor().name();
               Integer count = map.get(colorName);
                if(count!=null){
                    map.put(colorName,count+1);
                }else {
                    map.put(colorName,1);
                }
            }

            System.out.println(map.toString());

            System.out.println("---------------");

            //方案2:使用EnumMap
            Map<Color,Integer> enumMap=new EnumMap<>(Color.class);

            for (Clothes clothes:list){
                Color color=clothes.getColor();
                Integer count = enumMap.get(color);
                if(count!=null){
                    enumMap.put(color,count+1);
                }else {
                    enumMap.put(color,1);
                }
            }

            System.out.println(enumMap.toString());
        }

        /**
         输出结果:
         {RED=2, BLUE=3, YELLOW=3, GREEN=2}
         ---------------
         {GREEN=2, RED=2, BLUE=3, YELLOW=3}
         */
    }

代码比较简单，我们使用两种解决方案，一种是HashMap，一种EnumMap，虽然都统计出了正确的结果，但是EnumMap作为枚举的专属的集合，我们没有理由再去使用HashMap，毕竟EnumMap要求其Key必须为Enum类型，因而使用Color枚举实例作为key是最恰当不过了，也避免了获取name的步骤，更重要的是EnumMap效率更高，因为其内部是通过数组实现的（稍后分析），注意EnumMap的key值不能为null，虽说是枚举专属集合，但其操作与一般的Map差不多，概括性来说EnumMap是专门为枚举类型量身定做的Map实现，虽然使用其它的Map（如HashMap）也能完成相同的功能，但是使用EnumMap会更加高效，它只能接收同一枚举类型的实例作为键值且不能为null，由于枚举类型实例的数量相对固定并且有限，所以EnumMap使用数组来存放与枚举类型对应的值，毕竟数组是一段连续的内存空间，根据程序局部性原理，效率会相当高。下面我们来进一步了解EnumMap的用法，先看构造函数：

    //创建一个具有指定键类型的空枚举映射。
    EnumMap(Class<K> keyType) 
    //创建一个其键类型与指定枚举映射相同的枚举映射，最初包含相同的映射关系（如果有的话）。     
    EnumMap(EnumMap<K,? extends V> m) 
    //创建一个枚举映射，从指定映射对其初始化。
    EnumMap(Map<K,? extends V> m)       

与HashMap不同，它需要传递一个类型信息，即Class对象，通过这个参数EnumMap就可以根据类型信息初始化其内部数据结构，另外两只是初始化时传入一个Map集合，代码演示如下：

    //使用第一种构造
    Map<Color,Integer> enumMap=new EnumMap<>(Color.class);
    //使用第二种构造
    Map<Color,Integer> enumMap2=new EnumMap<>(enumMap);
    //使用第三种构造
    Map<Color,Integer> hashMap = new HashMap<>();
    hashMap.put(Color.GREEN, 2);
    hashMap.put(Color.BLUE, 3);
    Map<Color, Integer> enumMap = new EnumMap<>(hashMap);

至于EnumMap的方法，跟普通的map几乎没有区别，注意与HashMap的主要不同在于构造方法需要传递类型参数和EnumMap保证Key顺序与枚举中的顺序一致，但请记住Key不能为null。

## <a name="t16"></a><font color="#BE1921">EnumMap实现原理剖析</font>

EnumMap的源码有700多行，这里我们主要分析其内部存储结构，添加查找的实现，了解这几点，对应EnumMap内部实现原理也就比较清晰了，先看数据结构和构造函数

    public class EnumMap<K extends Enum<K>, V> extends AbstractMap<K, V>
        implements java.io.Serializable, Cloneable
    {
        //Class对象引用
        private final Class<K> keyType;

        //存储Key值的数组
        private transient K[] keyUniverse;

        //存储Value值的数组
        private transient Object[] vals;

        //map的size
        private transient int size = 0;

        //空map
        private static final Enum<?>[] ZERO_LENGTH_ENUM_ARRAY = new Enum<?>[0];

        //构造函数
        public EnumMap(Class<K> keyType) {
            this.keyType = keyType;
            keyUniverse = getKeyUniverse(keyType);
            vals = new Object[keyUniverse.length];
        }

    }

EnumMap继承了AbstractMap类，因此EnumMap具备一般map的使用方法，keyType表示类型信息，keyUniverse表示键数组，存储的是所有可能的枚举值，vals数组表示键对应的值，size表示键值对个数。在构造函数中通过`keyUniverse = getKeyUniverse(keyType);`初始化了keyUniverse数组的值，内部存储的是所有可能的枚举值，接着初始化了存在Value值得数组vals，其大小与枚举实例的个数相同，getKeyUniverse方法实现如下

    //返回枚举数组
    private static <K extends Enum<K>> K[] getKeyUniverse(Class<K> keyType) {
            //最终调用到枚举类型的values方法，values方法返回所有可能的枚举值
            return SharedSecrets.getJavaLangAccess()
                                            .getEnumConstantsShared(keyType);
        }

从方法的返回值来看，返回类型是枚举数组，事实也是如此，最终返回值正是枚举类型的values方法的返回值，前面我们分析过values方法返回所有可能的枚举值，因此keyUniverse数组存储就是枚举类型的所有可能的枚举值。接着看put方法的实现

     public V put(K key, V value) {
            typeCheck(key);//检测key的类型
            //获取存放value值得数组下标
            int index = key.ordinal();
            //获取旧值
            Object oldValue = vals[index];
            //设置value值
            vals[index] = maskNull(value);
            if (oldValue == null)
                size++;
            return unmaskNull(oldValue);//返回旧值
        }

这里通过typeCheck方法进行了key类型检测，判断是否为枚举类型，如果类型不对，会抛出异常

    private void typeCheck(K key) {
       Class<?> keyClass = key.getClass();//获取类型信息
       if (keyClass != keyType && keyClass.getSuperclass() != keyType)
           throw new ClassCastException(keyClass + " != " + keyType);
    }

接着通过`int index = key.ordinal()`的方式获取到该枚举实例的顺序值，利用此值作为下标，把值存储在vals数组对应下标的元素中即`vals[index]`，这也是为什么EnumMap能维持与枚举实例相同存储顺序的原因，我们发现在对vals[]中元素进行赋值和返回旧值时分别调用了maskNull方法和unmaskNull方法

     //代表NULL值得空对象实例
      private static final Object NULL = new Object() {
            public int hashCode() {
                return 0;
            }

            public String toString() {
                return "java.util.EnumMap.NULL";
            }
        };

        private Object maskNull(Object value) {
            //如果值为空，返回NULL对象，否则返回value
            return (value == null ? NULL : value);
        }

        @SuppressWarnings("unchecked")
        private V unmaskNull(Object value) {
            //将NULL对象转换为null值
            return (V)(value == NULL ? null : value);
        }

由此看来EnumMap还是允许存放null值的，但key绝对不能为null，对于null值，EnumMap进行了特殊处理,将其包装为NULL对象，毕竟vals[]存的是Object，maskNull方法和unmaskNull方法正是用于null的包装和解包装的。这就是EnumMap集合的添加过程。下面接着看获取方法

     public V get(Object key) {
            return (isValidKey(key) ?
                    unmaskNull(vals[((Enum<?>)key).ordinal()]) : null);
        }

     //对Key值的有效性和类型信息进行判断
     private boolean isValidKey(Object key) {
          if (key == null)
              return false;

          // Cheaper than instanceof Enum followed by getDeclaringClass
          Class<?> keyClass = key.getClass();
          return keyClass == keyType || keyClass.getSuperclass() == keyType;
      }

相对应put方法，get方法显示相当简洁，key有效的话，直接通过ordinal方法取索引，然后在值数组vals里通过索引获取值返回。remove方法如下：

     public V remove(Object key) {
            //判断key值是否有效
            if (!isValidKey(key))
                return null;
            //直接获取索引
            int index = ((Enum<?>)key).ordinal();

            Object oldValue = vals[index];
            //对应下标元素值设置为null
            vals[index] = null;
            if (oldValue != null)
                size--;//减size
            return unmaskNull(oldValue);
        }

非常简单，key值有效，通过key获取下标索引值，把vals[]对应下标值设置为null，size减一。查看是否包含某个值，

    判断是否包含某value
    public boolean containsValue(Object value) {
        value = maskNull(value);
        //遍历数组实现
        for (Object val : vals)
            if (value.equals(val))
                return true;

        return false;
    }
    //判断是否包含key
    public boolean containsKey(Object key) {
        return isValidKey(key) && vals[((Enum<?>)key).ordinal()] != null;
    }

判断value直接通过遍历数组实现，而判断key就更简单了，判断key是否有效和对应vals[]中是否存在该值。ok~，这就是EnumMap的主要实现原理，即内部有两个数组，长度相同，一个表示所有可能的键(枚举值)，一个表示对应的值，不允许keynull，但允许value为null，键都有一个对应的索引，根据索引直接访问和操作其键数组和值数组，由于操作都是数组，因此效率很高。

# <a name="t17"></a><font color="#BE1921">EnumSet</font>

EnumSet是与枚举类型一起使用的专用 Set 集合，EnumSet 中所有元素都必须是枚举类型。与其他Set接口的实现类HashSet/TreeSet(内部都是用对应的HashMap/TreeMap实现的)不同的是，EnumSet在内部实现是位向量(稍后分析)，它是一种极为高效的位运算操作，由于直接存储和操作都是bit，因此EnumSet空间和时间性能都十分可观，足以媲美传统上基于 int 的“位标志”的运算，重要的是我们可像操作set集合一般来操作位运算，这样使用代码更简单易懂同时又具备类型安全的优势。注意EnumSet不允许使用 null 元素。试图插入 null 元素将抛出 NullPointerException，但试图测试判断是否存在null 元素或移除 null 元素则不会抛出异常，与大多数collection 实现一样，EnumSet不是线程安全的，因此在多线程环境下应该注意数据同步问题，ok~，下面先来简单看看EnumSet的使用方式。

## <a name="t18"></a><font color="#BE1921">EnumSet用法</font>

创建EnumSet并不能使用new关键字，因为它是个抽象类，而应该使用其提供的静态工厂方法，EnumSet的静态工厂方法比较多，如下：

    创建一个具有指定元素类型的空EnumSet。
    EnumSet<E>  noneOf(Class<E> elementType)       
    //创建一个指定元素类型并包含所有枚举值的EnumSet
    <E extends Enum<E>> EnumSet<E> allOf(Class<E> elementType)
    // 创建一个包括枚举值中指定范围元素的EnumSet
    <E extends Enum<E>> EnumSet<E> range(E from, E to)
    // 初始集合包括指定集合的补集
    <E extends Enum<E>> EnumSet<E> complementOf(EnumSet<E> s)
    // 创建一个包括参数中所有元素的EnumSet
    <E extends Enum<E>> EnumSet<E> of(E e)
    <E extends Enum<E>> EnumSet<E> of(E e1, E e2)
    <E extends Enum<E>> EnumSet<E> of(E e1, E e2, E e3)
    <E extends Enum<E>> EnumSet<E> of(E e1, E e2, E e3, E e4)
    <E extends Enum<E>> EnumSet<E> of(E e1, E e2, E e3, E e4, E e5)
    <E extends Enum<E>> EnumSet<E> of(E first, E... rest)
    //创建一个包含参数容器中的所有元素的EnumSet
    <E extends Enum<E>> EnumSet<E> copyOf(EnumSet<E> s)
    <E extends Enum<E>> EnumSet<E> copyOf(Collection<E> c)

代码演示如下：

    package zejian;

    import java.util.ArrayList;
    import java.util.EnumSet;
    import java.util.List;

    /**
     * Created by wuzejian on 2017/5/12.
     *
     */
    enum Color {
        GREEN , RED , BLUE , BLACK , YELLOW
    }

    public class EnumSetDemo {

        public static void main(String[] args){

            //空集合
            EnumSet<Color> enumSet= EnumSet.noneOf(Color.class);
            System.out.println("添加前："+enumSet.toString());
            enumSet.add(Color.GREEN);
            enumSet.add(Color.RED);
            enumSet.add(Color.BLACK);
            enumSet.add(Color.BLUE);
            enumSet.add(Color.YELLOW);
            System.out.println("添加后："+enumSet.toString());

            System.out.println("-----------------------------------");

            //使用allOf创建包含所有枚举类型的enumSet，其内部根据Class对象初始化了所有枚举实例
            EnumSet<Color> enumSet1= EnumSet.allOf(Color.class);
            System.out.println("allOf直接填充："+enumSet1.toString());

            System.out.println("-----------------------------------");

            //初始集合包括枚举值中指定范围的元素
            EnumSet<Color> enumSet2= EnumSet.range(Color.BLACK,Color.YELLOW);
            System.out.println("指定初始化范围："+enumSet2.toString());

            System.out.println("-----------------------------------");

            //指定补集，也就是从全部枚举类型中去除参数集合中的元素，如下去掉上述enumSet2的元素
            EnumSet<Color> enumSet3= EnumSet.complementOf(enumSet2);
            System.out.println("指定补集："+enumSet3.toString());

            System.out.println("-----------------------------------");

            //初始化时直接指定元素
            EnumSet<Color> enumSet4= EnumSet.of(Color.BLACK);
            System.out.println("指定Color.BLACK元素："+enumSet4.toString());
            EnumSet<Color> enumSet5= EnumSet.of(Color.BLACK,Color.GREEN);
            System.out.println("指定Color.BLACK和Color.GREEN元素："+enumSet5.toString());

            System.out.println("-----------------------------------");

            //复制enumSet5容器的数据作为初始化数据
            EnumSet<Color> enumSet6= EnumSet.copyOf(enumSet5);
            System.out.println("enumSet6："+enumSet6.toString());

            System.out.println("-----------------------------------");

            List<Color> list = new ArrayList<Color>();
            list.add(Color.BLACK);
            list.add(Color.BLACK);//重复元素
            list.add(Color.RED);
            list.add(Color.BLUE);
            System.out.println("list:"+list.toString());

            //使用copyOf(Collection<E> c)
            EnumSet enumSet7=EnumSet.copyOf(list);
            System.out.println("enumSet7:"+enumSet7.toString());

            /**
             输出结果：
             添加前：[]
             添加后：[GREEN, RED, BLUE, BLACK, YELLOW]
             -----------------------------------
             allOf直接填充：[GREEN, RED, BLUE, BLACK, YELLOW]
             -----------------------------------
             指定初始化范围：[BLACK, YELLOW]
             -----------------------------------
             指定补集：[GREEN, RED, BLUE]
             -----------------------------------
             指定Color.BLACK元素：[BLACK]
             指定Color.BLACK和Color.GREEN元素：[GREEN, BLACK]
             -----------------------------------
             enumSet6：[GREEN, BLACK]
             -----------------------------------
             list:[BLACK, BLACK, RED, BLUE]
             enumSet7:[RED, BLUE, BLACK]
             */
        }

    }

`noneOf(Class<E> elementType)`静态方法，主要用于创建一个空的EnumSet集合，传递参数elementType代表的是枚举类型的类型信息，即Class对象。`EnumSet<E> allOf(Class<E> elementType)`静态方法则是创建一个填充了elementType类型所代表的所有枚举实例，奇怪的是EnumSet提供了多个重载形式的of方法，最后一个接受的的是可变参数，其他重载方法则是固定参数个数，EnumSet之所以这样设计是因为可变参数的运行效率低一些，所有在参数数据不多的情况下，强烈**_不建议_**使用传递参数为可变参数的of方法，即`EnumSet<E> of(E first, E... rest)`，其他方法就不分析了，看代码演示即可。至于EnumSet的操作方法，则与set集合是一样的，可以看API即可这也不过多说明。什么时候使用EnumSet比较恰当的，事实上当需要进行位域运算，就可以使用EnumSet提到位域，如下：

    public class EnumSetDemo {
        //定义位域变量
        public static final int TYPE_ONE = 1 << 0 ; //1
        public static final int TYPE_TWO = 1 << 1 ; //2
        public static final int TYPE_THREE = 1 << 2 ; //4
        public static final int TYPE_FOUR = 1 << 3 ; //8
        public static void main(String[] args){
            //位域运算
            int type= TYPE_ONE | TYPE_TWO | TYPE_THREE |TYPE_FOUR;
        }
    }

诸如上述情况，我们都可以将上述的类型定义成枚举然后采用EnumSet来装载，进行各种操作，这样不仅不用手动编写太多冗余代码，而且使用EnumSet集合进行操作也将使代码更加简洁明了。

    enum Type{
        TYPE_ONE,TYPE_TWO,TYPE_THREE,TYPE_FOUR 
    }

    public class EnumSetDemo {
        public static void main(String[] args){
        EnumSet set =EnumSet.of(Type.TYPE_ONE,Type.TYPE_FOUR);
        }
    }

其实博主认为EnumSet最有价值的是其内部实现原理，采用的是位向量，它体现出来的是一种高效的数据处理方式，这点很值得我们去学习它。

## <a name="t19"></a><font color="#BE1921">EnumSet实现原理剖析</font>

关于EnumSet实现原理可能会有点烧脑，内部执行几乎都是位运算，博主将尽力使用图片来分析，协助大家理解。

### <a name="t20"></a><font color="#BE1921">理解位向量</font>

在分析EnumSet前有必要先了解以下位向量，顾名思义位向量就是用一个bit位(0或1)标记一个元素的状态，用一组bit位表示一个集合的状态，而每个位对应一个元素，每个bit位的状态只可能有两种，即0或1。位向量能表示的元素个数与向量的bit位长度有关，如一个int类型能表示32个元素，而一个long类型则可以表示64个元素，对于EnumSet而言采用的就long类型或者long类型数组。比如现在有一个文件中的数据，该文件存储了N=1000000个无序的整数，需要把这些整数读取到内存并排序再重新写回文件中，该如何解决？最简单的方式是用int类型来存储每个数，并把其存入到数组(int a[m])中，再进行排序，但是这种方式将会导致存储空间异常大，对数据操作起来效率也能成问题，那有没更高效的方式呢？的确是有的，那就是运用位向量，我们知道一个int型的数有4个字节，也就是32位，那么我们可以用N/32个int型数组来表示这N个数：

    a[0]表示第1~32个数（0~31）
    a[1]表示第33~64个数（32~63）
    a[2]表示第65~96个数（64~95）
    ...... 以此类推

这样，每当输入一个数字m，我们应该先找到该数字在数组的第？个元素，也就是a[?]，然后再确定在这个元素的第几个bit位，找到后设置为1，代表存在该数字。举个例子来说，比如输入40，那么40/32为1余8，则应该将a[1]元素值的第9个bit位置为1(1的二进制左移8位后就是第9个位置)，表示该数字存在，40数字的表示原理图过程如下：

![](https://img-blog.csdn.net/20170513085533480?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

大概明白了位向量表示方式后，上述过程的计算方式，通过以下方式可以计算该数存储在数组的第?个元素和元素中第?个bit位置,为了演示方便，我们这里假设整第?个元素中的?为P，余值设置S

    //m 除以 2^n 则商(P)表示为 m >> n 
    //等同于 m / 2^5 取整数 即：40 / 32 = 1 ，那么P=1就是数组中第2个元素，即a[1]

    //位操作过程如下，40的二进制
    00000000 00000000 00000000 00101000

    //右移5位即 n=5 ， m >> 5 ，即结果转为10进制就是P=1
    00000000 00000000 00000000 00000001

在这里我们使用的int类型，即32位，所有2^5=32，因此n=5，由此计算出 P的值代表的是数组的第 P 个元素，接着利用下述方式计算出余数（S），以此设置该元素值的第（S+1）个bit位为1

    //m 除以2^n 的余数(S)表示为 m & (2^n-1) 
    //等同于： m % 2^5 取余数 即：40 % 32 = 8

    //m=40的二进制
    00000000 00000000 00000000 00101000

    //2^n-1（31）的二进制
    00000000 00000000 00000000 00011111

    // m & (2^n-1) 即40与31进行与操作得出余数 即 S=8
    00000000 00000000 00000000 00001000 

    //下面是将a[1]元素值的第(8+1)个bit设置为1，为什么是(8+1)不是8？因为1左移8位就在第9个bit位了，过程如下：

    //1的二进制如下：
    00000000 00000000 00000000 00000001

    //1 << 8 利用余数8对1进行左移动
    00000000 00000000 00000001 0000000 

    //然后再与a[1]执行或操作后就可以将对应的bit位设置为1
    //a[P] |= 1 << S 见下述java实现的代码

通过上述二进制位运算过程(关于位运算可以看博主的另一篇博文~[java位运算](http://blog.csdn.net/javazejian/article/details/51181320))就可以计算出整数部分P和余数部分S，并成功设置bit位为1，现在利用java来实现这个运算过程如下：

    //定义变量
    private int[] a; //数组存储元素的数组
    private int BIT_LENGTH = 32;//默认使用int类型
    private int P; //整数部分
    private int S; //余数
    private int MASK =  0x1F;// 2^5 - 1
    private int SHIFT = 5; // 2^n SHIFT=n=5 表示2^5=32 即bit位长度32

计算代码

    /**
     * 置位操作,添加操作
     * @param i
     */
    public void set(int i){
         P = i >> SHIFT; //结果等同  P = i / BIT_LENGTH; 取整数 ①
         S = i & MASK;   //结果等同  S = i % BIT_LENGTH; 取余数 ②

         a[P] |= 1 << S;  //赋值设置该元素bit位为1               ③
         //将int型变量j的第k个比特位设置为1， 即j=j|(1<<k),上述3句合并为一句
         //a[i >> SHIFT ] |= (1 << (i & MASK));               ④
     }

计算出P和S后，就可以进行赋值了，其中 a[P]代表数组中第P个元素，`a[P] |= 1 << S` 整句意思是把a[P]元素的第S+1位设置为1，注意从低位到高位设置，即从右到左，①②③合并为④，代码将更佳简洁。当然有添加操作，那么就会有删除操作，删除操作过程与添加类似，只不过删除是把相对应的bit位设置0，代表不存在该数值。

    /**
    * 置0操作，相当于清除元素
    * @param i
    */
    public void clear(int i){
       P =  i >> SHIFT; //计算位于数组中第？个元素 P = i / BIT_LENGTH;
       S =  i & MASK;   //计算余数  S = i % BIT_LENGTH;
       //把a[P]元素的第S+1个(从低位到高位)bit位设置为0
       a[P] &= ~(1 << S);

       //更优写法
       //将int型变量j的第k个比特位设置为0，即j= j&~(1<<k)
       //a[i>>SHIFT] &= ~(1<<(i &MASK));
    }

与添加唯一不同的是，计算出余数S，利用1左移S位，再取反(~)操作，最后进行与(&)操作，即将a[P]元素的第S+1个(从低位到高位)bit位设置为0，表示删除该数字，这个计算过程大家可以自行推算一下。这就是位向量表示法的添加和清除方法，然后我们可以利用下述的get方法判断某个bit是否存在某个数字：

    /**
     * 读取操作，返回1代表该bit位有值，返回0代表该bit位没值
     * @param i
     * @return
     */
    public int get(int i){
        //a[i>>SHIFT] & (1<<(i&MASK));
        P = i >> SHIFT;
        S = i &  MASK;
        return Integer.bitCount(a[P] & (1 << S));
    }

其中Integer.bitCount()是返回指定 int 值的二进制补码(计算机数字的二进制表示法都是使用补码表示的)表示形式的 1 位的数量。位向量运算整体代码实现如下：

    package com.zejian;

    import java.util.ArrayList;
    import java.util.List;
    import java.util.Random;

    /**
     * Created by zejian on 2017/5/13.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     * 位向量存储数据
     */
    public class BitVetory {
        private int count;
        private int[] a; //数组
        private int BIT_LENGTH = 32;//默认使用int类型
        private int P; //整数部分
        private int S; //余数
        private int MASK =  0x1F;// 2^5 - 1
        private int SHIFT = 5; // 2^n SHIFT=n=5 表示2^5=32 即bit位长度32

        /**
         * 初始化位向量
         * @param count
         */
        public BitVetory(int count) {
            this.count = count;
            a = new int[(count-1)/BIT_LENGTH + 1];
            init();
        }

        /**
         * 将数组中元素bit位设置为0
         */
        public void init(){
            for (int i = 0; i < count; i++) {
                clear(i);
            }
        }

        /**
         * 获取排序后的数组
         * @return
         */
        public List<Integer> getSortedArray(){
            List<Integer> sortedArray = new ArrayList<Integer>();

            for (int i = 0; i < count; i++) {
                if (get(i) == 1) {//判断i是否存在
                    sortedArray.add(i);
                }
            }
            return sortedArray;
        }
        /**
         * 置位操作,设置元素
         * @param i
         */
        public void set(int i){
            P = i >> SHIFT; //P = i / BIT_LENGTH; 取整数
            S = i & MASK; //S = i % BIT_LENGTH; 取余数
            a[P] |= 1 << S;

            //将int型变量j的第k个比特位设置为1， 即j=j|(1<<k),上述3句合并为一句
            //a[i >> SHIFT ] |= (1 << (i & MASK));
        }

        /**
         * 置0操作，相当于清除元素
         * @param i
         */
        public void clear(int i){
            P =  i >> SHIFT; //计算位于数组中第？个元素 P = i / BIT_LENGTH;
            S =  i & MASK;   //计算余数  S = i % BIT_LENGTH;
            a[P] &= ~(1 << S);

            //更优写法
            //将int型变量j的第k个比特位设置为0，即j= j&~(1<<k)
            //a[i>>SHIFT] &= ~(1<<(i &MASK));
        }

        /**
         * 读取操作，返回1代表该bit位有值，返回0代表该bit位没值
         * @param i
         * @return
         */
        public int get(int i){
            //a[i>>SHIFT] & (1<<(i&MASK));
            P = i >> SHIFT;
            S = i &  MASK;
            return Integer.bitCount(a[P] & (1 << S));
        }

        //测试
        public static void main(String[] args) {
            int count = 25;
            List<Integer> randoms = getRandomsList(count);
            System.out.println("排序前：");

            BitVetory bitVetory = new BitVetory(count);
            for (Integer e : randoms) {
                System.out.print(e+",");
                bitVetory.set(e);
            }

            List<Integer> sortedArray = bitVetory.getSortedArray();
            System.out.println();
            System.out.println("排序后：");
            for (Integer e : sortedArray) {
                System.out.print(e+",");
            }

            /**
             输出结果:
             排序前：
             6,3,20,10,18,15,19,16,13,4,21,22,24,2,14,5,12,7,23,8,1,17,9,11,
             排序后：
             1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
             */
        }

        private static List<Integer> getRandomsList(int count) {
            Random random = new Random();

            List<Integer> randomsList = new ArrayList<Integer>();
            while(randomsList.size() < (count - 1)){
                int element = random.nextInt(count - 1) + 1;//element ∈  [1,count)
                if (!randomsList.contains(element)) {
                    randomsList.add(element);
                }
            }
            return randomsList;
        }
    }

### <a name="t21"></a><font color="#BE1921">EnumSet原理</font>

有前面位向量的分析，对于了解EnumSet的实现原理就相对简单些了，EnumSet内部使用的位向量实现的，前面我们说过EnumSet是一个抽象类，事实上它存在两个子类，RegularEnumSet和JumboEnumSet。RegularEnumSet使用一个long类型的变量作为位向量，long类型的位长度是64，因此可以存储64个枚举实例的标志位，一般情况下是够用的了，而JumboEnumSet使用一个long类型的数组，当枚举个数超过64时，就会采用long数组的方式存储。先看看EnumSet内部的数据结构：

    public abstract class EnumSet<E extends Enum<E>> extends AbstractSet<E>
        implements Cloneable, java.io.Serializable
    {
        //表示枚举类型
        final Class<E> elementType;
        //存储该类型信息所表示的所有可能的枚举实例
        final Enum<?>[] universe;
        //..........
    }

EnumSet中有两个变量，一个elementType用于表示枚举的类型信息，universe是数组类型，存储该类型信息所表示的所有可能的枚举实例，EnumSet是抽象类，因此具体的实现是由子类完成的，下面看看`noneOf(Class<E> elementType)`静态构建方法

      public static <E extends Enum<E>> EnumSet<E> noneOf(Class<E> elementType) {
            //根据EnumMap中的一样，获取所有可能的枚举实例
            Enum<?>[] universe = getUniverse(elementType);
            if (universe == null)
                throw new ClassCastException(elementType + " not an enum");

            if (universe.length <= 64)
                //枚举个数小于64，创建RegularEnumSet
                return new RegularEnumSet<>(elementType, universe);
            else
                //否则创建JumboEnumSet
                return new JumboEnumSet<>(elementType, universe);
        }

从源码可以看出如果枚举值个数小于等于64，则静态工厂方法中创建的就是RegularEnumSet，否则大于64的话就创建JumboEnumSet。无论是RegularEnumSet还是JumboEnumSet，其构造函数内部都间接调用了EnumSet的构造函数，因此最终的elementType和universe都传递给了父类EnumSet的内部变量。如下：

    //RegularEnumSet构造
    RegularEnumSet(Class<E>elementType, Enum<?>[] universe) {
          super(elementType, universe);
      }

    //JumboEnumSet构造
    JumboEnumSet(Class<E>elementType, Enum<?>[] universe) {
          super(elementType, universe);
          elements = new long[(universe.length + 63) >>> 6];
      }

在RegularEnumSet类和JumboEnumSet类中都存在一个elements变量，用于记录位向量的操作，

    //RegularEnumSet
    class RegularEnumSet<E extends Enum<E>> extends EnumSet<E> {
        private static final long serialVersionUID = 3411599620347842686L;
        //通过long类型的elements记录位向量的操作
        private long elements = 0L;
        //.......
    }

    //对于JumboEnumSet则是：
    class JumboEnumSet<E extends Enum<E>> extends EnumSet<E> {
        private static final long serialVersionUID = 334349849919042784L;
        //通过long数组类型的elements记录位向量
        private long elements[];
         //表示集合大小
        private int size = 0;

        //.............
        }

在RegularEnumSet中elements是一个long类型的变量，共有64个bit位，因此可以记录64个枚举常量，当枚举常量的数量超过64个时，将使用JumboEnumSet，elements在该类中是一个long型的数组，每个数组元素都可以存储64个枚举常量，这个过程其实与前面位向量的分析是同样的道理，只不过前面使用的是32位的int类型，这里使用的是64位的long类型罢了。接着我们看看EnumSet是如何添加数据的，RegularEnumSet中的add实现如下

    public boolean add(E e) {
        //检测是否为枚举类型
        typeCheck(e);
        //记录旧elements
        long oldElements = elements;
        //执行位向量操作，是不是很熟悉？
        //数组版：a[i >> SHIFT ] |= (1 << (i & MASK))
        elements |= (1L << ((Enum)e).ordinal());
        return elements != oldElements;
    }

关于`elements |= (1L << ((Enum)e).ordinal());`这句跟我们前面分析位向量操作是相同的原理，只不过前面分析的是数组类型实现，这里用的long类型单一变量实现，`((Enum)e).ordinal()`通过该语句获取要添加的枚举实例的序号，然后通过1左移再与 long类型的elements进行或操作，就可以把对应位置上的bit设置为1了，也就代表该枚举实例存在。图示演示过程如下，注意universe数组在EnumSet创建时就初始化并填充了所有可能的枚举实例，而elements值的第n个bit位1时代表枚举存在，而获取的则是从universe数组中的第n个元素值。

![](https://img-blog.csdn.net/20170513151544085?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

这就是枚举实例的添加过程和获取原理。而对于JumboEnumSet的add实现则是如下：

    public boolean add(E e) {
        typeCheck(e);
        //计算ordinal值
        int eOrdinal = e.ordinal();
        int eWordNum = eOrdinal >>> 6;

        long oldElements = elements[eWordNum];
        //与前面分析的位向量相同：a[i >> SHIFT ] |= (1 << (i & MASK))
        elements[eWordNum] |= (1L << eOrdinal);
        boolean result = (elements[eWordNum] != oldElements);
        if (result)
            size++;
        return result;
    }

关于JumboEnumSet的add实现与RegularEnumSet区别是一个是long数组类型，一个long变量，运算原理相同，数组的位向量运算与前面分析的是相同的，这里不再分析。接着看看如何删除元素

    //RegularEnumSet类实现
    public boolean remove(Object e) {
        if (e == null)
            return false;
        Class eClass = e.getClass();
        if (eClass != elementType && eClass.getSuperclass() != elementType)
            return false;

        long oldElements = elements;
        //将int型变量j的第k个比特位设置为0，即j= j&~(1<<k)
        //数组类型：a[i>>SHIFT] &= ~(1<<(i &MASK));

        elements &= ~(1L << ((Enum)e).ordinal());//long遍历类型操作
        return elements != oldElements;
    }

    //JumboEnumSet类的remove实现
    public boolean remove(Object e) {
            if (e == null)
                return false;
            Class<?> eClass = e.getClass();
            if (eClass != elementType && eClass.getSuperclass() != elementType)
                return false;
            int eOrdinal = ((Enum<?>)e).ordinal();
            int eWordNum = eOrdinal >>> 6;

            long oldElements = elements[eWordNum];
            //与a[i>>SHIFT] &= ~(1<<(i &MASK));相同
            elements[eWordNum] &= ~(1L << eOrdinal);
            boolean result = (elements[eWordNum] != oldElements);
            if (result)
                size--;
            return result;
        }

删除remove的实现，跟位向量的清空操作是同样的实现原理，如下：  
![](https://img-blog.csdn.net/20170513171112915?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

至于JumboEnumSet的实现原理也是类似的，这里不再重复。下面为了简洁起见，我们以RegularEnumSet类的实现作为源码分析，毕竟JumboEnumSet的内部实现原理可以说跟前面分析过的位向量几乎一样。o~，看看如何判断是否包含某个元素

    public boolean contains(Object e) {
        if (e == null)
            return false;
        Class eClass = e.getClass();
        if (eClass != elementType && eClass.getSuperclass() != elementType)
            return false;
        //先左移再按&操作
        return (elements & (1L << ((Enum)e).ordinal())) != 0;
    }

    public boolean containsAll(Collection<?> c) {
        if (!(c instanceof RegularEnumSet))
            return super.containsAll(c);

        RegularEnumSet<?> es = (RegularEnumSet<?>)c;
        if (es.elementType != elementType)
            return es.isEmpty();
        //~elements取反相当于elements补集，再与es.elements进行&操作，如果为0，
        //就说明elements补集与es.elements没有交集，也就是es.elements是elements的子集
        return (es.elements & ~elements) == 0;
    }

对于contains(Object e) 方法，先左移再按位与操作，不为0，则表示包含该元素，跟位向量的get操作实现原理类似，这个比较简单。对于`containsAll(Collection<?> c)`则可能比较难懂，这里分析一下，elements变量(long类型)标记EnumSet集合中已存在元素的bit位，如果bit位为1则说明存在枚举实例，为0则不存在，现在执行`~elements` 操作后 则说明`~elements`是elements的补集，那么只要传递进来的es.elements与补集`~elements` 执行&操作为0，那么就可以证明es.elements与补集`~elements` 没有交集的可能，也就是说es.elements只能是elements的子集，这样也就可以判断出当前EnumSet集合中包含传递进来的集合c了，借着下图协助理解：

![](https://img-blog.csdn.net/20170513163057795?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

图中，elements代表A，`es.elements`代表S，`~elements`就是求A的补集，`(es.elements & ~elements) == 0`就是在验证A’∩B是不是空集，即S是否为A的子集。接着看retainAll方法，求两个集合交集

    public boolean retainAll(Collection<?> c) {
            if (!(c instanceof RegularEnumSet))
                return super.retainAll(c);

            RegularEnumSet<?> es = (RegularEnumSet<?>)c;
            if (es.elementType != elementType) {
                boolean changed = (elements != 0);
                elements = 0;
                return changed;
            }

            long oldElements = elements;
            //执行与操作，求交集，比较简单
            elements &= es.elements;
            return elements != oldElements;
        }

最后来看看迭代器是如何取值的

     public Iterator<E> iterator() {
            return new EnumSetIterator<>();
        }

        private class EnumSetIterator<E extends Enum<E>> implements Iterator<E> {
            //记录elements
            long unseen;

            //记录最后一个返回值
            long lastReturned = 0;

            EnumSetIterator() {
                unseen = elements;
            }

            public boolean hasNext() {
                return unseen != 0;
            }

            @SuppressWarnings("unchecked")
            public E next() {
                if (unseen == 0)
                    throw new NoSuchElementException();
                //取值过程，先与本身负执行&操作得出的就是二进制低位开始的第一个1的数值大小
                lastReturned = unseen & -unseen;
                //取值后减去已取得lastReturned
                unseen -= lastReturned;
                //返回在指定 long 值的二进制补码表示形式中最低位（最右边）的 1 位之后的零位的数量
                return (E) universe[Long.numberOfTrailingZeros(lastReturned)];
            }

            public void remove() {
                if (lastReturned == 0)
                    throw new IllegalStateException();
                elements &= ~lastReturned;
                lastReturned = 0;
            }
        }

比较晦涩的应该是

    //取值过程，先与本身负执行&操作得出的就是二进制低位开始的第一个1的数值大小
    lastReturned = unseen & -unseen; 
    //取值后减去已取得lastReturned
    unseen -= lastReturned;
    return (E) universe[Long.numberOfTrailingZeros(lastReturned)];

我们通过原理图来协助理解，现在假设集合中已保存所有可能的枚举实例变量，我们需要把它们遍历展示出来，下面的第一个枚举元素的获取过程，显然通过`unseen & -unseen;`操作，我们可以获取到二进制低位开始的第一个1的数值，该计算的结果是要么全部都是0，要么就只有一个1，然后赋值给lastReturned，通过`Long.numberOfTrailingZeros(lastReturned)`获取到该bit为1在64位的long类型中的位置，即从低位算起的第几个bit，如图，该bit的位置恰好是低位的第1个bit位置，也就指明了universe数组的第一个元素就是要获取的枚举变量。执行`unseen -= lastReturned;`后继续进行第2个元素的遍历，依次类推遍历出所有值，这就是EnumSet的取值过程，真正存储枚举变量的是universe数组，而通过long类型变量的bit位的0或1表示存储该枚举变量在universe数组的那个位置，这样做的好处是任何操作都是执行long类型变量的bit位操作，这样执行效率将特别高，毕竟是二进制直接执行，只有最终获取值时才会操作到数组universe。

![](https://img-blog.csdn.net/20170513174622751?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

ok~，到这关于EnumSet的实现原理主要部分我们就分析完了，其内部使用位向量，存储结构很简洁，节省空间，大部分操作都是按位运算，直接操作二进制数据，因此效率极高。当然通过前面的分析，我们也掌握位向量的运算原理。好~，关于java枚举，我们暂时聊到这。

> 参考资料 《Thinking in Java》 And 《Effective Java》

</div>

<link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet"></div>

</article>

</div>

<script>$(".MathJax").remove(); if ($('div.markdown_views pre.prettyprint code.hljs').length > 0) { $('div.markdown_views')[0].className = 'markdown_views'; }</script>

<div class="recommend-box">

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/testcs_dn/article/details/78604547,BlogCommendFromThirdServiceAll_0&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _Java_ 枚举(_enum_) 详解7种常见的用法

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-22</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/testcs_dn/article/details/78604547 "Java 枚举(enum) 详解7种常见的用法")

[<span class="desc oneline">JDK1.5引入了新的类型——枚举。在 Java 中它虽然算个“小”功能，却给我的开发带来了“大”方便。大师兄我又加上自己的理解，来帮助各位理解一下。用法一：常量在JDK1.5 之前，我们定义常量都是...</span>](https://blog.csdn.net/testcs_dn/article/details/78604547 "Java 枚举(enum) 详解7种常见的用法") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">无知人生，记录点滴</span>](https://blog.csdn.net/testcs_dn)</span>

</div>

</div>

</div>

<a id="commentBox"></a>

<div class="comment-box">

<div class="comment-edit-box d-flex"><a id="commentsedit"></a>

<div class="user-img">[![](https://avatar.csdn.net/6/F/7/3_weixin_44094314.jpg)](//me.csdn.net/weixin_44094314) </div>

<form id="commentform"><input type="hidden" id="comment_replyId"> <textarea class="comment-content" name="comment_content" id="comment_content" placeholder="想对作者说点什么"></textarea>

<div class="opt-box">

<div id="ubbtools" class="add_code">[](#insertcode)</div>

<input type="hidden" id="comment_replyId" name="comment_replyId"> <input type="hidden" id="article_id" name="article_id" value="71333103"> <input type="hidden" id="comment_userId" name="comment_userId" value=""> <input type="hidden" id="commentId" name="commentId" value="">

<div style="display: none;" class="csdn-tracking-statistics tracking-click" data-mod="popu_384">[发表评论](#)</div>

<div class="dropdown" id="myDrap"><a class="dropdown-face d-flex align-items-center" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">

<div class="txt-selected text-truncate">添加代码片</div>

</a>

*   <a data-code="html">HTML/XML</a>
*   <a data-code="objc">objective-c</a>
*   <a data-code="ruby">Ruby</a>
*   <a data-code="php">PHP</a>
*   <a data-code="csharp">C</a>
*   <a data-code="cpp">C++</a>
*   <a data-code="javascript">JavaScript</a>
*   <a data-code="python">Python</a>
*   <a data-code="java">Java</a>
*   <a data-code="css">CSS</a>
*   <a data-code="sql">SQL</a>
*   <a data-code="plain">其它</a>

</div>

<div class="right-box"><span id="tip_comment" class="tip">还能输入_1000_个字符</span> <input type="submit" class="btn btn-sm btn-red btn-comment" value="发表评论"></div>

</div>

</form>

</div>

<div class="comment-list-container"><a id="comments"></a>

<div class="comment-list-box" style="max-height: 573px;">

*   [![turodog](https://avatar.csdn.net/0/2/6/3_turodog.jpg)](https://me.csdn.net/turodog)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">一个优秀的废人：</span>](https://me.csdn.net/turodog) <span class="comment">刚想了解这块，写的太好了，能否转载？会在开头标注原文地址</span><span class="date" title="2019-05-26 15:31:57">(1周前</span><span class="floor-num">#75楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9857439"><span></span></div>

    </div>

*   [![liuyanlin007](https://avatar.csdn.net/E/8/C/3_liuyanlin007.jpg)](https://me.csdn.net/liuyanlin007)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">Tortoise007：</span>](https://me.csdn.net/liuyanlin007) <span class="comment">哦</span><span class="date" title="2019-05-06 12:19:22">(4周前</span><span class="floor-num">#74楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9702995"><span></span></div>

    </div>

*   [![long_dragon123](https://avatar.csdn.net/E/9/4/3_long_dragon123.jpg)](https://me.csdn.net/long_dragon123)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">long_dragon123：</span>](https://me.csdn.net/long_dragon123) <span class="comment">请问一下：在retainAll 方法中，为什么要直接对本身的elements 进行操作，1\. 如果不同的枚举类型的话，直接将本身的elements 位向量进行清除，那么该实例本身的位向量还能用吗？2\. 如果相同类型的话，直接用实例本身的elements 和 es.elements 进行相与，那么本身的elements 已经被改变了。这两种情况，实例本身的elements 已经被改变，还能够使用吗？

    <pre name="code2" class="java hljs">

    2.  <div class="hljs-ln-code">

        <div class="hljs-ln-line">`<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">retainAll</span><span class="hljs-params">(Collection&lt;?&gt; c)</span></span> {`</div>

        </div>

    3.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">if</span> (!(c <span class="hljs-keyword">instanceof</span> RegularEnumSet))`</div>

        </div>

    4.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.retainAll(c);`</div>

        </div>

    6.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `RegularEnumSet&lt;?&gt; es = (RegularEnumSet&lt;?&gt;)c;`</div>

        </div>

    7.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">if</span> (es.elementType != elementType) {`</div>

        </div>

    8.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">boolean</span> changed = (elements != <span class="hljs-number">0</span>);`</div>

        </div>

    9.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `elements = <span class="hljs-number">0</span>;`</div>

        </div>

    10.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">return</span> changed;`</div>

        </div>

    11.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `}`</div>

        </div>

    13.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">long</span> oldElements = elements;`</div>

        </div>

    14.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">//执行与操作，求交集，比较简单</span>`</div>

        </div>

    15.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `elements &= es.elements;`</div>

        </div>

    16.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">return</span> elements != oldElements;`</div>

        </div>

    17.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `}`</div>

        </div>

    </pre>

    </span><span class="date" title="2019-05-02 15:30:46">(1个月前</span><span class="floor-num">#73楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9682231"><span></span></div>

    </div>

*   [![id_1122](https://avatar.csdn.net/4/0/7/3_id_1122.jpg)](https://me.csdn.net/id_1122)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">id_1122：</span>](https://me.csdn.net/id_1122) <span class="comment">服气，牛批</span><span class="date" title="2019-04-28 16:01:56">(1个月前</span><span class="floor-num">#72楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9655328"><span></span></div>

    </div>

*   [![u013467442](https://avatar.csdn.net/0/A/B/3_u013467442.jpg)](https://me.csdn.net/u013467442)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">jieniyimiao：</span>](https://me.csdn.net/u013467442) <span class="comment">写的很透彻</span><span class="date" title="2019-04-24 17:31:15">(1个月前</span><span class="floor-num">#71楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9625239"><span></span></div>

    </div>

*   [![qq_42444845](https://avatar.csdn.net/8/2/8/3_qq_42444845.jpg)](https://me.csdn.net/qq_42444845)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">qq_42444845：</span>](https://me.csdn.net/qq_42444845) <span class="comment">楼主,你好,我想问下 m 除以2^n 的余数(S)表示为 m & (2^n-1) 这个规律是怎么退出来的</span><span class="date" title="2019-04-19 16:37:23">(1个月前</span><span class="floor-num">#70楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9586231"><span></span></div>

    </div>

*   [![woaitt5213](https://avatar.csdn.net/E/4/D/3_woaitt5213.jpg)](https://me.csdn.net/woaitt5213)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">天下第一阿里里：</span>](https://me.csdn.net/woaitt5213) <span class="comment">叹为观止</span><span class="date" title="2019-04-18 22:14:00">(1个月前</span><span class="floor-num">#69楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9580882"><span></span></div>

    </div>

*   [![weixin_43109884](https://avatar.csdn.net/5/5/6/3_weixin_43109884.jpg)](https://me.csdn.net/weixin_43109884)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">阳光多灿烂wxc：</span>](https://me.csdn.net/weixin_43109884) <span class="comment">看完之后发现，基础好重要（要是没有位运算的基础，根本看不懂）</span><span class="date" title="2019-04-17 11:27:42">(1个月前</span><span class="floor-num">#68楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9566427"><span></span></div>

    </div>

*   [![u013280397](https://avatar.csdn.net/8/0/A/3_u013280397.jpg)](https://me.csdn.net/u013280397)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">乞力马扎罗-雪：</span>](https://me.csdn.net/u013280397) <span class="comment">真的是优秀</span><span class="date" title="2019-04-12 11:42:20">(1个月前</span><span class="floor-num">#67楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9529608"><span></span></div>

    </div>

*   [![qq_35306443](https://avatar.csdn.net/2/B/5/3_qq_35306443.jpg)](https://me.csdn.net/qq_35306443)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">3075763007：</span>](https://me.csdn.net/qq_35306443) <span class="comment">秀啊，一个枚举都能玩出花，很秀，天秀，非常秀，陈独秀，蒂花之秀</span><span class="date" title="2019-04-11 15:55:07">(1个月前</span><span class="floor-num">#66楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9523113"><span></span></div>

    </div>

*   [![qq_30746587](https://avatar.csdn.net/8/1/2/3_qq_30746587.jpg)](https://me.csdn.net/qq_30746587)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">qq_30746587：</span>](https://me.csdn.net/qq_30746587) <span class="comment">enumset里面既然有个enum[]，为什么还要对一个long变量操作呢，直接对enum[]数组进行随机存取效率不同样的高？</span><span class="date" title="2019-03-21 20:48:19">(2个月前</span><span class="floor-num">#65楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9374056"><span></span></div>

    </div>

*   [![superharder](https://avatar.csdn.net/C/1/5/3_superharder.jpg)](https://me.csdn.net/superharder)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">superharder：</span>](https://me.csdn.net/superharder) <span class="comment">根据位排序哪里对数据应该是有条件的吧，必须是有多少个值最大值就为多少。但是对普通的数据（不连续）来说就有点不适用了。</span><span class="date" title="2019-03-19 14:53:32">(2个月前</span><span class="floor-num">#64楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9354927"><span></span></div>

    </div>

*   [![sinat_30634865](https://avatar.csdn.net/3/C/5/3_sinat_30634865.jpg)](https://me.csdn.net/sinat_30634865)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">秋景异：</span>](https://me.csdn.net/sinat_30634865) <span class="comment">你好,问你一个问题,就是我 反编译Day.class,等不到和你文章反编译一样的结果 ,请问我要和你一样结果,怎么样能做到?</span><span class="date" title="2018-09-13 15:49:47">(8个月前</span><span class="floor-num">#63楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-read-reply" data-type="readreply">查看回复(2)</a><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="8448577"><span></span></div>

    </div>

*   *   [![ZOKEKAI](https://avatar.csdn.net/2/F/1/3_zokekai.jpg)](https://me.csdn.net/ZOKEKAI)

        <div class="right-box reply-box">

        <div class="info-box">[<span class="name mr-8">ZOKEKAI</span>](https://me.csdn.net/ZOKEKAI)<span class="text">回复</span> <span class="name">秋景异：</span> <span class="comment">使用 jad 这个工具即可</span><span class="date" title="2019-03-08 15:27:22">(2个月前</span><span class="text">)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

        <div class="comment-like " data-commentid="9286641"><span></span></div>

        </div>

    *   [![u014452539](https://avatar.csdn.net/5/5/E/3_u014452539.jpg)](https://me.csdn.net/u014452539)

        <div class="right-box reply-box">

        <div class="info-box">[<span class="name mr-8">David丁</span>](https://me.csdn.net/u014452539)<span class="text">回复</span> <span class="name">秋景异：</span> <span class="comment">使用jad.exe反编译可以出这个结果</span><span class="date" title="2018-12-27 09:29:50">(5个月前</span><span class="text">)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

        <div class="comment-like " data-commentid="8947047"><span></span></div>

        </div>

*   [![ZOKEKAI](https://avatar.csdn.net/2/F/1/3_zokekai.jpg)](https://me.csdn.net/ZOKEKAI)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">ZOKEKAI：</span>](https://me.csdn.net/ZOKEKAI) <span class="comment">博主，这个values方法里面使用的clone方法是Enum里面的还是Object里面的？ 根据Enum源码，如果使用的是Enum的，不应该抛异常吗？

    <pre name="code2" class="java hljs">

    2.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-comment">//编译器为我们添加的静态的values()方法</span>`</div>

        </div>

    3.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Day[] values()`</div>

        </div>

    4.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `{`</div>

        </div>

    5.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `<span class="hljs-keyword">return</span> (Day[])$VALUES.clone();`</div>

        </div>

    6.  <div class="hljs-ln-code">

        <div class="hljs-ln-line"> `}`</div>

        </div>

    </pre>

    </span><span class="date" title="2019-03-08 15:26:29">(2个月前</span><span class="floor-num">#62楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9286630"><span></span></div>

    </div>

*   [![qq_38783098](https://avatar.csdn.net/2/2/2/3_qq_38783098.jpg)](https://me.csdn.net/qq_38783098)

    <div class="right-box ">

    <div class="info-box">[<span class="name ">小柯点点：</span>](https://me.csdn.net/qq_38783098) <span class="comment">博主厉害</span><span class="date" title="2019-03-05 20:10:02">(2个月前</span><span class="floor-num">#61楼)</span><span class="opt-box"><a class="btn btn-link-blue btn-report" data-type="report">举报</a><a class="btn btn-link-blue btn-reply" data-type="reply">回复</a></span></div>

    <div class="comment-like " data-commentid="9267556"><span></span></div>

    </div>

</div>

<div id="commentPage" class="pagination-box d-none" style="display: block;">

<div id="Paging_04610817376502361" class="ui-paging-container">

*   上一页
*   1
*   2
*   3
*   4
*   5
*   下一页

</div>

</div>

<div class="opt-box text-center">

<div class="btn btn-sm btn-link-blue" id="btnMoreComment"><span>查看 91 条热评</span></div>

</div>

</div>

</div>

<div class="recommend-box">

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/luo_rp/article/details/80891238,BlogCommendFromThirdServiceAll_1&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/luo_rp/article/details/80891238,BlogCommendFromThirdServiceAll_1&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _Enum_用法

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-20</span> <span class="read-num hover-hide">阅读数 1460</span>

</div>

](https://blog.csdn.net/luo_rp/article/details/80891238 "Enum用法")

[<span class="desc oneline">枚举（enum），是指一个经过排序的、被打包成一个单一实体的项列表。一个枚举的实例可以使用枚举项列表中任意单一项的值。枚举在各个语言当中都有着广泛的应用，通常用来表示诸如颜色、方式、类别、状态等等数目...</span>](https://blog.csdn.net/luo_rp/article/details/80891238 "Enum用法") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">luo_rp的博客</span>](https://blog.csdn.net/luo_rp)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hellojoy/article/details/79883671,BlogCommendFromThirdServiceAll_2&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hellojoy/article/details/79883671,BlogCommendFromThirdServiceAll_2&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _Enum_（枚举类）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">04-10</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/hellojoy/article/details/79883671 "Enum（枚举类）")

[<span class="desc oneline">一、什么情况下使用枚举类？　　有的时候一个类的对象是有限且固定的，这种情况下我们使用枚举类就比较方便？二、为什么不用静态常量来替代枚举类呢？publicstaticfinalintSEASON_SPR...</span>](https://blog.csdn.net/hellojoy/article/details/79883671 "Enum（枚举类）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">hellojoy的博客</span>](https://blog.csdn.net/hellojoy)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/VBcom/article/details/7245186,BlogCommendFromThirdServiceAll_3&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### DirectX修复工具增强版

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-09</span> <span class="read-num hover-hide">阅读数 205万+</span>

</div>

](https://blog.csdn.net/VBcom/article/details/7245186 "DirectX修复工具增强版")

[<span class="desc oneline">最后更新：2019-5-26DirectX修复工具最新版：DirectXRepairV3.8增强版NEW!版本号：V3.8.0.11638大小:107MB/7z格式压缩，189MB/zip格式压缩，3...</span>](https://blog.csdn.net/VBcom/article/details/7245186 "DirectX修复工具增强版") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">VBcom的专栏</span>](https://blog.csdn.net/VBcom)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq574857122/article/details/16361033,BlogCommendFromThirdServiceAll_4&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 强连通分量及缩点tarjan算法解析

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-16</span> <span class="read-num hover-hide">阅读数 66万+</span>

</div>

](https://blog.csdn.net/qq574857122/article/details/16361033 "强连通分量及缩点tarjan算法解析")

[<span class="desc oneline">强连通分量：简言之就是找环（每条边只走一次，两两可达）孤立的一个点也是一个连通分量 使用tarjan算法在嵌套的多个环中优先得到最大环(最小环就是每个孤立点） 定义：intTime,DFN[N],Lo...</span>](https://blog.csdn.net/qq574857122/article/details/16361033 "强连通分量及缩点tarjan算法解析") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">九野的博客</span>](https://blog.csdn.net/qq574857122)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/wuchengzeng/article/details/50037611,BlogCommendFromThirdServiceAll_5&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### jquery/js实现一个网页同时调用多个倒计时(最新的)

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-25</span> <span class="read-num hover-hide">阅读数 53万+</span>

</div>

](https://blog.csdn.net/wuchengzeng/article/details/50037611 "jquery/js实现一个网页同时调用多个倒计时(最新的)")

[<span class="desc oneline">jquery/js实现一个网页同时调用多个倒计时(最新的)最近需要网页添加多个倒计时.查阅网络,基本上都是千遍一律的不好用.自己按需写了个.希望对大家有用.有用请赞一个哦!//js//js2varpl...</span>](https://blog.csdn.net/wuchengzeng/article/details/50037611 "jquery/js实现一个网页同时调用多个倒计时(最新的)") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Websites</span>](https://blog.csdn.net/wuchengzeng)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/candycat1992/article/details/41254799,BlogCommendFromThirdServiceAll_6&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 【Unity技巧】四元数（Quaternion）和旋转

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-23</span> <span class="read-num hover-hide">阅读数 26万+</span>

</div>

](https://blog.csdn.net/candycat1992/article/details/41254799 "【Unity技巧】四元数（Quaternion）和旋转")

[<span class="desc oneline">旋转，应该是三种坐标变换——缩放、旋转和平移，中最复杂的一种了。大家应该都听过，有一种旋转的表示方法叫四元数。按照我们的习惯，我们更加熟悉的是另外两种旋转的表示方法——矩阵旋转和欧拉旋转。矩阵旋转使用...</span>](https://blog.csdn.net/candycat1992/article/details/41254799 "【Unity技巧】四元数（Quaternion）和旋转") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">candycat</span>](https://blog.csdn.net/candycat1992)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zhmxy555/article/details/40955607,BlogCommendFromThirdServiceAll_7&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 【Unity3D Shader编程】之二 雪山飞狐篇：Unity的基本Shader框架写法&颜色、光照与材质

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-09</span> <span class="read-num hover-hide">阅读数 8万+</span>

</div>

](https://blog.csdn.net/zhmxy555/article/details/40955607 "【Unity3D Shader编程】之二 雪山飞狐篇：Unity的基本Shader框架写法&颜色、光照与材质")

[<span class="desc oneline">本篇文章中，我们学习了UnityShader的基本写法框架，以及学习了Shader中Properties（属性）的详细写法，光照、材质与颜色的具体写法。写了6个Shader作为本文Shader讲解的实...</span>](https://blog.csdn.net/zhmxy555/article/details/40955607 "【Unity3D Shader编程】之二 雪山飞狐篇：Unity的基本Shader框架写法&颜色、光照与材质") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">【浅墨的游戏编程Blog】毛星云（浅墨）的专栏</span>](https://blog.csdn.net/zhmxy555)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/clover_hxy/article/details/50683832,BlogCommendFromThirdServiceAll_8&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### bsgs算法

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-18</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/clover_hxy/article/details/50683832 "bsgs算法")

[<span class="desc oneline">bsgs算法bsgs算法，又称大小步算法（某大神称拔山盖世算法）。主要用来解决 A^x=B(modC)(C是质数)，都是整数，已知A、B、C求x。（poj2417 DiscreteLogging）具体...</span>](https://blog.csdn.net/clover_hxy/article/details/50683832 "bsgs算法") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">clover_hxy的博客</span>](https://blog.csdn.net/clover_hxy)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/chentravelling/article/details/53558096,BlogCommendFromThirdServiceAll_9&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 计算机视觉：相机成像原理：世界坐标系、相机坐标系、图像坐标系、像素坐标系之间的转换

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-10</span> <span class="read-num hover-hide">阅读数 4万+</span>

</div>

](https://blog.csdn.net/chentravelling/article/details/53558096 "计算机视觉：相机成像原理：世界坐标系、相机坐标系、图像坐标系、像素坐标系之间的转换")

[<span class="desc oneline">相机成像原理：世界坐标系、相机坐标系、图像坐标系、像素坐标系之间的转换...</span>](https://blog.csdn.net/chentravelling/article/details/53558096 "计算机视觉：相机成像原理：世界坐标系、相机坐标系、图像坐标系、像素坐标系之间的转换") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">生活没有if-else</span>](https://blog.csdn.net/chentravelling)</span>

</div>

</div>

<div class="recommend-item-box baiduSearch" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/liuchaoxuan/article/details/79938276,searchFromBaidu1_0,-&quot;}" data-flg="true">[

#### _深入__理解__Java__枚举类型_(_enum_) - 起风了 - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">11-4</span>

</div>

出自【zejian的博客】 关联文章: 深入理解Java类型信息(Class对象)与反射机制 深入理解Java枚举类型(enum) 深入理解Java注解类型(@Annotation) 深入理解Java并发之...

](https://blog.csdn.net/liuchaoxuan/article/details/79938276)</div>

<div class="recommend-item-box baiduSearch" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/IFollowRivers/article/details/82078781,searchFromBaidu1_1,-&quot;}" data-flg="true">[

#### ...详解7种常见的用法&_深入__理解__Java__枚举类型_(_enum_) - I..._CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">11-14</span>

</div>

下面我在使用enum过程中一些经验和总结,主要包括如下内容: 1.原始的接口定义变量...深入理解Java枚举类型(enum) - zejian的博客 05-13 19.2万 【版权申明】...

](https://blog.csdn.net/IFollowRivers/article/details/82078781)</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yangwei282367751/article/details/52426911,BlogCommendFromThirdServiceAll_10&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 关于计算时间复杂度和空间复杂度

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-04</span> <span class="read-num hover-hide">阅读数 7万+</span>

</div>

](https://blog.csdn.net/yangwei282367751/article/details/52426911 "关于计算时间复杂度和空间复杂度")

[<span class="desc oneline">相信学习编程的同学，或多或少都接触到算法的时间复杂度和空间复杂度了，那我来讲讲怎么计算。    常用的算法的时间复杂度和空间复杂度一，求解算法的时间复杂度，其具体步骤是：　　⑴ 找出算法中的基本语句；...</span>](https://blog.csdn.net/yangwei282367751/article/details/52426911 "关于计算时间复杂度和空间复杂度") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">杨威的博客</span>](https://blog.csdn.net/yangwei282367751)</span>

</div>

</div>

<div class="recommend-item-box baiduSearch" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zhoufanyang_china/article/details/86707727,searchFromBaidu1_2,-&quot;}" data-flg="true">[

#### _深入__理解__Java_中的_enum_(枚举) - 扬帆舟的博客 - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">5-19</span>

</div>

](https://blog.csdn.net/zhoufanyang_china/article/details/86707727)</div>

<div class="recommend-item-box baiduSearch" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/liupeifeng3514/article/details/80712164,searchFromBaidu1_3,-&quot;}" data-flg="true">[

#### 源码学习 | _深入__理解__Java__枚举类型_(_enum_) - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">6-16</span>

</div>

源码学习 | 深入理解Java枚举类型(enum)2018年06月16日 11:58:31 阅读数:2 https://blog.csdn.net/javazejian/article/details/71333103 阅读更多 版权...

](https://blog.csdn.net/liupeifeng3514/article/details/80712164)</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ch_liu23/article/details/53558549,BlogCommendFromThirdServiceAll_11&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### YOLOv2训练自己的数据集（VOC格式）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-10</span> <span class="read-num hover-hide">阅读数 5万+</span>

</div>

](https://blog.csdn.net/ch_liu23/article/details/53558549 "YOLOv2训练自己的数据集（VOC格式）")

[<span class="desc oneline">最近在用yolo来做视频中的人员检测，选择YOLO是从速度考虑，在训练数据集的过程中碰到很多坑，并且现在yolo又到了v2的版本，在网络和命令中都有区别...</span>](https://blog.csdn.net/ch_liu23/article/details/53558549 "YOLOv2训练自己的数据集（VOC格式）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">ch_liu23的博客</span>](https://blog.csdn.net/ch_liu23)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/younghaiqing/article/details/52911023,BlogCommendFromThirdServiceAll_12&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _enum_ _枚举类型_，及其描述调用

<div class="info-box d-flex align-content-center">

<span class="date hover-show">10-24</span> <span class="read-num hover-hide">阅读数 8096</span>

</div>

](https://blog.csdn.net/younghaiqing/article/details/52911023 "enum 枚举类型，及其描述调用")

[<span class="desc oneline">枚举类型　　C语言或C++的一种构造类型，它用于声明一组命名的常数。　　(1)枚举的声明:枚举声明用于声明新的枚举类型。　　访问修辞符enum枚举名:基础类型　　{　　枚举成员　　};　　基础类型必须...</span>](https://blog.csdn.net/younghaiqing/article/details/52911023 "enum 枚举类型，及其描述调用") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">没有斜杠の斜杠青年</span>](https://blog.csdn.net/younghaiqing)</span>

</div>

</div>

<div class="recommend-item-box baiduSearch" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,http://blog.csdn.net/qq_39017150/article/details/78743391,searchFromBaidu1_4,-&quot;}" data-flg="true">[

#### _深入__理解_枚举(转载自Blog : http://blog.csdn.net/_java_zejian ) -...

<div class="info-box d-flex align-content-center">

<span class="date">5-23</span>

</div>

](http://blog.csdn.net/qq_39017150/article/details/78743391)</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zlfprogram/article/details/74066800,searchFromBaidu1_5,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zlfprogram/article/details/74066800,searchFromBaidu1_5,-&quot;}" data-flg="true">[

#### _Java_记录 -80- _深入__理解_枚举(_Enum_s) - 秀才的专栏 - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">11-6</span>

</div>

枚举(Enums) JDK1.5加入了一个全新的类型的“类”-- 枚举类型。为此JDK1.5引入...深入理解Java枚举类型(enum) - zejian的博客 05-13 18.8万 【版权申明】...

](https://blog.csdn.net/zlfprogram/article/details/74066800)</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/L_xiaole/article/details/52182568,BlogCommendFromThirdServiceAll_13&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/L_xiaole/article/details/52182568,BlogCommendFromThirdServiceAll_13&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### xutils3框架之数据库使用详解！

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-11</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/L_xiaole/article/details/52182568 "xutils3框架之数据库使用详解！")

[<span class="desc oneline">这段时间公司做项目，基本每天都要和数据库打交道，当初选择使用xutils3框架；刚开始使用的时候，也是遇到很多坑，小弟在此一一总结一下，希望能帮到大家，顺便自己也做个笔记。如何导入SDK我就不说了，先...</span>](https://blog.csdn.net/L_xiaole/article/details/52182568 "xutils3框架之数据库使用详解！") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">L_xiaole的博客</span>](https://blog.csdn.net/L_xiaole)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xmt1139057136/article/details/33725825,BlogCommendFromThirdServiceAll_14&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xmt1139057136/article/details/33725825,BlogCommendFromThirdServiceAll_14&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### jqm文件上传,上传图片,jqm的表单操作,jqm的ajax的使用,jqm文件操作大全,文件操作demo

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-23</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/xmt1139057136/article/details/33725825 "jqm文件上传,上传图片,jqm的表单操作,jqm的ajax的使用,jqm文件操作大全,文件操作demo")

[<span class="desc oneline">最近在论坛中看到，在使用html5中上传图片或文件，出现各种问题。这一方面，我也一直没有做过，今天就抽出了一点时间来学习一下。现在的示例已经ok了，我就给大家分享一下，希望对大家有帮助。好吧，我们先看...</span>](https://blog.csdn.net/xmt1139057136/article/details/33725825 "jqm文件上传,上传图片,jqm的表单操作,jqm的ajax的使用,jqm文件操作大全,文件操作demo") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">xmt1139057136的专栏</span>](https://blog.csdn.net/xmt1139057136)</span>

</div>

</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,http://blog.csdn.net/testcs_dn/article/details/78604547,searchFromBaidu1_6,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,http://blog.csdn.net/testcs_dn/article/details/78604547,searchFromBaidu1_6,-&quot;}" data-flg="true">[

#### _Java_ 枚举(_enum_) 详解7种常见的用法 - 无知人生,记录点..._CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">5-25</span>

</div>

](http://blog.csdn.net/testcs_dn/article/details/78604547)</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,http://blog.csdn.net/u013256816/article/details/50562905,searchFromBaidu1_7,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,http://blog.csdn.net/u013256816/article/details/50562905,searchFromBaidu1_7,-&quot;}" data-flg="true">[

#### _Java__枚举类型__enum_ - 朱小厮的博客 - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">5-23</span>

</div>

](http://blog.csdn.net/u013256816/article/details/50562905)</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/meng564764406/article/details/52444644,BlogCommendFromThirdServiceAll_15&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/meng564764406/article/details/52444644,BlogCommendFromThirdServiceAll_15&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 将Excel文件导入数据库（POI+Excel+MySQL+jsp页面导入）第一次优化

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-05</span> <span class="read-num hover-hide">阅读数 6万+</span>

</div>

](https://blog.csdn.net/meng564764406/article/details/52444644 "将Excel文件导入数据库（POI+Excel+MySQL+jsp页面导入）第一次优化")

[<span class="desc oneline">本篇文章是根据我的上篇博客，给出的改进版，由于时间有限，仅做了一个简单的优化。相关文章：将excel导入数据库2018年4月1日，新增下载地址链接：点击打开源码下载地址十分抱歉，这个链接地址没有在这篇...</span>](https://blog.csdn.net/meng564764406/article/details/52444644 "将Excel文件导入数据库（POI+Excel+MySQL+jsp页面导入）第一次优化") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Lynn_Blog</span>](https://blog.csdn.net/meng564764406)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u013360850/article/details/78861442,BlogCommendFromThirdServiceAll_16&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u013360850/article/details/78861442,BlogCommendFromThirdServiceAll_16&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Spring Boot MyBatis 动态数据源切换、多数据源，读写分离

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-21</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/u013360850/article/details/78861442 "Spring Boot MyBatis 动态数据源切换、多数据源，读写分离")

[<span class="desc oneline">项目地址：https://github.com/helloworlde/SpringBoot-DynamicDataSource/tree/dev在SpringBoot应用中使用到了MyBatis作为...</span>](https://blog.csdn.net/u013360850/article/details/78861442 "Spring Boot MyBatis 动态数据源切换、多数据源，读写分离") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">HelloWood</span>](https://blog.csdn.net/u013360850)</span>

</div>

</div>

<div class="recommend-item-box baiduSearch recommend-box-ident" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/javazejian/article/details/71333103#%E6%9E%9A%E4%B8%BE%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86,searchFromBaidu1_8,-&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/javazejian/article/details/71333103#%E6%9E%9A%E4%B8%BE%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86,searchFromBaidu1_8,-&quot;}" data-flg="true">[

#### _深入__理解__Java__枚举类型_(_enum_) - zejian的博客 - CSDN博客

<div class="info-box d-flex align-content-center">

<span class="date">11-15</span>

</div>

亲爱的用户,您使用了广告屏蔽软件,广告是CSDN向您免费提供服务与产品的重要支持,希望您将csdn.net加入AdBlock Plus白名单,感谢支持!...

](https://blog.csdn.net/javazejian/article/details/71333103#%E6%9E%9A%E4%B8%BE%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86)</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_36747842/article/details/75453560,BlogCommendFromThirdServiceAll_17&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/qq_36747842/article/details/75453560,BlogCommendFromThirdServiceAll_17&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### size_t到底多大

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-20</span> <span class="read-num hover-hide">阅读数 620</span>

</div>

](https://blog.csdn.net/qq_36747842/article/details/75453560 "size_t到底多大")

[<span class="desc oneline">C语言中：size_t一般用来表示一种计数，比如有多少东西被拷贝等。sizeof操作符的结果类型是size_t，数组大小也是size_t类型。它在头文件中typedef为unsigned int类型，...</span>](https://blog.csdn.net/qq_36747842/article/details/75453560 "size_t到底多大") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">云淡风清的Coding</span>](https://blog.csdn.net/qq_36747842)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yideqianfenzhiyi/article/details/79422857,BlogCommendFromThirdServiceAll_18&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yideqianfenzhiyi/article/details/79422857,BlogCommendFromThirdServiceAll_18&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 【计算机视觉】_深入__理解_Attention机制

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-16</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/yideqianfenzhiyi/article/details/79422857 "【计算机视觉】深入理解Attention机制")

[<span class="desc oneline">1.什么是Attention机制？其实我没有找到attention的具体定义，但在计算机视觉的相关应用中大概可以分为两种：1）学习权重分布：输入数据或特征图上的不同部分对应的专注度不同，对此Jason...</span>](https://blog.csdn.net/yideqianfenzhiyi/article/details/79422857 "【计算机视觉】深入理解Attention机制") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Slow down, Keep learning and Enjoy life</span>](https://blog.csdn.net/yideqianfenzhiyi)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u013256816/article/details/50562905,BlogCommendFromThirdServiceAll_19&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u013256816/article/details/50562905,BlogCommendFromThirdServiceAll_19&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _Java__枚举类型__enum_

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-22</span> <span class="read-num hover-hide">阅读数 5338</span>

</div>

](https://blog.csdn.net/u013256816/article/details/50562905 "Java枚举类型enum")

[<span class="desc oneline">欢迎支持笔者新作：《深入理解Kafka:核心设计与实践原理》和《RabbitMQ实战指南》，同时欢迎关注笔者的微信公众号：朱小厮的博客。 枚举的语法1.Enum的全称为enumeration,中文俗称...</span>](https://blog.csdn.net/u013256816/article/details/50562905 "Java枚举类型enum") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">朱小厮的博客</span>](https://blog.csdn.net/u013256816)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lichengyu/article/details/20743877,BlogCommendFromThirdServiceAll_20&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lichengyu/article/details/20743877,BlogCommendFromThirdServiceAll_20&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### OpenCV实现Gabor滤波

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-08</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/lichengyu/article/details/20743877 "OpenCV实现Gabor滤波")

[<span class="desc oneline">图1 不同中心震荡频率下在Gabor函数代码：根据http://blog.csdn.net/watkinsong/article/details/7876361实现#include#include#i...</span>](https://blog.csdn.net/lichengyu/article/details/20743877 "OpenCV实现Gabor滤波") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">lichengyu的专栏</span>](https://blog.csdn.net/lichengyu)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ShaneLooLi/article/details/7212812,BlogCommendFromThirdServiceAll_21&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ShaneLooLi/article/details/7212812,BlogCommendFromThirdServiceAll_21&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 由 Windows 向 Linux 迁移字体

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-20</span> <span class="read-num hover-hide">阅读数 9450</span>

</div>

](https://blog.csdn.net/ShaneLooLi/article/details/7212812 "由 Windows 向 Linux 迁移字体")

[<span class="desc oneline">以下内容部分来自互联网，由作者，也就是ShaneLooLi整理1.FromWindowsWindows下字体库的位置为C:\Windows\fonts，这里面包含所有windows下可用的字体。2.T...</span>](https://blog.csdn.net/ShaneLooLi/article/details/7212812 "由 Windows 向 Linux 迁移字体") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Shane from Spads</span>](https://blog.csdn.net/ShaneLooLi)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/daisy0923/article/details/73325681,BlogCommendFromThirdServiceAll_22&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/daisy0923/article/details/73325681,BlogCommendFromThirdServiceAll_22&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### C# Chart控件的使用总结

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-16</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/daisy0923/article/details/73325681 "C# Chart控件的使用总结")

[<span class="desc oneline">最近一直在画图表，总结一下，方便以后参考。1、 图表的各种属性对不起，我太懒了，详情看如下的链接吧。。。。http://blog.sina.com.cn/s/blog_621e24e20101cp64...</span>](https://blog.csdn.net/daisy0923/article/details/73325681 "C# Chart控件的使用总结") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">快乐阿拉蕾的博客</span>](https://blog.csdn.net/daisy0923)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/mz4138/article/details/80927656,BlogCommendFromThirdServiceAll_23&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/mz4138/article/details/80927656,BlogCommendFromThirdServiceAll_23&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _enum_ 详解

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-05</span> <span class="read-num hover-hide">阅读数 286</span>

</div>

](https://blog.csdn.net/mz4138/article/details/80927656 "enum 详解")

[<span class="desc oneline">enum简介jdk版本1.8.0_102新建枚举首先新建一个枚举:packagecom.aya;publicenumSex{MALE,FEMALE;publicvoidgoToilet(){Syste...</span>](https://blog.csdn.net/mz4138/article/details/80927656 "enum 详解") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">开心学源码</span>](https://blog.csdn.net/mz4138)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tostq/article/details/51786265,BlogCommendFromThirdServiceAll_24&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tostq/article/details/51786265,BlogCommendFromThirdServiceAll_24&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 编写C语言版本的卷积神经网络CNN之一：前言与Minst数据集

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-29</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/tostq/article/details/51786265 "编写C语言版本的卷积神经网络CNN之一：前言与Minst数据集")

[<span class="desc oneline">卷积神经网络是深度学习的基础，但是学习CNN却不是那么简单，虽然网络上关于CNN的相关代码很多，比较经典的是tiny_cnn（C++）、DeepLearnToolbox（Matlab）等等，但通过C语...</span>](https://blog.csdn.net/tostq/article/details/51786265 "编写C语言版本的卷积神经网络CNN之一：前言与Minst数据集") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">tostq的专栏</span>](https://blog.csdn.net/tostq)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011442682/article/details/79078199,BlogCommendFromThirdServiceAll_25&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u011442682/article/details/79078199,BlogCommendFromThirdServiceAll_25&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### mysql _enum_ 字段类型的使用

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-16</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/u011442682/article/details/79078199 "mysql  enum 字段类型的使用")

[<span class="desc oneline">为什么使用枚举限定值的取值范围，比如性别（男，女，未知）等。枚举类型使用陷阱超级不推荐在mysql中设置某一字段类型为enum，但是存的值为数字，比如‘0’，‘1’，‘2’；解释1：你会混淆，因为en...</span>](https://blog.csdn.net/u011442682/article/details/79078199 "mysql  enum 字段类型的使用") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">777的博客</span>](https://blog.csdn.net/u011442682)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/maoyuanming0806/article/details/78067446,BlogCommendFromThirdServiceAll_26&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/maoyuanming0806/article/details/78067446,BlogCommendFromThirdServiceAll_26&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 搭建图片服务器《二》-linux安装nginx

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-22</span> <span class="read-num hover-hide">阅读数 8万+</span>

</div>

](https://blog.csdn.net/maoyuanming0806/article/details/78067446 "搭建图片服务器《二》-linux安装nginx")

[<span class="desc oneline">nginx是个好东西，Nginx(enginex)是一个高性能的HTTP和反向代理服务器，也是一个IMAP/POP3/SMTP服务器。Nginx是由伊戈尔·赛索耶夫为俄罗斯访问量第二的Rambler....</span>](https://blog.csdn.net/maoyuanming0806/article/details/78067446 "搭建图片服务器《二》-linux安装nginx") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">maoyuanming0806的博客</span>](https://blog.csdn.net/maoyuanming0806)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/wangyibo0201/article/details/51705966,BlogCommendFromThirdServiceAll_27&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/wangyibo0201/article/details/51705966,BlogCommendFromThirdServiceAll_27&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 异常点/离群点检测算法——LOF

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-18</span> <span class="read-num hover-hide">阅读数 8万+</span>

</div>

](https://blog.csdn.net/wangyibo0201/article/details/51705966 "异常点/离群点检测算法——LOF")

[<span class="desc oneline">局部异常因子算法-LocalOutlierFactor(LOF)　　在数据挖掘方面，经常需要在做特征工程和模型训练之前对数据进行清洗，剔除无效数据和异常数据。异常检测也是数据挖掘的一个方向，用于反作弊...</span>](https://blog.csdn.net/wangyibo0201/article/details/51705966 "异常点/离群点检测算法——LOF") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">wangyibo0201的博客</span>](https://blog.csdn.net/wangyibo0201)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/luyan_abaci/article/details/48014807,BlogCommendFromThirdServiceAll_28&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/luyan_abaci/article/details/48014807,BlogCommendFromThirdServiceAll_28&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### VS下生成与配置静态库与动态库（一）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-26</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/luyan_abaci/article/details/48014807 "VS下生成与配置静态库与动态库（一）")

[<span class="desc oneline">此处仅以VS2010为例，详细说明一下如何在VS环境下生成和使用C++的静态库与动态库。Qt下生成和使用静态和动态库后续再讲。本文仅供初学者参考，如果有问题欢迎大家指正。    首先简单地理解一下静态...</span>](https://blog.csdn.net/luyan_abaci/article/details/48014807 "VS下生成与配置静态库与动态库（一）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">luyan的博客</span>](https://blog.csdn.net/luyan_abaci)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Smile_qiqi/article/details/32724931,BlogCommendFromThirdServiceAll_29&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Smile_qiqi/article/details/32724931,BlogCommendFromThirdServiceAll_29&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 魔兽争霸3冰封王座1.24e 多开联机补丁 信息发布与收集点

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-20</span> <span class="read-num hover-hide">阅读数 6万+</span>

</div>

](https://blog.csdn.net/Smile_qiqi/article/details/32724931 "魔兽争霸3冰封王座1.24e 多开联机补丁 信息发布与收集点")

[<span class="desc oneline">畅所欲言！</span>](https://blog.csdn.net/Smile_qiqi/article/details/32724931 "魔兽争霸3冰封王座1.24e 多开联机补丁 信息发布与收集点") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Smile_qiqi的专栏</span>](https://blog.csdn.net/Smile_qiqi)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/gefangshuai/article/details/50328451,BlogCommendFromThirdServiceAll_30&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/gefangshuai/article/details/50328451,BlogCommendFromThirdServiceAll_30&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 关于SpringBoot bean无法注入的问题（与文件包位置有关）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-16</span> <span class="read-num hover-hide">阅读数 26万+</span>

</div>

](https://blog.csdn.net/gefangshuai/article/details/50328451 "关于SpringBoot bean无法注入的问题（与文件包位置有关）")

[<span class="desc oneline">问题场景描述整个项目通过Maven构建，大致结构如下：核心Spring框架一个modulespring-boot-baseservice和dao一个moduleserver-core提供系统后台数据管...</span>](https://blog.csdn.net/gefangshuai/article/details/50328451 "关于SpringBoot bean无法注入的问题（与文件包位置有关）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">开发随笔</span>](https://blog.csdn.net/gefangshuai)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/skyflying2012/article/details/22736633,BlogCommendFromThirdServiceAll_31&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/skyflying2012/article/details/22736633,BlogCommendFromThirdServiceAll_31&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### C语言_enum__枚举类型_解析

<div class="info-box d-flex align-content-center">

<span class="date hover-show">04-01</span> <span class="read-num hover-hide">阅读数 15万+</span>

</div>

](https://blog.csdn.net/skyflying2012/article/details/22736633 "C语言enum枚举类型解析")

[<span class="desc oneline">在实际应用中，有的变量只有几种可能取值。如人的性别只有两种可能取值，星期只有七种可能取值。在C语言中对这样取值比较特殊的变量可以定义为枚举类型。所谓枚举是指将变量的值一一列举出来，变量只限于列举出来的...</span>](https://blog.csdn.net/skyflying2012/article/details/22736633 "C语言enum枚举类型解析") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">做一个有技术追求的人</span>](https://blog.csdn.net/skyflying2012)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tsj11514oo/article/details/51794330,BlogCommendFromThirdServiceAll_32&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tsj11514oo/article/details/51794330,BlogCommendFromThirdServiceAll_32&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### fiddler抓包代理设置问题（PC端）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-30</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/tsj11514oo/article/details/51794330 "fiddler抓包代理设置问题（PC端）")

[<span class="desc oneline">前篇文章说了fiddler的工作原理，现在具体说一下fiddler抓包代理设置和在设置中出现的一些问题。1，安装好Fiddler后，我们一般是还抓不了数据的，需要在Fiddler和代理浏览器上做一些设...</span>](https://blog.csdn.net/tsj11514oo/article/details/51794330 "fiddler抓包代理设置问题（PC端）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">童小绿 学无止境</span>](https://blog.csdn.net/tsj11514oo)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/roguesir/article/details/77104246,BlogCommendFromThirdServiceAll_33&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/roguesir/article/details/77104246,BlogCommendFromThirdServiceAll_33&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 人脸检测工具face_recognition的安装与应用

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-11</span> <span class="read-num hover-hide">阅读数 8万+</span>

</div>

](https://blog.csdn.net/roguesir/article/details/77104246 "人脸检测工具face_recognition的安装与应用")

[<span class="desc oneline">人脸检测工具face_recognition的安装与应用</span>](https://blog.csdn.net/roguesir/article/details/77104246 "人脸检测工具face_recognition的安装与应用") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">roguesir的博客</span>](https://blog.csdn.net/roguesir)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u012436149/article/details/53341372,BlogCommendFromThirdServiceAll_34&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u012436149/article/details/53341372,BlogCommendFromThirdServiceAll_34&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### tensorflow学习笔记（二十二）：Supervisor

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-25</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/u012436149/article/details/53341372 "tensorflow学习笔记（二十二）：Supervisor")

[<span class="desc oneline">如何使用Supervisor在不使用Supervisor的时候，我们的代码经常是这么组织的variables...ops...summary_op...merge_all_summariesaveri...</span>](https://blog.csdn.net/u012436149/article/details/53341372 "tensorflow学习笔记（二十二）：Supervisor") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Keith</span>](https://blog.csdn.net/u012436149)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Tiaaaaa/article/details/58116346,BlogCommendFromThirdServiceAll_35&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Tiaaaaa/article/details/58116346,BlogCommendFromThirdServiceAll_35&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### R语言逻辑回归、ROC曲线和十折交叉验证

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-27</span> <span class="read-num hover-hide">阅读数 8万+</span>

</div>

](https://blog.csdn.net/Tiaaaaa/article/details/58116346 "R语言逻辑回归、ROC曲线和十折交叉验证")

[<span class="desc oneline">自己整理编写的逻辑回归模板，作为学习笔记记录分享。数据集用的是14个自变量Xi，一个因变量Y的australian数据集。1.测试集和训练集3、7分组australian...</span>](https://blog.csdn.net/Tiaaaaa/article/details/58116346 "R语言逻辑回归、ROC曲线和十折交叉验证") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Tiaaaaa的博客</span>](https://blog.csdn.net/Tiaaaaa)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zhoufanyang_china/article/details/86707727,BlogCommendFromThirdServiceAll_36&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/zhoufanyang_china/article/details/86707727,BlogCommendFromThirdServiceAll_36&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _深入__理解__Java_中的_enum_（枚举）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-30</span> <span class="read-num hover-hide">阅读数 61</span>

</div>

](https://blog.csdn.net/zhoufanyang_china/article/details/86707727 "深入理解Java中的enum（枚举）")

[<span class="desc oneline">项目中如果要定义组变量，你可能会这样定义： publicstaticfinalStringKEY_PRE=&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;qu...</span>](https://blog.csdn.net/zhoufanyang_china/article/details/86707727 "深入理解Java中的enum（枚举）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">扬帆舟的博客</span>](https://blog.csdn.net/zhoufanyang_china)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/pengjc2001/article/details/54924699,BlogCommendFromThirdServiceAll_37&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/pengjc2001/article/details/54924699,BlogCommendFromThirdServiceAll_37&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 三菱FX系列PLC与PC通讯的实现之专有协议（计算机联接）的程序设计之一

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-11</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/pengjc2001/article/details/54924699 "三菱FX系列PLC与PC通讯的实现之专有协议（计算机联接）的程序设计之一")

[<span class="desc oneline">阅读内容为：FX系列微型可编程控制器用户手册（通讯篇）中计算机链接功能章节。采用本方法通信，pc端的实现，其实就是，把操作按照协议（2种）翻译成相应的字符串，通过串口发送给plc。编写一应用程序，使得...</span>](https://blog.csdn.net/pengjc2001/article/details/54924699 "三菱FX系列PLC与PC通讯的实现之专有协议（计算机联接）的程序设计之一") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">pengjc2001的博客</span>](https://blog.csdn.net/pengjc2001)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ymj7150697/article/details/7384126,BlogCommendFromThirdServiceAll_38&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ymj7150697/article/details/7384126,BlogCommendFromThirdServiceAll_38&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### expat介绍文档翻译

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-22</span> <span class="read-num hover-hide">阅读数 7万+</span>

</div>

](https://blog.csdn.net/ymj7150697/article/details/7384126 "expat介绍文档翻译")

[<span class="desc oneline">原文地址：http://www.xml.com/pub/a/1999/09/expat/index.html因为需要用，所以才翻译了这个文档。但总归赖于英语水平很有限，翻译出来的中文有可能会词不达意。...</span>](https://blog.csdn.net/ymj7150697/article/details/7384126 "expat介绍文档翻译") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">ymj7150697的专栏</span>](https://blog.csdn.net/ymj7150697)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/haitao111313/article/details/7875392,BlogCommendFromThirdServiceAll_39&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/haitao111313/article/details/7875392,BlogCommendFromThirdServiceAll_39&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 基于PCA的人脸检测（Matlab版代码）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-16</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/haitao111313/article/details/7875392 "基于PCA的人脸检测（Matlab版代码）")

[<span class="desc oneline">花了几天，终于把matlab版的人脸检测运行成功了，虽然正确率不是很高，看着各种论文上的人脸检测正确率都出奇的高，我是不怎么相信的，有的论文连基于平均脸的人脸检测正确率都能达到98%，汗啊～～ 也许真...</span>](https://blog.csdn.net/haitao111313/article/details/7875392 "基于PCA的人脸检测（Matlab版代码）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">海海人生</span>](https://blog.csdn.net/haitao111313)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/c5153000/article/details/6210783,BlogCommendFromThirdServiceAll_40&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/c5153000/article/details/6210783,BlogCommendFromThirdServiceAll_40&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 关于面试时项目的介绍

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-27</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/c5153000/article/details/6210783 " 关于面试时项目的介绍")

[<span class="desc oneline">面试一般都带简历的，简历上都会写自己做过什么项目，而且要写自己做过的能做出来的。如果项目经理让你说说自己做的项目时，你就答你在简历上写的东西。先从业务上说起，都啥功能，干啥的。在多加点就是你用了什么技...</span>](https://blog.csdn.net/c5153000/article/details/6210783 " 关于面试时项目的介绍") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">猫儿</span>](https://blog.csdn.net/c5153000)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hayixia606/article/details/79237220,BlogCommendFromThirdServiceAll_41&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hayixia606/article/details/79237220,BlogCommendFromThirdServiceAll_41&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-02</span> <span class="read-num hover-hide">阅读数 18万+</span>

</div>

](https://blog.csdn.net/hayixia606/article/details/79237220 "微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用")

[<span class="desc oneline">扫二维码关注，获取更多技术分享本文承接之前发布的博客《微信支付V3微信公众号支付PHP教程/thinkPHP5公众号支付》必须阅读上篇文章后才可以阅读这篇文章。由于最近一段时间工作比较忙，博客更新比较...</span>](https://blog.csdn.net/hayixia606/article/details/79237220 "微信支付V3微信公众号支付PHP教程(thinkPHP5公众号支付)/JSSDK的使用") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Marswill</span>](https://blog.csdn.net/hayixia606)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/logogcn/article/details/7879398,BlogCommendFromThirdServiceAll_42&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/logogcn/article/details/7879398,BlogCommendFromThirdServiceAll_42&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### _enum_ 在c中的使用

<div class="info-box d-flex align-content-center">

<span class="date hover-show">08-17</span> <span class="read-num hover-hide">阅读数 14万+</span>

</div>

](https://blog.csdn.net/logogcn/article/details/7879398 "enum 在c中的使用")

[<span class="desc oneline">如果一个变量你需要几种可能存在的值，那么就可以被定义成为枚举类型。之所以叫枚举就是说将变量或者叫对象可能存在的情况也可以说是可能的值一一例举出来。 　　举个例子来说明一吧，为了让大家更明白一点，比如一...</span>](https://blog.csdn.net/logogcn/article/details/7879398 "enum 在c中的使用") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">logogcn的专栏</span>](https://blog.csdn.net/logogcn)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/jnulzl/article/details/49894041,BlogCommendFromThirdServiceAll_43&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/jnulzl/article/details/49894041,BlogCommendFromThirdServiceAll_43&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 史上最好的LDA(线性判别分析)教程

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-17</span> <span class="read-num hover-hide">阅读数 5万+</span>

</div>

](https://blog.csdn.net/jnulzl/article/details/49894041 "史上最好的LDA(线性判别分析)教程")

[<span class="desc oneline">一、前言最近由于研究需要，要用到线性判别分析(LDA)。于是找了很多资料来看，结果发现大部分讲的都是理论知识，因此最后还是看的一知半解，后来终于找到了个英文的文档，作者由PCA引入LDA，看过后豁然开...</span>](https://blog.csdn.net/jnulzl/article/details/49894041 "史上最好的LDA(线性判别分析)教程") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">jnulzl的专栏</span>](https://blog.csdn.net/jnulzl)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Main_Stage/article/details/41989499,BlogCommendFromThirdServiceAll_44&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Main_Stage/article/details/41989499,BlogCommendFromThirdServiceAll_44&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Android圆形图片--自定义控件

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-17</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/Main_Stage/article/details/41989499 "Android圆形图片--自定义控件")

[<span class="desc oneline">Android圆形图片--自定义控件</span>](https://blog.csdn.net/Main_Stage/article/details/41989499 "Android圆形图片--自定义控件") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Main_Stage的专栏</span>](https://blog.csdn.net/Main_Stage)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lubiaopan/article/details/6233517,BlogCommendFromThirdServiceAll_45&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lubiaopan/article/details/6233517,BlogCommendFromThirdServiceAll_45&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### .NET和_java_的RSA互通，仅此而已

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-09</span> <span class="read-num hover-hide">阅读数 7万+</span>

</div>

](https://blog.csdn.net/lubiaopan/article/details/6233517 ".NET和java的RSA互通，仅此而已")

[<span class="desc oneline">RSA.netjva互通解决不能互通的问题</span>](https://blog.csdn.net/lubiaopan/article/details/6233517 ".NET和java的RSA互通，仅此而已") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">lubiaopan的专栏</span>](https://blog.csdn.net/lubiaopan)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lujiandong1/article/details/44464785,BlogCommendFromThirdServiceAll_46&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lujiandong1/article/details/44464785,BlogCommendFromThirdServiceAll_46&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### error LNK2019: 无法解析的外部符号 opencv

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-19</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/lujiandong1/article/details/44464785 "error LNK2019: 无法解析的外部符号 opencv")

[<span class="desc oneline">LBP.obj:errorLNK2019:无法解析的外部符号_cvCreateImage，该符号在函数"public:void__thiscallLBP::CalGrayInvariant(charc...</span>](https://blog.csdn.net/lujiandong1/article/details/44464785 "error LNK2019: 无法解析的外部符号 opencv") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">lujiandong1的专栏</span>](https://blog.csdn.net/lujiandong1)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/silentpebble/article/details/41279285,BlogCommendFromThirdServiceAll_47&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/silentpebble/article/details/41279285,BlogCommendFromThirdServiceAll_47&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### centos 查看命令源码

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-19</span> <span class="read-num hover-hide">阅读数 13万+</span>

</div>

](https://blog.csdn.net/silentpebble/article/details/41279285 "centos 查看命令源码")

[<span class="desc oneline">#yuminstallyum-utils设置源:[base-src]name=CentOS-5.4-Basesrc-baseurl=http://vault.centos.org/5.4/os/SRP...</span>](https://blog.csdn.net/silentpebble/article/details/41279285 "centos 查看命令源码") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">linux/unix</span>](https://blog.csdn.net/silentpebble)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/arthur503/article/details/19974057,BlogCommendFromThirdServiceAll_48&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/arthur503/article/details/19974057,BlogCommendFromThirdServiceAll_48&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 使用libsvm对MNIST数据集进行实验

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-26</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/arthur503/article/details/19974057 "使用libsvm对MNIST数据集进行实验")

[<span class="desc oneline">在学SVM中的实验环节，老师介绍了libsvm的使用。当时看完之后感觉简单的说不出话来。1.libsvm介绍虽然原理要求很高的数学知识等，但是libsvm中，完全就是一个工具包，拿来就能用。当时问了好...</span>](https://blog.csdn.net/arthur503/article/details/19974057 "使用libsvm对MNIST数据集进行实验") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">问道于盲</span>](https://blog.csdn.net/arthur503)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/diandianxiyu/article/details/53068012,BlogCommendFromThirdServiceAll_49&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/diandianxiyu/article/details/53068012,BlogCommendFromThirdServiceAll_49&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 【小程序】微信小程序开发实践

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-07</span> <span class="read-num hover-hide">阅读数 31万+</span>

</div>

](https://blog.csdn.net/diandianxiyu/article/details/53068012 "【小程序】微信小程序开发实践")

[<span class="desc oneline">帐号相关流程注册范围企业政府媒体其他组织换句话讲就是不让个人开发者注册。:)填写企业信息不能使用和之前的公众号账户相同的邮箱,也就是说小程序是和微信公众号一个层级的。填写公司机构信息,对公账户信息绑定...</span>](https://blog.csdn.net/diandianxiyu/article/details/53068012 "【小程序】微信小程序开发实践") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">小雨同学的技术博客</span>](https://blog.csdn.net/diandianxiyu)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hellostory/article/details/7265357,BlogCommendHotData_0&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hellostory/article/details/7265357,BlogCommendHotData_0&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Spring3MVC提交弹出窗口表单后，自动返回父窗口的列表页面

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-16</span> <span class="read-num hover-hide">阅读数 6653</span>

</div>

](https://blog.csdn.net/hellostory/article/details/7265357 "Spring3MVC提交弹出窗口表单后，自动返回父窗口的列表页面")

[<span class="desc oneline">方法： @RequestMapping(value = "/save") public String save(HttpServletResponse response){ ...</span>](https://blog.csdn.net/hellostory/article/details/7265357 "Spring3MVC提交弹出窗口表单后，自动返回父窗口的列表页面") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">hellostory的专栏</span>](https://blog.csdn.net/hellostory)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/booirror/article/details/45490523,BlogCommendHotData_1&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/booirror/article/details/45490523,BlogCommendHotData_1&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 最佳实战：用Cocos2d-x3.x和C++11编写2048游戏以及游戏AI（全民2048 Android版上线啦）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">05-05</span> <span class="read-num hover-hide">阅读数 7597</span>

</div>

](https://blog.csdn.net/booirror/article/details/45490523 "最佳实战：用Cocos2d-x3.x和C++11编写2048游戏以及游戏AI（全民2048 Android版上线啦）")

[<span class="desc oneline">话说，年仅19岁的意大利人Gabriele Cirulli于2014年3月完成并发布在github上，游戏设计来自于《1024》，而《1024》灵感来源于《Threes!》的移动端游戏。然而游戏飙升的...</span>](https://blog.csdn.net/booirror/article/details/45490523 "最佳实战：用Cocos2d-x3.x和C++11编写2048游戏以及游戏AI（全民2048 Android版上线啦）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">代码菌的blog</span>](https://blog.csdn.net/booirror)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ghsau/article/details/20466351,BlogCommendHotData_2&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/ghsau/article/details/20466351,BlogCommendHotData_2&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 共同父域下的单点登录

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-04</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/ghsau/article/details/20466351 "共同父域下的单点登录")

[<span class="desc oneline">单点登录(Single Sign On)，简称为SSO，SSO不仅在企业级开发很常用，在互联网中更是大行其道。随便举几个例子，比如我们登录新浪微博后，再访问新浪首页后，我们发现，已经自动登录了；再比如...</span>](https://blog.csdn.net/ghsau/article/details/20466351 "共同父域下的单点登录") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">高爽|Coder</span>](https://blog.csdn.net/ghsau)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tubinbin5201314/article/details/50247383,BlogCommendHotData_3&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tubinbin5201314/article/details/50247383,BlogCommendHotData_3&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 安卓开发--textView的字体样式设置（设置宋体，微软雅黑等）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-10</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/tubinbin5201314/article/details/50247383 "安卓开发--textView的字体样式设置（设置宋体，微软雅黑等）")

[<span class="desc oneline">  最近项目中出现把字体设置成宋体，微软雅黑，黑体，楷体等的需求; 度娘发现Android系统默认支持三种字体，分别为：“sans”, “serif”, “monospace&quot;，除此之外...</span>](https://blog.csdn.net/tubinbin5201314/article/details/50247383 "安卓开发--textView的字体样式设置（设置宋体，微软雅黑等）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">tubinbin5201314的博客</span>](https://blog.csdn.net/tubinbin5201314)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/han1202012/article/details/18812279,BlogCommendHotData_4&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/han1202012/article/details/18812279,BlogCommendHotData_4&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 【代码管理】GitHub超详细图文攻略 - Git客户端下载安装 GitHub提交修改源码工作流程 Git分支 标签 过滤 Git版本工作流

<div class="info-box d-flex align-content-center">

<span class="date hover-show">01-29</span> <span class="read-num hover-hide">阅读数 3万+</span>

</div>

](https://blog.csdn.net/han1202012/article/details/18812279 "【代码管理】GitHub超详细图文攻略 - Git客户端下载安装 GitHub提交修改源码工作流程 Git分支 标签 过滤 Git版本工作流")

[<span class="desc oneline">① 总结GitHub常用操作, 看不懂看下面的详细讲解; ② 对Git进行详细的介绍 : 详解Git的分布式, 离线操作 ; ③ msysgit的下载, 安装, 配置, Git Bash 和 Git ...</span>](https://blog.csdn.net/han1202012/article/details/18812279 "【代码管理】GitHub超详细图文攻略 - Git客户端下载安装 GitHub提交修改源码工作流程 Git分支 标签 过滤 Git版本工作流") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">让 学习 成为一种 习惯 ( 韩曙亮 の 技术博客 )</span>](https://blog.csdn.net/han1202012)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u012874222/article/details/79400154,BlogCommendHotData_6&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/u012874222/article/details/79400154,BlogCommendHotData_6&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 卡顿监测之真正轻量级的卡顿监测工具BlockDetectUtil（仅一个类）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-01</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/u012874222/article/details/79400154 "卡顿监测之真正轻量级的卡顿监测工具BlockDetectUtil（仅一个类）")

[<span class="desc oneline">一、背景    一直以来，应用的流畅度都关乎着用户的体验性，而体验性好的产品自然而然会受到更多用户的欢迎，所以对于广大的工程师来说，界面的卡顿优化一直是Android应用性能优化的重要一环。而当前应用...</span>](https://blog.csdn.net/u012874222/article/details/79400154 "卡顿监测之真正轻量级的卡顿监测工具BlockDetectUtil（仅一个类）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">u012874222的博客</span>](https://blog.csdn.net/u012874222)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yszwn/article/details/5033576,BlogCommendHotData_7&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/yszwn/article/details/5033576,BlogCommendHotData_7&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### web.config中的session配置详解

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-18</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/yszwn/article/details/5033576 "web.config中的session配置详解")

[<span class="desc oneline">     打开某个应用程序的配置文件Web.config后，我们会发现以下这段： < sessionState mode="InProc" stateConnectionString="tcpip=1...</span>](https://blog.csdn.net/yszwn/article/details/5033576 "web.config中的session配置详解") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">yszwn的专栏</span>](https://blog.csdn.net/yszwn)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/crazy1235/article/details/44069267,BlogCommendHotData_8&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/crazy1235/article/details/44069267,BlogCommendHotData_8&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 百度地图开发（五）之公交信息检索 + 路线规划

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-05</span> <span class="read-num hover-hide">阅读数 5万+</span>

</div>

](https://blog.csdn.net/crazy1235/article/details/44069267 "百度地图开发（五）之公交信息检索 + 路线规划")

[<span class="desc oneline">转载请注明出处：     在上一篇blog中介绍过POI检索的使用，本篇blog主要介绍公交信息检索和线路规划的内容。 公交信息检索     实际上，公交信息检索与POI检索、在线建议检索非常相似，也...</span>](https://blog.csdn.net/crazy1235/article/details/44069267 "百度地图开发（五）之公交信息检索 + 路线规划") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">crazy_jack</span>](https://blog.csdn.net/crazy1235)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/jiangtongcn/article/details/13509633,BlogCommendHotData_9&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/jiangtongcn/article/details/13509633,BlogCommendHotData_9&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Activex打包于发布完整版---ActiveX打包

<div class="info-box d-flex align-content-center">

<span class="date hover-show">10-29</span> <span class="read-num hover-hide">阅读数 5268</span>

</div>

](https://blog.csdn.net/jiangtongcn/article/details/13509633 "Activex打包于发布完整版---ActiveX打包")

[<span class="desc oneline">前面介绍了数字证书的原理与制作：http://blog.csdn.net/jiangtongcn/article/details/13508365，下面来看一下ActiveX组件的打包。 我现在有一...</span>](https://blog.csdn.net/jiangtongcn/article/details/13509633 "Activex打包于发布完整版---ActiveX打包") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">jiangtongcn的专栏</span>](https://blog.csdn.net/jiangtongcn)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/iloveyin/article/details/39998651,BlogCommendHotData_10&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/iloveyin/article/details/39998651,BlogCommendHotData_10&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 腾讯视频解析接口

<div class="info-box d-flex align-content-center">

<span class="date hover-show">10-11</span> <span class="read-num hover-hide">阅读数 4万+</span>

</div>

](https://blog.csdn.net/iloveyin/article/details/39998651 "腾讯视频解析接口")

[<span class="desc oneline">普通流视频（完整视频） http://vv.video.qq.com/geturl?vid=v00149uf4ir&otype=json 高清视频（分段视频） 1080P-fhd，超...</span>](https://blog.csdn.net/iloveyin/article/details/39998651 "腾讯视频解析接口") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">专注于互联网架构技术，努力成为一名架构师</span>](https://blog.csdn.net/iloveyin)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xu__cg/article/details/53054439,BlogCommendHotData_12&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/xu__cg/article/details/53054439,BlogCommendHotData_12&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Java设计模式11——享元模式

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-06</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/xu__cg/article/details/53054439 "Java设计模式11——享元模式")

[<span class="desc oneline">一、适用场景　　内存属于稀缺资源，不能随意浪费。如果在一个系统中有很多个完全相同或相似的对象，我们就可以使用享元模式，让他们共享一份内存即可，不必每个都去实例化对象，从而节省内存空间。二、模式核心 享...</span>](https://blog.csdn.net/xu__cg/article/details/53054439 "Java设计模式11——享元模式") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">小小本科生成长之路</span>](https://blog.csdn.net/xu__cg)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Jaster_wisdom/article/details/51332891,BlogCommendHotData_13&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/Jaster_wisdom/article/details/51332891,BlogCommendHotData_13&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### EGE 在Dev下的环境配置 和 第一个绘图程序

<div class="info-box d-flex align-content-center">

<span class="date hover-show">05-06</span> <span class="read-num hover-hide">阅读数 7284</span>

</div>

](https://blog.csdn.net/Jaster_wisdom/article/details/51332891 "EGE 在Dev下的环境配置 和 第一个绘图程序")

[<span class="desc oneline">EGE（Easy Graphics Engine），是windows下的简易绘图库，是一个类似BGI(graphics.h)的面向C/C++语言新手的图形库，它的目标也是为了替代TC的BGI库而存在。...</span>](https://blog.csdn.net/Jaster_wisdom/article/details/51332891 "EGE 在Dev下的环境配置 和 第一个绘图程序") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Jaster_wisdom的专栏</span>](https://blog.csdn.net/Jaster_wisdom)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lutinghuan/article/details/46820023,BlogCommendHotData_14&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/lutinghuan/article/details/46820023,BlogCommendHotData_14&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 4种方法让SpringMVC接收多个对象

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-10</span> <span class="read-num hover-hide">阅读数 14万+</span>

</div>

](https://blog.csdn.net/lutinghuan/article/details/46820023 "4种方法让SpringMVC接收多个对象")

[<span class="desc oneline">问题背景： 我要在一个表单里同时一次性提交多名乘客的个人信息到SpringMVC，前端HTML和SpringMVC Controller里该如何处理？ 第1种方法：表单提交，以字段数组接收； 第2种...</span>](https://blog.csdn.net/lutinghuan/article/details/46820023 "4种方法让SpringMVC接收多个对象") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">一个情绪猿的脖克...</span>](https://blog.csdn.net/lutinghuan)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/isea533/article/details/49806637,BlogCommendHotData_15&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/isea533/article/details/49806637,BlogCommendHotData_15&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Docx4j 简单操作文字图片（包含页眉页脚和主体内容）

<div class="info-box d-flex align-content-center">

<span class="date hover-show">11-12</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/isea533/article/details/49806637 "Docx4j 简单操作文字图片（包含页眉页脚和主体内容）")

[<span class="desc oneline">docx4j官方提供了一些例子，本文只是其中一部分应用的简单例子。需要注意的地方是页眉和页脚，必须创建对应关系才能起作用。页眉和页脚添加图片的时候，第二个参数sourcePart是必须的，调用的cre...</span>](https://blog.csdn.net/isea533/article/details/49806637 "Docx4j 简单操作文字图片（包含页眉页脚和主体内容）") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">偶尔记一下</span>](https://blog.csdn.net/isea533)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/sx341125/article/details/39086717,BlogCommendHotData_16&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/sx341125/article/details/39086717,BlogCommendHotData_16&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 关于Arcgis数据导入mdb完成后如何立刻解除mdb的锁定

<div class="info-box d-flex align-content-center">

<span class="date hover-show">09-05</span> <span class="read-num hover-hide">阅读数 8635</span>

</div>

](https://blog.csdn.net/sx341125/article/details/39086717 "关于Arcgis数据导入mdb完成后如何立刻解除mdb的锁定")

[<span class="desc oneline">今天尝试</span>](https://blog.csdn.net/sx341125/article/details/39086717 "关于Arcgis数据导入mdb完成后如何立刻解除mdb的锁定") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Sean的专栏</span>](https://blog.csdn.net/sx341125)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/shanyongxu/article/details/51189335,BlogCommendHotData_17&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/shanyongxu/article/details/51189335,BlogCommendHotData_17&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 同步传输字符串

<div class="info-box d-flex align-content-center">

<span class="date hover-show">04-19</span> <span class="read-num hover-hide">阅读数 1932</span>

</div>

](https://blog.csdn.net/shanyongxu/article/details/51189335 "同步传输字符串")

[<span class="desc oneline">同步传输字符串 接下来考虑着一种情况,完成一个简单的文本通信:(1).客户端将字符串发送到服务端,服务端接受字符串并显示(2).服务端将字符串由英文的小写转换为大写,然后发回给客户端,客户端接受并显示...</span>](https://blog.csdn.net/shanyongxu/article/details/51189335 "同步传输字符串") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">见证大牛成长之路的专栏</span>](https://blog.csdn.net/shanyongxu)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/chenyufei1013/article/details/7032270,BlogCommendHotData_18&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/chenyufei1013/article/details/7032270,BlogCommendHotData_18&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 重读C++之一：封装、继承和多态

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-01</span> <span class="read-num hover-hide">阅读数 3326</span>

</div>

](https://blog.csdn.net/chenyufei1013/article/details/7032270 "重读C++之一：封装、继承和多态")

[<span class="desc oneline">导读         前段时间重新看了一下C++，一是感觉清晰了许多，二是觉得若是换个角度看的话，会有不一样的体会，并且也容易记住C++中的一些特性。本文就试图将集合论中的相关知识引入到C+...</span>](https://blog.csdn.net/chenyufei1013/article/details/7032270 "重读C++之一：封装、继承和多态") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">陈俞飞的专栏</span>](https://blog.csdn.net/chenyufei1013)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/wwj_748/article/details/30072379,BlogCommendHotData_20&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/wwj_748/article/details/30072379,BlogCommendHotData_20&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Cocos2d-x 2.2.3 使用NDK配置编译环境

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-11</span> <span class="read-num hover-hide">阅读数 2万+</span>

</div>

](https://blog.csdn.net/wwj_748/article/details/30072379 "Cocos2d-x 2.2.3 使用NDK配置编译环境")

[<span class="desc oneline">Cocos2d-x 2.2.3 使用NDK配置编译环境2014年6月11日 Cocos2d-x 3.0以下的开发环境的配置恐怕折磨了很多人，使用cygwin配置编译环境足够让初学者蛋疼一阵子了。本篇博...</span>](https://blog.csdn.net/wwj_748/article/details/30072379 "Cocos2d-x 2.2.3 使用NDK配置编译环境") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">巫山老妖</span>](https://blog.csdn.net/wwj_748)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/myNameIssls/article/details/51302633,BlogCommendHotData_24&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/myNameIssls/article/details/51302633,BlogCommendHotData_24&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### ApacheActiveMQ安装必要条件

<div class="info-box d-flex align-content-center">

<span class="date hover-show">05-03</span> <span class="read-num hover-hide">阅读数 8849</span>

</div>

](https://blog.csdn.net/myNameIssls/article/details/51302633 "ApacheActiveMQ安装必要条件")

[<span class="desc oneline">ApacheActiveMQ安装必要条件</span>](https://blog.csdn.net/myNameIssls/article/details/51302633 "ApacheActiveMQ安装必要条件") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">业精于勤-行成于思</span>](https://blog.csdn.net/myNameIssls)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hanjun0612/article/details/50441437,BlogCommendHotData_25&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hanjun0612/article/details/50441437,BlogCommendHotData_25&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### ajax 提交数组 泛型集合

<div class="info-box d-flex align-content-center">

<span class="date hover-show">12-31</span> <span class="read-num hover-hide">阅读数 1万+</span>

</div>

](https://blog.csdn.net/hanjun0612/article/details/50441437 "ajax 提交数组 泛型集合")

[<span class="desc oneline">转载：http://blog.csdn.net/lingxyd_0/article/details/10428785     在项目上用到了批量删除与批量更改状态，前台使用了EasyUI的Dat...</span>](https://blog.csdn.net/hanjun0612/article/details/50441437 "ajax 提交数组 泛型集合") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">正怒月神的博客</span>](https://blog.csdn.net/hanjun0612)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/sunyinggang/article/details/79383053,BlogCommendHotData_26&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/sunyinggang/article/details/79383053,BlogCommendHotData_26&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### phpstudy设置允许远程访问mysql数据库

<div class="info-box d-flex align-content-center">

<span class="date hover-show">02-26</span> <span class="read-num hover-hide">阅读数 9817</span>

</div>

](https://blog.csdn.net/sunyinggang/article/details/79383053 "phpstudy设置允许远程访问mysql数据库")

[<span class="desc oneline">1、先在服务器中通过命令行方式（打开phpstudy界面-&amp;gt;右下角其他菜单选项-&amp;gt;MySQL工具-&amp;gt;MySQL命令行）登录mysql：mysql   -u r...</span>](https://blog.csdn.net/sunyinggang/article/details/79383053 "phpstudy设置允许远程访问mysql数据库") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">sunyinggang的博客</span>](https://blog.csdn.net/sunyinggang)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tanhuifang520/article/details/79623978,BlogCommendHotData_28&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/tanhuifang520/article/details/79623978,BlogCommendHotData_28&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### ffmpeg命令录制windows音视频

<div class="info-box d-flex align-content-center">

<span class="date hover-show">03-20</span> <span class="read-num hover-hide">阅读数 3820</span>

</div>

](https://blog.csdn.net/tanhuifang520/article/details/79623978 "ffmpeg命令录制windows音视频")

[<span class="desc oneline">欢迎转载请注明出处：海漩涡http://blog.csdn.net/tanhuifang520                ffmpeg命令录制windows音视频一、下载ffmpeg存放在wind...</span>](https://blog.csdn.net/tanhuifang520/article/details/79623978 "ffmpeg命令录制windows音视频") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">tanhuifang520的博客</span>](https://blog.csdn.net/tanhuifang520)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/bob601450868/article/details/52073805,BlogCommendHotData_29&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/bob601450868/article/details/52073805,BlogCommendHotData_29&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### Spark2学习1之基本环境搭建（win）问题

<div class="info-box d-flex align-content-center">

<span class="date hover-show">07-30</span> <span class="read-num hover-hide">阅读数 5万+</span>

</div>

](https://blog.csdn.net/bob601450868/article/details/52073805 "Spark2学习1之基本环境搭建（win）问题")

[<span class="desc oneline">更多代码请见：https://github.com/xubo245/SparkLearning 版本：Spark-2.0.01解释 从【2】中下载release版，idea打开mvn packag...</span>](https://blog.csdn.net/bob601450868/article/details/52073805 "Spark2学习1之基本环境搭建（win）问题") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">Keep Learning</span>](https://blog.csdn.net/bob601450868)</span>

</div>

</div>

<div class="recommend-item-box type_blog clearfix" data-track-view="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hero_fantao/article/details/34533533,BlogCommendHotData_30&quot;}" data-track-click="{&quot;mod&quot;:&quot;popu_387&quot;,&quot;con&quot;:&quot;,https://blog.csdn.net/hero_fantao/article/details/34533533,BlogCommendHotData_30&quot;}" data-flg="true">

<div class="content" style="width: 852px;">[

#### 连续特征离散化和归一化

<div class="info-box d-flex align-content-center">

<span class="date hover-show">06-25</span> <span class="read-num hover-hide">阅读数 6万+</span>

</div>

](https://blog.csdn.net/hero_fantao/article/details/34533533 "连续特征离散化和归一化")

[<span class="desc oneline">连续特征进行离散化处理。</span>](https://blog.csdn.net/hero_fantao/article/details/34533533 "连续特征离散化和归一化") <span class="blog_title_box oneline "><span class="type-show type-show-blog type-show-after">博文</span> [来自： <span class="blog_title">hero_fantao的专栏</span>](https://blog.csdn.net/hero_fantao)</span>

</div>

</div>

<div class="recommend-item-box type_hot_word">

<div class="content clearfix" style="width: 852px;">

<div class="word float-left"><span>[设计制作学习](https://edu.csdn.net/combos/o363_l0_t ) </span><span>[机器学习教程](https://edu.csdn.net/courses/o5329_s5330_k ) </span><span>[Objective-C培训](https://edu.csdn.net/courses/o280_s351_k ) </span><span>[交互设计视频教程](https://edu.csdn.net/combos/o7115_s388_l0_t ) </span><span>[颜色模型](https://edu.csdn.net/course/play/5599/104252 )</span></div>

</div>

<div class="content clearfix" style="width: 852px;">

<div class="float-left"><span>[mysql关联查询两次本表](https://www.csdn.net/gather_24/MtTaEg3sMDM5MS1ibG9n.html)</span> <span>[native底部 react](https://www.csdn.net/gather_10/MtjaIg3sMTUzMy1kb3dubG9hZAO0O0OO0O0O.html)</span> <span>[extjs glyph 图标](https://www.csdn.net/gather_1b/Ntzagg1sOTU3LWRvd25sb2Fk.html)</span> <span>[java枚举类型学习](https://www.csdn.net/gather_4a/NtzaMg4sMDQtZWR1.html)</span> <span>[8天深入理解python教程](https://www.csdn.net/gather_4a/MtzacgysNi1lZHUO0O0O.html)</span></div>

</div>

</div>

<div class="recommend-loading-box">![](https://csdnimg.cn/release/phoenix/images/feedLoading.gif)</div>

<div class="recommend-end-box" style="display: block;">

没有更多推荐了，[返回首页](https://blog.csdn.net/)

</div>

</div>

</main>
