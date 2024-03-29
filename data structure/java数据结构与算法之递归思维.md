<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-1 float-left">原</span>

# java数据结构与算法之递归思维(让我们更通俗地理解递归)

</div>

<div class="article-info-box">

<div class="article-bar-top" style="height: 26px;"><span class="time">2016年12月12日 11:50:26</span> [zejian_](https://me.csdn.net/javazejian) <span class="read-count">阅读数 18075</span> <span class="tags-box artic-tag-box"><span class="label">标签：</span> [java](https://so.csdn.net/so/search/s.do?q=java&t=blog) [数据结构](https://so.csdn.net/so/search/s.do?q=数据结构&t=blog) [汉诺塔](https://so.csdn.net/so/search/s.do?q=汉诺塔&t=blog) [斐波那契](https://so.csdn.net/so/search/s.do?q=斐波那契&t=blog) [递归](https://so.csdn.net/so/search/s.do?q=递归&t=blog) <span class="article_info_click">更多</span></span>

<div class="tags-box space"><span class="label">个人分类：</span> [java数据结构与算法](https://blog.csdn.net/javazejian/article/category/6505437)</div>

</div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">

<div class="article-copyright">版权声明：本文为博主原创文章，请尊重原创，未经博主允许禁止转载，保留追究权 https://blog.csdn.net/javazejian/article/details/53452971</div>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-cd6c485e8b.css">

<div id="content_views" class="markdown_views">

> <font size="4" color="#D90E0E">【版权申明】未经博主同意，不允许转载！（请尊重原创，博主保留追究权）  
> [http://blog.csdn.net/javazejian/article/details/53452971](http://blog.csdn.net/javazejian/article/details/53452971)  
> 出自[【zejian的博客】](http://blog.csdn.net/javazejian)</font>

<font size="4">关联文章:</font>

[java数据结构与算法之顺序表与链表设计与实现分析](http://blog.csdn.net/javazejian/article/details/52953190)  
[java数据结构与算法之双链表设计与实现](http://blog.csdn.net/javazejian/article/details/53047590)  
[java数据结构与算法之改良顺序表与双链表类似ArrayList和LinkedList（带Iterator迭代器与fast-fail机制）](http://blog.csdn.net/javazejian/article/details/53073995)  
[java数据结构与算法之栈（Stack）设计与实现](http://blog.csdn.net/javazejian/article/details/53362993)  
[java数据结构与算法之队列(Queue)设计与实现](http://blog.csdn.net/javazejian/article/details/53375004)  
[java数据结构与算法之递归思维(让我们更通俗地理解递归)](http://blog.csdn.net/javazejian/article/details/53452971)  
[java数据结构与算法之树基本概念及二叉树（BinaryTree）的设计与实现](http://blog.csdn.net/javazejian/article/details/53727333)  
[java数据结构与算法之平衡二叉查找树(AVL树)的设计与实现](http://blog.csdn.net/javazejian/article/details/53892797)

  本篇是数据结构与算法的第6篇，从这篇种我们将深入了解递归算法，这可能是一篇分水岭的博文，因为只有在理解递归的基础上，我们才可能更轻松地学习树的数据结构，实际上数据结构系列书籍中递归并没有讲得特别通俗易懂，博主目前看过的书籍中分析递归最好的是日本人吉城浩写的《程序员的数学》，因此本篇会结合个人对递归的理解以及该书中的两个博主认为比较合适例子来分析，本篇可能不会涉及太多的代码，相反的，更希望呈现给大家一种通俗易懂的思维方式，重在理解，毕竟理解得越多，需要记忆自然也就越少了，以下是主要知识点

<div class="toc">

<div class="toc">

*   [汉诺塔的问题](#汉诺塔的问题)
*   [递归的思维方式](#递归的思维方式)
*   [汉诺塔的递归算法程序实现](#汉诺塔的递归算法程序实现)
*   [递归的定义](#递归的定义)
*   [斐波那契数列中的递归思想](#斐波那契数列中的递归思想)
*   [斐波那契数列的递归程序实现](#斐波那契数列的递归程序实现)
*   [递归算法的效率问题](#递归算法的效率问题)

</div>

</div>

# <a name="t0"></a><font color="#D90E0E">汉诺塔的问题</font>

  现在我们先不需要知道递归是什么，也没必要，我们先来看一个非常经典的游戏—汉诺塔，该游戏是数学家爱德华卢卡斯于1883年发明的，游戏的规则如下，有三根细柱（A、B、C），A柱上套着6个圆盘，圆盘的大小都不一样，它们按照从大到小的顺序自下而上地摆放，现在我们需要把A柱上的圆盘全部移动到B柱上去，并且在移动时有如下约定：

*   一次只能移动柱子最上端的一个圆盘。
*   小圆盘上不能放大圆盘

此时约定将一个圆盘从一根柱子移动另一根柱子算移动“1”次，那么将6个圆盘全部从A移动到B至少需要移动多少次呢？模型如下图：  
![](https://img-blog.csdn.net/20161210103510175?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
  图虽然很清晰，但我们依然无法立即找到特别清晰的解法，既然如此，我们就尝试先把问题的规模缩小点，把6个圆盘改为3个圆盘，先找出3层汉诺塔的解法，模型变为下图:  
![](https://img-blog.csdn.net/20161210154208276?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
  3层汉诺塔的解法就相对来说简单多了，我们要把3个圆盘全部从A移动到B，只需要先将最小的圆盘从A移动到B，然后将次小的圆盘从A移动到C，接着再把最小的圆盘从B移动到C，然后把最大的圆盘从A移动到B，接着把最小盘从C移动到A，在把次小盘从C移动到B，最后把最小盘从A移动到B即可，这样我们就完成了3此汉诺塔的解法了。这里我们把3个圆盘从小到大分别设为a,b,c，那么其移动过程如下：

    /**
       元素   过程   
        a    A->B   
        b    A->C   
        a    B->C   
        c    A->B   
        a    C->A   
        b    C->B   
        a    A->B
        移动7次完结..
     **/

整个过程如下图所示：  
![汉诺塔](https://img-blog.csdn.net/20161210164705998?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  从上图中，我们很容易理解3层汉诺塔的解法，但是细想一下会发现这7次动中我们好像在做重复的事情：移动圆盘，只不过方向时而不同罢了。重新回顾一下①②③④⑤⑥⑦的移动过程，然后把它们分为如下3种情况：

*   在①②③中，移动了3次将2个圆盘从A柱移动到了C柱
*   在④中，将最大的圆盘从A柱移动到了B柱
*   在⑤⑥⑦中，移动了3次将2个圆盘从C柱移动到了B柱

  我们发现这个过程移动的操作是几乎一样的，只不过是移动的方向不同了，A->C和C->B两种，其过程如下图：  
![3层汉诺塔解法](https://img-blog.csdn.net/20161211122622873?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  从图确实可以看出虽然两次移动的目的地不相同，但是两次移动的操作却是非常相似的，而且我们发现如果把3次移动看成是“移动2个圆盘”的操作就是“2层汉诺塔的解法”，也就是说在解决3层汉诺塔的过程中，我们使用了“2层汉诺塔的解法“。既然如此，那是不是意味着解决”4层汉诺塔“的过程中可以使用解决”3层汉诺塔的解法“呢？嗯，确实是如此的，这就是汉诺塔的解法规律，没错，我们已经发现这种规律！这样的话，我们解决前面的6层汉诺塔的问题时，只需要先解决5层汉诺塔的问题，然后利用5层汉诺塔的解法来解决6层汉诺塔的问题即可！我们来看看利用5层汉诺塔解出6层汉诺塔的过程，如下：  
![](https://img-blog.csdn.net/20161211160052027?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  从图中我们可以看出（a）和（c）就是5层汉诺塔的解法，为了解出6层汉诺塔需要使用到5层汉诺塔的解法，因此只要5层汉诺塔被解出，6层汉诺塔也就迎刃而解了。而5层汉诺塔的解法呢？没错利用我们前面发现的规律，用4层汉诺塔的解法去解出5层汉诺塔，如下过程：

*   ①.先将4个圆盘从A柱移动到C柱，即解出4层汉诺塔
*   ②.然后再将最大的圆盘(5个中最大的圆盘)从A柱移动到B柱
*   ③.最后将4个圆盘从C柱移动到B柱，即再次利用解出的4层汉诺塔

这样5层汉诺塔就被解出了，而4层汉诺塔则可以利用同样的解法即使用3层汉诺塔的解法，3层汉诺塔再利用2层汉诺塔的解法……..依次类推即可，到此便已解出6层汉诺塔，实际上我们知道有了6层汉诺塔的解法自然就可以很轻松地解出7层汉诺塔，8层汉诺塔…….N层汉诺塔，也很容易发现这种利用已知的N-1层的解法来解决N层的问题的解题方式，它们每一层的解法结构都是相同即利用前一个已解决的问题结果来解决后一个问题。通过这种思考的方式，我们来总结一下N层汉诺塔的解法，不再使用具体的ABC三根柱子，而是将它们设为x、y、z。这样的话，x、y、z在不同的情况下会不固定对应ABC中的某一根。这里以x为起点柱，y为目标柱，z为中转柱，然后给出解出N层汉诺塔的过程。利用z柱将n个圆盘从x柱转移到y柱的解法如下：

    Blog :http://blog.csdn.net/javazejian[原文地址]
    /**
    当 n=0时，无需任何移动
    当 n>0时，
        ①将n-1个圆盘从x柱，经y柱中转，移动到z柱(即解出n-1层汉诺塔)
        ②然后将1个圆盘从x柱移动到y柱(最大的圆盘)
        ③最后将n-1个圆盘从z柱，经x中转移动到y柱(即解出n-1层汉诺塔) 
    **/

  从上述过程可知为了解出n层汉诺塔，我们同样需要先解出n-1层汉诺塔，为更通用地表示解出n层汉诺塔的移动次数，将其设为H(n)。利用上述步骤，则有如下关系：  
![](https://img-blog.csdn.net/20161212091951958?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
  在数学上我们将这种H(n)和H(n-1)的关系式取了个名称，叫做递推公式，即已知H(0),由H(n-1)构成H(n)的方法也必然是已知的，只要依次计算便可以得出，如6层汉诺塔的递推过程如下：

    Blog :http://blog.csdn.net/javazejian[原文地址]
    /**
        H(0)=0                     = 1-1
        H(1)=H(0)+1+H(0) = 1       = 2-1
        H(2)=H(1)+1+H(1) = 3       = 4-1
        H(3)=H(2)+1+H(2) = 7       = 8-1
        H(4)=H(3)+1+H(3) = 15      = 16-1
        H(5)=H(4)+1+H(4) = 31      = 32-1
        H(6)=H(5)+1+H(5) = 63      = 64-1
        .......                    = .........
        H(n)=H(n-1)+1+H(n-1)       = 2^n -1
    **/

  这样我们也就知道了6层次汉诺塔的最少移动次数为63次（关于2^n-1的公式只是总结出更为简单的计算方式摆了）。到此我们来重新梳理一下汉诺塔的整个解题过程，在解出6层汉诺塔前，我们由于一时找不到解决的方法，因此先尝试解出更为简单3层汉诺塔的，而在这个过程中，我们慢慢发现了解决汉诺塔问题的通用规律，即使用n-1层的解法来解决n层汉诺塔的思考方式,通过这种思考方式最终成功地解决了6层汉诺塔的问题。而实际上我们利用的这种思考方式的本质就是将复杂的问题转换为较为简单的同类问题(回忆一下汉诺塔的问题解法)然后再找出解决方法最终利用简单同类问题解出复杂问题的过程，而这种思维的方式就是递归！！是的，没错！递归不是算法而是一种思考的思维方式，只不过我们将这种递归思维方式采用程序来解决时，该程序被称为递归算法罢了，而递归本身是一种思考问题的思维方式！到此我们对递归是否有些焕然大悟的感觉呢？或对递归有些许的理解了吧？

# <a name="t1"></a><font color="#D90E0E">递归的思维方式</font>

  有了上述的分析，我们就可以这样去理解和使用递归，假设现在碰到了一个很复杂的难题，我们也明白‘简单问题易解’的道理，那么此时就可以利用类似于汉诺塔的解题的思考方式，即<font color="#D90E0E">判断能否将目前复杂的问题转换为较为简单的同类问题呢？</font>可以的话，就先转换为简单同类的问题来解决，然后再利用简单的同类问题解法来解决复杂的同类问题，这就恰恰就是递归思维方式的精髓所在，嗯，这就是递归！大家现在是不是已开始理解递归了呢？我们在回顾一下汉诺塔问题的解法，以便加深对递归的理解，如下图：

![](https://img-blog.csdn.net/20161211190832510?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  上图很清晰表现出n层汉诺塔的解法过程，通过复杂问题化为同类简单问题来求解，上述的图形还有一个名称叫做递归结构，根据该结构我们就可以建立起之前H(n)递推公式了，很显然发现递归结构并建立递推公式的过程十分重要，这样有助于我们把握本质问题即通过n-1层汉诺塔的解法来解决n层汉诺塔的问题，这样的发现能力需要我们有比较敏锐的洞察力和思维能力，这就需要我们再遇到复杂问题时，多采用递归的思维（复杂问题简单化）方式去思考，去挖掘规律。ok~，到此相信我们对递归已有比较清晰的了解了吧。接下来我们看看如何使用程序来实现递归算法并解决汉诺塔的问题。

# <a name="t2"></a><font color="#D90E0E">汉诺塔的递归算法程序实现</font>

  通过前面的分析，我们明白所谓的递归不过就是把复杂问题简单化的思维方式，而这种思维方式从程序语言的角度出发则称为递归算法，它通过程序的函数方法直接或者间接调用函数自身的过程，回忆一下前面分析汉诺塔的递推公式：H(n)=H(n-1)+1+H(n+1)

我们通过程序的递归算法实现汉诺塔如下：

    package com.zejian.structures.recursion;

    /**
    * Created by zejian on 2016/12/11.
    * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
    * 汉诺塔的递归算法实现
    */
    public class HanoiRecursion {

     /**
      * @param n 汉诺塔的层数
      * @param x x柱 起点柱(A)
      * @param y y柱 目标柱(B)
      * @param z z柱 中转柱(C)
      * 其中 A B C 只是作为辅助思考
      */
     public void hanoi(int n, char x ,char y ,char z){

         //H(0)=0
         if (n==0){
             //什么也不做
         }else {
             //递推公式：H(n)=H(n-1) + 1 + H(n-1)
             //将n-1个圆盘从x移动到z,y为中转柱
             hanoi(n-1,x,z,y); //----------------------->解出n-1层汉诺塔:H(n-1)

             //移动最大圆盘到目的柱
             System.out.println(x+"->"+y);//------------> 1

             //将n-1个圆盘从z移动到y,x为中转柱
             hanoi(n-1,z,y,x);//------------------------>解出n-1层汉诺塔:H(n-1)
         }

     }

     /**
      * @param n 汉诺塔的层数
      * @param x x柱 起点柱(A)
      * @param y y柱 目标柱(B)
      * @param z z柱 中转柱(C)
      * 其中 A B C 只是作为辅助思考
      */
     public int hanoiCount(int n, char x ,char y ,char z){
         int moveCount=0;
         //H(0)=0
         if (n==0){
             //什么也不做
             return 0;
         }else {
             //递推公式：H(n)=H(n-1) + 1 + H(n-1)
             //将n-1个圆盘从x移动到z,y为中转柱
             moveCount += hanoiCount(n-1,x,z,y); //------------->解出n-1层汉诺塔:H(n-1)

             //移动最大圆盘到目的柱
             moveCount += 1; //---------------------------------> 1

             //将n-1个圆盘从z移动到y,x为中转柱
             moveCount +=hanoiCount(n-1,z,y,x);//--------------->解出n-1层汉诺塔:H(n-1)
         }

         return moveCount;
     }
     //测试
     public static void main(String[] args){
         HanoiRecursion hanoi=new HanoiRecursion();
         System.out.println("moveCount="+hanoi.hanoiCount(6,'A','B','C'));

         hanoi.hanoi(3,'A','B','C');
     }

    }

从代码可以发现递归算法的踪影：

    /**
    *Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
    */
    public void hanoi(int n, char x ,char y ,char z){

       //H(0)=0
       if (n==0){
           //什么也不做
       }else {
           //调用自身函数hanoi()
           hanoi(n-1,x,z,y);
           //移动最大圆盘到目的柱
           System.out.println(x+"->"+y);
           //调用自身函数hanoi()
           hanoi(n-1,z,y,x);
       }
    }

  因此到此我们也就明白了，递归思维在程序中的体现即为递归算法，而递归算法本身在程序内部的实现就是函数调用自身函数，这样大家总该理解递归算法了吧。这里有点要提醒大家的是，不要陷入程序递归的内部去思考递归算法，记住要从递归思维的本质(复杂问题简单化)出发去理解递归算法，千万不要去通过试图解析程序执行的每一个步骤来理解递归（解析程序的执行是指给函数一个真实值，然后自己一步步去推出结果，这样的思考方式是错误的！），那样只会让自己得到伪理解(没有真正理解)的结果。记住！递归并不是算法，是一种复杂问题简单化的思维方式，而这种思维方式在程序中的体现就递归算法！递归算法在实现上就是函数不断调用自身的过程！

# <a name="t3"></a><font color="#D90E0E">递归的定义</font>

  通过前面大篇幅的分析，到此我们总算是理解递归了，那么接下来我们给出递归的正式定义，相信有了上述基础，理解递归的正式定义还是比较轻松的，递归其实是数学中一种重要的概念定义方式，而递归算法则是针对程序设计而言的，即不同角度的两种称呼但本质是一样的。  
递归的定义(从数学的角度)：用一个概念的本身直接定义自己。如阶乘函数F(n)=n!可以定义为：  
![](https://img-blog.csdn.net/20161211210225754?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

关于阶乘这里简单说明一下

    阶乘是什么？
    1 x 2 x 3 x 4 x 5 = 5!
    这里的5!就称为5的阶乘，之所以称为阶乘是因为乘数呈阶梯状递减而得名，如下：
    5! = 5 x 4 x 3 x 2 x 1 = 120
    4! = 4 x 3 x 2 x 1 = 24
    3! = 3 x 2 x 1 = 6
    2! = 2 x 1 = 2
    1! = 1 = 1
    0! = 1
    注意0的阶乘0！被定义为1，这是数学里的规定。
    n的阶乘如下：
    n!= n x (n-1) x (n-2) x … x 2 x 1
    很显然n!是一种递推公式，也符合递归思维，因此有：
    当n=0时，n! = 1 ;
    当n>=1时，n x (n-1)!
    可以发现它使用了阶乘(n-1)!来定义阶乘n!，是不是跟汉诺塔很相似？没错，确实是递归思维的体现。
    ok~，关于阶乘我们就简单了解这些。

  递归算法的定义(从程序的角度)：任何调用自身函数的过程都可以称为递归算法(前面实现的汉诺塔程序就是一个很好的例子)。这里需要注意的是递归必须满足以下两个条件：

*   ①边界条件：至少有一条初始定义是非递归的，如汉诺塔的H(0)=0，阶乘的0!=1。
*   ②递归通式：由已知函数值逐步计算出未知函数值，如汉诺塔的H(0)=0，可以推算出H(1)=H(0)+1+H(0)。

边界条件和递推通式是递归定义的两个基本要素，缺一不可，并且递归通式必须在有限次数内运算完成达到边界条件以保证能够正常结束递归，得到运算结果。好~，以上便是递归的定义，还是那句话理解好递归思维(复杂问题简单化)才是重点！

# <a name="t4"></a><font color="#D90E0E">斐波那契数列中的递归思想</font>

  如果上述的分析都明白了，那就说明你已掌握了递归，但为了加深对递归的理解，我们再来看一个思考题（来自程序员的数学思考题），题目是这样的，假如动物中有一种特殊的种类，它出生2天后就开始以每天1只的速度繁殖后代。假设第1天，有1只这样的动物（该动物刚出生，从第3天开始繁殖后代）。那么到第11天，共有多少只呢？

    我们先来按一般顺序思考，先不要考虑第11天，先从第1天开始，看能不能找出规律：
    【第1天】只有1只动物
    【第2天】只有1只动物，还没有繁殖后代，总量为1
    【第3天】第1天的1只动物，繁殖1个后代，总量为2
    【第4天】第1天的1只动物又繁殖1只，其他还没繁殖，总量为3
    【第5天】第1天和第3天出生的动物又繁殖1个后代，其他没有繁殖，总量为5
    【第n天】.....

     第1天 ------1
     第2天 ------1
     第3天 ------2 = 1 + 1
     第4天 ------3 = 1 + 2
     第5天 ------5 = 2 + 3 
     第6天 ------8 = 3 + 5
     第7天 ------13 = 5 + 8

   这个过程中貌似没发现什么规律，但我们发现从第3天开始动物的数量似乎前两天的总和，也就是第3天，是第1天的动物数量加上第2天的动物数量，而第4天则是第2天和第3天的动物数量的和。这样的话我们可以归纳一下，不去直接想”第n天有多少只动物“而是如下思考：

*   第n-1天出生的动物，在第n天还存活着。
*   第n-2天以前出生的动物，在第n天繁殖了后代

  因此可以总结出递推公式，假设在第n天时，第n-1天以前繁殖的动物都活着，并且第n-2天以前出生的动物会繁殖1个后代，设第n天的动物总数为F(n)，则有：F(n)=F(n-1)+F(n-2) 其中 n>=3，如下图所示  
![](https://img-blog.csdn.net/20161211215025928?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
注意为了让F(2)=F(1)+F(0)成立，定义F(0)=0,而F(1)则依然为1，因此有如下公式：  
![](https://img-blog.csdn.net/20161211215456649?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
我们来验证这个递推公式是否符合递归条件

*   ①边界条件：至少有一条初始定义是非递归的，F(0)=0;F(1)=1。
*   ②递归通式：由已知函数值逐步计算出未知函数值，F(0)=0;F(1)=1,可以推算出F(2)=1,最终也可以推算F(n)的结束。

显然两个条件都符合，说明该通用公式可以在有限的次数内运算完成并达到边界条件得出结果，因此我们可以利用递推公式求出第11天的动物的数量：

    F(0)=0
    F(1)=1
    F(2)=F(0)+F(1)=1
    F(3)=F(2)+F(1)=2
    F(4)=F(3)+F(2)=3
    F(5)=F(4)+F(3)=5
    F(6)=F(5)+F(4)=8
    F(7)=F(6)+F(5)=13
    F(8)=F(7)+F(6)=21
    F(9)=F(8)+F(7)=34
    F(10)=F(9)+F(8)=55
    F(11)=F(10)+F(9)=89

    也就是说第11天的动物总数为89只

在这个问题中出现的数列就是著名的斐波那契数列，是由数学家斐波那契发现的，由此得名斐波那契数列。

    0 ，1 ，1 ，2 ，3 ，5 ，8，13 ，21 ，34 ，55 ，89 ，…

  到此我们也就知道斐波那契数列同样是用递归定义的，前面我们将求解第n天的动物数量分解为求第n-1天和第n-2天以前的动物繁殖后代数量，从把复杂的问题分解为较为简单的同类问题，而不去纠结第n天到此有多少只动物的问题，最终发现求解的规律，并通过递推公式求得第n天的结果，这个过程再次体现了递归的思维方式。既然斐波那契数列是递归思维的产物，那么也可以通过程序的递归算法来求解，接下来我们就看看如何使用程序中的递归算法来实现斐波那契数列。

# <a name="t5"></a><font color="#D90E0E">斐波那契数列的递归程序实现</font>

实现代码比较简单就不过多分析了，代码如下：

    package com.zejian.structures.recursion;

    /**
     * Created by zejian on 2016/12/11.
     * Blog : http://blog.csdn.net/javazejian [原文地址,请尊重原创]
     * 斐波那契数列的实现
     */
    public class Fibonacci  {

        /**
         * 斐波那契数列的实现
         * 0,1,1,2,3,5,8,13,21......
         * @param day
         */
        public long fibonacci(int day){

            if(day==0){ //F(0)=0
                return 0;
            }else if (day==1||day==2){//F(1)=1
                return 1;
            }else {
               return fibonacci(day-1)+fibonacci(day-2); //F(n)=F(n-1)+F(n-2)
            }
        }

        /**
         * 更为简洁的写法
         * @param day
         * @return
         */
        public long fib(int day) {
            return day== 0 ? 0 : (day== 1 || day==2 ? 1 : fib(day - 1) + fib(day - 2));
        }

        //测试
        public static void main(String[] args){
            Fibonacci fibonacci=new Fibonacci();
            System.out.println("第11天动物数量为:"+ fibonacci.fib(11));
            System.out.println("第11天动物数量为:"+ fibonacci.fibonacci(11));
        }
    }

# <a name="t6"></a><font color="#D90E0E">递归算法的效率问题</font>

  到此我们已对递归分析完了，相信大家对递归已很熟悉了，通过递归的思维方式，在解决某些问题的时候确实使得我们思考的方式得以简化，同时代码也更加精炼，容易阅读。那么既然如此，那是不是什么问题都要用递归来解决呢？难道递归就没有缺点吗？下面我们就来讨论一下递归的不足之处也就是它的效率问题。我们这里以斐波那契数列的实现为例：

    /**
     * 更为简洁的写法
     * @param day
     * @return
     */
    public long fib(int day) {
           return day== 0 ? 0 : (day== 1 || day==2 ? 1 : fib(day - 1) + fib(day - 2));
     }

  这段代码相当精简直观清晰,但是！如果用这段代码计算fib(500)时，我们就泪奔了，它的运行时间也许会让人抓狂呐。我们以fib(5)为例，计算过程如下：  
![](https://img-blog.csdn.net/20161211234844810?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
  从上图可以看出，在计算Fib(5)的过程中，Fib(1)计算了两次、Fib(2)计算了3次，Fib(3)计算了两次，原本只需要5次计算就可以完成的任务却计算了9次。更重要的是这个问题随着规模的增加会愈发明显，以至于Fib(500)的计算时间已相当恐怖。造成这种困境的原因是，当调用fib(n-1)时，还要调用fib(n-2)，也就是说fib(n-2)调用了两次，同样的道理，调用f(n-2)时f(n-3)也调用了两次，而这些多余的调用是完全没有必要的，还可预见的是这种计算方式随着数量的增加，计算量将呈指数级增长，这是一个相当严重的问题。那么如何改良这个计算过程呢？我们重新回顾一下斐波那契数列：

    0 ，1 ，1 ，2 ，3 ，5 ，8，13 ，21 ，34 ，55 ，89 ，…

  为了减少函数重复调用提高效率，我们使用迭代的方式来实现斐波那契数列代码如下：

    //BigInteger可以防止数据异常
    //BigInteger 任意大的整数，原则上是，只要你的计算机的内存足够大，可以有无限位的
    // 递推实现方式（迭代的方式效率高，时间复杂度O(n)）
    public  BigInteger fibonacciN(int n){
       if (n == 1) {
           return new BigInteger("0");
       }
       //f(0)=0;
       BigInteger n1 = new BigInteger("0")；
       //f(1)=1;
       BigInteger n2 = new BigInteger("1")；
       //记录最终值f(n)
       BigInteger sn = new BigInteger("0");
       for (int i = 0; i < n - 1; i++) {
           sn = n1.add(n2);//相加
           n1 = n2;
           n2 = sn;
       }
       return sn;
    }

      // 与上述相同的递推实现方式 ，使用long返回值，当n过大会造成数据溢出，计算结果可能是一个未知的负数，因此建议使用BigInteger
    public static long fibonacciNormal(int n){
          if(n <= 2){
              return 1;
          }
          long n1 = 1, n2 = 1, sn = 0;
          for(int i = 0; i < n - 2; i ++){
              sn = n1 + n2;
              n1 = n2;
              n2 = sn;
          }
          return sn;
      }

  这样我们就把问题的规模降低到O(n)级别了，运行时间也很快，那为什么使用迭代就快，而使用递归就会变得慢呢？我们都知道，递归调用实际上是函数自己在调用自己，而函数的调用开销是很大的（包括空间和时间），而系统要为每次函数调用分配存储空间，提供给函数进行运行。而在函数调用结束后，则需要释放空间，即所谓的弹栈复点。因此函数调用消耗的空间和时间并不是非常乐观的。但难度就不用递归了么？并非如此，当我们在遇到同一个问题时，如果递归解决的（时间和空间）复杂度不明显优于其它解决方案时，此时就不应该使用递归，否则可以使用递归。其实博主想说的是递归虽然有缺点，但在很多复杂的问题上我们使用递归的形式来解释或者求解时问题确实很容易被解释的更清楚，而使用迭代是无法实现的或者难以理解的（如汉诺塔问题，树的遍历等等），此时递归巨大的优势就显示出来了。同时我们更应该记住在相同的问题面前，如果使用递归的效果与迭代的效果相差不了多少，我们更应该倾向于使用迭代，毕竟运行效率上迭代还是相当有优势的。  
  ok~，关于递归我们就聊到这里吧，相信已经很清晰了，记住重在理解，切勿陷入递归程序内部去思考！  
[github源码下载（含文章列表）](https://github.com/shinezejian/javaStructures)

</div>

<link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet"></div>

</article>

</div>
