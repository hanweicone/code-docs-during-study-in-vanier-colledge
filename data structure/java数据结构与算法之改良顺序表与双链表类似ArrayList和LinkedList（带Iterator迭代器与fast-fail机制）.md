<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-1 float-left">原</span>

# java数据结构与算法之改良顺序表与双链表类似ArrayList和LinkedList（带Iterator迭代器与fast-fail机制）

</div>

<div class="article-info-box">

<div class="article-bar-top"><span class="time">2016年11月21日 08:35:26</span> [zejian_](https://me.csdn.net/javazejian) <span class="read-count">阅读数 7029</span></div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">

<div class="article-copyright">版权声明：本文为博主原创文章，请尊重原创，未经博主允许禁止转载，保留追究权 https://blog.csdn.net/javazejian/article/details/53073995</div>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-cd6c485e8b.css">

<div id="content_views" class="markdown_views">

> <font size="4">转载请注明出处（请尊重原创！谢谢~）：  
> [http://blog.csdn.net/javazejian/article/details/53073995](http://blog.csdn.net/javazejian/article/details/53073995)  
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

  这篇是数据结构与算法的第3篇，通过前两篇的介绍，对应顺序表和链表已有比较深入的了解，而本篇是前两篇的延续，即优化前面所分析过的顺序表和双向链表（带头结点和尾结点，均不带数据）。以下是主要的知识点：

<div class="toc">

<div class="toc">

*   [理解Iterator接口](#理解iterator接口)
    *   [为什么需要迭代器Iterator](#为什么需要迭代器iterator)
    *   [迭代器Iterator的分析](#迭代器iterator的分析)
    *   [迭代器Iterator的简单实现](#迭代器iterator的简单实现)
    *   [迭代器Iterator与集合间存在的问题](#迭代器iterator与集合间存在的问题)
*   [理解快速失败机制fast-fail机制](#理解快速失败机制fast-fail机制)
*   [进化版的ListIterator接口](#进化版的listiterator接口)
*   [改良的MyArraryList的实现](#改良的myarrarylist的实现)
*   [改良的MyLinkedList的实现](#改良的mylinkedlist的实现)

</div>

</div>

# <a name="t0"></a><font color="#D90E0E">理解Iterator接口</font>

## <a name="t1"></a><font color="#D90E0E">为什么需要迭代器（Iterator）</font>

  在分析迭代器前，我们先来了解一下为什么需要迭代器，在以前的代码中，我们总是通过如下去循环获取某些集合中的元素：

    List<String> list = new ArrayList<String>();
    for(int i = 0 ; i < list.size() ;  i++){
         String str = list.get(i);
         //do something....
      }

或者是

    List<String> list = new LinkedList<String>();
    for(int i = 0 ; i < list.size() ;  i++){
         String str = list.get(i);
         //do something....
      }

  事实上以上的方式是完全没有问题的，但是大家有没想过为什么可以这样去获取值呢？其实很大原因是我们已了解了ArrayList和LinkedList集合的内部结构，因此我们知道可以通过list.get(i)可以获取到元素也可以通过list.remove()可以删除元素，什么意思？现在来假设一个集合（不属于Collection和Map），该集合是SquenceHashColl，请遍历该集合元素，此时大家会如何做呢，有人会说很简单啊，去查该集合的API啊，是的，没错，那去查API不就相当于去了解其结构了么？难道就没有其他方法可以在不查看API或了解内部结构的情况下去遍历SquenceHashColl集合的吗？到此先来屡屡问题出现的原因，然后再给出解决方案，上述在遍历SquenceHashColl集合时，之所以无法在不知道API或内部结构的时候获取元素，主要原因是访问代码和集合本身是紧密耦合的，无法将访问逻辑从集合类和客户端代码中分离出来，也就是说我们没有办法遍历集合的原因是访问集合元素的逻辑与集合本身耦合度太高了，从而必须在了解其API或者内部结构的基础上才能遍历该集合，那么现在只要把访问逻辑从集合本身的代码剥离出来问题也就迎刃而解了，但该如何剥离两者呢？这时迭代器就出场了，有了迭代器访问集合元素的逻辑和集合本身就很容易分离开来了，问题迭代器是什么啊？客官，别急，且听，慢慢道来…..

## <a name="t2"></a><font color="#D90E0E">迭代器（Iterator）的分析</font>

  关于迭代器，在这里我们可以简单地理解为遍历，是一个标准化遍历各类容器里面的所有对象的方法类，它是本身也是一种典型的设计模式。Iterator 模式是用于遍历集合类的标准访问方法。它可以把访问逻辑从不同类型的集合类中抽象出来，从而避免向客户端暴露集合的内部结构。由于迭代器总是用同一种逻辑来遍历集合，因此只要该集合内部实现了迭代器，就可以在不知道API或者集合内部结构的情况下通过迭代器遍历该集合的元素。下面我们先来对比一下使用迭代器和不使用迭代器的遍历方法：

    List<String> list = new LinkedList<String>();
    //不使用迭代器
    for(int i = 0 ; i < list.size() ;  i++){
         String str = list.get(i);
         //do something......
      }
     //使用迭代器
     //获取该集合的迭代器
     Iterator iterator = list.iterator();
     //判断是否有下一个元素
     while(iterator.hasNext()){
        //获取迭代器的值
        String string = iterator.next();
        //do something......
       }

    //SquenceHashColl集合(虚构的集合，假设该集合内部实现Iterator)
    SquenceHashColl shc=new SquenceHashColl();
    //获取该集合的迭代器
     Iterator iterator = shc.iterator();
     //判断是否有下一个元素
     while(iterator.hasNext()){
        //获取迭代器的值
        String string = iterator.next();
        //do something......
       }

  由上述代码可见，使用迭代器(Iterator)可以在不知道集合API和内部结构的情况下很容易的获取集合的元素。接下来我们引入Java JDK中为我们提供的Iterator接口，它提供了迭代了基本规则，在Java JDK 中他是这样定义的：对 collection 进行迭代的迭代器。其接口定义如下：

    public interface Iterator<E> {
       /**
        * 判断是否还有下一个元素
        */
       boolean hasNext();

       /**
        * 返回元素的值
        */
       E next();

       /**
         * 移除元素
        */
       default void remove() {
           throw new UnsupportedOperationException("remove");
       }

       /**
        * 这是Java8为Iterator新增的默认方法，该方法可使用lambda表达式来遍历集合元素。
        * 本篇我们先不分析该方法
        * @since 1.8
        */
       default void forEachRemaining(Consumer<? super E> action) {
           Objects.requireNonNull(action);
           while (hasNext())
               action.accept(next());
       }
    }

  在大多数情况下，我们一般只需使用 next()、hasNext() 两个方法即可完成元素迭代。

## <a name="t3"></a><font color="#D90E0E">迭代器（Iterator）的简单实现</font>

  ok~，在理解了迭代器后，我们来看看在顺序表中迭代器的实现（为了避免与Java中的ArrayList名字冲突，这里顺序表就命名为MyArrayList，关于MyArrayList的get方法和remove方法的实现与前两篇的实现基本一样，Itr为迭代器，是顺序表MyArrayList的内部类）：

    **
     * 迭代器-Itr
     * Blog : http://blog.csdn.net/javazejian
     */
    private class Itr implements Iterator<T> {
        /**
         * 表示将要访问的下一个元素的下标
         * index of next element to return
         */
        int cursor;

        /**
         * 当前正在访问的元素下标,如果没有则返回-1
         * index of last element returned; -1 if no such
         */
        int lastRet = -1;

        /**
         * 先判断是否还有下一个元素
         * @return
         */
        public boolean hasNext() {
            return cursor != size;
        }

        @SuppressWarnings("unchecked")
        public T next() {
            int i = cursor;
            if (i >= size)
                throw new NoSuchElementException();
            //获取顺序表中的数组集合，然后操作该数组元素
            Object[] elementData = MyArrayList.this.elementData;

            if (i >= elementData.length)
                throw new ConcurrentModificationException();

            cursor = i + 1;//加一,移动到下一个要访问的下标

            return (T) elementData[lastRet = i];
        }

        /**
         * 使用迭代器的方法移除元素
         */
        public void remove() {
            if (lastRet < 0)
                throw new IllegalStateException();
            try {
                //移除当前操作的元素
                MyArrayList.this.remove(lastRet);
                //修改当前下标指向
                cursor = lastRet;
                //复原
                lastRet = -1;
            } catch (IndexOutOfBoundsException ex) {
                throw new ConcurrentModificationException();
            }
        }
    }

  从代码可以知道，cursor表示还未被访问的下一个元素下标，lastRet表示的是正在被访问的元素下标，hasNext()方法实现中可知，通过判断还未被访问的下一个元素的下标来判断是否还有可访问元素。

    public boolean hasNext() {
          return cursor != size;
      }

  而在next()方法实现中，可看出在执行next时，cursor可访问的下标元素会赋值i变量，最终i会赋值给lastRet变量，此时lastRet下标就代表着正在被访问元素的下标，而cursor则执行加1操作，继而指向下一个未被访问的元素(此时并不知道还有没下一个元素，需要通过hasNext()方法判断)，还有一点需要特别注意的是，在next方法中使用的元素数组是来自顺序表MyArrayList.this.elementData，实际上迭代器是顺序表MyArrayList的内部类Itr。

    @SuppressWarnings("unchecked")
    public T next() {
        int i = cursor;
        if (i >= size)
            throw new NoSuchElementException();
        //获取当前集合
        Object[] elementData = MyArrayList.this.elementData;

        if (i >= elementData.length)
            throw new ConcurrentModificationException();

        cursor = i + 1;//加一,移动到下一个要访问的下标

        return (T) elementData[lastRet = i];
    }

  在remove方法中，通过在next()方法访问时记录的当前正在访问的元素下标lastRet，然后调用顺序表的MyArrayList.this.remove(lastRet)移除元素，此时由于移除了元素，lastRet所代表下标的元素即为删除元素后移动到该位置的新元素，因此该元素是未被访问的元素即修改cursor的值为lastRet，同时lastRet的值复原为-1。

    public void remove() {
       if (lastRet < 0)
           throw new IllegalStateException();
       try {
           //移除当前操作的元素
           MyArrayList.this.remove(lastRet);
           //修改当前下标指向
           cursor = lastRet;
           //复原
           lastRet = -1;
       } catch (IndexOutOfBoundsException ex) {
           throw new ConcurrentModificationException();
       }
    }

到此迭代器的3个方法分析完成，可以小结出以下几点：  
1、迭代器Iterator内部最终操作的也是顺序表MyArrayList的数组和方法  
2、hasNext()通过cursor判断将要被访问的元素是否存在  
3、next()返回的正在被访问的元素，同时会保存该元素的下标指向lastRet，而cursor会指向下一个未被访问的元素。  
4、remove()移除后数组元素需要移动，同时cursor指向需要更新为lastRet，因为lastRet此时代表着往前移动的元素。移除过程可以简单理解为下图：  
![](https://img-blog.csdn.net/20161119161235672)  
顺序表有了迭代器，我们就可以通过以下方式访问顺序表MyArrayList的元素了，简易代码如下：

    MyArrayList<Integer> myArrayList=new MyArrayList<>();
    myArrayList.add(2);
    myArrayList.add(10);
    myArrayList.add(1);
    myArrayList.add(9);

    //通过迭代器方法
    Iterator iterator=myArrayList.iterator();
    while (iterator.hasNext()){
        System.out.println("iterator.next->"+iterator.next());
    }

## <a name="t4"></a><font color="#D90E0E">迭代器（Iterator）与集合间存在的问题</font>

  虽然上述过程中我们已在顺序表MyArrayList集合中实现了迭代器，但是MyArrayList集合与迭代器间却还存在着一个严重的问题，那就是数据一致性，为什么会出现这个问题呢？现在假设我们通过myArrayList的迭代器遍历元素，此时会调用next方法，其内部会进行一个操作：

    //获取当前MyArrayList的数组集合
    Object[] elementData = MyArrayList.this.elementData;

  迭代器会先获取整个数组对象，然后进行取值操作，但是在使用iterator的同时，假设我们又去操作调用了myArrayList本身的方法比如MyArrayList.remove(index)，那么此时elementData数组的元素就会发生变化，而迭代器此时刚好也通过了hasNext方法判断，正在调用next方法，但最后获取到的值却已被之前修改过了，不是期望值，从而也就造成了数据不一致的问题。举个简单的例子如下，假如集合中存放了10号、20号、30号、40号的球衣，我们可以通过两种方式取出球衣，一种是通过MyArrayList集合本身的方法remove()（在迭代过程中调用，迭代器并不知情），另一种则是通过迭代器本身的remove方法，过程如下所示（这里我们简单把remove理解为获取球衣）：

    MyArrayList<Integer> myArrayList=new MyArrayList<>();
    myArrayList.add(10);
    myArrayList.add(20);
    myArrayList.add(30);
    myArrayList.add(40);
    System.out.println("-------------iterator--------------");
    //迭代前获取到的集合有4件球衣
    boolean flag=true;
    Iterator<Integer> it = myArrayList.iterator();
    while (it.hasNext()) {
        //调用集合myArrayList的remove
        //在迭代器不知情的情况下移除了20,剩余3个球衣
        if(flag){
          flag=false;
          myArrayList.remove(new Integer(20));
        }
        //结果只拿到3件球衣
        it.remove();//迭代器本身的方法
    }

  从程序中可以看出，迭代器想从集合中获取4件球衣，实际上获取迭代器it时，集合中确实是有4件球衣的，但是在通过it.hasNext()判断后，却调用了myArrayList.remove(new Integer(20))拿走了20号球衣，注意此时迭代器并不知情，最后的结果就是迭代器压根儿没有拿到20号球衣，在迭代过程20号球衣不翼而飞，连声通知都没有，这显然是不合理的啊，要拿走至少也得通知一声吧，说好的人与人之间的信任呢？淡然无存，悲凉呐。。这还是单线程呢，那么多线程问题就更明显了，是吧？现在来屡屡问题在哪里，显然是myArrayList用自身的remove方法拿走了一件球衣却没有通知迭代器（Iterator）,如果有通知，那么迭代器执行相应的策略也就合理了，那现在的问题是该如何通知迭代器呢？要解决这个问题，我们得看到最本质的问题，移除后（remove），最显著的变化是啥？没错，MyArrayList.this.elementData的存储元素实际个数发生变化了，也可理解为结构发生变化了(因为元素被移除了)，也就意味着我们必须在结构发生变化时告诉迭代器，”myArrayList:‘迭代器啊，我拿了一个元素了，你自己注意一下啊’；Iterator:‘好的，我正在遍历呢，我改变一下策略。’”，这样的话使用起来也就合情合理。那么这个策略到底是啥呢？其实事情的经过是这样的，在MyArrayList我们可以用一个变量，比如modCount=0来记录结构变化的次数，当添加元素或删除元素或清空集合时，让modCount++,记录变化，那么每次我们在获取迭代器时，把当前记录的modCount变化值赋予给内部类Iterator的一个变量比如expectedModCount=modCount,然后每次在操作it.next()或者it.remove()就去判断expectedModCount与modCount是否相等即可，只要不相等就说明集合结构已发生变化，这时我们便不再迭代元素并执行对应的逻辑即可。简易代码过程如下：

    /**
    * Created by zejian on 2016/11/8.
    * Blog : http://blog.csdn.net/javazejian [请尊重原创,转载注明出处]
    * 改良的顺序表类似java集合类ArrayList
    */
    public class MyArrayList<T>  implements java.io.Serializable,IList<T>,Iterable<T>{

    private static final long serialVersionUID = 8683452581122892389L;

    /**
    * 默认大小
    */
    private static final int DEFAULT_CAPACITY = 10；

    private int size;

    /**
    * 记录修改次数,适用于快速失败机制
    */
    private int modCount;

    /**
    * 存储数据的数组
    */
    private T[] elementData;

    //......省略其他代码

    /**
    * 扩容的方法
    * @param capacity
    */
    public void ensureCapacity(int capacity) {
       //如果需要拓展的容量比现在数组的容量还小,则无需扩容
       if (capacity<size)
           return;

       modCount++;//<-------------------------------记录元素变化
       .......
    }

    /**
    * 清空数据
    */
    @Override
    public void clear() {
       modCount++;//<-------------------------------记录元素变化

       // clear to let GC do its work
       for (int i = 0; i < size; i++)
           elementData[i] = null;

       size = 0;
    }

    /**
    * 添加
    * Blog : http://blog.csdn.net/javazejian
    * @param index
    * @param data
    */
    @Override
    public void add(int index, T data) {
       ........省略其他代码
       size++;
       //记录变化
       modCount++;//<-------------------------------记录元素变化
    }

    /**
    * 根据下标移除元素
    * Blog : http://blog.csdn.net/javazejian
    * @param index
    * @return
    */
    @Override
    public T remove(int index) {

       rangeCheck(index);
       modCount++;//<-------------------------------记录元素变化

       .......省略其他代码
    }

    /**
    * 返回迭代器
    * @return
    */
    @Override
    public Iterator<T> iterator() {
       return new Itr();
    }

    /**
    * 迭代器-Itr
    * Blog : http://blog.csdn.net/javazejian
    */
    private class Itr implements Iterator<T> {
       /**
        * 表示将要访问的下一个元素的下标
        * index of next element to return
        */
       int cursor;

       /**
        * 当前正在访问的元素下标,如果没有则返回-1
        * index of last element returned; -1 if no such
        */
       int lastRet = -1;
       /**
        * 修改标识符,用于判断集合是否被修改
        */
       int expectedModCount = modCount;//<-------------------初始化修改标识符

       /**
        * 先判断是否还有下一个元素
        * @return
        */
       public boolean hasNext() {
           return cursor != size;
       }

       @SuppressWarnings("unchecked")
       public T next() {
           //检测集合是否已被修改
           checkForComodification();//<---------------------------调用前检测集合是否已被修改
           ....... 省略其他代码
       }

       /**
        * 使用迭代器的方法移除元素
        */
       public void remove() {
           if (lastRet < 0)
               throw new IllegalStateException();
           //检测集合是否已被改变
           checkForComodification();//<---------------------------调用前检测集合是否已被修改
          //........省略其他代码

       }

       /**
        * 检测modCount标识符
        */
       final void checkForComodification() {
           if (modCount != expectedModCount)
               throw new ConcurrentModificationException();//<-------修改则抛出异常
       }
    }

  上述省略大部分代码（完整源码最终会通过GitHub提供给大家），此时我们关注点是MyArrayList本身的modCount和Iterator的expectedModCount，通过这两个变量我们就可以实现上述描述的策略，可以看到在添加删除或者情况元素时都会使modCount++来记录集合结构修改次数，在获取迭代器时，会把modCount赋值给Iterator.expectedModCount变量，此时modCount与expectedModCount肯定是相等，在Iterator迭代元素的过程中如果MyArrayList调用自身方法使集合结构发生变化，那么modCount肯定会变化即modCount与expectedModCount肯定会不相等，也就是说在Iterator迭代的过程中只要检测到modCount！=expectedModCount,则说明结构发生了变化也就没必要继续迭代元素了，此时便ConcurrentModificationException异常，终止迭代操作。其实该策略就是Java JDK的常用集合中的快速失败机制(fast-fail机制)，接下来我们就来重新整理一下前面的问题，然后深入理解Java JDK中的快速失败机制。

# <a name="t5"></a><font color="#D90E0E">理解快速失败机制(fast-fail机制)</font>

  通过上述的分析，我们已经大概了解了解快速失败机制的执行原理。现在就来重新了解fail-fast机制，“快速失败”即fail-fast，它是 Java 集合的一种错误检测机制。当多个线程对集合进行结构上的改变的操作或者集合在迭代元素时直接直接调用自身方法改变集合结构而没有通知迭代器时，有可能会触发 fail-fast 机制并抛出ConcurrentModificationException异常。这里需要特别注意的是，有可能触发 fail-fast 机制而不是肯定。触发原理是在迭代过程中，集合的结构发生了变化而此时迭代器并不知道或者还没来得及反应时便会产生fail-fast机制。这里我们再次强调，迭代器的快速失败行为无法得到保证，因为一般来说，不可能对是否出现不同步并发修改或者自身修改做出任何硬性保证。快速失败迭代器会尽最大努力抛出 ConcurrentModificationException。因此，为提高这类迭代器的正确性而编写一个依赖于此异常的程序是错误的做法，因为迭代器的快速失败行为应该仅用于检测 bug而已。为了更好的理解fail-fast机制，在这里我们使用Java JDK提供的ArrayList作为测试对象（当然我们自己实现的MyArrayList和MyLinkedList也实现的fail-fast机制，但为了更有说服力在此还是使用官方的ArrayList）。

    /**
     * Created by zejian on 2016/11/20.
     * Blog : http://blog.csdn.net/javazejian [请尊重原创,转载注明出处]
     */
    public class FailFastTest {

        public static void main(String[] args){
            ArrayList<Integer> list =new ArrayList<>();
            list.add(10);
            list.add(20);
            list.add(30);

            Iterator iterator=list.iterator();
            while (iterator.hasNext()){
                list.remove(1);//移除第2个元素
                int value= (int) iterator.next();
                System.out.println(value);
            }
        }
    }

迭代过程移除调用list自身方法移除元素，运行结构如下：  
![](https://img-blog.csdn.net/20161120200328237)  
  该异常是不是很熟悉，相信不少人在操作集合过程中都遇到过。那么该异常如何解决呢？实际上最根本的原因使我们调用了list自身的remove方法，只要我们调用Iterator的remove方法，那么问题就迎刃而解了，如下：

    /**
     * Created by zejian on 2016/11/20.
     * Blog : http://blog.csdn.net/javazejian [请尊重原创,转载注明出处]
     */
    public class FailFastTest {

        public static void main(String[] args){
            ArrayList<Integer> list =new ArrayList<>();
            list.add(10);
            list.add(20);
            list.add(30);

            Iterator iterator=list.iterator();
            while (iterator.hasNext()){
                Integer value= (Integer) iterator.next();
                if(value==20){
                    iterator.remove();//调用iterator的方法移除第2个元素
                }else {
                    System.out.println("value-->"+value);
                }
            }
        }
    }

输出结果如下：  
![](https://img-blog.csdn.net/20161120210457253)  
此时我们可能有点迷糊了，为什么iterator的remove就没有问题呢，其实看一下源码就明白了，Iterator的remove方法源码如下：

     public void remove() {
                if (lastRet < 0)
                    throw new IllegalStateException();
                //检测modCount与expectedModCount是否相等
                checkForComodification();

                try {
                    //注意本身还是调用ArrayList.this.remove()
                    ArrayList.this.remove(lastRet);
                    cursor = lastRet;
                    lastRet = -1;
                    //但是！！！expectedModCount重新赋值了！
                    expectedModCount = modCount;
                } catch (IndexOutOfBoundsException ex) {
                    throw new ConcurrentModificationException();
                }
            }

  现在明白了吧。虽然Iterator的remove方法调用了ArrayList的remove方法（此时modCount++），但同时也对expectedModCount 重新赋值了 ，所以迭代器和ArrayList的结构变化达到一致协调（可以简单理解为迭代器接收到了ArrayList的通知），因此不会触发fast-fail。当然，还有一种情况，那就是多线程操作，比如存在两个线程（线程 A、线程 B），线程 A通过 Iterator 在遍历集合 list 中的元素，在某个时候线程 B修改了集合 list 的结构（注意是结构上面的修改，而不是修改集合元素的内容），那么这个时候也很可能会触发 fail-fast 机制并抛出 ConcurrentModificationException 异常，但是解决该场景的方案是使用CopyOnWriteArrayList （线程安全的集合类）来替换 ArrayList，但此知识点不在本篇讨论范围就不过多解释了。到此相信大家对fast-fail机制已有比较深入的理解了，切记fast-fail机制只会尽可能的抛出异常。稍后我们改良的顺序表MyArraryList和链表MyLinkedList也会实现fail-fast机制。

# <a name="t6"></a><font color="#D90E0E">进化版的ListIterator接口</font>

  在开始实现MyArraryList和MyLinkedList之前，我们最后来简单了解一下ListIterator接口，有了前面的Iterator接口，那为什么还需要ListIterator呢？其实ListIterator可以说是Iterator的升级版接口，因为在Iterator中指向向后迭代元素和删除元素，而ListIterator的出现使得迭代过程添加元素也成为可能，同时还可以向前遍历元素，下面我们简单看一下ListIterator接口方法即可：

    public interface ListIterator<E> extends Iterator<E> {
        /**
         * 是否还有下一个元素即cursor指向的下一元素
         * @return
         */
        boolean hasNext();

        /**
         * 获取元素值
         * @return
         */
        E next();

        /**
         * 是否有前驱元素
         * @return
         */
        boolean hasPrevious();

        /**
         * 获取上一个元素的值
         * @return
         */
        E previous();

        /**
         * 下一个将要访问元素的下标
         * @return
         */
        int nextIndex();

        /**
         * 上一个将要访问元素的下标
         * @return
         */
        int previousIndex();

        /**
         * 删除元素
         */
        void remove();

        /**
         * 替换元素的值
         * @param e
         */
        void set(E e);

        /**
         * 添加元素
         * @param e
         */
        void add(E e);
    }

ok~，关于ListIterator我们就先了解到这。

# <a name="t7"></a><font color="#D90E0E">改良的MyArraryList的实现</font>

  前面终于铺垫完了，现在开始改良我们的顺序表，不过在前面我们已聊得差不多了，改良后的顺序表添加了Iterator和ListIterator迭代器，同时新增了fast-fail机制，初始化MyArraryList时默认大小为10等，下面我们直接给出源码吧，实现比较简单，有点类似Java中的ArrayList集合，如果我们搞明白了MyArraryList后看JDK的ArrayList集合源码是相当轻松的事。

    package com.zejian.structures.LinkedList.MyCollection;

    import java.util.ConcurrentModificationException;
    import java.util.Iterator;
    import java.util.ListIterator;
    import java.util.NoSuchElementException;

    /**
     * Created by zejian on 2016/11/8.
     * Blog : http://blog.csdn.net/javazejian [请尊重原创,转载注明出处]
     * 改良的顺序表类似java集合类ArrayList
     */
    public class MyArrayList<T>  implements java.io.Serializable,IList<T>,Iterable<T>{

        private static final long serialVersionUID = 8683452581122892389L;

        /**
         * 默认大小
         */
        private static final int DEFAULT_CAPACITY = 10;

        /**
         * 空值数组
         */
        private static final Object[] EMPTY_ELEMENTDATA = {};

        private int size;

        /**
         * 记录修改次数,适用于快速失败机制
         */
        private int modCount;

        /**
         * 存储数据的数组
         */
        private T[] elementData;

        public MyArrayList(int initialCapacity) {
            if (initialCapacity > 0) {
                this.elementData = (T[]) new Object[initialCapacity];
            } else if (initialCapacity == 0) {
                this.elementData = (T[]) EMPTY_ELEMENTDATA;
            } else {
                throw new IllegalArgumentException("Illegal Capacity: "+
                        initialCapacity);
            }
        }

        public MyArrayList() {
            this.elementData = (T[]) new Object[DEFAULT_CAPACITY];
        }

        /**
         * 扩容的方法
         * @param capacity
         */
        public void ensureCapacity(int capacity) {
            //如果需要拓展的容量比现在数组的容量还小,则无需扩容
            if (capacity<size)
                return;

            modCount++;//记录元素变化

            T[] old = elementData;
            elementData = (T[]) new Object[capacity];
            //复制元素
            for (int i=0; i<size() ; i++)
                elementData[i]=old[i];
        }
        @Override
        public int size() {
            return size;
        }

        @Override
        public boolean isEmpty() {
            return size()==0;
        }

        /**
         * 清空数据
         */
        @Override
        public void clear() {
            modCount++;

            // clear to let GC do its work
            for (int i = 0; i < size; i++)
                elementData[i] = null;

            size = 0;
        }

        @Override
        public T get(int index) {
            //检测下标
            rangeCheck(index);

            return elementData[index];
        }

        @Override
        public T set(int index, T data) {
            //检测下标
            rangeCheck(index);

            T old=elementData[index];
            elementData[index]=data;
            return old;
        }

        @Override
        public boolean add(T data) {
            add(size(),data);
            return true;
        }

        /**
         * 添加
         * Blog : http://blog.csdn.net/javazejian
         * @param index
         * @param data
         */
        @Override
        public void add(int index, T data) {
            //判断容量是否充足
            if(elementData.length==size())
                ensureCapacity(size()*2+1);//扩容
            //根据index找到需要插入的位置
            for (int i=size; i>index; i--)
                elementData[i]=elementData[i-1];
            //赋值
            elementData[index]=data;
            size++;
            //记录变化
            modCount++;
        }

        /**
         * 根据data查询下标
         * Blog : http://blog.csdn.net/javazejian
         * @param data
         * @return
         */
        @Override
        public int indexOf(T data) {
            if (data == null) {
                //查找null的下标
                for (int i = 0; i < size; i++)
                    if (elementData[i]==null)
                        return i;
            } else {
                //查找有数据的下标
                for (int i = 0; i < size; i++)
                    if (data.equals(elementData[i]))
                        return i;
            }
            return -1;
        }

        /**
         * 根据data查找最后一个的index
         * Blog : http://blog.csdn.net/javazejian
         * @param data
         * @return
         */
        @Override
        public int lastIndexOf(T data) {
            //倒序查找即可
            if (data == null) {
                for (int i = size-1; i >= 0; i--)
                    if (elementData[i]==null)
                        return i;
            } else {
                for (int i = size-1; i >= 0; i--)
                    if (data.equals(elementData[i]))
                        return i;
            }
            return -1;
        }

        @Override
        public boolean remove(T data) {
            if (data == null) {
                throw new NullPointerException("data can\'t be empty");
            } else {
                for (int index = 0; index < size; index++)
                    if (data.equals(elementData[index])) {
                        this.remove(indexOf(data));
                        return true;
                    }
            }
            return false;
        }

        /**
         * 根据下标移除元素
         * Blog : http://blog.csdn.net/javazejian
         * @param index
         * @return
         */
        @Override
        public T remove(int index) {
            rangeCheck(index);
            modCount++;
            T oldValue = elementData[index];
            for (int i=index;i<size()-1;i++){
                elementData[i]=elementData[i+1];
            }

            elementData[--size] = null; // clear to let GC do its work
            return oldValue;
        }

        /**
         * 检测下标
         * @param index
         */
        private void rangeCheck(int index) {
            if (index<0||index >= size)
                throw new IndexOutOfBoundsException("Index: "+index+", Size: "+size);
        }

        @Override
        public boolean contains(T data) {
            return indexOf(data) >= 0;
        }

        /**
         * 提供从指定index开始遍历的迭代器
         * Blog : http://blog.csdn.net/javazejian
         * @param index
         * @return
         */
        public ListIterator<T> listIterator(int index) {
            if (index < 0 || index > size)
                throw new IndexOutOfBoundsException("Index: "+index);
            return new ListItr(index);
        }

        /**
         * 提供从0开始遍历的迭代器
         * Blog : http://blog.csdn.net/javazejian
         * @return
         */
        public ListIterator<T> listIterator() {
            return new ListItr(0);
        }

        /**
         * 返回迭代器
         * @return
         */
        @Override
        public Iterator<T> iterator() {
            return new Itr();
        }

        /**
         * 迭代器-Itr
         * Blog : http://blog.csdn.net/javazejian
         */
        private class Itr implements Iterator<T> {
            /**
             * 表示将要访问的下一个元素的下标
             * index of next element to return
             */
            int cursor;

            /**
             * 当前正在访问的元素下标,如果没有则返回-1
             * index of last element returned; -1 if no such
             */
            int lastRet = -1;
            /**
             * 修改标识符,用于判断集合是否被修改
             */
            int expectedModCount = modCount;

            /**
             * 先判断是否还有下一个元素
             * @return
             */
            public boolean hasNext() {
                return cursor != size;
            }

            @SuppressWarnings("unchecked")
            public T next() {
                //检测集合是否已被修改
                checkForComodification();
                int i = cursor;
                if (i >= size)
                    throw new NoSuchElementException();
                //获取当前集合
                Object[] elementData = MyArrayList.this.elementData;

                if (i >= elementData.length)
                    throw new ConcurrentModificationException();

                cursor = i + 1;//加一,移动到下一个要访问的下标

                return (T) elementData[lastRet = i];
            }

            /**
             * 使用迭代器的方法移除元素
             */
            public void remove() {
                if (lastRet < 0)
                    throw new IllegalStateException();

                //检测集合是否已被改变
                checkForComodification();

                try {
                    //移除当前操作的元素
                    MyArrayList.this.remove(lastRet);

                    //修改当前下标指向
                    cursor = lastRet;
                    //复原
                    lastRet = -1;
                    //更新标识符,防止抛出异常
                    expectedModCount = modCount;
                } catch (IndexOutOfBoundsException ex) {
                    throw new ConcurrentModificationException();
                }
            }

            /**
             * 检测modCount标识符
             */
            final void checkForComodification() {
                if (modCount != expectedModCount)
                    throw new ConcurrentModificationException();
            }
        }

        /**
         * Blog : http://blog.csdn.net/javazejian
         * 可以前移指向的迭代器-ListItr
         */
        private class ListItr extends Itr implements ListIterator<T> {
            ListItr(int index) {
                super();
                cursor = index;
            }

            public boolean hasPrevious() {
                return cursor != 0;
            }

            public int nextIndex() {
                return cursor;
            }

            public int previousIndex() {
                return cursor - 1;
            }
            //获取当前正在被遍历的元素值
            @SuppressWarnings("unchecked")
            public T previous() {
                checkForComodification();
                int i = cursor - 1;
                if (i < 0)
                    throw new NoSuchElementException();
                Object[] elementData = MyArrayList.this.elementData;
                if (i >= elementData.length)
                    throw new ConcurrentModificationException();
                cursor = i;
                return (T) elementData[lastRet = i];
            }

            public void set(T e) {
                if (lastRet < 0)
                    throw new IllegalStateException();
                checkForComodification();

                try {
                    MyArrayList.this.set(lastRet, e);
                } catch (IndexOutOfBoundsException ex) {
                    throw new ConcurrentModificationException();
                }
            }
            //遍历过程可用于添加元素
            public void add(T data) {
                checkForComodification();

                try {
                    int i = cursor;
                    MyArrayList.this.add(i, data);
                    cursor = i + 1;
                    lastRet = -1;
                    expectedModCount = modCount;
                } catch (IndexOutOfBoundsException ex) {
                    throw new ConcurrentModificationException();
                }
            }
        }
    //测试
    public static void main(String[] args){
       MyArrayList<Integer> myArrayList=new MyArrayList<>();
        myArrayList.add(2);
        myArrayList.add(10);
        myArrayList.add(1);
        myArrayList.add(9);

        print(myArrayList);
        System.out.println("-------------");
        myArrayList.remove(2);
        print(myArrayList);
        System.out.println("-------------");
        System.out.println("index-->"+myArrayList.indexOf(10));
        myArrayList.set(0,0);
        print(myArrayList);

        System.out.println("-------------iterator--------------");
        Iterator iterator=myArrayList.iterator();
        while (iterator.hasNext()){
            System.out.println("iterator.next-->"+iterator.next());
        }

        System.out.println("-------------foreach--------------");
        for(Integer data : myArrayList){
            System.out.println("data-->"+data);
        }

    }

        public static void print(MyArrayList myArrayList){
            for (int i=0;i<myArrayList.size();i++) {
                System.out.println("i->"+myArrayList.get(i));
            }
        }

    }

# <a name="t8"></a><font color="#D90E0E">改良的MyLinkedList的实现</font>

  关于MyLinkedList，我们主要进行了以下的改良，声明全局size，不再通过遍历链表的方式去获取size的大小，而在增加或者减少结点的同时更新size，因此size()方法的操作时间为O(1)。

    @Override
    public int size() {
        return size;
    }

同时为不区分插入删除位置操作情况，MyLinkedList中新建了两个没有带数据的结点，分别为头结点first和尾结点last，声明如下：

    /**
     * 头部指向结点,不带数据,排除特殊情况,优化代码量
     */
    private Node<T> first;

    /**
     * 尾部指向结点,不带数据,排除特殊情况,优化代码量
     */
    private Node<T> last;

    /**
     * 初始化链表
     */
    public MylinkeList() {
        first=new Node<>(null,null,null);
        last=new Node<>(first,null,null);
        first.next=last;
        size=0;
        modCount++;//记录修改次数
    }

结构如下：  
![](https://img-blog.csdn.net/20161120231418318)

接着我们对结点的查找，采用了二分查找的方式，根据index传入值分为从头结点往后查找和尾结点往前查找，使查询效率更高效代码如下：

     /**
         * 优化结点查询,根据情况而定查询起点
         * Blog : http://blog.csdn.net/javazejian
         * @param index
         * @return
         */
        Node<T> getNode(int index) {
            //如果index小于size的一半,则从头结点开始查找,否则从尾部开始查找(右移2位相当除以2)
            if (index < (size >> 1)) {
                Node<T> x = first.next;
                for (int i = 0; i < index; i++)
                    x = x.next;
                return x;
            } else {
                Node<T> x = last.prev;
                for (int i = size - 1; i > index; i--)
                    x = x.prev;
                return x;
            }
        }

在情况数据时，我们采用更利于GC回收的方式来处理数据：

        /**
         * 清空数据,GC更容易回收
         * Blog : http://blog.csdn.net/javazejian
         */
        @Override
        public void clear() {
            for (Node<T> x = first.next; x != null; ) {
                Node<T> next = x.next;
                x.data = null;
                x.next = null;
                x.prev = null;
                x = next;
            }
            //初始化链表
            first=new Node<>(null,null,null);
            last=new Node<>(first,null,null);
            first.next=last;
            size = 0;
            modCount++;
        }

同时我们抽取了头部插入，尾部插入，以及在某个结点前插入的代码，由于存在头结点和尾结点，无需判断各种基于操作位置插入的情况，使代码更简洁化：

    /**
      * 在succ结点前插入
      * Blog : http://blog.csdn.net/javazejian
      */
     void linkBefore(T T, Node<T> succ) {
         // assert succ != null;
         final Node<T> newNode = new Node<>(succ.prev, T, succ);
         succ.prev.next=newNode;
         succ.prev = newNode;
         size++;
         modCount++;
     }

     /**
      * 链表头部添加,由于拥有头结点和尾结点,无需判断插入情况
      * Blog : http://blog.csdn.net/javazejian
      * @param data
      */
     private void linkFirst(T data) {
         //头结点的下一个结点
         final Node<T> f = first.next;
         final Node<T> newNode = new Node<>(first, data, f);
         f.prev=newNode;
         first.next = newNode;
         size++;
         modCount++;
     }

     /**
      * 链表尾部添加,由于拥有头结点和尾结点,无需判断插入情况
      * Blog : http://blog.csdn.net/javazejian
      * @param data
      */
     void linkLast(T data) {
         //尾部结点的前一个结点
         final Node<T> l = last.prev;
         final Node<T> newNode = new Node<>(l, data, last);
         l.next = newNode;
         last.prev=newNode;
         size++;
         //记录修改
         modCount++;
     }

最后我们添加迭代器Iterator和fast-fail机制，还有点需要注意的是MyArrayList和MyLinkedList都实现了Iterable接口：

    public class MyArrayList<T>  implements Serializable,IList<T>,Iterable<T>

    public class MylinkeList<T> implements Serializable,IList<T>, Iterable<T>

Iterable接口

    /**
     * Implementing this interface allows an object to be the target of
     * the "for-each loop" statement. See
     * <strong>
     * <a href="{@docRoot}/../technotes/guides/language/foreach.html">For-each Loop</a>
     * </strong>
     *
     * @param <T> the type of elements returned by the iterator
     *
     * @since 1.5
     * @jls 14.14.2 The enhanced for statement
     */
    public interface Iterable<T> {

实现该接口的同时我们必须实现iterator()并返回一个迭代器Itr

    /**
     * 返回迭代器
     * @return
     */
    @Override
    public Iterator<T> iterator() {
        return new Itr();
    }

实现Iterable接口的另外一个好处是，我们的集合可以使用foreach增强for循环的方式来迭代元素，如果没有实现Iterable接口是无法使用foreach增强for循环的方式迭代元素的，代码示例如下：

    System.out.println("-------------foreach--------------");
    for(Integer data : mylinkeList){
        System.out.println("data-->"+data);
    }

好~，关于改良的链表我们就分析到这，因为大部分实现的过程在前两篇已分析得非常明白了，这里也就没必要重复了，最后贴一下实现源码（需要注意的是Java JDK中的LinkedList内部结构和我们实现的并不一样，LinkedList内部采用的虽然也有头结点和尾结点，可头结点和尾结点都分别指向第一个元素和最后一个元素，但它们的实现原理都是一样的，大家不妨自己查阅一下源码就明白了）：

    package com.zejian.structures.LinkedList.MyCollection;

    import java.io.Serializable;
    import java.util.*;

    /**
    * Created by zejian on 2016/11/10.
    * Blog : http://blog.csdn.net/javazejian [请尊重原创,转载注明出处]
    * 改良的双链表表(带头结点和尾结点)类似java集合类LinkedList
    */
    public class MylinkeList<T> implements Serializable,IList<T>, Iterable<T>{

       private static final long serialVersionUID = 8683452581122892300L;

       /**
        * 链表size,优化计算过程,无需遍历链表
        */
       private int size = 0;

       /**
        * 修改的记录符
        */
       private int modCount=0;

       /**
        * 头部指向结点,不带数据,排除特殊情况,优化代码量
        */
       private Node<T> first;

       /**
        * 尾部指向结点,不带数据,排除特殊情况,优化代码量
        */
       private Node<T> last;

       /**
        * 初始化链表
        */
       public MylinkeList() {
           first=new Node<>(null,null,null);
           last=new Node<>(first,null,null);
           first.next=last;
           size=0;
           modCount++;
       }

       @Override
       public int size() {
           return size;
       }

       @Override
       public boolean isEmpty() {
           return size==0;
       }

       @Override
       public boolean contains(T data) {
           return indexOf(data)!=-1;
       }

       /**
        * 清空数据,GC更容易回收
        * Blog : http://blog.csdn.net/javazejian
        */
       @Override
       public void clear() {
           for (Node<T> x = first.next; x != null; ) {
               Node<T> next = x.next;
               x.data = null;
               x.next = null;
               x.prev = null;
               x = next;
           }
           //初始化链表
           first=new Node<>(null,null,null);
           last=new Node<>(first,null,null);
           first.next=last;
           size = 0;
           modCount++;
       }

       /**
        * 根据index查询数据
        * @param index
        * @return
        */
       @Override
       public T get(int index) {
           checkElementIndex(index);
           return getNode(index).data;
       }

       @Override
       public T set(int index, T data) {
           //检测下标是否越界
           checkElementIndex(index);
           Node<T> x = getNode(index);
           T oldVal = x.data;
           x.data = data;
           return oldVal;
       }

       /**
        * 尾部添加
        * @param data
        * @return
        */
       @Override
       public boolean add(T data) {
           linkLast(data);
           return true;
       }

       @Override
       public void add(int index, T data) {
           checkElementIndex(index);

           if (index == size)//直接尾部添加
               linkLast(data);
           else
               linkBefore(data, getNode(index));//查找到插入结点并在其前插入
       }

       @Override
       public boolean remove(T data) {
           if (data == null) {
               for (Node<T> x = first.next; x != null; x = x.next) {
                   if (x.data == null) {
                       unlink(x);
                       return true;
                   }
               }
           } else {
               for (Node<T> x = first; x != null; x = x.next) {
                   if (data.equals(x.data)) {
                       unlink(x);
                       return true;
                   }
               }
           }
           return false;
       }

       @Override
       public T remove(int index) {
           checkElementIndex(index);
           //移除
           return  unlink(getNode(index));
       }

       /**
        * 根据值查下标
        * Blog : http://blog.csdn.net/javazejian
        * @param data
        * @return
        */
       @Override
       public int indexOf(T data) {
           int index = 0;
           if (data == null) {
               //注意起始结点
               for (Node<T> x = first.next; x != null; x = x.next) {
                   if (x.data == null)
                       return index;
                   index++;
               }
           } else {
               for (Node<T> x = first.next; x != null; x = x.next) {
                   if (data.equals(x.data))
                       return index;
                   index++;
               }
           }
           return -1;
       }

       /**
        * 根据data查询最后一个下标
        * Blog : http://blog.csdn.net/javazejian
        * @param data
        * @return
        */
       @Override
       public int lastIndexOf(T data) {
           int index = size;
           if (data == null) {
               for (Node<T> x = last.prev; x != null; x = x.prev) {
                   index--;
                   if (x.data == null)
                       return index;
               }
           } else {
               for (Node<T> x = last.prev; x != null; x = x.prev) {
                   index--;
                   if (data.equals(x.data))
                       return index;
               }
           }
           return -1;
       }

       /**
        * 删除x结点
        * Blog : http://blog.csdn.net/javazejian
        * @param x
        * @return
        */
       T unlink(Node<T> x) {
           // assert x != null;
           x.next.prev=x.prev;
           x.prev.next=x.next;
           size--;
           modCount++;
           return  x.data;
       }

       /**
        * 在succ结点前插入
        * Blog : http://blog.csdn.net/javazejian
        */
       void linkBefore(T T, Node<T> succ) {
           // assert succ != null;
           final Node<T> newNode = new Node<>(succ.prev, T, succ);
           succ.prev.next=newNode;
           succ.prev = newNode;
           size++;
           modCount++;
       }

       /**
        * 链表头部添加,由于拥有头结点和尾结点,无需判断插入情况
        * Blog : http://blog.csdn.net/javazejian
        * @param data
        */
       private void linkFirst(T data) {
           //头结点的下一个结点
           final Node<T> f = first.next;
           final Node<T> newNode = new Node<>(first, data, f);
           f.prev=newNode;
           first.next = newNode;
           size++;
           modCount++;
       }

       /**
        * 链表尾部添加,由于拥有头结点和尾结点,无需判断插入情况
        * Blog : http://blog.csdn.net/javazejian
        * @param data
        */
       void linkLast(T data) {
           //尾部结点的前一个结点
           final Node<T> l = last.prev;
           final Node<T> newNode = new Node<>(l, data, last);
           l.next = newNode;
           last.prev=newNode;
           size++;
           //记录修改
           modCount++;
       }

       /**
        * 优化结点查询,根据情况而定查询起点
        * Blog : http://blog.csdn.net/javazejian
        * @param index
        * @return
        */
       Node<T> getNode(int index) {
           //如果index小于size的一半,则从头结点开始查找,否则从尾部开始查找(右移2位相当除以2)
           if (index < (size >> 1)) {
               Node<T> x = first.next;
               for (int i = 0; i < index; i++)
                   x = x.next;
               return x;
           } else {
               Node<T> x = last.prev;
               for (int i = size - 1; i > index; i--)
                   x = x.prev;
               return x;
           }
       }

       /**
        * 判断index是否越界
        * Blog : http://blog.csdn.net/javazejian
        * @param index
        */
       private void checkElementIndex(int index) {
           if (!(index >= 0 && index < size))
               throw new IndexOutOfBoundsException("Index: "+index+", Size: "+size);
       }

       @Override
       public Iterator<T> iterator() {
           return new Itr();
       }

       /**
        * 迭代器,支持变量过程删除结点
        * Blog : http://blog.csdn.net/javazejian
        */
       private class Itr implements Iterator<T> {
           /**
            * 指向下一个结点的下标
            */
           int cursor = 0;

           /**
            * 当前需要返回结点的下标
            */
           int lastRet = -1;

           /**
            *用于判断是否集合被修改
            */
           int expectedModCount = modCount;

           /**
            * 是否还有下一个结点
            * @return
            */
           public boolean hasNext() {
               return cursor != size();
           }

           /**
            * 获取当前结点的值
            * @return
            */
           public T next() {
               checkForComodification();
               try {
                   int i = cursor;
                   T next = get(i);
                   lastRet = i;//指向当前结点
                   cursor = i + 1;//更新,指向下一个还未访问的结点
                   return next;
               } catch (IndexOutOfBoundsException T) {
                   checkForComodification();
                   throw new NoSuchElementException();
               }
           }

           public void remove() {
               if (lastRet < 0)
                   throw new IllegalStateException();
               checkForComodification();

               try {
                   MylinkeList.this.remove(lastRet);
                   if (lastRet < cursor)
                       cursor--;//回撤一位
                   lastRet = -1;//复原
                   expectedModCount = modCount;
               } catch (IndexOutOfBoundsException T) {
                   throw new ConcurrentModificationException();
               }
           }

           /**
            * 检测是否集合已变更
            * 快速失败机制
            */
           final void checkForComodification() {
               if (modCount != expectedModCount)
                   throw new ConcurrentModificationException();
           }
       }

       public ListIterator<T> listIterator(int index) {
           checkElementIndex(index);
           return new ListItr(index);
       }

       /**
        * 含前后指向的迭代器,支持变量过程添加元素,删除元素
        * Blog : http://blog.csdn.net/javazejian
        */
       private class ListItr implements ListIterator<T> {
           private Node<T> lastReturned;//指向当前正在被访问的结点
           private Node<T> next;//还未被访问的结点
           private int nextIndex;//还未被访问的结点下标
           private int expectedModCount = modCount;//用于判断集合是否被修改

           /**
            * 结点指向传入值index的结点
            * @param index
            */
           ListItr(int index) {
               // assert isPositionIndex(index);
               next = (index == size) ? null : getNode(index);
               nextIndex = index;
           }

           public boolean hasNext() {
               return nextIndex < size;
           }

           /**
            * 获取结点数据
            * @return
            */
           public T next() {
               checkForComodification();
               if (!hasNext())
                   throw new NoSuchElementException();

               lastReturned = next;//当前正在被访问的结点
               next = next.next;//更新至还未被访问的结点
               nextIndex++;//更新至还未被访问结点的下标
               return lastReturned.data;
           }

           /**
            * 是否有前驱结点
            * @return
            */
           public boolean hasPrevious() {
               return nextIndex > 0;
           }

           /**
            * 功能与next()一样,但previous()是往前遍历
            * @return
            */
           public T previous() {
               checkForComodification();
               if (!hasPrevious())
                   throw new NoSuchElementException();

               lastReturned = next = (next == null) ? last.prev : next.prev;
               nextIndex--;
               return lastReturned.data;
           }

           public int nextIndex() {
               return nextIndex;
           }

           public int previousIndex() {
               return nextIndex - 1;
           }

           /**
            * 移除操作
            */
           public void remove() {
               checkForComodification();
               if (lastReturned == null)
                   throw new IllegalStateException();

               Node<T> lastNext = lastReturned.next;
               unlink(lastReturned);
               //如果next还未更新,则直接执行lastNext
               if (next == lastReturned)
                   next = lastNext;
               else
                   //如果next已更新,那么nextIndex必定已执行了nextIndex++操作,此时由于删除结点
                   //所以必须执行nextIndex--,才能使nextIndex与next相对应
                   nextIndex--;

               //复原
               lastReturned = null;
               expectedModCount++;
           }

           public void set(T T) {
               if (lastReturned == null)
                   throw new IllegalStateException();
               checkForComodification();
               lastReturned.data = T;
           }

           public void add(T T) {
               checkForComodification();
               lastReturned = null;
               if (next == null)
                   linkLast(T);
               else
                   linkBefore(T, next);
               nextIndex++;
               expectedModCount++;
           }

           final void checkForComodification() {
               if (modCount != expectedModCount)
                   throw new ConcurrentModificationException();
           }
       }

       /**
        * 双向结点类
        * Blog : http://blog.csdn.net/javazejian
        * @param <T>
        */
       private static class Node<T> {
           T data;
           Node<T> next;
           Node<T> prev;

           Node(Node<T> prev, T data, Node<T> next) {
               this.data = data;
               this.next = next;
               this.prev = prev;
           }
       }

       //测试
       public static void main(String[] args){
           System.out.println("------init-------");
           MylinkeList<Integer> mylinkeList=new MylinkeList<>();
           mylinkeList.add(2);
           mylinkeList.add(10);
           mylinkeList.add(1);
           mylinkeList.add(9);
           mylinkeList.add(20);
           mylinkeList.add(555);

           print(mylinkeList);
           System.out.println("------remove(2)-------");
           mylinkeList.remove(2);
           print(mylinkeList);
           System.out.println("------indexOf(10)&set(0,0)-------");
           System.out.println("index-->"+mylinkeList.indexOf(10));
           mylinkeList.set(0,0);
           print(mylinkeList);

           System.out.println("-------------iterator--------------");
           Iterator<Integer> iterator=mylinkeList.iterator();
           while (iterator.hasNext()){
               System.out.println("iterator.next-->"+iterator.next());
           }

           System.out.println("-------------iteratorList--------------");
           ListIterator<Integer> iteratorList=mylinkeList.listIterator(0);
           iteratorList.add(88);
           while (iteratorList.hasNext()){
               System.out.println("iteratorList.next-->"+iteratorList.next());
           }
           iteratorList.add(100);
           System.out.println("-------------iteratorList1.add--------------");
           //使用完后必须重新new
           ListIterator<Integer> iteratorList1=mylinkeList.listIterator(0);
           while (iteratorList1.hasNext()){
               int i=iteratorList1.next();
               if(i==555){
                   System.out.println("i==555");
                   iteratorList1.remove();
               }else {
                   System.out.println("iteratorList.next-->" +i);
               }
           }

           System.out.println("-------------foreach--------------");
           for(Integer data : mylinkeList){
               System.out.println("data-->"+data);
           }

           System.out.println("-------------iterator--------------");
           //抛异常:java.util.ConcurrentModificationException
           //在迭代时删除元素必须使用iterator自身的删除方法,使用mylinkeList的
           //删除方法将会触发快速失败机制
           Iterator<Integer> it = mylinkeList.iterator();
           while (it.hasNext()) {
               mylinkeList.remove(new Integer(100));
               Integer value = it.next();
               if (value==100) {
                   System.out.println("该集合含100!");
               }else {
                   System.out.println("该集合不含100!");
               }
           }
       }

       public static void print(MylinkeList mylinkeList){
           for (int i=0;i<mylinkeList.size();i++) {
               System.out.println("i->"+mylinkeList.get(i));
           }
       }

    }

源码地址如下：  
[github源码下载，欢迎star（含文章列表，持续更新）](https://github.com/shinezejian/javaStructures)

<font size="4">关联文章:</font>

[java数据结构与算法之顺序表与链表设计与实现分析](http://blog.csdn.net/javazejian/article/details/52953190)  
[java数据结构与算法之双链表设计与实现](http://blog.csdn.net/javazejian/article/details/53047590)  
[java数据结构与算法之改良顺序表与双链表类似ArrayList和LinkedList（带Iterator迭代器与fast-fail机制）](http://blog.csdn.net/javazejian/article/details/53073995)

</div>

<link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet"></div>

</article>

</div>
