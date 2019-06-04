<h1 align="center">java可变参数实例分析</h1>

Java方法中的可变参数类型是一个非常重要的概念，有着非常广泛的应用。本文就以实例形式对此加以分析。具体如下：

一般来说，许多Java初学者在看到下面的这段代码的时候，都会问一个问题：dealArray方法里那三个小点点是什么啊？

    public class TestVarArgus { 
      public static void dealArray(int... intArray){ 

      } 

      public static void main(String args[]){ 

      } 
    } 
这就是本文所要讨论的问题：可变的参数类型，也称为不定参数类型。英文缩写是varargus，还原一下就是variable argument type。通过它的名字可以很直接地看出来，这个方法在接收参数的时候，个数是不定的。那么好，现在就先来调用下这个方法。请看代码和输出：


    public class TestVarArgus { 
      public static void dealArray(int... intArray){ 
        for (int i : intArray) 
          System.out.print(i +" "); 

        System.out.println(); 
      } 

      public static void main(String args[]){ 
        dealArray(); 
        dealArray(1); 
        dealArray(1, 2, 3); 
      } 
    } 
    输出：

    1   
    1 2 3  

通过main方法里的调用，可以看出来这个可变参数既可以是没有参数（空参数），也可以是不定长的。看到这里估计都能明白，这个不定长的参数其实和数组参数挺像的。事实上，也确实是这么回事儿。编译器会在悄悄地把这最后一个形参转化为一个数组形参，并在编译出的class文件里作上一个记号，表明这是个实参个数可变的方法。请看代码：

    dealArray(); //dealArray(int[] intArray{}); 
    dealArray(1); //dealArray(int[] intArray{1}); 
    dealArray(1, 2, 3); //dealArray(int[] intArray{1, 2, 3}); 
说到这里，那么可以来验证一下，看看是不是这个可变参数就是数组类参数？看代码：

    public class TestVarArgus { 
      public static void dealArray(int... intArray){ 
        for (int i : intArray) 
          System.out.print(i +" "); 

        System.out.println(); 
      } 

      public static void dealArray(int[] intArray){//会有Duplicate method dealArray(int[]) in type TestVarArgus的错误 
        for (int i : intArray) 
          System.out.print(i +" "); 

        System.out.println(); 
      } 

      public static void main(String args[]){ 
        dealArray();  
        dealArray(1); 
        dealArray(1, 2, 3); 
      } 
    } 
从上面这段代码可以看出，这两个方法是冲突的，是无法重载的。到这里，再来做一个有意思的实验：

代码1：

    public class TestVarArgus { 
      public static void dealArray(int... intArray){ 
        for (int i : intArray) 
          System.out.print(i +" "); 

        System.out.println(); 
      } 

      public static void main(String args[]){ 
        int[] intArray = {1, 2, 3}; 

        dealArray(intArray); //通过编译，正常运行 
      } 
    } 
代码2：

    public class TestVarArgus { 
      public static void dealArray(int[] intArray){ 
        for (int i : intArray) 
          System.out.print(i +" "); 

        System.out.println(); 
      } 

      public static void main(String args[]){ 
        dealArray(1, 2, 3); //编译错误 
      } 
    } 
从上面这两段代码可以看出来，可变参数是兼容数组类参数的，但是数组类参数却无法兼容可变参数。其实对于第二段代码而言，编译器并不知道什么可变不可变，在它看来，需要定义一个dealArray(int, int, int)类的方法。所以，自然就无法去匹配数组类参数的dealArray方法了。

既然Java方法接收可变参数，那么接下来我们再来看一下下面的代码：


    public class TestVarArgus { 
      public static void dealArray(int count, int... intArray){ 

      } 

      public static void dealArray(int... intArray, int count){//编译报错，可变参数类型应该作为参数列表的最后一项 

      } 

      public static void main(String args[]){ 

      } 
    } 
这段代码说明了，可变参数类型必须作为参数列表的最后一项，而不能放在定长参数的前面。估计你会想到一个词“优先级”。因为没有确切的说明，只是这样一种规定，这里可以借用“优先级”这个词来理解一下，请看下面的代码：


    public class TestVarArgus { 
      public static void dealArray(int... intArray){ 
        System.out.println("1"); 
      } 

      public static void dealArray(int count, int count2){ 
        System.out.println("2"); 
      } 

      public static void main(String args[]){ 
        dealArray(1, 2); 
      } 
    } 
代码贴出来估计都知道是输出2，而不是1。这里需要记住：能匹配定长的方法，那么优先匹配该方法。含有不定参数的那个重载方法是最后被选中的。

最后，大家都知道main方法的参数就是一个数组类型的，那么它其实也是可以改成不定参数类型。试一试吧，看看有没有编译错误。

相信本文所述对大家Java程序设计的学习有一定的借鉴价值。
