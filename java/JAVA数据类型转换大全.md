<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-2 float-left">转</span>

# JAVA数据类型转换大全

</div>

<div class="article-info-box">

<div class="article-bar-top" style="height: 24px;"><span class="c-gray">置顶</span> <span class="time">2016年12月15日 18:20:52</span> [ching_zhi](https://me.csdn.net/ching_zhi) <span class="read-count">阅读数：11240</span><span class="article_info_click" style="position: static;">更多</span>

<div class="tags-box space"><span class="label">个人分类：</span> [Java基础知识](https://blog.csdn.net/ching_zhi/article/category/6497997)</div>

</div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post"><link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css"> <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">

<div class="htmledit_views" id="content_views">

<div class="reader-page-wrap" id="reader-pageNo-1" style="border:1px solid rgb(211,211,211);font-family:'微软雅黑', 'Hiragino Sans GB';font-size:12px;line-height:15.996px;">

JAVA数据类型转换大全

**1）将字符串转化为整型；**

int i = Integer.parseInt(String str);

int i = Integer.valueOf(String str).intValue();

注：Integer.parseInt和 Integer.valueOf 不同，前者生成的是整型，而后者是一个对象，所以要通过intValue()来获得对象的值；

字串转成 Double, Float, Long 的方法大同小异.

**2) 整型转化为字符串：**

String str = String.valueOf(int i);

String str = Integer.toString(int i);

String str = “” + i ;

注： Double, Float, Long 的方法大同小异.

**3) Long转化为date：**

SimpleDateFormat sf = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");

//tieml,timef是long,前面转化过来的

Date date = new Date(timel - timef);

String time = sf.parse(date);

**1、float型转换为double型：**

float f1=100.00f;

Float F1=new Float(f1);

<span style="color:#333333;">//F1.doubleValue()</span><span style="color:#ff0000;">为Float类的返回double值型的方法</span>

double d1=F1.doubleValue();

**2、double型转换为int型：**

double d1=100.00;

Double D1=new Double(d1);

int i1=D1.intValue();

**3、int型转换为double型：**

int i1=200;

double d1=i1;

(2). 字符串与其它数据类型的转换

<span style="color:#3333ff;">4、字符串与其它类型间的转换：</span>

<span style="color:#ff0000;">⑴其它类型向字符串的转换</span>

<span style="color:#ff0000;">①调用类的串转换方法:X.toString();</span>

<span style="color:#ff0000;">②自动转换:X+“”;</span>

<span style="color:#ff0000;">③使用String的方法:String.valueOf(X);</span>

<span style="color:#009900;">⑵字符串作为值,向其它类型的转换</span>

<span style="color:#009900;">①先转换成相应的封装器实例,再调用对应的方法转换成其它类型</span>

例如，字符中“32.1”转换double型的值的格式为:new Float(“32.1”).doubleValue()。

也可以用:Double.valueOf(“32.1”).doubleValue()

<span style="color:#009900;">②静态parseXXX方法</span>

<span style="color:#009900;">String s = "1";</span>

<span style="color:#009900;">byte b = Byte.parseByte( s );</span>

<span style="color:#009900;">short t = Short.parseShort( s );</span>

<span style="color:#009900;">int i = Integer.parseInt( s );</span>

<span style="color:#009900;">long l = Long.parseLong( s );</span>

<span style="color:#009900;">Float f = Float.parseFloat( s );</span>

<span style="color:#009900;">Double d = Double.parseDouble( s );</span>

③Character的getNumericValue(char ch)方法

返回指定的 Unicode 字符表示的 `int` 值。

(3). 其它实用数据类型转换

5．Date类与其它数据类型的相互转换

整型和Date类之间并不存在直接的对应关系，只是你可以使用int型为分别表示年、月、日、时、分、秒，这样就在两者之间建立了一个对应关系，在作这种转换时，你可以使用**Date类构造函数的三种形式**：

<span style="color:#ff0000;">①Date(int year, int month, int date)：以int型表示年、月、日</span>

<span style="color:#ff0000;">②Date(int year, int month, int date, int hrs, int min)：以int型表示年、月、日、时、分</span>

