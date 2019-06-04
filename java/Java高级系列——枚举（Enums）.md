# Java高级系列——枚举（Enums）
## 一、介绍

<p>本系列文章的这一部分我们将会介绍Java 5版本之后引入的除泛型之外的另外一个强大特性：枚举。可以将枚举看成一种特殊的类，并且可以将注解看成一种特殊的接口。</p>

<p>枚举的思想很简单，也很方便：它代表了一组固定的常量值。实际上，枚举经常用来设计一些状态常量。比如，星期几就是枚举的一个最好例子，因为他们被限制在周一、周二、周三、周四、周五、 周六和周日。</p>

<p><strong>二、枚举作为特殊的类</strong></p>

<p>在枚举被引入Java语言之前，在Java中模拟一组固定值的常规方法是通过声明一组常量。例如：</p>

<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DaysOfTheWeekConstants</span> {</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> MONDAY = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> TUESDAY = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> WEDNESDAY = <span class="hljs-number">2</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> THURSDAY = <span class="hljs-number">3</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> FRIDAY = <span class="hljs-number">4</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> SATURDAY = <span class="hljs-number">5</span>;
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> SUNDAY = <span class="hljs-number">6</span>;
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>

<p>虽然这种方法有效，但远非理想的解决方案。主要是因为常量本身只是int类型的值，而代码中需要这些常量（而不是任意的int值）的每一个地方都应该被一直明确地记录和断言。从语义上来讲，比如下面的这个方法演示所表现出来的就不符合类型安全的概念：</p>



<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>( <span class="hljs-keyword">int</span> day ) {
    <span class="hljs-keyword">return</span>( day == SATURDAY || day == SUNDAY );
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>从逻辑角度去看，day参数应该是在DaysOfTheWeekConstants类中声明的值之一。然而，如果没有编写额外的说明文档（给后来的一些人阅读），就不可能猜测到这一点。对于Java编译器来说类似于isWeekend(100)的这种调用看起来完全是正确的并且不会引起任何顾虑。</p>

<p>此时枚举就能解决这些问题。枚举允许用类型化的值替换常量并在任何地方使用这些类型。让我们使用枚举重写上面的方案。</p>



<pre class="prettyprint" name="code"><code class="hljs cs has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">enum</span> DaysOfTheWeek {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li></ul></pre>

<p>这里将关键字class改成了enum并且这些可能的值在枚举定义时被列举出来。有区别的一部分就是被声明在枚举类（在我们的例子中是DaysOfTheWeek ）中的每一个单独的值都是一个实例。因此，每当枚举被使用，Java编译器都能够进行类型检查。比如：</p>



<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>(DaysOfTheWeek day) {
    <span class="hljs-keyword">return</span>(day == SATURDAY || day == SUNDAY);
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>请注意枚举中的大写命名法的使用是一个约定，但是如果你不这样做也没有谁能够阻止你，但是最好还是遵守约定，这样更有利于代码的维护。</p>

<p><strong>三、枚举与实例字段（Enums and instance fields）</strong></p>

<p>枚举是一个特殊的类，因此它是可拓展的。这意味着他们可以有实例字段、构造器和方法（默认无参构造器不能够被声明并且所有的构造器必须被private修饰）。让我们使用枚举的实例和构造器添加一个isWeekend属性。</p>



<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">enum</span> DaysOfTheWeekFields {
    MONDAY(<span class="hljs-keyword">false</span>),
    TUESDAY(<span class="hljs-keyword">false</span>),
    WEDNESDAY(<span class="hljs-keyword">false</span>),
    THURSDAY(<span class="hljs-keyword">false</span>),
    FRIDAY(<span class="hljs-keyword">false</span>),
    SATURDAY(<span class="hljs-keyword">true</span>),
    SUNDAY(<span class="hljs-keyword">true</span>);

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">boolean</span> isWeekend;

    <span class="hljs-keyword">private</span> <span class="hljs-title">DaysOfTheWeekFields</span>( <span class="hljs-keyword">final</span> <span class="hljs-keyword">boolean</span> isWeekend ) {
        <span class="hljs-keyword">this</span>.isWeekend = isWeekend;
    }

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
        <span class="hljs-keyword">return</span> isWeekend;
    }
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li></ul></pre>

<p>我们看到，枚举值只是简单的调用了构造器而并没有要求使用new关键字。isWeekend()方法可以用来确定是否枚举值代表工作日或者周末。比如：</p>



<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>( DaysOfTheWeek day ) {
    <span class="hljs-keyword">return</span> day.isWeekend();
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>Java中枚举的实例字段有很大的用处。在常规的类声明规则中，它们经常用来将一些额外的细节与每个值相关联。</p>

<p><strong>四、枚举与接口（Enums and interfaces）</strong></p>

<p>另外一个强大的特性，我们再次确认一下枚举是是一个特殊的类，所以它能够实现接口（然而枚举不能够继承任何类）。比如，让我们引入接口DayOfWeek。</p>



<pre class="prettyprint" name="code"><code class="hljs axapta has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">DayOfWeek</span> {</span>
    <span class="hljs-keyword">boolean</span> isWeekend();
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>然后使用接口实现代替常规实例字段的方式重写前面的枚举例子。</p>



<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">enum</span> DaysOfTheWeekInterfaces implements DayOfWeek {
    MONDAY() {
        <span class="hljs-annotation">@Override</span>
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        }
    },
    TUESDAY() {
        <span class="hljs-annotation">@Override</span>
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        }
    },
    WEDNESDAY() {
        <span class="hljs-annotation">@Override</span>
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        }
    },
    THURSDAY() {
        <span class="hljs-annotation">@Override</span>
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        }
    },
    FRIDAY() {
        <span class="hljs-annotation">@Override</span>
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        }
    },
    SATURDAY() {
        <span class="hljs-annotation">@Override</span>
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
        }
    },
    SUNDAY() {
        <span class="hljs-annotation">@Override</span>
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">true</span>;
        }
    };
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li><li style="color: rgb(153, 153, 153);">21</li><li style="color: rgb(153, 153, 153);">22</li><li style="color: rgb(153, 153, 153);">23</li><li style="color: rgb(153, 153, 153);">24</li><li style="color: rgb(153, 153, 153);">25</li><li style="color: rgb(153, 153, 153);">26</li><li style="color: rgb(153, 153, 153);">27</li><li style="color: rgb(153, 153, 153);">28</li><li style="color: rgb(153, 153, 153);">29</li><li style="color: rgb(153, 153, 153);">30</li><li style="color: rgb(153, 153, 153);">31</li><li style="color: rgb(153, 153, 153);">32</li><li style="color: rgb(153, 153, 153);">33</li><li style="color: rgb(153, 153, 153);">34</li><li style="color: rgb(153, 153, 153);">35</li><li style="color: rgb(153, 153, 153);">36</li><li style="color: rgb(153, 153, 153);">37</li><li style="color: rgb(153, 153, 153);">38</li><li style="color: rgb(153, 153, 153);">39</li><li style="color: rgb(153, 153, 153);">40</li><li style="color: rgb(153, 153, 153);">41</li><li style="color: rgb(153, 153, 153);">42</li><li style="color: rgb(153, 153, 153);">43</li><li style="color: rgb(153, 153, 153);">44</li></ul></pre>

