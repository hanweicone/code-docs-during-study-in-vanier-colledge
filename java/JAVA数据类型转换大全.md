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
