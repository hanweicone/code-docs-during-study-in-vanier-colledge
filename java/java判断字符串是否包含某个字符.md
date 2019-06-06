# java判断字符串是否包含某个字符
 
## 判断一个字符串是否包含某个子串的n种方法

* startsWith()
* contains方法
* indexOf方法
## startsWith()
这个方法有两个变体并测试如果一个字符串开头的指定索引指定的前缀或在默认情况下从字符串开始位置

此方法定义的语法如下:

    public boolean startsWith(String prefix, int toffset)
or
    public boolean startsWith(String prefix)
这里是参数的细节:

prefix – 要匹配的前缀。
toffset – 从哪里开始寻找字符串。
返回值为true和false

```java
import java.io.*;

public class Test{
   public static void main(String args[]){
      String Str = new String("Welcome to Yiibai.com");

      System.out.print("Return Value :" );
      System.out.println(Str.startsWith("Welcome") );

      System.out.print("Return Value :" );
      System.out.println(Str.startsWith("Tutorials") );

      System.out.print("Return Value :" );
      System.out.println(Str.startsWith("Yiibai", 11) );
   }
}
```
## contains方法

java.lang.String.contains() 方法返回true，当且仅当此字符串包含指定的char值序列

返回值为true和false

```java
public static void main(String[] args) {



        String str = "abc";



        boolean status = str.contains("a");



        if(status){



            System.out.println("包含");



        }else{



            System.out.println("不包含");



        }



    }
```
## indexOf方法
java.lang.String.indexOf() 的用途是在一个字符串中寻找一个字的位置，同时也可以判断一个字符串中是否包含某个字符

indexOf的返回值为int

```java
public static void main(String[] args) {
    String str1 = "abcdefg";
    int result1 = str1.indexOf("ab");
    if(result1 != -1){
        System.out.println("字符串str中包含子串“ab”"+result1);
    }else{
        System.out.println("字符串str中不包含子串“ab”"+result1);
    }
    
}
```