<p>我们实现接口的这种方式显得代码有些冗长，然而合并实例字段和接口实现可以解决这个问题，比如：</p>



<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">enum</span> DaysOfTheWeekFieldsInterfaces implements DayOfWeek {
    MONDAY( <span class="hljs-keyword">false</span> ),
    TUESDAY( <span class="hljs-keyword">false</span> ),
    WEDNESDAY( <span class="hljs-keyword">false</span> ),
    THURSDAY( <span class="hljs-keyword">false</span> ),
    FRIDAY( <span class="hljs-keyword">false</span> ),
    SATURDAY( <span class="hljs-keyword">true</span> ),
    SUNDAY( <span class="hljs-keyword">true</span> );

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">boolean</span> isWeekend;

    <span class="hljs-keyword">private</span> <span class="hljs-title">DaysOfTheWeekFieldsInterfaces</span>(<span class="hljs-keyword">final</span> <span class="hljs-keyword">boolean</span> isWeekend){
        <span class="hljs-keyword">this</span>.isWeekend = isWeekend;
    }

    <span class="hljs-annotation">@Override</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isWeekend</span>() {
        <span class="hljs-keyword">return</span> isWeekend;
    }
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li><li style="color: rgb(153, 153, 153);">14</li><li style="color: rgb(153, 153, 153);">15</li><li style="color: rgb(153, 153, 153);">16</li><li style="color: rgb(153, 153, 153);">17</li><li style="color: rgb(153, 153, 153);">18</li><li style="color: rgb(153, 153, 153);">19</li><li style="color: rgb(153, 153, 153);">20</li></ul></pre>

