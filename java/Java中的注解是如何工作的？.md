<div class="grid-8">

<div class="post-10294 post type-post status-publish format-standard hentry category-basic tag-360 odd" id="post-10294">

<div class="entry-header">

# Java中的注解是如何工作的？

</div>

<div class="entry-meta">

2014/03/22 | 分类： [基础技术](http://www.importnew.com/cat/basic "查看 基础技术 中的全部文章") | [8 条评论](http://www.importnew.com/10294.html#comments "《Java中的注解是如何工作的？》上的评论") | 标签： [注解](http://www.importnew.com/tag/%e6%b3%a8%e8%a7%a3)

<div class="jiathis_style" style="display: block; margin: 0 0px; clear: both;"><span class="jiathis_txt">分享到：</span><a class="jiathis_button_tsina"></a><a class="jiathis_button_weixin"></a><a class="jiathis_button_qzone"></a><a class="jiathis_button_fb"></a><a class="jiathis_button_renren"></a><a class="jiathis_button_douban"></a><a class="jiathis_button_readitlater"></a><a class="jiathis_button_evernote"></a><a class="jiathis_button_ydnote"></a>[](http://www.jiathis.com/share?uid=1745061)<a class="jiathis_counter_style"></a></div>

</div>

<div class="entry">

<div class="copyright-area">本文由 [ImportNew](http://www.importnew.com) - [人晓](http://www.importnew.com/author/mandy) 翻译自 [idlebrains](http://idlebrains.org/tutorials/java-tutorials/how-annotations-work-java/)。欢迎加入[翻译小组](http://group.jobbole.com/category/feedback/trans-team/)。转载请见文末要求。</div>

自Java5.0版本引入**注解**之后，它就成为了Java平台中非常重要的一部分。开发过程中，我们也时常在应用代码中会看到诸如@Override，@Deprecated这样的注解。这篇文章中，我将向大家讲述到底什么是注解，为什么要引入注解，注解是如何工作的，如何编写自定义的注解(通过例子)，什么情况下可以使用注解以及最新注解和ADF(应用开发框架)。这会花点儿时间，所以为自己准备一杯咖啡，让我们来进入注解的世界吧。

[![](http://www.importnew.com/wp-content/uploads/2014/03/55211fcb7df719e4ccdff7569873be0a.png "java-annotations")](http://www.importnew.com/?attachment_id=10298)

### 什么是注解？

用一个词就可以描述注解，那就是元数据，即一种描述数据的数据。所以，可以说注解就是源代码的元数据。比如，下面这段代码：

<div>

<div id="highlighter_764059" class="syntaxhighlighter notranslate java">

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

<div class="line number2 index1 alt1">2</div>

<div class="line number3 index2 alt2">3</div>

<div class="line number4 index3 alt1">4</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`@Override`</div>

<div class="line number2 index1 alt1">`public` `String toString() {`</div>

<div class="line number3 index2 alt2">`return` `"This is String Representation of current object."``;`</div>

<div class="line number4 index3 alt1">`}`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

上面的代码中，我重写了`toString()`方法并使用了`@Override`注解。但是，即使我不使用`@Override注解标记代码，程序也能够正常执行。那么，该注解表示什么？这么写有什么好处吗？事实上，`@Override`告诉编译器这个方法是一个重写方法(描述方法的元数据)，如果父类中不存在该方法，编译器便会报错，提示该方法没有重写父类中的方法。如果我不小心拼写错误，例如将toString()`写成了`toStrring(){double r}`，而且我也没有使用`@Override`注解，那程序依然能编译运行。但运行结果会和我期望的大不相同。现在我们了解了什么是注解，并且使用注解有助于阅读程序。

Annotation是一种应用于类、方法、参数、变量、构造器及包声明中的特殊修饰符。它是一种由JSR-175标准选择用来描述元数据的一种工具。

### 为什么要引入注解？

使用Annotation之前(甚至在使用之后)，XML被广泛的应用于描述元数据。不知何时开始一些应用开发人员和架构师发现XML的维护越来越糟糕了。他们希望使用一些和代码紧耦合的东西，而不是像XML那样和代码是松耦合的(在某些情况下甚至是完全分离的)代码描述。如果你在Google中搜索“XML vs. annotations”，会看到许多关于这个问题的辩论。最有趣的是XML配置其实就是为了分离代码和配置而引入的。上述两种观点可能会让你很疑惑，两者观点似乎构成了一种循环，但各有利弊。下面我们通过一个例子来理解这两者的区别。

假如你想为应用设置很多的常量或参数，这种情况下，XML是一个很好的选择，因为它不会同特定的代码相连。如果你想把某个方法声明为服务，那么使用Annotation会更好一些，因为这种情况下需要注解和方法紧密耦合起来，开发人员也必须认识到这点。

另一个很重要的因素是Annotation定义了一种标准的描述元数据的方式。在这之前，开发人员通常使用他们自己的方式定义元数据。例如，使用标记interfaces，注释，transient关键字等等。每个程序员按照自己的方式定义元数据，而不像Annotation这种标准的方式。

目前，许多框架将XML和Annotation两种方式结合使用，平衡两者之间的利弊。

### Annotation是如何工作的？怎么编写自定义的Annotation？

在讲述这部分之前，建议你首先下载Annotation的示例代码[AnnotationsSample.zip](https://docs.google.com/file/d/0B1N2DVZFnNU0dVdFVjVFeTVtcXc/edit) 。下载之后放在你习惯使用的IDE中，这些代码会帮助你更好的理解Annotation机制。

编写Annotation非常简单，可以将Annotation的定义同接口的定义进行比较。我们来看两个例子：一个是标准的注解@Override，另一个是用户自定义注解@Todo。

<div>

<div id="highlighter_459444" class="syntaxhighlighter notranslate java">

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

<div class="line number2 index1 alt1">2</div>

<div class="line number3 index2 alt2">3</div>

<div class="line number4 index3 alt1">4</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`@Target``(ElementType.METHOD)`</div>

<div class="line number2 index1 alt1">`@Retention``(RetentionPolicy.SOURCE)`</div>

<div class="line number3 index2 alt2">`public` `@interface` `Override {`</div>

<div class="line number4 index3 alt1">`}`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

对于@Override注释你可能有些疑问，它什么都没做，那它是如何检查在父类中有一个同名的函数呢。当然，不要惊讶，我是逗你玩的。@Override注解的定义不仅仅只有这么一点代码。这部分内容很重要，我不得不再次重复：**Annotations仅仅是元数据，和业务逻辑无关。**理解起来有点困难，但就是这样。如果Annotations不包含业务逻辑，那么必须有人来实现这些逻辑。元数据的用户来做这个事情。Annotations仅仅提供它定义的属性(类/方法/包/域)的信息。Annotations的用户(同样是一些代码)来读取这些信息并实现必要的逻辑。

当我们使用Java的标注Annotations(例如@Override)时，JVM就是一个用户，它在字节码层面工作。到这里，应用开发人员还不能控制也不能使用自定义的注解。因此，我们讲解一下如何编写自定义的Annotations。

我们来逐个讲述编写自定义Annotations的要点。上面的例子中，你看到一些注解应用在注解上。

J2SE5.0版本在 java.lang.annotation提供了四种元注解，专门注解其他的注解：

`@Documented –注解是否将包含在JavaDoc中  
@Retention –什么时候使用该注解  
@Target? –注解用于什么地方  
@Inherited – 是否允许子类继承该注解`

**@Documented**–一个简单的Annotations标记注解，表示是否将注解信息添加在java文档中。

**@Retention**– 定义该注解的生命周期。

**RetentionPolicy.SOURCE** – 在编译阶段丢弃。这些注解在编译结束之后就不再有任何意义，所以它们不会写入字节码。@Override, @SuppressWarnings都属于这类注解。

**RetentionPolicy.CLASS** – 在类加载的时候丢弃。在字节码文件的处理中有用。注解默认使用这种方式。

**RetentionPolicy.RUNTIME**– 始终不会丢弃，运行期也保留该注解，因此可以使用反射机制读取该注解的信息。我们自定义的注解通常使用这种方式。

**@Target** – 表示该注解用于什么地方。如果不明确指出，该注解可以放在任何地方。以下是一些可用的参数。需要说明的是：属性的注解是兼容的，如果你想给7个属性都添加注解，仅仅排除一个属性，那么你需要在定义target包含所有的属性。

`ElementType.TYPE:用于描述类、接口或enum声明  
ElementType.FIELD:用于描述实例变量  
ElementType.METHOD  
ElementType.PARAMETER  
ElementType.CONSTRUCTOR  
ElementType.LOCAL_VARIABLE  
ElementType.ANNOTATION_TYPE 另一个注释  
ElementType.PACKAGE 用于记录java文件的package信息`

**@Inherited** – 定义该注释和子类的关系

那么，注解的内部到底是如何定义的呢？Annotations只支持基本类型、String及枚举类型。注释中所有的属性被定义成方法，并允许提供默认值。

<div>

<div id="highlighter_463604" class="syntaxhighlighter notranslate java">

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

<div class="line number2 index1 alt1">2</div>

<div class="line number3 index2 alt2">3</div>

<div class="line number4 index3 alt1">4</div>

<div class="line number5 index4 alt2">5</div>

<div class="line number6 index5 alt1">6</div>

<div class="line number7 index6 alt2">7</div>

<div class="line number8 index7 alt1">8</div>

<div class="line number9 index8 alt2">9</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`@Target``(ElementType.METHOD)`</div>

<div class="line number2 index1 alt1">`@Retention``(RetentionPolicy.RUNTIME)`</div>

<div class="line number3 index2 alt2">`@interface` `Todo {`</div>

<div class="line number4 index3 alt1">`public` `enum` `Priority {LOW, MEDIUM, HIGH}`</div>

<div class="line number5 index4 alt2">`public` `enum` `Status {STARTED, NOT_STARTED}`</div>

<div class="line number6 index5 alt1">`String author()` `default` `"Yash"``;`</div>

<div class="line number7 index6 alt2">`Priority priority()` `default` `Priority.LOW;`</div>

<div class="line number8 index7 alt1">`Status status()` `default` `Status.NOT_STARTED;`</div>

<div class="line number9 index8 alt2">`}`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

下面的例子演示了如何使用上面的注解。

<div>

<div id="highlighter_232753" class="syntaxhighlighter notranslate java">

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

<div class="line number2 index1 alt1">2</div>

<div class="line number3 index2 alt2">3</div>

<div class="line number4 index3 alt1">4</div>

<div class="line number5 index4 alt2">5</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`@Todo``(priority = Todo.Priority.MEDIUM, author =` `"Yashwant"``, status = Todo.Status.STARTED)`</div>

<div class="line number2 index1 alt1">`public` `void` `incompleteMethod1() {`</div>

<div class="line number3 index2 alt2">`//Some business logic is written`</div>

<div class="line number4 index3 alt1">`//But it’s not complete yet`</div>

<div class="line number5 index4 alt2">`}`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

如果注解中只有一个属性，可以直接命名为“value”，使用时无需再标明属性名。

<div>

<div id="highlighter_256103" class="syntaxhighlighter notranslate java">

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

<div class="line number2 index1 alt1">2</div>

<div class="line number3 index2 alt2">3</div>

<div class="line number4 index3 alt1">4</div>

<div class="line number5 index4 alt2">5</div>

<div class="line number6 index5 alt1">6</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`@interface` `Author{`</div>

<div class="line number2 index1 alt1">`String value();`</div>

<div class="line number3 index2 alt2">`}`</div>

<div class="line number4 index3 alt1">`@Author``(``"Yashwant"``)`</div>

<div class="line number5 index4 alt2">`public` `void` `someMethod() {`</div>

<div class="line number6 index5 alt1">`}`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

但目前为止一切看起来都还不错。我们定义了自己的注解并将其应用在业务逻辑的方法上。现在我们需要写一个用户程序调用我们的注解。这里我们需要使用反射机制。如果你熟悉反射代码，就会知道反射可以提供类名、方法和实例变量对象。所有这些对象都有getAnnotation()这个方法用来返回注解信息。我们需要把这个对象转换为我们自定义的注释(使用 instanceOf()检查之后)，同时也可以调用自定义注释里面的方法。看看以下的实例代码，使用了上面的注解:

<div>

<div id="highlighter_724065" class="syntaxhighlighter notranslate java">

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

<div class="line number2 index1 alt1">2</div>

<div class="line number3 index2 alt2">3</div>

<div class="line number4 index3 alt1">4</div>

<div class="line number5 index4 alt2">5</div>

<div class="line number6 index5 alt1">6</div>

<div class="line number7 index6 alt2">7</div>

<div class="line number8 index7 alt1">8</div>

<div class="line number9 index8 alt2">9</div>

<div class="line number10 index9 alt1">10</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`Class businessLogicClass = BusinessLogic.``class``;`</div>

<div class="line number2 index1 alt1">`for``(Method method : businessLogicClass.getMethods()) {`</div>

<div class="line number3 index2 alt2">`Todo todoAnnotation = (Todo)method.getAnnotation(Todo.``class``);`</div>

<div class="line number4 index3 alt1">`if``(todoAnnotation !=` `null``) {`</div>

<div class="line number5 index4 alt2">`System.out.println(``" Method Name : "` `+ method.getName());`</div>

<div class="line number6 index5 alt1">`System.out.println(``" Author : "` `+ todoAnnotation.author());`</div>

<div class="line number7 index6 alt2">`System.out.println(``" Priority : "` `+ todoAnnotation.priority());`</div>

<div class="line number8 index7 alt1">`System.out.println(``" Status : "` `+ todoAnnotation.status());`</div>

<div class="line number9 index8 alt2">`}`</div>

<div class="line number10 index9 alt1">`}`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

### 注解用例

注解的功能很强大，Spring和Hebernate这些框架在日志和有效性中大量使用了注解功能。注解可以应用在使用标记接口的地方。不同的是标记接口用来定义完整的类，但你可以为单个的方法定义注释，例如是否将一个方法暴露为服务。

在最新的servlet3.0中引入了很多新的注解，尤其是和servlet安全相关的注解。

**HandlesTypes** –该注解用来表示一组传递给ServletContainerInitializer的应用类。

**HttpConstraint** – 该注解代表所有HTTP方法的应用请求的安全约束，和ServletSecurity注释中定义的HttpMethodConstraint安全约束不同。

**HttpMethodConstraint** – 指明不同类型请求的安全约束，和ServletSecurity 注解中描述HTTP协议方法类型的注释不同。

**MultipartConfig** –该注解标注在Servlet上面，表示该Servlet希望处理的请求的 MIME 类型是 multipart/form-data。

**ServletSecurity** 该注解标注在Servlet继承类上面，强制该HTTP协议请求遵循安全约束。

**WebFilter** – 该注解用来声明一个Server过滤器；

**WebInitParam** – 该注解用来声明Servlet或是过滤器的中的初始化参数，通常配合 @WebServlet 或者 @WebFilter 使用。

**WebListener** –该注解为Web应用程序上下文中不同类型的事件声明监听器。

**WebServlet** –该注解用来声明一个Servlet的配置。

### ADF (应用程序框架)和注解

现在我们开始讨论文章的最后一部分了。应用程序框架，被称为ADF，由Oracle开发用来创建Oracle融合应用。我们已经了解了注解的优缺点，也知道如何编写自定义的注解，但我们应该将注解应用在ADF的哪部分呢？ADF是否提供了一些朴素的注解？很好的问题，确实在ADF中大量使用注解有一些限制。之前提到的应用框架如Spring和Hibernate使用AOP(面向侧面的程序设计)。在AOP中，框架提供了一种机制，在事件的预处理和后续处理中注入代码。例如：你有一个钩子用来在方法执行之前和之后添加代码，所以你可以在这些地方编写你的用户代码。ADF不使用AOP。如果我们有任何注解的用例可用，我们可能需要通过继承的方式实现。

希望你喜欢这篇文章。写下你的评论吧！

原文链接： [idlebrains](http://idlebrains.org/tutorials/java-tutorials/how-annotations-work-java/) 翻译： [ImportNew.com](http://www.importnew.com) - [人晓](http://www.importnew.com/author/mandy)  
译文链接： [http://www.importnew.com/10294.html](http://www.importnew.com/10294.html)  
[ <span style="color:#ff0000">**转载请保留原文出处、译者和译文链接。**</span>]  

<div id="author-bio">

### 关于作者： [人晓](http://www.importnew.com/author/mandy)

<div class="alignleft">[](http://www.importnew.com/author/mandy)</div>

（新浪微博：**[@人晓](http://weibo.com/u/1988305475)**）

[查看人晓的更多文章 >>](http://www.importnew.com/author/mandy)

</div>

</div>

<div class="jiathis_style_24x24"><a class="jiathis_button_tsina"></a><a class="jiathis_button_weixin"></a><a class="jiathis_button_qzone"></a><a class="jiathis_button_fb"></a><a class="jiathis_button_renren"></a><a class="jiathis_button_douban"></a><a class="jiathis_button_googleplus"></a><a class="jiathis_button_readitlater"></a><a class="jiathis_button_evernote"></a><a class="jiathis_button_ydnote"></a>[](http://www.jiathis.com/share?uid=1745061)<a class="jiathis_counter_style"></a></div>

<script type="text/javascript">var jiathis_config={ data_track_clickback:false, title:"《Java中的注解是如何工作的？》", summary:"自Java5.0版本引入注解之后，它就成为了Java平台中非常重要的一部分。开发过程中，我们也时常在应用代码中会看到诸如@Override，@Deprecated这样的注解。这篇文章中，我将向大家讲述到底什么是注解，为什么要引入注解，注解是如何工作的，如何编写自定义的注解(通过例子)，什么情况下可以使用注解以及最新注解和ADF(应用开发框架)。这会花点儿时间，所以为自己准备一杯咖啡，让我们来进入注解的世界吧。", pic:"http://cdn1.importnew.com/2014/03/55211fcb7df719e4ccdff7569873be0a.png", appkey:{ "tsina":2284713194 //for importnew }, ralateuid:{ "tsina":2991905905 //for importnew }, hideMore:false }</script>  

<div id="text-13">

<div class="textwidget">

[![](http://cdn1.importnew.com/2019/06/69727c9be7c84dff11c69bb668bf5ffd.jpg)](http://blog.jobbole.com/106093/)

</div>

</div>

</div>

<script type="text/javascript">window._wp_rp_static_base_url = "http://dtmvdvtzf8rz0.cloudfront.net/static/";</script>

### 相关文章

*   [Spring源码探究：容器](http://www.importnew.com/30835.html)
*   [使用 Java 注解自动化处理对应关系实现注释代码化](http://www.importnew.com/28577.html)
*   [注解的那点事儿](http://www.importnew.com/27071.html)
*   [Java Annotation的RetentionPolicy介绍](http://www.importnew.com/24051.html)
*   [Java核心技术点之注解](http://www.importnew.com/23816.html)
*   [框架开发之Java注解的妙用](http://www.importnew.com/23564.html)
*   [Spring：基于注解的Spring MVC（下）](http://www.importnew.com/23019.html)
*   [Spring：基于注解的Spring MVC（上）](http://www.importnew.com/23015.html)
*   [正确实现用spring扫描自定义的annotation](http://www.importnew.com/22934.html)
*   [Java注解教程及自定义注解](http://www.importnew.com/20286.html)

<div id="respond">

### 发表评论

[点击这里取消回复。](/10294.html#respond)

<form action="http://www.importnew.com/wp-comments-post.php" method="post" id="comment-form">

<fieldset><legend class="none">Comment form</legend>

<div class="container">

<div class="grid-4 margin-20"><label for="author">Name<span class="red">*</span></label></div>

<div class="grid-4 margin-20">

<div class="input-wrapper"><input type="text" name="author" id="author" value="" tabindex="1" size="30" class="required" placeholder="姓名"></div>

</div>

<div class="grid-4 margin-20"><label for="email">邮箱<span class="red">*</span></label></div>

<div class="grid-4 margin-20">

<div class="input-wrapper"><input type="email" name="email" id="email" value="" tabindex="2" size="30" class="required email" placeholder="请填写邮箱"></div>

</div>

<div class="grid-4 margin-20"><label for="url">网站 (请以 http://开头)</label></div>

<div class="grid-4 margin-20">

<div class="input-wrapper"><input type="url" name="url" id="url" value="" tabindex="3" size="30" placeholder="请填写网站地址"></div>

</div>

<div class="grid-8 margin-20"><label for="comment" class="none margin-20">评论内容<span class="red">*</span></label>

<div class="input-wrapper"><textarea name="comment" id="comment" rows="20" cols="30" class="required" tabindex="4" onkeydown="if(event.ctrlKey &amp;&amp; event.keyCode==13){document.getElementById('comment-form-submit').click(); return false;}" placeholder="请填写评论内容"></textarea></div>

</div>

</div>

(<span class="red">*</span>) 表示必填项

<div class="submit-wrapper"><a id="comment-form-submit" class="submit">提交评论</a></div>

<input type="hidden" name="comment_post_ID" value="10294" id="comment_post_ID"> <input type="hidden" name="comment_parent" id="comment_parent" value="0">

<input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="79f195fb4d">

</fieldset>

</form>

</div>

### 8 条评论

1.  <div id="div-comment-21916" class="comment-body">

    <div class="comment-author vcard"><cite class="fn">Retina</cite> <span class="says">说道：</span></div>

    <div class="comment-meta commentmetadata">[2014/03/23 下午 10:37](http://www.importnew.com/10294.html#comment-21916)</div>

    <div style="background-color:#FFFFCC !important">

    学习了！

    </div>

    Well-loved. Like or Dislike: ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-21916-up" style="font-size:12px; color:#009933;">36</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-21916-down" style="font-size:12px; color:#990033;">8</span>

    <div class="reply">[回复](/10294.html?replytocom=21916#respond)</div>

    </div>

2.  <div id="div-comment-22873" class="comment-body">

    <div class="comment-author vcard"><cite class="fn">[踏雁寻花](http://www.songtao.me)</cite> <span class="says">说道：</span></div>

    <div class="comment-meta commentmetadata">[2014/03/27 上午 10:15](http://www.importnew.com/10294.html#comment-22873)</div>

    <div style="background-color:#FFFFCC !important">

    恩 ，跟以前看过的文章差不多

    </div>

    Well-loved. Like or Dislike: ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-22873-up" style="font-size:12px; color:#009933;">23</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-22873-down" style="font-size:12px; color:#990033;">10</span>

    <div class="reply">[回复](/10294.html?replytocom=22873#respond)</div>

    </div>

3.  <div id="div-comment-503343" class="comment-body">

    <div class="comment-author vcard"><cite class="fn">1</cite> <span class="says">说道：</span></div>

    <div class="comment-meta commentmetadata">[2016/07/15 上午 10:16](http://www.importnew.com/10294.html#comment-503343)</div>

    没有说出注解的原理，是怎么解析的

    ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-503343-up" style="font-size:12px; color:#009933;">2</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-503343-down" style="font-size:12px; color:#990033;">2</span>

    <div class="reply">[回复](/10294.html?replytocom=503343#respond)</div>

    </div>

    *   <div id="div-comment-514224" class="comment-body">

        <div class="comment-author vcard"><cite class="fn">罗xx</cite> <span class="says">说道：</span></div>

        <div class="comment-meta commentmetadata">[2016/09/29 下午 4:15](http://www.importnew.com/10294.html#comment-514224)</div>

        <div style="background-color:#FFFFCC !important">

        只说了通过annotation找到那个incompleteMethod，（没说出注解的元注解，元数据有什么作用），（也没说注解是如何工作的），只是用了反射的机制。如何有时间的话 ，麻烦大神讲讲autowired的原理吗？

        </div>

        Well-loved. Like or Dislike: ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-514224-up" style="font-size:12px; color:#009933;">24</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-514224-down" style="font-size:12px; color:#990033;">3</span>

        <div class="reply">[回复](/10294.html?replytocom=514224#respond)</div>

        </div>

4.  <div id="div-comment-512671" class="comment-body">

    <div class="comment-author vcard"><cite class="fn">mok</cite> <span class="says">说道：</span></div>

    <div class="comment-meta commentmetadata">[2016/09/27 下午 4:40](http://www.importnew.com/10294.html#comment-512671)</div>

    <div style="background-color:#FFF0F5 !important">

    很赞的文章！希望有更多介绍新技术的文章能有这样的写作风格。为什么需要（什么情况下”引入”的这项技术）、什么是、本质是什么、helloworld、应用场景是什么（这点本文写得不是很详细），对于了解一个新技术点来说，这些点是让你“登堂入室”的步骤，也是最符合认知的步骤！

    </div>

    Hot debate. What do you think? ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-512671-up" style="font-size:12px; color:#009933;">3</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-512671-down" style="font-size:12px; color:#990033;">9</span>

    <div class="reply">[回复](/10294.html?replytocom=512671#respond)</div>

    </div>

5.  <div id="div-comment-539066" class="comment-body">

    <div class="comment-author vcard"><cite class="fn">spoon</cite> <span class="says">说道：</span></div>

    <div class="comment-meta commentmetadata">[2017/01/12 下午 4:21](http://www.importnew.com/10294.html#comment-539066)</div>

    <div style="background-color:#FFF0F5 !important">

    学习了!受益匪浅。接下来可以开始自己研究了

    </div>

    Hot debate. What do you think? ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-539066-up" style="font-size:12px; color:#009933;">0</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-539066-down" style="font-size:12px; color:#990033;">11</span>

    <div class="reply">[回复](/10294.html?replytocom=539066#respond)</div>

    </div>

6.  <div id="div-comment-560124" class="comment-body">

    <div class="comment-author vcard"><cite class="fn">航院小将</cite> <span class="says">说道：</span></div>

    <div class="comment-meta commentmetadata">[2017/06/12 下午 1:16](http://www.importnew.com/10294.html#comment-560124)</div>

    确实很好，对于我来说

    ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-560124-up" style="font-size:12px; color:#009933;">1</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-560124-down" style="font-size:12px; color:#990033;">0</span>

    <div class="reply">[回复](/10294.html?replytocom=560124#respond)</div>

    </div>

7.  <div id="div-comment-651076" class="comment-body">

    <div class="comment-author vcard"><cite class="fn">hao wu</cite> <span class="says">说道：</span></div>

    <div class="comment-meta commentmetadata">[2018/04/27 下午 5:12](http://www.importnew.com/10294.html#comment-651076)</div>

    写的非常清晰，一直不明白注解的作用，现在终于明白了

    ![Thumb up](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_up.png "赞同") <span id="karma-651076-up" style="font-size:12px; color:#009933;">2</span> ![Thumb down](http://www.importnew.com/wp-content/plugins/comment-rating/images/1_14_down.png "反对") <span id="karma-651076-down" style="font-size:12px; color:#990033;">3</span>

    <div class="reply">[回复](/10294.html?replytocom=651076#respond)</div>

    </div>

<div class="navigation margin-20">

<div class="alignleft">[« Java问答：终极父类（上）](http://www.importnew.com/10304.html)</div>

<div class="alignright">[减少GC开销的5个编码技巧 »](http://www.importnew.com/10472.html)</div>

</div>

</div>