<span style="color:#ff0000;">③Date(int year, int month, int date, int hrs, int min, int sec)：以int型表示年、月、日、时、</span>

<span style="color:#ff0000;">分、秒</span>

在长整型和Date类之间有一个很有趣的对应关系，就是将一个时间表示为距离格林尼治标准时间1970年1月1日0时0分0秒的毫秒数。对于这种对应关系，Date类也有其相应的构造函数：Date(long date)。

获取Date类中的年、月、日、时、分、秒以及

</div>

<div class="reader-page-wrap" id="reader-pageNo-2" style="border:1px solid rgb(211,211,211);font-family:'微软雅黑', 'Hiragino Sans GB';font-size:12px;line-height:15.996px;">

星期你可以使用Date类的getYear()、getMonth()、getDate()、getHours()、getMinutes()、getSeconds()、getDay()方法，你也可以将其理解为将Date类转换成int。

而Date类的getTime()方法可以得到我们前面所说的一个时间对应的长整型数，与包装类一样，Date类也有一个toString()方法可以将其转换为String类。

有时我们希望得到Date的特定格式，例如20020324，我们可以使用以下方法，首先在文件开始引入，

import java.text.SimpleDateFormat;

import java.util.*;

java.util.Date date = new java.util.Date();

//如果希望得到YYYYMMDD的格式

SimpleDateFormat sdf=new SimpleDateFormat("yyyyMMDD");

String dateFormat=<span style="color:rgb(51,51,51);font-family:'微软雅黑', 'Hiragino Sans GB';font-size:19px;line-height:26.6px;">sdf</span>.format(date);

//如果希望分开得到年，月，日

SimpleDateFormat sy=newSimpleDateFormat("yyyy");

SimpleDateFormat sm=new SimpleDateFormat("MM");

SimpleDateFormat sd=new SimpleDateFormat("dd");

String syear=sy.format(date);

String smon=sm.format(date);

String sday=sd.format(date);

//js中将Data转换成String类型

* 对Date的扩展，将 Date转化为指定格式的String

* 月(M)、日(d)、12小时(h)、24小时(H)、分(m)、秒(s)、周(E)、季度(q) 可以用 1-2个占位符

* 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3位的数字)

*eg:

* (new Date()).pattern("yyyy-MM-dd hh:mm:ss.S") ==>2006-07-0208:09:04.423

* (new Date()).pattern("yyyy-MM-dd E HH:mm:ss") ==>2009-03-10 二20:09:04

* (new Date()).pattern("yyyy-MM-dd EE hh:mm:ss") ==>2009-03-10 周二08:09:04

* (new Date()).pattern("yyyy-MM-dd EEE hh:mm:ss")==> 2009-03-10 星期二08:09:04

* (new Date()).pattern("yyyy-M-d h:m:s.S") ==>2006-7-2 8:9:4.

<span style="color:#cc0000;">**6.字符型转时间型：**</span><span style="color:#333333;">（2005-10-1）</span>

reportdate_str ＝ “2005-10-01”；

reportdate_str ＝ reportdate_str ＋ “ 00:00:00.0”

<span style="color:rgb(51,51,51);">reportdate =</span><span style="color:#cc0000;"> **java.sql.Timestamp.valueOf(reportdate_str);**</span>

**7.时间型转字符型：**

V_DATE = reportdate.toString();

8.将long型转化为String型

long APP_UNIT = (long)userview.getDEPT_ID();

String S_APP_UNIT = String.valeOf(APP_UNIT);

**<span style="color:#cc0000;">基本类型s都可以通过String.valueof(s)来转化为String型。</span>**

JAVA中常用数据类型转换函数

虽然都能在JAVA API中找到，整理一下做个备份。string->byte

Byte static byte parseByte(String s) byte->string

Byte static String toString(byte b)char->string

Character static String to String (char c)string->Short

Short static Short parseShort(String s)Short->String

Short static String toString(Short s)String->Integer

Integer static int parseInt(String s)Integer->String

Integer static String tostring(int i)String->Long

Long static long parseLong(String s)Long->String

Long static String toString(Long i)String->Float

Float static float parseFloat(String s)Float->String

Float static String toString(float f)String->Double

