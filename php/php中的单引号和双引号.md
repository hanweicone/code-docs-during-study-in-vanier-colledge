<div id="cnblogs_post_body" class="blogpost-body ">

【1】单引号和双引号在处理变量的时候做法：

括在双引号内的变量会解释出值，但是括在单引号内则不做处理，直接输出；

<div class="cnblogs_Highlighter sh-gutter">

<div>

<div id="highlighter_484408" class="syntaxhighlighter  php">

<div class="toolbar"><span>[?](#)</span></div>

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

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`<?php`</div>

<div class="line number2 index1 alt1">`$var` `=` `'my name is huige'``;`</div>

<div class="line number4 index3 alt1">`echo` `"$var"``;` `//结果是:my name is huige`</div>

<div class="line number6 index5 alt1">`echo` `'$var'``;` `//结果是:$var`</div>

<div class="line number7 index6 alt2">`?>`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

【2】如果在语句中要转义操作，那么就一定要用双引号了。

比如，转定义单引号时，写成这样的话：

<div class="cnblogs_Highlighter sh-gutter">

<div>

<div id="highlighter_469771" class="syntaxhighlighter  php">

<div class="toolbar"><span>[?](#)</span></div>

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`$a` `= ‘He\’s name is Huige.’ ;`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

程序会把He\’s name is Tom.原封不动的显示出来，如果这样写：

<div class="cnblogs_Highlighter sh-gutter">

<div>

<div id="highlighter_61255" class="syntaxhighlighter  php">

<div class="toolbar"><span>[?](#)</span></div>

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`$a` `= “He\’s name is Huige.”;`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

程序就会显示：He’s name is Tom.

====================================================

下面列举写转义字符的含义（当在双引号内使用这些字符时，它们具有特殊的含义）

<table border="0">

<tbody>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">转义字符的代码</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">转义字符的含义</span></td>

</tr>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">\"</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">双引号</span></td>

</tr>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">\'</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">单引号</span></td>

</tr>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">\\</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">反斜杠</span></td>

</tr>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">\n</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">换行符</span></td>

</tr>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">\r</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">回车符</span></td>

</tr>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">\t</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">制表符</span></td>

</tr>

<tr>

<td style="text-align: center;"><span style="font-size: 16px;">\$</span></td>

<td style="text-align: center;"><span style="font-size: 16px;">美元符号</span></td>

</tr>

</tbody>

</table>

 ====================================================

下面在来一个例子来演示了使用单引号和双引号之间的区别：

<div class="cnblogs_Highlighter sh-gutter">

<div>

<div id="highlighter_837750" class="syntaxhighlighter  php">

<div class="toolbar"><span>[?](#)</span></div>

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

<div class="line number11 index10 alt2">11</div>

<div class="line number12 index11 alt1">12</div>

<div class="line number13 index12 alt2">13</div>

<div class="line number14 index13 alt1">14</div>

<div class="line number15 index14 alt2">15</div>

<div class="line number16 index15 alt1">16</div>

<div class="line number17 index16 alt2">17</div>

<div class="line number18 index17 alt1">18</div>

<div class="line number19 index18 alt2">19</div>

<div class="line number20 index19 alt1">20</div>

<div class="line number21 index20 alt2">21</div>

<div class="line number22 index21 alt1">22</div>

<div class="line number23 index22 alt2">23</div>

<div class="line number24 index23 alt1">24</div>

<div class="line number25 index24 alt2">25</div>

<div class="line number26 index25 alt1">26</div>

<div class="line number27 index26 alt2">27</div>

<div class="line number28 index27 alt1">28</div>

<div class="line number29 index28 alt2">29</div>

<div class="line number30 index29 alt1">30</div>

<div class="line number31 index30 alt2">31</div>

<div class="line number32 index31 alt1">32</div>

<div class="line number33 index32 alt2">33</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`<!DOCTYPE html PUBLIC` `"-//W3C//DTD XHTML 1.0 Transitional//EN"` `"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"``>`</div>

<div class="line number2 index1 alt1">`<html xmlns=``"http://www.w3.org/1999/xhtml"``>`</div>

<div class="line number3 index2 alt2">`<head>`</div>

<div class="line number4 index3 alt1">`<meta http-equiv=``"Content-Type"` `content=``"text/html; charset=utf-8"` `/>`</div>

<div class="line number5 index4 alt2">`<title>引号</title>`</div>

<div class="line number6 index5 alt1">`</head>`</div>

<div class="line number8 index7 alt1">`<body>`</div>

<div class="line number9 index8 alt2">`<?php`</div>

<div class="line number11 index10 alt2">`// 设置必要要的变量:`</div>

<div class="line number12 index11 alt1">`$quantity` `= 30;` `// 出售30件产品.`</div>

<div class="line number13 index12 alt2">`$price` `= 119.95;` `// 单价.`</div>

<div class="line number14 index13 alt1">`$taxrate` `= .05;` `// 5%的发票税.`</div>

<div class="line number16 index15 alt1">`// 计算总额:`</div>

<div class="line number17 index16 alt2">`$total` `=` `$quantity` `*` `$price``;`</div>

<div class="line number18 index17 alt1">`$total` `=` `$total` `+ (``$total` `*` `$taxrate``);` `// Calculate and add the tax.`</div>

<div class="line number20 index19 alt1">`// 格式化总额:`</div>

<div class="line number21 index20 alt2">`$total` `= number_format (``$total``, 2);`</div>

<div class="line number23 index22 alt2">`// 打印结果使用双引号：`</div>

<div class="line number24 index23 alt1">`echo` `"<h3>使用双引号：</h3>"``;`</div>

<div class="line number25 index24 alt2">`echo` `"<p>你所出售的 <b>$quantity</b> 件产品,成本单价为 <b>\$price</b>. 加上发票税，总额为 <b>\$total</b>.</p>\n"``;`</div>

<div class="line number27 index26 alt2">`// 打印结果使用单引号：`</div>

<div class="line number28 index27 alt1">`echo` `'<h3>使用单引号：</h3>'``;`</div>

<div class="line number29 index28 alt2">`echo` `'<p>你所出售的 <b>$quantity</b> 件产品,成本单价为 <b>\$price</b>. 加上发票税，总额为 <b>\$total</b>.</p>\n'``;`</div>

<div class="line number31 index30 alt2">`?>`</div>

<div class="line number32 index31 alt1">`</body>`</div>

<div class="line number33 index32 alt2">`</html>`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

 最后结果如下图：

================================================================

![](https://images0.cnblogs.com/i/373150/201403/121530006862697.jpg)

================================================================

1、这个例子中用双引号打印结果，是这篇文章（[php入门变量之数字](http://www.cnblogs.com/huige728/p/3596080.html)）中一个例子的单引号打印结果的另一个解决方法。

2、在这个例子中由于双引号是能打印出变量的，所以我们把要打印的东西全部放到双引号中，但是唯一的问题就是打印$符号问题了，要打印出$符号，我们直接进行转义即可。

3、同时在这两种引号内使用换行符（\n ）会有什么区别呢？？？

答：当把换行符（\n ）置于双引号内时，它会在HTML 源代码中创建一个新行。当把它置于单引号内时，它会直接打印出\和n。

================================================================

<span style="color: #ff0000;">**FAQ：**</span>

1、在运行效率上单引号和双引号也是有区别的，一般来说单引号的运行速度会比较快，双引号会比较慢，原因在于双引号要先查找语句中是否有变量，而单引号则不用，因此，如果语句中没有代入变量尽量采用单引号。这是写程序一种习惯，时刻想着提高程序的效率。

2、当利用PHP 打印HTML 时，使用单引号最容易。

<div class="cnblogs_Highlighter sh-gutter">

<div>

<div id="highlighter_61500" class="syntaxhighlighter  php">

<div class="toolbar"><span>[?](#)</span></div>

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`echo` `'<table width="80% " border="0" cellspacing="2" cellpadding="3" align="center">'``;`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

如果想使用双引号打印出这段HTML 代码，将不得不对字符串中的所有双引号进行转义。

<div class="cnblogs_Highlighter sh-gutter">

<div>

<div id="highlighter_913942" class="syntaxhighlighter  php">

<div class="toolbar"><span>[?](#)</span></div>

<table border="0" cellpadding="0" cellspacing="0">

<tbody>

<tr>

<td class="gutter">

<div class="line number1 index0 alt2">1</div>

</td>

<td class="code">

<div class="container">

<div class="line number1 index0 alt2">`echo` `"<table width=\"80%\" border= \"0\" cellspacing=\"2\" cellpadding=\"3\" align=\" center\">"``;`</div>

</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

3、如果你仍然不清楚这两种引号之间的区别，可以使用双引号，这样不太可能出问题。

</div>