<p>通过支持实例字段和接口，枚举可以以更加面向对象的方式使用，从而带来一定程度的抽象。</p>

<p><strong>五、枚举与泛型</strong></p>

<p>在Java中，虽然咋一看并看不出来枚举和泛型的关系，但是他们之间存在一种关系。Java中的每一个单独的枚举自动继承自泛型类Enum&lt;T&gt;，在这里T就是枚举类型本身。Java编译器在编译时代表开发者做了这个转换，拓展一下枚举声明public enum DaysOfTheWeek 如下：</p>



<pre class="prettyprint" name="code"><code class="hljs php has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DaysOfTheWeek</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Enum</span>&lt; <span class="hljs-title">DaysOfTheWeek</span> &gt; {</span>
    <span class="hljs-comment">// Other declarations here</span>
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>这也就说明了为什么枚举可以实现接口但不能继承其他类：因为它隐式的继承自Enum&lt;T&gt;并且我们在使用对象的公共方法时已经讨论过，Java中不支持多继承。</p>

<p>实际上每一个继承自Enum&lt;T&gt;的枚举允许定义泛型类、接口和方法，通过这种方式可以让枚举类型的实例参数化或者类型参数化。比如：</p>



<pre class="prettyprint" name="code"><code class="hljs java has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span>&lt;T extends Enum&lt; ? &gt;&gt; <span class="hljs-keyword">void</span> <span class="hljs-title">performAction</span>(<span class="hljs-keyword">final</span> T instance) {
    <span class="hljs-comment">// Perform some action here</span>
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>在上面的方法声明中，类型T被约定为任意枚举类型的实例并且Java编译器将会对其做验证。</p>

<p><strong>六、枚举方法</strong></p>

<p>基础类 Enum&lt;T&gt;为自动继承它的枚举实例提供了一些非常有用的方法。</p>

<div class="table-box"><table>
<thead>
<tr>
  <th>方法</th>
  <th>描述</th>
</tr>
</thead>
<tbody><tr>
  <td>String name()</td>
  <td>返回枚举声明声明的枚举常量的名称</td>
</tr>
<tr>
  <td>int ordinal()</td>
  <td>返回枚举常量的次序（即枚举声明时的位置，初始常量分配的位置是0）</td>
</tr>
</tbody></table></div>


<p>此外，Java编译器为每个枚举类型自动生成两个更有用的静态方法（让我们将这个特殊的枚举类型假设为T）。</p>

<div class="table-box"><table>
<thead>
<tr>
  <th>方法</th>
  <th>描述</th>
</tr>
</thead>
<tbody><tr>
  <td>T[] values()</td>
  <td>返回枚举T所声明的所有常量</td>
</tr>
<tr>
  <td>T valueOf(String name)</td>
  <td>返回指定名称的枚举常量</td>
</tr>
</tbody></table></div>


<p>在代码中使用枚举还有一个好处：可以使用switch/case语法。例如：</p>



<pre class="prettyprint" name="code"><code class="hljs cs has-numbering" onclick="mdcp.copyCode(event)"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">performAction</span>( DaysOfTheWeek instance ) {
    <span class="hljs-keyword">switch</span>( instance ) {
    <span class="hljs-keyword">case</span> MONDAY:
        <span class="hljs-comment">// Do something</span>
    <span class="hljs-keyword">break</span>;

    <span class="hljs-keyword">case</span> TUESDAY:
        <span class="hljs-comment">// Do something</span>
    <span class="hljs-keyword">break</span>;

    <span class="hljs-comment">// Other enum constants here</span>
    }
}<div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li><li style="color: rgb(153, 153, 153);">5</li><li style="color: rgb(153, 153, 153);">6</li><li style="color: rgb(153, 153, 153);">7</li><li style="color: rgb(153, 153, 153);">8</li><li style="color: rgb(153, 153, 153);">9</li><li style="color: rgb(153, 153, 153);">10</li><li style="color: rgb(153, 153, 153);">11</li><li style="color: rgb(153, 153, 153);">12</li><li style="color: rgb(153, 153, 153);">13</li></ul></pre>

<p><strong>七、专用集合：EnumSet和EnumMap</strong></p>

