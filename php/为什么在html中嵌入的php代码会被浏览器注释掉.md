<div id="mainContent">

<div class="forFlow">

<div id="post_detail">

<div id="topics">

<div class="post">

# [【转】为什么在html中嵌入的php代码会被浏览器注释掉](https://www.cnblogs.com/6luv-ml/p/6678138.html)

<div class="postBody">

<div id="cnblogs_post_body" class="blogpost-body ">

> html中嵌入php代码时，没有输出内容，执行时被注释掉了。什么原因呢？我有在本地搭建xamp环境，文件扩展名由html改为php就没问题？

**<span style="font-size: 18pt;">答：</span>**

php可以写在html里面，比如

<body>

    <?php echo 'fffffff';?>

</body>

但是如果插入了php语句，必须要用php的环境来运行这个html的文件才能有效果，比如WAMPServer。

另外后缀要把html改成php,因为html不能解析php的内容，除非使用模板引擎，比如：TP(ThinkPHP)。

当访问一个网页时，服务器会根据文件扩展名来判断如何处理页面，一般来说，当检查到扩展名为htm或html时，服务器将文件直接呈现到浏览器端，不做任何处理；如果检测到扩展名是PHP、shtml、ASP或JSP等文件时，服务器会先将这些文件解析成html代码，然后将代码呈现到流程器上。若你想在html文件中能够运行php代码，则需要修改Apache的配置文件。

首先，打开在安装Apache的安装目录，即apache\conf下找到：【httpd.conf】文件，用记事本打开，在最后添加下列代码：

![http://img.mukewang.com/588fece30001e29c03820230.jpg](http://img.mukewang.com/588fece30001e29c03820230.jpg)

如下图所示：

![http://img.mukewang.com/588fed220001c99304190118.jpg](http://img.mukewang.com/588fed220001c99304190118.jpg)

【注意】

（1）添加上述代码后，必须重启Apache服务器；

（2）html文件必须放在Apache配置文件httpd.conf中DocumentRoot指定的目录下，否则无法运行，见下图

![http://img.mukewang.com/588fed5b0001c69006940093.jpg](http://img.mukewang.com/588fed5b0001c69005000068.jpg)

如果你只想在一个html文件中包含和运行php脚本，那么你可以这样设置：

![http://img.mukewang.com/588fed880001e89204350091.jpg](http://img.mukewang.com/588fed880001e89204350091.jpg)

如下图所示，其中index.html是添加了PHP代码（脚本）的文件，#AddType application/x-httpd-php .htm .html前面的#，表示注释掉该行语句

![http://img.mukewang.com/588fedae00017c7a05200147.jpg](http://img.mukewang.com/588fedae00017c7a05000142.jpg)


</div>

</div>

</div>

</div>
