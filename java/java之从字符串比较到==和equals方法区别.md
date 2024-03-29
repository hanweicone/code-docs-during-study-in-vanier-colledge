# java之从字符串比较到==和equals方法区别
 

我们先看代码

 

    String str1 = new String("hello");
    String str2 = "hello";

    System.out.println("str1==str2： " + (str1==str2));  \\1
    System.out.println("str1.equals(str2)： " + str1.equals(str2));  \\2


    输出结果：

    str1==str2： false
    str1.equals(str2)： true

关于==和equals，我们需要知道java中的数据类型，可分为两类：


## 1.基本数据类型，也称原始数据类型。

byte,short,char,int,long,float,double,boolean 他们之间的比较，应用双等号（==）,比较的是他们的值。

## 2.复合数据类型(类) 

当他们用（==）进行比较的时候，比较的是他们在内存中的存放地址，所以，除非是同一个new出来的对象，他们的比较后的结果为true，否则比较后结果为false。 JAVA当中所有的类都是继承于Object这个基类的，在Object中的基类中定义了一个equals的方法，这个方法的初始行为是比较对象的内存地 址，但在一些类库当中这个方法被覆盖掉了，如String,Integer,Date在这些类当中equals有其自身的实现，而不再是比较类在堆内存中的存放地址了。
对于复合数据类型之间进行equals比较，在没有覆写equals方法的情况下，他们之间的比较还是基于他们在内存中的存放位置的地址值的，因为Object的equals方法也是用双等号（==）进行比较的，所以比较后的结果跟双等号（==）的结果相同。

因为string属于符合数据类型，所以应该是使用equals，假如我们使用==比较，肯定是比较它们的内存地址了，所以\\1 \\2 的结果显而易见了

要想判断两个对象是否相等，不能通过比较两个对象的引用是否相等，这是永远都得不到相等的结果的，因为两个对象的引用永远不会相等，所以正确的比较方法是直接比较这两个对象，比较这两个对象的实质是不是一样的，即这两个对象里面的内容是不是相同的，通过比较这两个对象的属性值是否相同而决定这两个对象是否相等。

Object类提供了一个equals()方法来比较两个对象的内容是否相同，因此我们可以采用这个方法去比较两个对象是否在逻辑上“相等”。如：c1.equals(c2);这里是调用从Object类继承下来的equals()方法，通过查阅API文档得到Object类里的equals方法的定义如下：

public boolean equals(Object obj)

注意，在重写equals方法时，需要按照以下几个规则设计：

1自反性 ：对任意引用值X，x.equals(x)的返回值一定为true.
2对称性： 对于任何引用值x,y,当且仅当y.equals(x)返回值为true时，x.equals(y)的返回值一定为true;
3传递性：如果x.equals(y)=true, y.equals(z)=true,则x.equals(z)=true
4一致性：如果参与比较的对象没任何改变，则对象比较的结果也不应该有任何改变
5非空性：任何非空的引用值X，x.equals(null)的返回值一定为false

 

 再看代码：

    String str2 = "hello";
    String str3 = "hello";
    System.out.println("str3==str2： " + (str3==str2));  \\3
    System.out.println("str3.equals(str2)： " + str3.equals(str2));  \\4


    输出结果：

    str3==str2： true
    str3.equals(str2)： true
 

这里的又为什么都是输出true呢，因为它们都是从缓冲池取出来的，由于string类比较特殊，jdk专门做了缓存优化。

 

　　原来Java运行时会维护一个String Pool（String池）。String池用来存放运行时中产生的各种字符串，并且池中的字符串的内容不重复。而一般对象不存在这个缓冲池，并且创建的对象仅仅存在于方法的堆栈区。
也就是说需要看string创建的方式：

 

1 当使用任何方式来创建一个字符串对象s时，Java运行时（运行中JVM）会拿着这个X在String池中找是否存在内容相同的字符串对象，如果不存在，则在池中创建一个字符串s，否则，不在池中添加。
2 Java中，只要使用new关键字来创建对象，则一定会（在堆区或栈区）创建一个新的对象。
3 使用直接指定或者使用纯字符串串联来创建String对象，则仅仅会检查维护String池中的字符串，池中没有就在池中创建一个，有则罢了！但绝不会在堆栈区再去创建该String对象。
4 使用包含变量的表达式来创建String对象，则不仅会检查维护String池，而且还会在堆栈区创建一个String对象。

　　另外，String的intern()方法是一个本地方法，定义为public native String intern(); intern()方法的价值在于让开发者能将注意力集中到String池上。当调用 intern 方法时，如果池已经包含一个等于此 String 对象的字符串（该对象由 equals(Object) 方法确定），则返回池中的字符串。否则，将此 String 对象添加到池中，并且返回此 String 对象的引用。