Double static double parseDouble(String s)Double->String

Double static String toString(Double)

<div class="reader-page-wrap" id="reader-pageNo-3" style="border:1px solid rgb(211,211,211);font-family:'微软雅黑', 'Hiragino Sans GB';font-size:12px;line-height:15.996px;">

++++++++++++++++++++++++++++++++++++++++++++++++++++++

**数据类型**

**基本类型有以下四种：**

**int长度数据类型有：byte(8bits)、short(16bits)、int(32bits)、long(64bits)、**

**float长度数据类型有：单精度（32bits float）、双精度（64bits double）**

**boolean类型变量的取值有：ture、false**

**char数据类型有：unicode字符,16位**

**对应的类类型：Integer、Float、Boolean、Character、Double、Short、Byte、Long**

转换原则

**从低精度向高精度转换**

**byte 、short、int、long、float、double、char**

<span style="color:#333333;">注：</span>**<span style="color:#990000;">两个char型运算时，自动转换为int型；当char与别的类型运算时，也会先自动转换为int型的，再做其它类型的自动转换</span>**

基本类型向类类型转换

正向转换：通过类包装器来new出一个新的类类型的变量

Integer a= new Integer(2);

反向转换：通过类包装器来转换

int b=a.intValue();

类类型向字符串转换

正向转换：因为每个类都是object类的子类，而所有的object类都有一个toString()函数，所以通过toString()函数来转换即可

反向转换：通过类包装器new出一个新的类类型的变量

eg1: int i=Integer.valueOf(“123”).intValue()

说明：上例是将一个字符串转化成一个Integer对象，然后再调用这个对象的intValue()方法返回其对应的int数值。

eg2: float f=Float.valueOf(“123”).floatValue()

说明：上例是将一个字符串转化成一个Float对象，然后再调用这个对象的floatValue()方法返回其对应的float数值。

eg3: boolean b=Boolean.valueOf(“123”).booleanValue()

说明：上例是将一个字符串转化成一个Boolean对象，然后再调用这个对象的booleanValue()方法返回其对应的boolean数值。

eg4:double d=Double.valueOf(“123”).doubleValue()

说明：上例是将一个字符串转化成一个Double对象，然后再调用这个对象的doubleValue()方法返回其对应的double数值。

eg5: long l=Long.valueOf(“123”).longValue()

说明：上例是将一个字符串转化成一个Long对象，然后再调用这个对象的longValue()方法返回其对应的long数值。

eg6: char=Character.valueOf(“123”).charValue()

说明：上例是将一个字符串转化成一个Character对象，然后再调用这个对象的charValue()方法返回其对应的char数值。

基本类型向字符串的转换

正向转换：

如：int a=12;

String b;b=a+””;

反向转换：

通过类包装器

eg1:int i=Integer.parseInt(“123”)

说明：此方法只能适用于字符串转化成整型变量

eg2: float f=Float.valueOf(“123”).floatValue()

说明：上例是将一个字符串转化成一个Float对象，然后再调用这个对象的floatValue()方法返回其对应的float数值。

eg3: boolean b=Boolean.valueOf(“123”).booleanValue()

说明：上例是将一个字符串转化成一个Boolean对象，然后再调用这个对象的booleanValue()方法返回其对应

</div>

<div class="reader-page-wrap" id="reader-pageNo-4" style="color:rgb(51,51,51);border:1px solid rgb(211,211,211);font-family:'微软雅黑', 'Hiragino Sans GB';font-size:12px;line-height:15.996px;">

的boolean数值。

eg4:double d=Double.valueOf(“123”).doubleValue()

说明：上例是将一个字符串转化成一个Double对象，然后再调用这个对象的doubleValue()方法返回其对应的double数值。

eg5: long l=Long.valueOf(“123”).longValue()

说明：上例是将一个字符串转化成一个Long对象，然后再调用这个对象的longValue()方法返回其对应的long数值。

eg6: char=Character.valueOf(“123”).charValue()

说明：上例是将一个字符串转化成一个Character对象，然后再调用这个对象的charValue()方法返回其对应的char数值。

</div>

</div>

</div>

</div>

</article>

</div>
