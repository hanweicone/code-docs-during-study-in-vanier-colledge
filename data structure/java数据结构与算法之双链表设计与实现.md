<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-1 float-left">原</span>

# java数据结构与算法之双链表设计与实现

</div>

<div class="article-info-box">

<div class="article-bar-top"><span class="time">2016年11月06日 22:37:24</span> [zejian_](https://me.csdn.net/javazejian) <span class="read-count">阅读数 13096</span></div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">

<div class="article-copyright">版权声明：本文为博主原创文章，请尊重原创，未经博主允许禁止转载，保留追究权 https://blog.csdn.net/javazejian/article/details/53047590</div>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-cd6c485e8b.css">

<div id="content_views" class="markdown_views">

> <font size="4">转载请注明出处（万分感谢！）：  
> [http://blog.csdn.net/javazejian/article/details/53047590](http://blog.csdn.net/javazejian/article/details/53047590)  
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

  上一篇文章分析顺序表和单链表，本篇就接着上篇继续聊链表，在单链表分析中，我们可以知道每个结点只有一个指向后继结点的next域，倘若此时已知当前结点p，需要查找其前驱结点，那么就必须从head头指针遍历至p的前驱结点，操作的效率很低，因此如果p有一个指向前驱结点的next域，那效率就高多了，对于这种一个结点中分别包含了前驱结点域pre和后继结点域next的链表，称之为双链表。本篇我们将从以下结点来分析双链表

<div class="toc">

*   [双链表的设计与实现](#双链表的设计与实现)
*   [循环双链表的设计与实现](#循环双链表的设计与实现)
*   [排序循环双链表的实现](#排序循环双链表的实现)
*   [双链表的执行效率分析](#双链表的执行效率分析)
*   [异或高效存储双链表的设计原理概要](#异或高效存储双链表的设计原理概要)

</div>

# <a name="t0"></a><font color="#D90E0E">双链表的设计与实现</font>

  双链表的主要优点是对于任意给的结点，都可以很轻易的获取其前驱结点或者后继结点，而主要缺点是每个结点需要添加额外的next域，因此需要更多的空间开销，同时结点的插入与删除操作也将更加耗时，因为需要更多的指针指向操作。双链表的结构图如下：  
![](https://img-blog.csdn.net/20161105212613736)  
创建HeadDoubleILinkedList类并实现IlinekedList接口(和上篇博文的接口一样)

    /**
     * Created by zejian on 2016/10/23.
     * 双链表的实现,带头结点(不带数据)的双链表,为了更高的效率该类包含指向尾部的指针tail
     */
    public class HeadDoubleILinkedList<T> implements ILinkedList<T> {

        protected DNode<T> head; //不带数据的头结点
        protected DNode<T> tail; //指向尾部的指针

        public HeadDoubleILinkedList(){
            //初始化头结点
            this.head =this.tail= new DNode<>();          
        }
        //先省略其他代码
        ........
    }

结点类结构如下：

    package com.zejian.structures.LinkedList.doubleLinked;

    /**
     * Created by zejian on 2016/10/23.
     * 双链表结点
     */
    public class DNode<T> {

        public T data;
        public DNode<T> prev, next;//前继指针和后继指针
        public DNode(T data, DNode<T> prev, DNode<T> next)
        {
            this.data = data;
            this.prev = prev;
            this.next = next;
        }

        public DNode(T data)
        {
            this(data, null, null);
        }

        public DNode()
        {
            this(null, null, null);
        }

        public String toString()
        {
            return this.data.toString();
        }
    }

通过上篇的分析，我们对链表的插入、删除、查找、替换等操作也比较熟悉了，因此针对双链表的实现，主要分析其插入、删除、查找、替换等方法，其他没有分析的看实现源码即可（最后会给出双链表的实现代码）

*   <font color="#27844F">双链表的插入操作分析与实现</font>  
      我们先来看看双链表的插入，虽然有不带数据的头结点，但是由于是双向链表，所以在插入双链表时需分两种情况，一种是在插入空双链表和尾部插入，另一种是双链表的中间插入，如下图在空双链表插入值x：  
    ![](https://img-blog.csdn.net/20161106112556619)  
    从图可以看出（a）和（b）属于同种情况，需要注意front.next != null的情况，否则就会抛空指针，而（c）的情况属于中间插入无需无需理会front.next != null的条件，因为中间插入时无论如何其后继结点时不会为null的，插入方法的实现代码如下：

        /**
         * 插入结点
         * @param index
         * @param data
         * @return
         */
        @Override
        public boolean add(int index, T data) {
            if(index<0||data==null)
                throw new NullPointerException("index < 0 || data == null");

                int j = 0;
                DNode<T> front = this.head;
                //查找要插入结点位置的前一个结点
                while (front.next != null && j < index) {
                    j++;
                    front = front.next;
                }

                //创建需要插入的结点,并让其前继指针指向front,后继指针指向front.next
                DNode<T> q = new DNode<T>(data, front, front.next);

                //空双链表插入和尾部插入，无需此操作
                if(front.next != null) {
                    //更改front.next的前继指针
                    front.next.prev = q;
                }
                //更改front的后继指针
                front.next = q;

                //在尾部插入时需要注意更新tail指向
                if(front==this.tail){
                    this.tail=q;
                }
                return true;
        }

*   <font color="#27844F">双链表的删除操作分析与实现</font>  
      双链表的删除操作与插入操作原理上是相似的，我们可以看出（a）（b）是属于同种情况，需要防止 p.next.prev抛空指针的情况，而对于（c）情况则无需关系 p.next.prev的值，删除的具体实现如下：  
    ![](https://img-blog.csdn.net/20161106144119657)

        /**
          * 根据下标删除结点
          * 1.头删除
          * 2.中间删除
          * 3.尾部删除,更新tail指向
          * @param index 下标起始值为0
          * @return
          */
         @Override
         public T remove(int index) {

             int size=length();
             T temp=null;

             if(index<0||index>=size||isEmpty()){
                 return temp;
             }

             DNode<T> p=this.head;
             int j=0;
             //头删除/尾删除/中间删除,查找需要删除的结点(要删除的当前结点因此i<=index)
             while (p!=null&&j<=index){
                 p=p.next;
                 j++;
             }
             //当双链表只有一个结点时或尾部删除时,无需此步
             if(p.next!=null){
                 p.next.prev=p.prev;
             }
             p.prev.next=p.next;
             //如果是尾结点
             if (p==this.tail) {
                 this.tail = p.prev;//更新未结点的指向
             }
             temp=p.data;

             return temp;
         }

*   <font color="#27844F">双链表的查值操作分析与实现</font>  
    双链表的查找值的操作与单链表并没有什么区别，只要找到需要查找的当前结点获取其值即可，如下：  
    ![](https://img-blog.csdn.net/20161106113359435)  
    代码实现如下：

        @Override
        public T get(int index) {
            if (index>=0)
            {
                int j=0;
                //注意起始结点为this.head.next
                //如果起始点为this.head时，j的判断为j<=index，
                //因为需要寻找的是当前结点而不是前一个结点。
                DNode<T> pre=this.head.next;
                while (pre!=null && j<index)
                {
                    j++;
                    pre=pre.next;
                }
                if (pre!=null)
                    return pre.data;
            }
            return null;
        }

*   <font color="#27844F">双链表的替换值操作分析与实现</font>  
    双链表的替换值过程，需要先查找到需要替换的结点，这个过程跟获取值的过程是一样的，找到结点后直接替换值并返回旧值即可。比较简单直接上代码：

        @Override
        public T set(int index, T data) {
           T old=null;
           if (index>0&&data!=null){
               int j=0;
               DNode<T> pre =this.head.next;
               //查找需要替换的位置
               while (pre!=null&&j<index){
                   j++;
                   pre=pre.next;
               }
               if (pre!=null){
                   old=pre.data;
                   //替换数据
                   pre.data=data;
               }
           }
           return old;
        }

ok~，到此双链表的主要操作实现已分析完，下面给出双链表的实现源码：

    package com.zejian.structures.LinkedList.doubleLinked;

    import com.zejian.structures.LinkedList.ILinkedList;

    /**
    * Created by zejian on 2016/10/23.
    * 双链表的实现,带头结点(不带数据)的双链表,为了更高的效率该类包含指向尾部的指针tail
    */
    public class HeadDoubleILinkedList<T> implements ILinkedList<T> {

     protected DNode<T> head; //不带数据的头结点
     protected DNode<T> tail; //指向尾部的指针

     public HeadDoubleILinkedList(){
         this.head =this.tail= new DNode<>();          //初始化头结点
     }

     /**
      * 传入一个数组,转换成链表
      * @param array
      */
     public HeadDoubleILinkedList(T[] array)
     {
         this();
         if (array!=null && array.length>0)
         {
             this.head.next = new DNode<T>(array[0]);
             tail =this.head.next;
             tail.prev=this.head;
             int i=1;
             while (i<array.length)
             {
                 tail.next=new DNode<T>(array[i++]);
                 tail.next.prev=tail;
                 tail = tail.next;
             }
         }
     }

     @Override
     public boolean isEmpty() {
         return head.next==null;
     }

     @Override
     public int length() {
         int length=0;
         DNode<T> pre=head.next;
         while (pre!=null){
             length++;
             pre=pre.next;
         }
         return length;
     }

     @Override
     public T get(int index) {
         if (index>=0)
         {
             int j=0;
             DNode<T> pre=this.head.next;
             while (pre!=null && j<index)
             {
                 j++;
                 pre=pre.next;
             }
             if (pre!=null)
                 return pre.data;
         }
         return null;
     }

     @Override
     public T set(int index, T data) {
         T old=null;
         if (index>0&&data!=null){
             int j=0;
             DNode<T> pre =this.head.next;
             //查找需要替换的位置
             while (pre!=null&&j<index){
                 j++;
                 pre=pre.next;
             }
             if (pre!=null){
                 old=pre.data;
                 //替换数据
                 pre.data=data;
             }
         }
         return old;
     }

     /**
      * 插入结点
      * @param index
      * @param data
      * @return
      */
     @Override
     public boolean add(int index, T data) {
         if(index<0||data==null)
             throw new NullPointerException("index < 0 || data == null");

             int j = 0;
             DNode<T> front = this.head;
             //查找要插入结点位置的前一个结点
             while (front.next != null && j < index) {
                 j++;
                 front = front.next;
             }

             //创建需要插入的结点,并让其前继指针指向front,后继指针指向front.next
             DNode<T> q = new DNode<T>(data, front, front.next);

             //空双链表插入,需要确保front.next不为空
             if(front.next != null) {
                 //更改front.next的前继指针
                 front.next.prev = q;
             }
             //更改front的后继指针
             front.next = q;

             //在尾部插入时需要注意更新tail指向
             if(front==this.tail){
                 this.tail=q;
             }

             return true;
     }

     /**
      * 尾部添加
      * @param data
      * @return
      */
     @Override
     public boolean add(T data) {
         if (data==null)
             return false;
         //创建新结点,并把其前继指针指向tail
         DNode<T> q = new DNode<T>(data, tail, null);
         tail.next=q;
         //更新尾部结点
         this.tail=q;
         return true;
     }

     /**
      * 根据下标删除结点
      * 1.头删除
      * 2.中间删除
      * 3.尾部删除,更新tail指向
      * @param index 下标起始值为0
      * @return
      */
     @Override
     public T remove(int index) {

         int size=length();
         T temp=null;

         if(index<0||index>=size||isEmpty()){
             return temp;
         }

         DNode<T> p=this.head;
         int j=0;
         //头删除/尾删除/中间删除,查找需要删除的结点(要删除的当前结点因此i<=index)
         while (p!=null&&j<=index){
             p=p.next;
             j++;
         }
         //当链表只要一个结点时,无需此步
         if(p.next!=null){
             p.next.prev=p.prev;
         }
         p.prev.next=p.next;
         //如果是尾结点
         if (p==this.tail) {
             this.tail = p.prev;//更新未结点的指向
         }
         temp=p.data;

         return temp;
     }

     /**
      * 根据data删除结点,无需像单向链表那样去存储要删除结点的前一个结点
      * 1.头删除
      * 2.中间删除
      * 3.尾部删除,更新tail指向
      * @param data
      * @return
      */
     @Override
     public boolean removeAll(T data) {

         boolean isRemove=false;

         if(data==null||isEmpty())
             return isRemove;

         //注意这里的起点,如果起点为this.head,那么情况区别如同前面的根据index的删除实现
         DNode<T> p=this.head.next;

         //头删除/尾删除/中间删除(size>1),查找所有需要删除的结点
         while (p!=null){

             if(data.equals(p.data)){
                 if (p==this.tail){
                     //如果是尾结点
                     this.tail=p.prev;//更新未结点的指向
                     p.prev=null;
                     this.tail.next=null;
                 }else {
                     //如果是在中间删除,更新前继和后继指针指向
                     p.prev.next=p.next;
                     p.next.prev=p.prev;
                 }
                 isRemove=true;
                 p=p.next;//继续查找
             }else {
                 p=p.next;
             }

         }
         return isRemove;
     }

     /**
      * 清空链表
      */
     @Override
     public void clear() {
         this.head.next=null;
         this.tail=this.head;
     }

     @Override
     public boolean contains(T data) {

         if(data==null){
             return false;
         }

         DNode<T> p=this.head.next;
         while (p!=null){
             if (data.equals(p.data)){
                 return true;
             }else {
                 p=p.next;
             }
         }

         return false;
     }

     @Override
     public String toString() {
         String str="(";
         DNode<T> pre = this.head.next;
         while (pre!=null)
         {
             str += pre.data;
             pre = pre.next;
             if (pre!=null)
                 str += ", ";
         }
         return str+")";
     }

     public static void main(String[] args){

         String[] letters={"A","B","C","D","Z","E","F"};
    //        String[] letters={"A"};
         HeadDoubleILinkedList<String> list=new HeadDoubleILinkedList<>(letters);

         System.out.println("list.get(3)->"+list.get(3));
         System.out.println("list:"+list.toString());

         System.out.println("list.add(4,Y)—>"+list.add(0,"Y"));
         System.out.println("list:"+list.toString());
         System.out.println("list.add(Z)—>"+list.add("Z"));
         System.out.println("list:"+list.toString());

         System.out.println("list.contains(Z)->"+list.contains("Z"));
         System.out.println("list.set(4,P)-->"+list.set(4,"P"));
         System.out.println("list:"+list.toString());

         System.out.println("list.remove(6)-->"+list.remove(6));
    //        System.out.println("list.remove(Z)->"+list.removeAll("Z"));
         System.out.println("list:"+list.toString());
     }
    }

# <a name="t1"></a><font color="#D90E0E">循环双链表的设计与实现</font>

  如果双链表的最后一个结点的next指针域指向头结点，而头结点的prev指针指向头最后一个结点，则构成了双链表（Circular Doubly LinkedList），其结构如下图示：  
![](https://img-blog.csdn.net/20161106123357743)  
在循环双链表中我们不再需要尾指向结点，因为整个链表已构成循环，在头结点head的位置也可以轻松获取到尾部结点的位置。对于循环双链表的插入、删除操作也无需区分位置操作的情况，这是由于循环双链表的本身的特殊性，使p.next.pre永远不可能为null，因此我们在插入和删除时代码实现相对简单些。下面我们先分析一下循环双链表的插入操作，图示如下：  
![](https://img-blog.csdn.net/20161106124352690)  
我们可以看出（a）（b）（c）三种情况都无需关系位置插入的区别，其代码实现如下：

    /**
     * 根据index插入
     * 循环链表中无论是prev还是next都不存在空的情况,因此添加时
     * 无论是头部还是尾部还是中,都视为一种情况对待
     * @param index
     * @param data
     * @return
     */
    @Override
    public boolean add(int index, T data) {
        int size=length();
        if(data==null||index<0||index>=size)
            return false;

        int j=0;
        DNode<T> p=this.head;
        //寻找插入点的位置
        while (p.next!=head&&j<index){
            p=p.next;
            j++;
        }

        //创建新结点,如果index=3,那么插入的位置就是第4个位置
        DNode<T> q=new DNode<>(data,p,p.next);
        p.next=q;
        p.next.prev=q;

        return true;
    }

循环双链表的删除操作图示如下：

![双链表的删除操作图示](https://img-blog.csdn.net/20161106144957879)

同样地，从图中我们也可以发现由于循环双链表的特性，（a）（b）（c）三种情况都无需区分操作位置，其代码实现如下：

    @Override
    public T remove(int index) {
        T old = null;
        int size=length();

        if (index<0||index>=size)
            return old;

        int j=0;
        DNode<T> p=this.head.next;

        while (p!=head && j<index)
        {
            j++;
            p = p.next;
        }

        if (p!=head)
        {
            old = p.data;
            p.prev.next = p.next;
            p.next.prev = p.prev;
        }
        return old;
    }

至于循环双链表的查找值、替换值等操作与双链表并没有多大的区别，但是需要特别注意的是在遍历循环双链表时，结束标志不再是尾部结点是否为空，而是尾结点的next指针是否指向头结点head。好~，下面我们给出循环双链表的实现代码：

    package com.zejian.structures.LinkedList.doubleLinked;

    import com.zejian.structures.LinkedList.ILinkedList;

    /**
    * Created by zejian on 2016/10/24.
    * 循环双链表,带空头结点(不含数据),循环链表可以不需要尾部指针
    */
    public class LoopHeadDILinkedList<T> implements ILinkedList<T> {

     protected DNode<T> head; //不带数据的头结点
    //   protected DNode<T> tail; //指向尾部的指针

     public LoopHeadDILinkedList(){
         this.head = new DNode<>();//初始化头结点
         this.head.next=head;
         this.head.prev=head;

     }

     /**
      * 传入一个数组,转换成链表
      * @param array
      */
     public LoopHeadDILinkedList(T[] array)
     {
         this();
         if (array!=null && array.length>0)
         {
             DNode<T> p= new DNode<>(array[0]);
             head.next=p;
             head.prev=p;
             p.prev=head;
             p.next=head;

             int i=1;
             while (i<array.length)
             {
                 p.next=new DNode<>(array[i++],p,head);
                 head.prev=p.next;
                 p=p.next;
             }
         }
     }

     @Override
     public boolean isEmpty() {
         return this.head.next==head;//循环双链表的后继指针指向自己说明是空链表
     }

     @Override
     public int length() {

         int length=0;
         DNode<T> p=this.head.next;
         while (p!=this.head){
             length++;
             p=p.next;
         }
         return length;
     }

     @Override
     public T get(int index) {

         if (index>=0)
         {
             int j=0;
             DNode<T> p=this.head.next;
             while (p!=head && j<index)
             {
                 j++;
                 p=p.next;
             }
             if (p!=head)
                 return p.data;
         }
         return null;
     }

     /**
      * 根据index修改data
      * @param index
      * @param data
      * @return 返回被替换的data
      */
     @Override
     public T set(int index, T data) {

         if (data==null){
             return null;
         }

         if(index>=0){
             int j=0;
             DNode<T> p=this.head.next;

             while (p!=head&&j<index){
                 j++;
                 p=p.next;
             }

             //如果不是头结点
             if(p!=head){
                 T old = p.data;
                 p.data=data;

                 return old;
             }
         }

         return null;
     }

     /**
      * 根据index添加
      * 循环链表中无论是prev还是next都不存在空的情况,因此添加时
      * 无论是头部还是尾部还是中,都视为一种情况对待
      * @param index
      * @param data
      * @return
      */
     @Override
     public boolean add(int index, T data) {
         int size=length();
         if(data==null||index<0||index>=size)
             return false;

         int j=0;
         DNode<T> p=this.head;
         //寻找插入点的位置
         while (p.next!=head&&j<index){
             p=p.next;
             j++;
         }

         //创建新结点,如果index=3,那么插入的位置就是第4个位置
         DNode<T> q=new DNode<>(data,p,p.next);
         p.next=q;
         p.next.prev=q;

         return true;
     }

     /**
      * 尾部添加
      * @param data
      * @return
      */
     @Override
     public boolean add(T data) {

         if(data==null)
             return false;
         //创建新结点,让前继指针指向head.pre,后继指针指向head
         DNode<T> p=new DNode<>(data,head.prev,head);
         //更新tail后继指针的指向
         this.head.prev.next=p;
         this.head.prev=p;

         return true;
     }

     @Override
     public T remove(int index) {
         T old = null;
         int size=length();

         if (index<0||index>=size)
             return old;

         int j=0;
         DNode<T> p=this.head.next;

         while (p!=head && j<index)
         {
             j++;
             p = p.next;
         }

         if (p!=head)
         {
             old = p.data;
             p.prev.next = p.next;
             p.next.prev = p.prev;
         }

         return old;
     }

     @Override
     public boolean removeAll(T data) {
         boolean isRemove=false;

         if(data==null){
             return isRemove;
         }

         DNode<T> p=this.head.next;
         while (p!=head){
             if(data.equals(p.data)){
                 p.prev.next=p.next;
                 p.next.prev=p.prev;
                 isRemove=true;
             }
             p=p.next;
         }

         return isRemove;
     }

     @Override
     public void clear() {
         this.head.prev = head;
         this.head.next = head;
     }

     @Override
     public boolean contains(T data) {

         if (data==null){
            return false;
         }

         DNode<T> p=this.head.next;

         while (p!=head){
             if(data.equals(p.data)){
                 return false;
             }

             p=p.next;
         }

         return false;
     }

     @Override
     public String toString()
     {
         String str="(";
         DNode<T> p = this.head.next;
         while (p!=head)
         {
             str += p.data.toString();
             p = p.next;
             if (p!=head)
                 str += ", ";
         }
         return str+")";
     }
     public static void main(String[] args){

         String[] letters={"A","B","C","D","Z","E","F"};
         LoopHeadDILinkedList<String> list=new LoopHeadDILinkedList<>(letters);

         System.out.println("init list-->"+list.toString());

         System.out.println("list.get(3)->"+list.get(3));
         System.out.println("list:"+list.toString());

         System.out.println("list.add(4,Y)—>"+list.add(4,"Y"));
         System.out.println("list:"+list.toString());
         System.out.println("list.add(Z)—>"+list.add("Z"));
         System.out.println("list:"+list.toString());

         System.out.println("list.contains(Z)->"+list.contains("Z"));
         System.out.println("list.set(4,P)-->"+list.set(4,"P"));
         System.out.println("list:"+list.toString());

         System.out.println("list.remove(3)-->"+list.remove(3));
         System.out.println("list.remove(Z)->"+list.removeAll("Z"));
         System.out.println("list:"+list.toString());
     }
    }

# <a name="t2"></a><font color="#D90E0E">排序循环双链表的实现</font>

  所谓的排序循环双链表指的是在插入元素时，不再根据index标志，而是根据值的大小寻找插入位置，但是有个插入值data必须是T或者T的父类而且实现了Comoarable接口。排序循环双链表的实现比较简单，我们只需继承前面的循环双链表并重写add方法即可，主要代码实现如下：

    package com.zejian.structures.LinkedList.doubleLinked;

    /**
    * Created by zejian on 2016/11/6.
    * 升序排序链表，继承LoopHeadDILinkedList
    */
    public class SortLoopHeadDIlinkedList<T extends Comparable<? extends T>> extends LoopHeadDILinkedList<T> {
      /**
       * 顺序插入
       * @param data
       * @return
       */
      @Override
      public boolean add(T data) {

          if(data==null||!(data instanceof Comparable))
              throw new NullPointerException("data can\'t be null or data instanceof Comparable must be true");

          Comparable cmp =data;//这里需要转一下类型,否则idea编辑器上检验不通过.

          //如果data值比最后一个结点大,那么直接调用父类方法,在尾部添加.
          if(this.isEmpty() || cmp.compareTo(this.head.prev.data) > 0){
              return super.add(data);
          }

          DNode<T> p=this.head.next;
          //查找插入点
          while (p!=head&&cmp.compareTo(p.data)>0)
              p=p.next;

          DNode<T> q=new DNode<>(data,p.prev,p);
          p.prev.next=q;
          p.prev=q;

          return true;
      }

      public static void main(String[] args){
          SortLoopHeadDIlinkedList<Integer> list=new SortLoopHeadDIlinkedList<>();
          list.add(50);
          list.add(40);
          list.add(80);
          list.add(20);
          System.out.println("init list-->"+list.toString());
      }
    }

# <a name="t3"></a><font color="#D90E0E">双链表的执行效率分析</font>

  其实上一篇已分析得差不多了，这里再简单说明一下，链表在插入和删除元素时执行效率比较高，从插入操作来看，我们假设front指向的是双向链表中的一个结点，此时插入front的后继结点或者是前驱结点所消耗的时间为常数时间O(1),这点在插入front的前驱结点的效率比单链表有所改善，无需从头结点开始遍历，但是上述都是从已知双向链表中front结点的情况下讨论的。如果从实现代码的操作上看，无论是插入还是删除，都需要查找插入结点或删除结点，而这个过程访问结点所花费的时间的是O(n)，因此双链表的插入或删除操作或是查值操作，其时间复杂度都为O(n),至于为什么说链表更适合插入删除，这点上一篇我们已讨论过，这里就不重复了。最后给出一张关于链表、数组、动态数组的比较表：

<div class="table-box">

<table>

<thead>

<tr>

<th>传递参数</th>

<th>链表</th>

<th>动态数组</th>

</tr>

</thead>

<tbody>

<tr>

<td>索引</td>

<td>O(n)</td>

<td>O(1)</td>

</tr>

<tr>

<td>在最前端插入或删除</td>

<td>O(1)</td>

<td>O(n)</td>

</tr>

<tr>

<td>在最末端插入</td>

<td>O(n)</td>

<td>O(1),如果数组空间没有被填满;O(n),如果数组空间已填满</td>

</tr>

<tr>

<td>在最末端删除</td>

<td>O(n)</td>

<td>O(1)</td>

</tr>

<tr>

<td>在中间插入</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

<tr>

<td>在中间删除</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

<tr>

<td>空间浪费</td>

<td>O(n)</td>

<td>O(n)</td>

</tr>

</tbody>

</table>

</div>

# <a name="t4"></a><font color="#D90E0E">异或高效存储双链表的设计原理概要</font>

  在上述分析的双链表的实现中，都是需要一个指向后继结点的正向指针和一个指向前驱结点的反向指针，出于此点的考虑，我们需要在构造一个结点类时需要一个数据域data、一个指向后继结点的指针next以及一个指向前驱结点的指针prev。但为了设计更高效节省存储空间，一种基于指针差运算存储高效的双向链表就诞生了。这种链表的每个结点仍然与单链表一样仅使用一个指针域来设计双向链表，新的双向链表结点类结构如下：

    package com.zejian.structures.LinkedList.XORLinked;

    /**
     * Created by zejian on 2016/11/6.
     * 异或结点
     */
    public class XORNode<T> {
        public T data;
        public XORNode<T> ptrdiff;//异或指针

        public XORNode() {
        }

        public XORNode(T data, XORNode<T> ptrdiff) {
            this.data = data;
            this.ptrdiff = ptrdiff;
        }
    }

其中的ptrdiff字段存储了后继结点与前驱结点的地址差，指针的差通过异或运行（对异或不熟悉的可以看博主的另一篇文章：[java运算符](http://blog.csdn.net/javazejian/article/details/51181320)）来实现的，我们这里使用⊕表示异或操作，则有如下计算：

> pridiff=后继结点的地址⊕前驱结点的地址

![](https://img-blog.csdn.net/20161106220441820)

如上图，我们采用异或差值来计算各个结点的位置：

> A的next域为head⊕B  
> B的next域为A⊕C  
> C的next域为B⊕D  
> D的next域为C⊕NULL

那么为什么可以这么计算呢？我们先来了解一下异或的特性：

*   X⊕X=0
*   X⊕0=X
*   X⊕Y=Y⊕X
*   (X⊕Y)⊕Z=X⊕(Y⊕Z)

  所以我们可以很容易利用上述的异或特性找到结点的对象，比如指向P想从结点C移动到结点B，已知C的ptrdiff值为B⊕D,那么就需要将结点C的ptrdiff的值与结点D的地址执行异或运算，这时就可以得到B的地址了，计算过程如下：

> (B ⊕ D) ⊕ D = B ⊕(D ⊕ D) = B ⊕ 0 =B

如果想从C结点移动到D结点，那么此时的计算如下：

> (B ⊕ D) ⊕ B = D ⊕(B ⊕ B) =B ⊕ 0 = D

  因此在确实可以通过一个next的指针域来实现双向链表的移动，而且这种存储高效的双向链表还可以节省空间开销。实际上，存储高效的双链表介绍来自《数据结构与算法经典问题分析》一书，不过博主发现，这种存储高效的链表，使用C语言比较容易实现，因为C语言可以通过指针(地址)获取到对象直接操作，但在java语言中，博主并没有想到如何实现这种存储高效的链表，至少目前还没想到可行的方案，google了一把实现语言都是C，没找到java的实现，不过博主想来想去都感觉这种存储高效的链表不太适合java来实现（仅个人观点），若有实现方案的还望留言告知，感谢呢。不过这样算法设计思想方式还是蛮有不错的。ok~，关于双向链表，我们暂且聊到这里，下面丢出github的地址：

[GITHUB博文源码下载地址](https://github.com/shinezejian/javaStructures)

<font size="4">关联文章:</font>

[java数据结构与算法之顺序表与链表设计与实现分析](http://blog.csdn.net/javazejian/article/details/52953190)  
[java数据结构与算法之双链表设计与实现](http://blog.csdn.net/javazejian/article/details/53047590)  
[java数据结构与算法之改良顺序表与双链表类似ArrayList和LinkedList（带Iterator迭代器与fast-fail机制）](http://blog.csdn.net/javazejian/article/details/53073995)

</div>

<link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet"></div>

</article>

</div>
