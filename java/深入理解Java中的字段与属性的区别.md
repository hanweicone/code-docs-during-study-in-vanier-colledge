深入理解Java中的字段与属性的区别

1、Java中的属性和字段有什么区别？ 
答：Java中的属性(property)，通常可以理解为get和set方法。
而字段(field)，通常叫做“类成员”，或 "类成员变量”，有时也叫“域”，理解为“数据成员”，用来承载数据的。

这两个概念是完全不同的。

2、属性和字段详解

 ◆◆字段（filed）
------------------------------------------------------------------------------------
类成员(字段)，通常是在类中定义的类成员变量，例如：
public class A{
    private String s = "123";
}
我们可以说A类中有一个成员变量叫做s，A类有一个字段s 。

字段一般用来承载数据，所以为了安全性，一般定义为私有的。

字段和常量描述了类的数据（域），当这些数据的某些部分不允许外界访问时，
根据 “对象封装” 的原则，应尽量避免将一个类型的字段以公有方式提供给外部。除了final修饰的常量。
一般将其设置为private类型。既然是私有，那外界怎么访问呢? 当然是通过Java的属性方法！

 ◆◆属性（property）
-------------------------------------------------------------------------
属性只局限于类中方法的声明，并不与类中其他成员相关，属于JavaBean的范畴。例如：
void setA(String s){}
String getA(){}
当一个类中拥有这样一对方法时，我们可以说，这个类中拥有一个可读写的a属性(注意是小写a)。如果去掉了set的方法，则是可读属性，反之亦然。

其规则是：去掉get或set后其剩余的字符串，
如果第二个字母是小写的，则把第一个字母也变成小写 
getAge---->age 
getCPU---->CPU 

比如有下面这个类: 
注：下面的User类不是JavaBean。


关于JavaBean、PO、DTO等概念的区别，请参考我的另外一篇博文《什么是JavaBean、Bean、POJO？》



public class User {
    private String id; //私有字段
    private String name; //私有字段
    private String identifier = "440282199008098076"; //私有字段
    public String getId() { //id的可读属性
        return id;
    }
    public void setId(String id) { //id的可写属性
        this.id = id;
    }
    public String getName() { //name的可读属性
        return name;
    }
    public void setName(String name) { //name的可写属性
        this.name = name;
    }
    public String getIdentifier() { //identifier只有一个get方法，所以它是只读属性         return identifier;
    }
    public final static Integer SHOW_STATUS_YES = 1; //公共字段
    public final static Integer SHOW_STATUS_No = 0; //公共字段
}

当我操作这个类时，比如调用getName()方法时，我们要说是获得name属性，调用setName(String name)方法时要说设置name属性，因为对我们来说name字段是私有的，我们操作该Person类时根本看不到有这个name字段 。
一个类主要包括字段、属性和方法。属性在此时指的就是get/set访问器。

同时我们可以看到，这个类有3个属性，5个字段。
SHOW_STATUS_YES 为公用字段，一般修饰为final static类型，可以通过User类直接访问该字段。 
getIdentifier为只读属性，只能读取私有的identifier字段，这样就起到了保护数据的安全性的作用。
id和name为私有字段，且有两个操作他们的public属性。可以通过getId()、setId(String id)、getName()、setName(String name)来读取和设置他们的值。

更形象的说就是：属性是对字段的封装，供外部访问。
通常属性将相应的私有字段通过封装成公共属性，以便于外界访问和修改。当然你在封装成属性时，也可以设置该属性为只读，可读写等等权限。

为了便于测试加上toString方法：


public class User {
   //其他代码同上...
   
    @Override
    public String toString() { //只有拥有属性的字段，才会被toString方法调用
        return "User [id=" + id + ", name=" + name + ", identifier=" + identifier + "]";
    }
}

测试类：


public class UserTest {
    public static void main(String[] args) {
        User user = new User();
        user.setId("100");
        user.setName("chunlynn");
        String identifier = user.getIdentifier();
        System.out.println("identifier==" + identifier);
        // 4402322BDFV323230001
        System.out.println(user);
        // User [id=100, name=chunlynn, identifier=4402322BDFV323230001]
        Integer status = User.SHOW_STATUS_YES; // public字段的访问
        System.out.println(status);
        // 1
    }
}

虽然在实际项目的开发过程中，公共字段和属性在合适的条件下都可以使用，但是我们应该尽可能的使用属性（property），而不是数据成员（field）；

把所有的字段都设置为私有字段，如果要暴露它们，则把它们封装成属性，这也是最佳实践推荐的方式。除了一些常量不能修改的字段，可以设置为public final static类型。

3、总结：

区别开属性与字段是为了更好的实现数据安全，比如当我们想给一个类的属性赋值或者其他类用到了，就需要将这个字段设置为public，然而这样可以对字段进行任意的读写操作，非常不利于数据安全。于是就加上了属性，简单说属性实现了字段的封装，属性有get、set 方法来控制字段，该字段的属性只有set方法没有get方法，就只可以对该方法进行赋值操作，没有读操作，反之亦然。就是对对字段的操作通过属性来控制。

可以创建属性，将字段和属性封装在一起。通过属性可以像访问字段一样访问数据成员，实现数据的封装，避免使用非法数据赋值，保证数据完整性，同时类内部发生修改时，避免整个程序的修改。

基于get,set方法的反射不会破坏对象数据，IDE可以通过约定做些智能提示。如果你自己用反射，你想做些通用处理，去遍历每个字段，没人跟你说哪个字段能写，那个能读，你没法处理嘛。

在我们项目中用到属性和字段的多半就是POJO、JavaBean、DTO、VO等等了。
标准的JavaBean：
JavaBean是一种特殊的类，主要用于传递数据信息，这种类中的方法主要用于访问私有的字段，且方法名符合某种命名规则。如果在两个模块之间传递信息，可以将信息封装进JavaBean中，这种对象称为“值对象”(Value Object)，或“VO”，有时也叫DTO（数据传输对象）。方法比较少。这些信息储存在类的私有变量中，通过set()、get()获得。

JavaBean在Java EE开发中，通常用于封装数据，对于遵循以上写法的JavaBean组件，其它程序可以通过反射技术实例化JavaBean对象（内省机制），并且通过反射那些遵循命名规范的方法，从而获知JavaBean的属性，进而调用其属性保存数据。




友情链接：
 什么是JavaBean、bean? 什么是POJO、PO、DTO、VO、BO ? 
--------------------- 
作者：chunlynn 
来源：CSDN 
原文：https://blog.csdn.net/chenchunlin526/article/details/71424844 
版权声明：本文为博主原创文章，转载请附上博文链接！
