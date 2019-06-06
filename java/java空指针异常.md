# java空指针异常：java.lang.NullPointException
## 一.什么是java空指针异常

我们都知道java是没有指针的，这里说的"java指针"指的就是java的引用,我们不在这里讨论叫指针究竟合不合适，而只是针对这个异常本身进行分析。空指针就是空引用，java空指针异常就是引用本身为空，却调用了方法，这个时候就会出现空指针异常。可以理解，成员变量和方法是属于对象的（除去静态），在对象中才存在相对应的成员变量和方法，然后通过对象去调用这些成员变量和方法。对于空指针来说，它不指向任何对象，也就没有所谓的成员变量和方法，这个时候用它去调用某些属性和方法，当然会出现空指针异常。

```java
 1 public class Test {
 2     private int a=1;
 3     private int b=2;
 4     public static void main(String[] args) {
 5         // TODO Auto-generated method stub
 6         Test t1 = new Test();
 7         Test t2 = null;
 8         System.out.println(t1.a);
 9         System.out.println(t2.a);
10         System.out.println(t2.c());
11     }
12     public String c(){
13         return "123";
14     }
15 }
```
我们分析上面这段示例代码，在Test类中，有两个成员变量a和b，和一个方法c()。然后在main()方法中，我们创建了两个对象t1和t2，其中t1指向通过构造方法实例出的Test对象，而t2只是声明，并指向了空，并没有指向实际的对象。调试的时候，第一条输出语句是可以通过编译的，而执行到第二条输出语句的时候，由于空指针调用了不属于它的a，程序终止，报告空指针异常。同样，注释第二条输出语句，程序在执行到第三条输出语句的时候，由于调用了不属于它的c()方法，会出现一样的错误。

 

## 二.如何解决

对于每一个java程序员来说，几乎都避免不了遇到空指针异常，特别是经验不足的初学者。而且由于它的调试和查找相对其它异常来说比较困难，常常需要花费很大的精力去解决它。

首先认识一下java中的null

null是Java中一个很重要的概念。null设计初衷是为了表示一些缺失的东西，例如缺失的用户、资源或其他东西。但是，一年后，令人头疼的空指针异常给Java程序员带来不少的骚扰。

null是java中的关键字，因此，它不能写成NULL，Null，只能是null。

null是所有引用类型的默认值，如果没有让一个引用指向一个实际存在的对象，它的默认值就是null。null本质上是一个值，这跟int的默认值是0，boolean的默认值是false一样。现在，我们通常都使用像eclipse等的集成开发环境进行开发，一般在定义变量的时候都会进行初始化（这也是写代码的一个良好的习惯），如果没有进行初始化，系统会进行提示。

报空指针异常的原因有以下几种： 

1字符串变量未初始化； 
2接口类型的对象没有用具体的类初始化，比如： 
List it；会报错 
List it = new ArrayList()；则不会报错了 
3当一个对象的值为空时，你没有判断为空的情况。你可以试着把下面的代码前加一行代码： 
if(rb!=null && rb!="") 
改成： 
if(rb==null); 
if(rb!==null&&rb!="") 或者if("").equals(rb)) 
空指针的解决办法： 
       重点关注报错发生的所在行，通过空指针异常产生的两条主要原因诊断具体的错误。同时为了避免空指针的发生，最好在做判断处理时将“null”或者空值放于 设定的值之前。 
常见空指针异常的简要分析： 
（1）空指针错误 
    Java中的8种基本数据类型，变量的值可以有其默认值，加入没有对其正常赋值，java虚拟机是不能 正确编译通过的，因此使用基本的Java数据类型一般是不会引起空指针异常的。实际开发中，大多数的空指针异常主要与对象的操作相关。 
    下面列出可能发生空指针异常的几种情况及相应解决方案： 
    代码段1： 
　　out.println(request.getParameter("username")); 
　　分析：代码段1的功能十分简单，就是输出用户输入"username"的值。 
       说明：看上去，上面的语句找不出什么语法错误，而且在大多数情况下也遇不到什么问题。但是，如果某个用户在输入数据时并没有提供表单 域"username" 的值，或通过某种途径绕过表单直接输入时，此request.getParameter("username")的值为空（注意不是空字符串，是空对象 null。），out对象的println方法是无法直接对空对象操作的，因此代码段1所在的JSP页面将会抛出 "Java.lang.NullPointerException"异常。而且即使对象可能为空时，也调用Java.lang.Object或 Object对象本身的一些方法如toString()， equal(Object obj)等操作。 
    代码段2： 
　　String userName = request.getParameter("username"); 
　　If (userName.equals("root")) 
　　{....} 
　　分析：代码段2的功能是检测用户提供的用户名，如果是用户名称为"root"的用户时，就执行一些特别的操作。                                                                        
      说明：在代码段2中，如果有用户没有提供表单域"username"的值时，字符串对象userName为null值，不能够将一个null的对象与另一 个对象直接比较，同样，代码段2所在的JSP页面就会抛空指针错误。 
     一个小技巧：如果要把某个方法的返回值与常量做比较，把常量放在前面，可以避免调用null对象的equals方法。譬如：  
    If ("root".equals(userName)) 
　 {....} 
    即使userName对象返回了null对象，这里也不会有空指针异常，可以照常运转。 
    代码段3： 
　　String userName = session.getAttribute("session.username").toString(); 
        分析：代码段3的功能是将session中session.username的值取出，并将该值赋给字符串对象userName。 
       说明：在一般情况下，如果在用户已经进行某个会话，则不会出现什么问题；但是，如果此时应用服务器重新启动，而用户还没有重新登录，（也可能是用户关闭浏 览器，但是仍打开原来的页面。）那么，此时该session的值就会失效，同时导致session中的session.username的值为空。对一个 为 null的对象的直接执行toString()操作，就会导致系统抛出空指针异常。 
    代码段4： 
public static void main(String args[]){ 
       Person p=null; 
       p.setName("张三")； 
       System.out.println(p.getName()); 
} 
分析：声明一个Person对象，并打印出该对象的中的Name名字。 
说明：这个时候你的p就出现空指针异常，因为你只是声明了这个Person类型的对象并没有创建对象，所以它的堆里面没有地址引用，切忌你要用对 象掉用方法的时候一定要创建对象。
