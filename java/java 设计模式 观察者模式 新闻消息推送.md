<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-1 float-left">原</span>

# java 设计模式 观察者模式 新闻消息推送

</div>

<div class="article-info-box">

<div class="article-bar-top"><span class="time">2017年06月22日 15:20:07</span> [彼天](https://me.csdn.net/android_hl) <span class="read-count">阅读数：1410</span></div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">

<div class="article-copyright">版权声明：本文为博主原创文章，未经博主允许不得转载。 https://blog.csdn.net/android_hl/article/details/73572549</div>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">

<div id="content_views" class="markdown_views">

观察者模式，字面意思有个观察者，那么就应该有一个被观察者。两个定义：  
观察者：Observer （比如新闻客户端，你自己的微信号）  
被观察者：Observable（新闻推送端，你关注的微信公众号）  
1.观察者可以同时订阅多个被观察者。  
2.被观察者可以同时被多个观察者订阅。  
3.被观察者发生改变时会影响到所有的观察者。  
![这里写图片描述](https://img-blog.csdn.net/20140420130751265?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbG1qNjIzNTY1Nzkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)  
对于每个用户都存在这三条线路。  
Java中已经帮我们实现了观察者模式，借助于java.util.Observable和java.util.Observer。  
接下来代码时间。  
需求：新闻推送端News，需要向某个客户ClientX端推送消息，客户端可以选择去打开或者关闭推送功能。  
**新闻推送端News代码**

    package test;

    import java.util.Observable;

    public class News extends Observable{

        private String news;

        public String getNews() {
            return news;
        }

        public void setNews(String news) {
            this.news = news;
            //发生改变
            setChanged();
            //推送消息到客户端
            notifyObservers();
        }
    }

**新闻客户端代码**

    package test;

    import java.util.Observable;
    import java.util.Observer;

    public class ClientX implements Observer {

        /**
         * 打开推送功能
         * @param observable  被观察者对象（这里是新闻推送端）
         */
        public void openPushMsg(Observable observable)  
        {  
            //添加到观察者列表
            observable.addObserver(this);  
        } 
        /**
         * 实现接口重新的方法
         * 有新消息推送来时，会被调用
         */
        public void update(Observable observable, Object arg) {
            if(observable instanceof News){//判断是否来自新闻推送端
                News news=(News) observable;
                System.out.println("现在最新消息："+news.getNews());
            }

        }
        /**
         * 关闭推送功能
         * @param observable  被观察者对象（这里是新闻推送端）
         */
        public void closePushMsg(Observable observable){
            //从观察者列表移除
            observable.deleteObserver(this);
        }

    }

**测试**

    package test;

    public class Test  
    {  
        public static void main(String[] args)  
        {  
            News news=new News();
            ClientX bObserver1=new ClientX();
            //客户端打开推送功能
            bObserver1.openPushMsg(news);
            news.setNews("世界末日了");
            //客户端关闭推送功能
            bObserver1.closePushMsg(news);
            news.setNews("发现新大陆");

        }  
    }

执行结果：

    现在最新消息：世界末日了

从执行结果上来看，只执行了打开推送功能时的消息推送。

**java.util.Observable和java.util.Observer，的源码解析**

*   先看一下观察者Observer接口的源码：

    /*
     * Copyright (c) 1994, 1998, Oracle and/or its affiliates. All rights reserved.
     * ORACLE PROPRIETARY/CONFIDENTIAL. Use is subject to license terms.

     */
    package java.util;

    /**
     * A class can implement the <code>Observer</code> interface when it
     * wants to be informed of changes in observable objects.
     *
     * @author  Chris Warth
     * @see     java.util.Observable
     * @since   JDK1.0
     */
    public interface Observer {
        /**
         * This method is called whenever the observed object is changed. An
         * application calls an <tt>Observable</tt> object's
         * <code>notifyObservers</code> method to have all the object's
         * observers notified of the change.
         *
         * @param   o     the observable object.
         * @param   arg   an argument passed to the <code>notifyObservers</code>
         *                 method.
         */
        void update(Observable o, Object arg);
    }

打开之后就一个update（）的方法。每当被观察者改变的时候，这个方法会得到执行。而且通过方法我们可以得到被观察者对象和传递的一个Object对象。

*   Observable的源码  
    代码虽然不多，也就不到一百行吧，但是注释太多，先看结构图吧：  
    ![这里写图片描述](https://img-blog.csdn.net/20170622145402404?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYW5kcm9pZF9obA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)  
    一个boolean changed变量用来判断，被观察者是否改变。  
    一个Vector< Observer > obs集合对象，用来保存注册的观察者。
*   **addObserver**

    /**
         * Adds an observer to the set of observers for this object, provided
         * that it is not the same as some observer already in the set.
         * The order in which notifications will be delivered to multiple
         * observers is not specified. See the class comment.
         *
         * @param   o   an observer to be added.
         * @throws NullPointerException   if the parameter o is null.
         */
        public synchronized void addObserver(Observer o) {
            if (o == null)
                throw new NullPointerException();
            if (!obs.contains(o)) {
                obs.addElement(o);
            }
        }

如果传递进来的观察者对象不为空，就添加进集合中

*   **deleteObserver**

     /**
         * Deletes an observer from the set of observers of this object.
         * Passing <CODE>null</CODE> to this method will have no effect.
         * @param   o   the observer to be deleted.
         */
        public synchronized void deleteObserver(Observer o) {
            obs.removeElement(o);
        }

有添加就有移除，移除观察者对象。

*   **notifyObservers无参**

    public void notifyObservers() {
            notifyObservers(null);
        }

无参的唤醒方法会调用有参的唤醒方法。

*   列表内容

     public void notifyObservers(Object arg) {
            Object[] arrLocal;

            synchronized (this) {

                if (!changed)
                    return;
                arrLocal = obs.toArray();
                clearChanged();
            }

            for (int i = arrLocal.length-1; i>=0; i--)
                ((Observer)arrLocal[i]).update(this, arg);
        }

如果被观察者发生改变，就会把集合变成数组，然后遍历数组，调用每个观察者的update方法。

几个主要的方法就这么多，所有的被观察者的注册、取消注册和唤醒观察者的方法都是一样的。java封装成一个类就完成了方法的重复利用。如果采用面向接口的设计模式，那么不同的被观察者就必须去实现这些方法，而这些方法的逻辑是一样的，就不能重复利用代码了。

</div>

<link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet"></div>

</article>

</div>
