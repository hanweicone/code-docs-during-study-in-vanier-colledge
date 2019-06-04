# Java中的字符串驻留（String Interning）

1. 首先String不属于8种基本数据类型，String是一个对象。

因为对象的默认值是null，所以String的默认值也是null；但它又是一种特殊的对象，有其它对象没有的一些特性。

2. new String()和new String(“”)都是申明一个新的空字符串，是空串不是null；

3. String str=”kvill”； 
String str=new String (“kvill”);的区别：

在这里，我们不谈堆，也不谈栈，只先简单引入常量池这个简单的概念。

常量池(constant pool)指的是在编译期被确定，并被保存在已编译的.class文件中的一些数据。它包括了关于类、方法、接口等中的常量，也包括字符串常量。

看例1：

    String s0=”kvill”; 
    String s1=”kvill”; 
    String s2=”kv” + “ill”; 
    System.out.println( s0==s1 ); 
    System.out.println( s0==s2 ); 
    结果为：

    true 
    true 
首先，我们要知道Java会确保一个字符串常量只有一个拷贝。

因为例子中的s0和s1中的”kvill”都是字符串常量，它们在编译期就被确定了，所以s0==s1为true；而”kv”和”ill”也都是字 符 串常量，当一个字符串由多个字符串常量连接而成时，它自己肯定也是字符串常量，所以s2也同样在编译期就被解析为一个字符串常量，所以s2也是常量池中 ”kvill”的一个引用。

所以我们得出s0==s1==s2;

用new String() 创建的字符串不是常量，不能在编译期就确定，所以new String() 创建的字符串不放入常量池中，它们有自己的地址空间。

看例2：

      String s0=”kvill”; 
      String s1=new String(”kvill”); 
      String s2=”kv” + new String(“ill”); 
      System.out.println( s0==s1 ); 
      System.out.println( s0==s2 ); 
      System.out.println( s1==s2 ); 
      结果为：

      false 
      false 
      false 
例2中s0还是常量池中”kvill”的应用，s1因为无法在编译期确定，所以是运 行时创建的新对象”kvill”的引用，s2因为有后半部分new String(“ill”)所以也无法在编译期确定，所以也是一个新创建对象”kvill”的应用;明白了这些也就知道为何得出此结果了。

4. String.intern()：

再补充介绍一点：存在于.class文件中的常量池，在运行期被JVM装载，并且可以扩充。String的intern()方法就是扩充常量池的一 个 方法；当一个String实例str调用intern()方法时，Java查找常量池中是否有相同Unicode的字符串常量，如果有，则返回其的引用， 如果没有，则在常量池中增加一个Unicode等于str的字符串并返回它的引用；看例3就清楚了

例3：

    String s0= “kvill”; 
    String s1=new String(”kvill”); 
    String s2=new String(“kvill”); 
    System.out.println( s0==s1 ); 
    System.out.println( “**********” ); 
    s1.intern(); 
    s2=s2.intern(); //把常量池中“kvill”的引用赋给s2 
    System.out.println( s0==s1); 
    System.out.println( s0==s1.intern() ); 
    System.out.println( s0==s2 ); 
    结果为：

    false 
    ********** 
    false //虽然执行了s1.intern(),但它的返回值没有赋给s1 
    true //说明s1.intern()返回的是常量池中”kvill”的引用 
    true 
最后我再破除一个错误的理解：

有人说，“使用String.intern()方法则可以将一个String类的保存到一个全局String表中，如果具有相同值的Unicode 字 符串已经在这个表中，那么该方法返回表中已有字符串的地址，如果在表中没有相同值的字符串，则将自己的地址注册到表中“如果我把他说的这个全局的 String表理解为常量池的话，他的最后一句话，“如果在表中没有相同值的字符串，则将自己的地址注册到表中”是错的：

看例4：

    String s1=new String("kvill"); 
    String s2=s1.intern(); 
    System.out.println( s1==s1.intern() ); 
    System.out.println( s1+" "+s2 ); 
    System.out.println( s2==s1.intern() ); 
    结果：

    false 
    kvill kvill 
    true 
在这个类中我们没有声名一个”kvill”常量，所以常量池中一开始是没有”kvill”的，当我们调用s1.intern()后就在常量池中新添加 了一个”kvill”常量，原来的不在常量池中的”kvill”仍然存在，也就不是“将自己的地址注册到常量池中”了。

s1==s1.intern()为false说明原来的“kvill”仍然存在；

