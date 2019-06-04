# ArrayList和LinkedList学习


## 摘要
ArrayList和LinkedList是对List接口的不同数据结构的实现。它们都是线程不安全的，线程不安全往往出现在数组的扩容、数据添加的时候。

## 一、ArrayList和LinkedList是什么？
ArrayList：ArrayList是List接口的可变数组的实现。

LinkedList：LinkedList是List接口的（双向）链表实现。

## 二、两个List的数据结构
### 1、ArrayList的数据结构
ArrayList的类继承图如下：

![](https://github.com/hanweicone/test1/blob/master/img/arraylist%E7%BB%A7%E6%89%BF%E5%9B%BE.png)

（1-1：ArrayList的类继承图）
存储

ArrayList使用数组（elememntData）存储数据，默认构造方法创建ArrayList时，会初始化一个空数组。

扩容

ArrayList使用数组存储数据，因此在添加数据的时候需要做容量检查，如果容量不足则需要进行扩容。

其新容量大小公式为：新容量=旧容量+旧容量/2

扩容过程请看下面源码：

    public boolean add(E e) {
        // 容量检查
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        elementData[size++] = e;
        return true;
    }

    // 计算数组需要的最小容量
    private void ensureCapacityInternal(int minCapacity) {
        if (elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA) {
            minCapacity = Math.max(DEFAULT_CAPACITY, minCapacity);
        }

        ensureExplicitCapacity(minCapacity);
    }

    // 判断是否需要扩容，如果需要则扩容
    private void ensureExplicitCapacity(int minCapacity) {
        // modCount表示List结构修改的次数，快速失败机制会用到，快速失败机制在后面会详细说明。
        modCount++;

        // overflow-conscious code
        if (minCapacity - elementData.length > 0)
            grow(minCapacity);
    }

    private void grow(int minCapacity) {
        // overflow-conscious code
        int oldCapacity = elementData.length;
        // 新容量=旧容量+旧容量/2
        int newCapacity = oldCapacity + (oldCapacity >> 1);
        if (newCapacity - minCapacity < 0)
            newCapacity = minCapacity;
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        // minCapacity is usually close to size, so this is a win:
        elementData = Arrays.copyOf(elementData, newCapacity);
    }
（1-2：ArrayList数组扩容源码）

### 2、LinkedList的数据结构
LinkedList的类继承图如下：

![](https://github.com/hanweicone/test1/blob/master/img/LinkedList%E7%9A%84%E7%B1%BB%E7%BB%A7%E6%89%BF%E5%9B%BE.png)

（2-1：LinkedList的类继承图）
存储

LinkedList使用双向链表来存储数据。其中链表结点定义如下：

    private static class Node<E> {
        E item;
        Node<E> next;
        Node<E> prev;

        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }
（2-2：LinkedList的存储结点定义）
添加/删除元素操作

LinkedList添加删除元素，实际上就是对链表进行结点添加/删除，下面给出实现细节，以供后面的线程安全讨论使用（注意modCount发生了变化）。

    // 添加元素
    public boolean add(E e) {
        // 往链表末尾添加元素
        linkLast(e);
        return true;
    }
    // 添加结点
    void linkLast(E e) {
        final Node<E> l = last;
        final Node<E> newNode = new Node<>(l, e, null);
        // 新结点作为尾结点
        last = newNode;
        if (l == null)
            first = newNode;
        else
            l.next = newNode; // 连接结点
        size++;
        modCount++;
    }

    // 删除元素（删除第一个匹配的元素）
    public boolean remove(Object o) {
        if (o == null) {
            for (Node<E> x = first; x != null; x = x.next) {
                if (x.item == null) {
                    unlink(x);
                    return true;
                }
            }
        } else {
            for (Node<E> x = first; x != null; x = x.next) {
                if (o.equals(x.item)) {
                    unlink(x);
                    return true;
                }
            }
        }
        return false;
    }
    // 删除结点
    E unlink(Node<E> x) {
        // assert x != null;
        final E element = x.item;
        final Node<E> next = x.next;
        final Node<E> prev = x.prev;

        if (prev == null) {
            first = next;
        } else {
            prev.next = next;
            x.prev = null;
        }

        if (next == null) {
            last = prev;
        } else {
            next.prev = prev;
            x.next = null;
        }

        x.item = null;
        size--;
        modCount++;
        return element;
    }
（2-3：LinkedList添加/删除结点关键代码）

## 三、线程安全讨论
首先确认一点的是，ArrayList和LinkedList均是线程不安全的，下面将分析多线程情况下会出现的一些问题。

### 1、快速失败（fail-fast）
快速失败，指的是使用遍历器对List进行遍历时，如果在遍历过程中，对List进行了修改，则会触发快速失败机制，抛出java.util.ConcurrentModificationException异常。

快速失败触发机制

前文谈到modCount的作用用于记录List的修改次数，在遍历器进行遍历时，代码正是通过这个值触发快速失败的。

相关核心代码如下：

    int expectedModCount = modCount;

    public E next() {
        checkForComodification();
        try {
            int i = cursor;
            E next = get(i);
            lastRet = i;
            cursor = i + 1;
            return next;
        } catch (IndexOutOfBoundsException e) {
            checkForComodification();
            throw new NoSuchElementException();
        }
    }

    // 检查修改次数，该方法在类中多次会被调用
    final void checkForComodification() {
        if (modCount != expectedModCount)
            throw new ConcurrentModificationException();
    }
（1-1：java.util.AbstractList内部类Itr代码片段）
### 2、ArrayList添加元素时的数组越界问题
添加元素时的数组越界问题发生在扩容判断上，当当前数组容量还差一个元素达到数组扩容的临界值时。并发插入元素时对数组大小的判断均是无需扩容，但是当前数组实际上仅有一个空闲位置，因此数组越界异常就发生了。

### 3、添加元素被覆盖
这种异常出现情况如下面代码注释所示：

多个线程对数组同一个位置进行赋值，导致元素被覆盖。

    elementData[size++] = e;
    // elementData[size] = e;  --- thread1
    // elementData[size] = e;  --- thread2
    // size++; --- thread1
    // size++; --- thread2
（3-1：ArrayList添加元素被覆盖）
类似的分析，LinkedList添加元素时也会出现这种情况。

### 4、线程安全的List
同步方法

全部使用同步方法，如：Vector、Collections.synchronizedList(list)

其它加锁

其它加锁实现线程安全，如：ConcurrentLinkedDeque（自旋+CAS）、CopyOnWriteArrayList（读写锁）

参考资料

[JAVA学习-ArrayList详解](https://www.jianshu.com/p/92373a603d42) 

[JAVA学习-LinkedList详解](https://www.jianshu.com/p/732b5294a985) 

[Java的快速失败和安全失败](https://www.cnblogs.com/ygj0930/p/6543350.html) 

[ArrayList线程不安全的表现](https://www.toocruel.net/arraylistxian-cheng-bu-an-quan-de-biao-xian/) 

[聊聊并发-Java中的Copy-On-Write容器](http://ifeve.com/java-copy-on-write/) 
