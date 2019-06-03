<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">
              <div class="article-copyright">

          版权声明：本文为博主原创文章，未经博主允许不得转载。          https://blog.csdn.net/jianyuerensheng/article/details/51200274        </div>
            <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">
                              <div id="content_views" class="markdown_views">
            <!-- flowchart 箭头图标 勿删 -->
            <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
              <path stroke-linecap="round" d="M5,0 0,2.5 5,5z" id="raphael-marker-block" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></path>
            </svg>

## <a name="t0"></a>一：单向链表基本介绍

链表是一种数据结构，和数组同级。比如，Java中我们使用的ArrayList，其实现原理是数组。而LinkedList的实现原理就是链表了。链表在进行循环遍历时效率不高，但是插入和删除时优势明显。下面对单向链表做一个介绍。

单向链表是一种线性表，实际上是由节点（Node）组成的，一个链表拥有不定数量的节点。其数据在内存中存储是不连续的，它存储的数据分散在内存中，每个结点只能也只有它能知道下一个结点的存储位置。由N各节点（Node）组成单向链表，每一个Node记录本Node的数据及下一个Node。向外暴露的只有一个头节点（Head），我们对链表的所有操作，都是直接或者间接地通过其头节点来进行的。 

![这里写图片描述](https://img-blog.csdn.net/20160420141138723) 

上图中最左边的节点即为头结点（Head），但是添加节点的顺序是从右向左的，添加的新节点会被作为新节点。最先添加的节点对下一节点的引用可以为空。引用是引用下一个节点而非下一个节点的对象。因为有着不断的引用，所以头节点就可以操作所有节点了。 

 下图描述了单向链表存储情况。存储是分散的，每一个节点只要记录下一节点，就把所有数据串了起来，形成了一个单向链表。 

![这里写图片描述](https://img-blog.csdn.net/20160420134010570) 

节点（Node）是由一个需要储存的对象及对下一个节点的引用组成的。也就是说，节点拥有两个成员：储存的对象、对下一个节点的引用。下面图是具体的说明：

![这里写图片描述](https://img-blog.csdn.net/20160420134000174)

## <a name="t1"></a>二、单项链表的实现

<pre class="prettyprint" name="code">`<span class="hljs-keyword">package</span> com.zjn.LinkAndQueue;

<span class="hljs-javadoc">/**
 * 自定义链表设计
 * 
 *<span class="hljs-javadoctag"> @author</span> zjn
 *
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyLink</span> {</span>
    Node head = <span class="hljs-keyword">null</span>; <span class="hljs-comment">// 头节点</span>

    <span class="hljs-javadoc">/**
     * 链表中的节点，data代表节点的值，next是指向下一个节点的引用
     * 
     *<span class="hljs-javadoctag"> @author</span> zjn
     *
     */</span>
    class Node {
        Node next = <span class="hljs-keyword">null</span>;<span class="hljs-comment">// 节点的引用，指向下一个节点</span>
        <span class="hljs-keyword">int</span> data;<span class="hljs-comment">// 节点的对象，即内容</span>

        <span class="hljs-keyword">public</span> <span class="hljs-title">Node</span>(<span class="hljs-keyword">int</span> data) {
            <span class="hljs-keyword">this</span>.data = data;
        }
    }

    <span class="hljs-javadoc">/**
     * 向链表中插入数据
     * 
     *<span class="hljs-javadoctag"> @param</span> d
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">addNode</span>(<span class="hljs-keyword">int</span> d) {
        Node newNode = <span class="hljs-keyword">new</span> Node(d);<span class="hljs-comment">// 实例化一个节点</span>
        <span class="hljs-keyword">if</span> (head == <span class="hljs-keyword">null</span>) {
            head = newNode;
            <span class="hljs-keyword">return</span>;
        }
        Node tmp = head;
        <span class="hljs-keyword">while</span> (tmp.next != <span class="hljs-keyword">null</span>) {
            tmp = tmp.next;
        }
        tmp.next = newNode;
    }

    <span class="hljs-javadoc">/**
     * 
     *<span class="hljs-javadoctag"> @param</span> index:删除第index个节点
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">deleteNode</span>(<span class="hljs-keyword">int</span> index) {
        <span class="hljs-keyword">if</span> (index &lt; <span class="hljs-number">1</span> || index &gt; length()) {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        }
        <span class="hljs-keyword">if</span> (index == <span class="hljs-number">1</span>) {
            head = head.next;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
        }
        <span class="hljs-keyword">int</span> i = <span class="hljs-number">1</span>;
        Node preNode = head;
        Node curNode = preNode.next;
        <span class="hljs-keyword">while</span> (curNode != <span class="hljs-keyword">null</span>) {
            <span class="hljs-keyword">if</span> (i == index) {
                preNode.next = curNode.next;
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
            }
            preNode = curNode;
            curNode = curNode.next;
            i++;
        }
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
    }

    <span class="hljs-javadoc">/**
     * 
     *<span class="hljs-javadoctag"> @return</span> 返回节点长度
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">length</span>() {
        <span class="hljs-keyword">int</span> length = <span class="hljs-number">0</span>;
        Node tmp = head;
        <span class="hljs-keyword">while</span> (tmp != <span class="hljs-keyword">null</span>) {
            length++;
            tmp = tmp.next;
        }
        <span class="hljs-keyword">return</span> length;
    }

    <span class="hljs-javadoc">/**
     * 在不知道头指针的情况下删除指定节点
     * 
     *<span class="hljs-javadoctag"> @param</span> n
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">deleteNode11</span>(Node n) {
        <span class="hljs-keyword">if</span> (n == <span class="hljs-keyword">null</span> || n.next == <span class="hljs-keyword">null</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        <span class="hljs-keyword">int</span> tmp = n.data;
        n.data = n.next.data;
        n.next.data = tmp;
        n.next = n.next.next;
        System.out.println(<span class="hljs-string">"删除成功！"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
    }

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printList</span>() {
        Node tmp = head;
        <span class="hljs-keyword">while</span> (tmp != <span class="hljs-keyword">null</span>) {
            System.out.println(tmp.data);
            tmp = tmp.next;
        }
    }

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(String[] args) {
        MyLink list = <span class="hljs-keyword">new</span> MyLink();
        list.addNode(<span class="hljs-number">5</span>);
        list.addNode(<span class="hljs-number">3</span>);
        list.addNode(<span class="hljs-number">1</span>);
        list.addNode(<span class="hljs-number">2</span>);
        list.addNode(<span class="hljs-number">55</span>);
        list.addNode(<span class="hljs-number">36</span>);
        System.out.println(<span class="hljs-string">"linkLength:"</span> + list.length());
        System.out.println(<span class="hljs-string">"head.data:"</span> + list.head.data);
        list.printList();
        list.deleteNode(<span class="hljs-number">4</span>);
        System.out.println(<span class="hljs-string">"After deleteNode(4):"</span>);
        list.printList();
    }
}
<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15
*   16
*   17
*   18
*   19
*   20
*   21
*   22
*   23
*   24
*   25
*   26
*   27
*   28
*   29
*   30
*   31
*   32
*   33
*   34
*   35
*   36
*   37
*   38
*   39
*   40
*   41
*   42
*   43
*   44
*   45
*   46
*   47
*   48
*   49
*   50
*   51
*   52
*   53
*   54
*   55
*   56
*   57
*   58
*   59
*   60
*   61
*   62
*   63
*   64
*   65
*   66
*   67
*   68
*   69
*   70
*   71
*   72
*   73
*   74
*   75
*   76
*   77
*   78
*   79
*   80
*   81
*   82
*   83
*   84
*   85
*   86
*   87
*   88
*   89
*   90
*   91
*   92
*   93
*   94
*   95
*   96
*   97
*   98
*   99
*   100
*   101
*   102
*   103
*   104
*   105
*   106
*   107
*   108
*   109
*   110
*   111
*   112
*   113
*   114
*   115
*   116
*   117
*   118
*   119
*   120
*   121
*   122
*   123
*   124
*   125
*   126
*   127
*   128</pre>

## <a name="t2"></a>三、链表相关的常用操作实现方法

**1. 链表反转**

<pre class="prettyprint" name="code">`<span class="hljs-javadoc">/**
     * 链表反转
     * 
     *<span class="hljs-javadoctag"> @param</span> head
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> Node <span class="hljs-title">ReverseIteratively</span>(Node head) {
        Node pReversedHead = head;
        Node pNode = head;
        Node pPrev = <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">while</span> (pNode != <span class="hljs-keyword">null</span>) {
            Node pNext = pNode.next;
            <span class="hljs-keyword">if</span> (pNext == <span class="hljs-keyword">null</span>) {
                pReversedHead = pNode;
            }
            pNode.next = pPrev;
            pPrev = pNode;
            pNode = pNext;
        }
        <span class="hljs-keyword">this</span>.head = pReversedHead;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.head;
    }<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15
*   16
*   17
*   18
*   19
*   20
*   21
*   22</pre>

**2. 查找单链表的中间节点**

采用快慢指针的方式查找单链表的中间节点，快指针一次走两步，慢指针一次走一步，当快指针走完时，慢指针刚好到达中间节点。

<pre class="prettyprint" name="code">`<span class="hljs-javadoc">/**
     * 查找单链表的中间节点
     * 
     *<span class="hljs-javadoctag"> @param</span> head
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> Node <span class="hljs-title">SearchMid</span>(Node head) {
        Node p = <span class="hljs-keyword">this</span>.head, q = <span class="hljs-keyword">this</span>.head;
        <span class="hljs-keyword">while</span> (p != <span class="hljs-keyword">null</span> &amp;&amp; p.next != <span class="hljs-keyword">null</span> &amp;&amp; p.next.next != <span class="hljs-keyword">null</span>) {
            p = p.next.next;
            q = q.next;
        }
        System.out.println(<span class="hljs-string">"Mid:"</span> + q.data);
        <span class="hljs-keyword">return</span> q;
    }<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15</pre>

**3.  查找倒数第k个元素**

采用两个指针P1,P2，P1先前移K步，然后P1、P2同时移动，当p1移动到尾部时，P2所指位置的元素即倒数第k个元素 。

<pre class="prettyprint" name="code">`<span class="hljs-javadoc">/**
     * 查找倒数 第k个元素
     * 
     *<span class="hljs-javadoctag"> @param</span> head
     *<span class="hljs-javadoctag"> @param</span> k
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> Node <span class="hljs-title">findElem</span>(Node head, <span class="hljs-keyword">int</span> k) {
        <span class="hljs-keyword">if</span> (k &lt; <span class="hljs-number">1</span> || k &gt; <span class="hljs-keyword">this</span>.length()) {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
        }
        Node p1 = head;
        Node p2 = head;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i &lt; k; i++)<span class="hljs-comment">// 前移k步</span>
            p1 = p1.next;
        <span class="hljs-keyword">while</span> (p1 != <span class="hljs-keyword">null</span>) {
            p1 = p1.next;
            p2 = p2.next;
        }
        <span class="hljs-keyword">return</span> p2;
    }<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15
*   16
*   17
*   18
*   19
*   20
*   21</pre>

**4. 对链表进行排序**

<pre class="prettyprint" name="code">`<span class="hljs-javadoc">/**
     * 排序
     * 
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> Node <span class="hljs-title">orderList</span>() {
        Node nextNode = <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">int</span> tmp = <span class="hljs-number">0</span>;
        Node curNode = head;
        <span class="hljs-keyword">while</span> (curNode.next != <span class="hljs-keyword">null</span>) {
            nextNode = curNode.next;
            <span class="hljs-keyword">while</span> (nextNode != <span class="hljs-keyword">null</span>) {
                <span class="hljs-keyword">if</span> (curNode.data &gt; nextNode.data) {
                    tmp = curNode.data;
                    curNode.data = nextNode.data;
                    nextNode.data = tmp;
                }
                nextNode = nextNode.next;
            }
            curNode = curNode.next;
        }
        <span class="hljs-keyword">return</span> head;
    }<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15
*   16
*   17
*   18
*   19
*   20
*   21
*   22
*   23</pre>

**5. 删除链表中的重复节点**

<pre class="prettyprint" name="code">`<span class="hljs-javadoc">/**
     * 删除重复节点
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">deleteDuplecate</span>(Node head) {
        Node p = head;
        <span class="hljs-keyword">while</span> (p != <span class="hljs-keyword">null</span>) {
            Node q = p;
            <span class="hljs-keyword">while</span> (q.next != <span class="hljs-keyword">null</span>) {
                <span class="hljs-keyword">if</span> (p.data == q.next.data) {
                    q.next = q.next.next;
                } <span class="hljs-keyword">else</span>
                    q = q.next;
            }
            p = p.next;
        }

    }<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15
*   16
*   17</pre>

**6. 从尾到头输出单链表，采用递归方式实现**

<pre class="prettyprint" name="code">`<span class="hljs-javadoc">/**
     * 从尾到头输出单链表，采用递归方式实现
     * 
     *<span class="hljs-javadoctag"> @param</span> pListHead
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printListReversely</span>(Node pListHead) {
        <span class="hljs-keyword">if</span> (pListHead != <span class="hljs-keyword">null</span>) {
            printListReversely(pListHead.next);
            System.out.println(<span class="hljs-string">"printListReversely:"</span> + pListHead.data);
        }
    }<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11</pre>

**7. 判断链表是否有环，有环情况下找出环的入口节点**

<pre class="prettyprint" name="code">`<span class="hljs-javadoc">/**
     * 判断链表是否有环，单向链表有环时，尾节点相同
     * 
     *<span class="hljs-javadoctag"> @param</span> head
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">IsLoop</span>(Node head) {
        Node fast = head, slow = head;
        <span class="hljs-keyword">if</span> (fast == <span class="hljs-keyword">null</span>) {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        }
        <span class="hljs-keyword">while</span> (fast != <span class="hljs-keyword">null</span> &amp;&amp; fast.next != <span class="hljs-keyword">null</span>) {
            fast = fast.next.next;
            slow = slow.next;
            <span class="hljs-keyword">if</span> (fast == slow) {
                System.out.println(<span class="hljs-string">"该链表有环"</span>);
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
            }
        }
        <span class="hljs-keyword">return</span> !(fast == <span class="hljs-keyword">null</span> || fast.next == <span class="hljs-keyword">null</span>);
    }

    <span class="hljs-javadoc">/**
     * 找出链表环的入口
     * 
     *<span class="hljs-javadoctag"> @param</span> head
     *<span class="hljs-javadoctag"> @return</span>
     */</span>
    <span class="hljs-keyword">public</span> Node <span class="hljs-title">FindLoopPort</span>(Node head) {
        Node fast = head, slow = head;
        <span class="hljs-keyword">while</span> (fast != <span class="hljs-keyword">null</span> &amp;&amp; fast.next != <span class="hljs-keyword">null</span>) {
            slow = slow.next;
            fast = fast.next.next;
            <span class="hljs-keyword">if</span> (slow == fast)
                <span class="hljs-keyword">break</span>;
        }
        <span class="hljs-keyword">if</span> (fast == <span class="hljs-keyword">null</span> || fast.next == <span class="hljs-keyword">null</span>)
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
        slow = head;
        <span class="hljs-keyword">while</span> (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        <span class="hljs-keyword">return</span> slow;
    }
<div class="hljs-button {2}" data-title="复制"></div>`

*   1
*   2
*   3
*   4
*   5
*   6
*   7
*   8
*   9
*   10
*   11
*   12
*   13
*   14
*   15
*   16
*   17
*   18
*   19
*   20
*   21
*   22
*   23
*   24
*   25
*   26
*   27
*   28
*   29
*   30
*   31
*   32
*   33
*   34
*   35
*   36
*   37
*   38
*   39
*   40
*   41
*   42
*   43
*   44
*   45
*   46</pre>          </div>
          <link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet">
                  </div>