<p>和所有其他类一样，枚举的实例也可以和标准Java集合库一起使用。然而，某些集合类型针对枚举做了优化，并且在大多数情况下推荐使用这些优化过后的集合代替通用的集合。</p>

<p>本节我们简单了解一下两个专用的集合：EnumSet&lt;T&gt;和EnumMap&lt;T, ?&gt;。这两个集合都非常容易使用。</p>

<p>我们首先来看一下EnumSet&lt;T&gt;集合。EnumSet&lt;T&gt;集合是常规的集合优化过后高效存储枚举类型的一个集合，EnumSet&lt;T&gt;不能够使用构造器进行实例化，但是它提供了很多非常有用的工厂方法。</p>

<p>比如，allOf工厂方法创建的EnumSet&lt;T&gt;实例就包含了所有枚举类型所枚举的常量：</p>



<pre class="prettyprint" name="code"><code class="hljs avrasm has-numbering" onclick="mdcp.copyCode(event)">final <span class="hljs-keyword">Set</span>&lt;DaysOfTheWeek&gt; enumSetAll = EnumSet<span class="hljs-preprocessor">.allOf</span>(DaysOfTheWeek<span class="hljs-preprocessor">.class</span>)<span class="hljs-comment">;</span><div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>noneOf工厂方法创建的是一个空的EnumSet&lt;T&gt;实例：</p>



<pre class="prettyprint" name="code"><code class="hljs avrasm has-numbering" onclick="mdcp.copyCode(event)">final <span class="hljs-keyword">Set</span>&lt;DaysOfTheWeek&gt; enumSetNone = EnumSet<span class="hljs-preprocessor">.noneOf</span>(DaysOfTheWeek<span class="hljs-preprocessor">.class</span>)<span class="hljs-comment">;</span><div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li></ul></pre>

<p>使用of工厂方法，可以指定枚举类型中那些枚举常量应该包含在EnumSet&lt;T&gt;中：</p>



<pre class="prettyprint" name="code"><code class="hljs avrasm has-numbering" onclick="mdcp.copyCode(event)">final <span class="hljs-keyword">Set</span>&lt; DaysOfTheWeek &gt; enumSetSome = EnumSet<span class="hljs-preprocessor">.of</span>(
    DaysOfTheWeek<span class="hljs-preprocessor">.SUNDAY</span>,
    DaysOfTheWeek<span class="hljs-preprocessor">.SATURDAY</span>
)<span class="hljs-comment">;</span><div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li><li style="color: rgb(153, 153, 153);">4</li></ul></pre>

<p>EnumMap&lt;T, ?&gt;是最接近于一般的map的，唯一的不同就是EnumMap&lt;T, ?&gt;的key是枚举类型的枚举常量。比如;</p>



<pre class="prettyprint" name="code"><code class="hljs avrasm has-numbering" onclick="mdcp.copyCode(event)">final Map&lt;DaysOfTheWeek, String&gt; enumMap = new EnumMap&lt;&gt;(DaysOfTheWeek<span class="hljs-preprocessor">.class</span>)<span class="hljs-comment">;</span>
enumMap<span class="hljs-preprocessor">.put</span>(DaysOfTheWeek<span class="hljs-preprocessor">.MONDAY</span>, <span class="hljs-string">"Lundi"</span>)<span class="hljs-comment">;</span>
enumMap<span class="hljs-preprocessor">.put</span>(DaysOfTheWeek<span class="hljs-preprocessor">.TUESDAY</span>, <span class="hljs-string">"Mardi"</span>)<span class="hljs-comment">;</span><div class="hljs-button {2}" data-title="复制"></div></code><ul class="pre-numbering" style=""><li style="color: rgb(153, 153, 153);">1</li><li style="color: rgb(153, 153, 153);">2</li><li style="color: rgb(153, 153, 153);">3</li></ul></pre>

<p>注意，和大多数集合实现一样，EnumSet&lt;T&gt;和EnumMap&lt;T, ?&gt;不是线程安全的所以不能在多线程环境下使用。</p>

<p><strong>八、何时使用枚举</strong></p>

<p>自Java 5发布以来，在解决一些固定常量集合的问题上枚举成为唯一首选和推荐的一种方式。不仅是因为它们是强类型，同时它们是可拓展并被当前的很多库和框架所支持。</p>          </div>
          <link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet">
                  </div>
  </article>
</div>