s2现在为常量池中“kvill”的地址，所以有s2==s1.intern()为true。

5. 关于equals()和==:

这个对于String简单来说就是比较两字符串的Unicode序列是否相当，如果相等返回true;而==是比较两字符串的地址是否相同，也就是是否是同一个字符串的引用。

6. 关于String是不可变的

这一说又要说很多，大家只要知道String的实例一旦生成就不会再改变了，比如说：String str=”kv”+”ill”+” “+”ans”; 
就 是有4个字符串常量，首先”kv”和”ill”生成了”kvill”存在内存中，然后”kvill”又和” “ 生成 ”kvill “存在内存中，最后又和生成了”kvill ans”;并把这个字符串的地址赋给了str,就是因为String的“不可变”产生了很多临时变量，这也就是为什么建议用StringBuffer的原 因了，因为StringBuffer是可改变的

 
总结出来其意思如下：
如果：s.intern()方法的时候，会将共享池中的字符串与外部的字符串(s)进行比较,如果共享池中有与之相等 的字符串，则不会将外部的字符串放到共享池中的，返回的只是共享池中的字符串，如果不同则将外部字符串放入共享池中，并返回其字符串的句柄（引用）-- 这样做的好处就是能够节约空间

最后看看这方面的一个很好的例子

在例子之前我们先假设我们在sqlserver2000里面有Test数据库，里面有表如下：
test1
name 
我们通过下面程序向里面添加8000条记录：

```java
import java.sql.*;

public class TestDB {

 private static String driverName = "com.microsoft.jdbc.sqlserver.SQLServerDriver";

 private static String dbURL =

"jdbc:microsoft:sqlserver://localhost:1433;DatabaseName=TEST";

 private static String userName = "sa";

 private static String userPwd = "";

 private static Connection dbConn;

 public static void main(String[] args) {

  try {
   Class.forName(driverName);
   dbConn = DriverManager.getConnection(dbURL, userName, userPwd);
   Statement stmt = dbConn.createStatement();
   String sql = "insert into test1 values('123456789123456789123456789');";
   for (int i = 0; i < 8000; i++) {
    stmt.executeUpdate(sql);
   }
   System.out.println("Connection Successful!");
  } catch (Exception e) {
   e.printStackTrace();
  }
 }
}
```
添加完成以后我们在查询分析器里面执行：
select count(*) from test1;
可以看到结果：8000  表明8000条数据插入正确

假设我们有这样一个类：Po.java

```java
public class Po {
 private String name;

 public void setName(String s) {
  name = s;
 }

}
```
我们执行下面的类：TestStringIntern.java

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class TestStringIntern {
 private static String driverName = "com.microsoft.jdbc.sqlserver.SQLServerDriver";

 private static String dbURL =

"jdbc:microsoft:sqlserver://localhost:1433;DatabaseName=TEST";

 private static String userName = "sa";

 private static String userPwd = "";

 private static Connection dbConn;

 private static List<Po> list= new ArrayList<Po>();
 public static void main(String[] args) {

  try {
   Class.forName(driverName);
   dbConn = DriverManager.getConnection(dbURL, userName, userPwd);
   Statement stmt = dbConn.createStatement();
   ResultSet rs = stmt.executeQuery("select name from test1");
   while(rs.next()){
    String s = rs.getString(1);;
    Po p = new Po();
    p.setName(s);
    list.add(p);
    s = null;
    p = null;
   }
   long total = Runtime.getRuntime().totalMemory();
   long free = Runtime.getRuntime().freeMemory();
   System.out.println("The busy memory is: " + (total - free));
   rs.close();
   stmt.close();
   dbConn.close();
   System.gc();
  } catch (Exception e) {
   e.printStackTrace();
  }
 }
}
```
我们可以看到执行的结果为：The busy memory is: 1252880
注意：如果把p.setName(s)这句换成p.setName(s.intern());
再执行该程序我们可以看到结果：The busy memory is: 515944
我们可以到经过细微的改变我们可以看到其占用的内存不是一个数量级的
那么这个intern()函数做了什么呢？
在 String对象维持的一个私有池里面存放的字符串“xxxx”只有一个，因为每次比对都是一样，所 以是不会将这样的对象重复放到池里面的，所以调用intern()方法就是完成的这个功能，其返回的只是里面的同一个字符串，而没有创建新的字符串，所以 不会占用太多的空间

注：以上很多只是个人理解，具体实现细节不太清楚，所以难免会有错的地方，希望指出。
