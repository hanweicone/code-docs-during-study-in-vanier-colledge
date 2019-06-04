

# Java 中Calendar、Date、SimpleDateFormat学习总结
  在之前的项目中，经常会遇到Calendar，Date的一些操作时间的类，并且总会遇到时间日期之间的格式转化问题，虽然做完了但是总是忘记，记不清楚，每次还都要查找资料。今天总结一下，加深印象。

 

## Calendar

Calendar是java.util 包下面的一个抽象类，它为特定瞬间与一组诸如YEAR、MONTH、DAY_OF_MONTH、HOUR等日历字段之间的转换提供了一些方法，并未操作日历字段（例如获得下星期的日期）提供了一些方法。瞬间值可用毫秒值来表示，它是距格林威治标准时间 1970 年1月 1日的 00:00:00:000的偏移量。

Java API 中说到，Calendar提供了一个类方法getInstance，以此获得此类型的一个通用对象，Calendar的getInstance返回一个Calendar对象，其日历字段值已由当前日期和时间初始化。我们知道，抽象类是不能够被实例化的，那为什么会返回一个Calendar对象呢？Calendar还有一个直接子类GregorianCalendar，这个类是Calendar的实现类，那么其实getInstance方法返回的是Calendar的子类GregorianCalendar的对象。

Calendar对日历字段的操作有三种方法:

set() ,add() , roll()

set(f,value),这个方法的含义是把日历字段f设置成value，api中说到，它设置了一个内部的成员变量，以指示f发生了改变，但是直到调用get()、getTime()、getTimeInMillis()、add() 或 roll() 时才会重新计算日历的时间值（以毫秒为单位）。

add(f,delate),将delate添加到f字段中，这相当于是set(f,get(f)+delate)，当然，这样改动的话，可能日历的其他字段也会发生相应的改变，与 set() 不同，add() 强迫日历系统立即重新计算日历的毫秒数和所有字段。

 

roll(f,value)与add(f,delate)的区别  ：在完成调用后，更大的字段无变化

在项目中，经常看见的是通过Calendar对象得到当前的年月日。

下面通过一个小小的例子看看是如何得到年月日的

    import java.util.Calendar;
    public class CalendarTest {
        public static void main(String[] args) {
            Calendar cal= Calendar.getInstance();
            int day= cal.get(Calendar.DATE);
            int month=cal.get(Calendar.MONTH)+1;
            int year=cal.get(Calendar.YEAR);
            String[] weekDays = {"星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"};
            int w = cal.get(Calendar.DAY_OF_WEEK) - 1;
            if (w < 0)
                w = 0;
            System.out.println(    year+"年"+month+"月"+day+"号,"+weekDays[w]);
        }
    }
此代码输出的是2017年6月15号，星期四

  为什么month要加1才能得到当前月份呢？

是因为在格里高利历和罗马儒略历中一年中的第一个月是 JANUARY，它为 0；最后一个月取决于一年中的月份数。 简单来说，因为这个值的初始值是0，因此我们要用它来表示正确的月份时就需要加1。
为什么week要减1呢？
这是因为一个星期中的第一天是SunDay，从星期日到星期六，对应的数字分别是1,2,3,4,5,6,7，所以需要减1。

Calendar还有其他的一些方法，比如getTimeMillis(),返回Calendar的时间值，以毫秒计算
getTime(),返回一个此Calendar的时间值的Date对象，和new Date()的值是一样的。


## Date

Date也是java.util包下的一个类，类 
Date
 表示特定的瞬间，精确到毫秒。
从 JDK 1.1 开始，应该使用 
Calendar
 类实现日期和时间字段之间转换，使用 
DateFormat
 类来格式化和解析日期字符串。
Date
 中的相应方法已废弃。


## SimpleDateFormat

SimpleDateFormat 是一个以与语言环境有关的方式来格式化和解析日期的具体类。
SimpleDateFormat是DateFormat抽象类的实现类，DateFormat继承Format，Format定义了编程接口，用于将语言环境敏感的对象格式化为 
String
（使用 
format
 方法）和将 
String
 重新解析为对象（使用 
parseObject
 方法）。 

 在格式化日期的时候，经常用到的构造方法是带一个String参数的
Public SimpleDateFormat（String pattern）
这个构造函数的意思是用给定的模式和默认的语言环境构的日期格式符号来格式化。

SimpleDateFormat中有format方法和pase方法，format方法是将Date对象转化为String字符串，pase是将字符串转化为Date对象。
下面通过代码来展示日期和字符串之间的转化。
假如我要将一个日期类型的时间格式转化成"yyyy-mm-dd"类型的字符串，需要用到format方法，
Date date=new Date();
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-mm-dd");
sdf.format(date);
如果需要将"yyyy-mm-dd"String类型的日期转化成日期对象类型，就需要用到parse,
String str= "2017-6-17"
sdf.parse(str),这样就可以得到一个日期类型。

附上项目当中的时间转换的util，里面包含了对时间的各种转化。



      1 import java.sql.Timestamp;
      2 import java.text.ParseException;
      3 import java.text.SimpleDateFormat;
      4 import java.util.Calendar;
      5 import java.util.Date;
      6 import java.util.Locale;
      7 import java.util.TimeZone;
      8 
      9 import org.apache.commons.lang3.StringUtils;
     10 
     11 public final class DateUtil {
     12     // 默认显示日期的格式
     13     public static final String DATAFORMAT_STR = "yyyy-MM-dd";
     14     // 默认显示日期的格式
     15     public static final String YYYY_MM_DATAFORMAT_STR = "yyyy-MM";
     16     // 默认显示日期时间的格式
     17     public static final String DATATIMEF_STR = "yyyy-MM-dd HH:mm:ss";
     18     // 默认显示日期时间的格式
     19     public static final String DATATIMEF_STR2 = "yyyyMMdd HH:mm:ss";
     20     // 默认显示日期时间的格式 精确到毫秒
     21     public static final String DATATIMEF_STR_MIS = "yyyyMMddHHmmssSSS";
     22     // 默认显示日期时间的格式 精确到分钟
     23     public static final String DATATIMEF_STR_MI = "yyyy-MM-dd HH:mm";
     24 
     25     public static final String DATATIMEF_STR_MDHm = "MM.dd HH:mm";
     26 
     27     public static final String HH_STR = "HH";
     28 
     29     // 精确到秒
     30     public static final String DATATIMEF_STR_SEC = "yyyyMMddHHmmss";
     31     // 默认显示简体中文日期的格式
     32     public static final String ZHCN_DATAFORMAT_STR = "yyyy年MM月dd日";
     33     // 默认显示简体中文日期时间的格式
     34     public static final String ZHCN_DATATIMEF_STR = "yyyy年MM月dd日HH时mm分ss秒";
     35     // 默认显示简体中文日期时间的格式
     36     public static final String ZHCN_DATATIMEF_STR_4yMMddHHmm = "yyyy年MM月dd日HH时mm分";
     37 
     38     // 默认显示月份和日期的格式
     39     public static final String MONTHANDDATE_STR = "MM.dd";
     40     
     41     public static final String DATATIMEF_STR_MIN = "yyyyMMddHHmm";
     42     
     43     public  static final String HOUR_END = " 23:59:59";
     44     
     45     public  static final String HOUR_START = " 00:00:00";
     46 
     47     private DateUtil() {
     48     }
     49 
     50     public static Date now() {
     51         
     52         return Calendar.getInstance(Locale.CHINESE).getTime();
     53     }
     54 
     55     public static Date daysAfter(Date baseDate, int increaseDate) {
     56         Calendar calendar = Calendar.getInstance(Locale.CHINESE);
     57         calendar.setTime(baseDate);
     58         calendar.add(Calendar.DATE, increaseDate);
     59         return calendar.getTime();
     60     }
     61     
     62     public static Date hoursAfter(Date baseDate, int increaseHours) {
     63         Calendar calendar = Calendar.getInstance(Locale.CHINESE);
     64         calendar.setTime(baseDate);
     65         calendar.add(Calendar.HOUR_OF_DAY, increaseHours);
     66         return calendar.getTime();
     67     }
     68 
     69     public static Date minuteAfter(Date baseDate, int increaseMonths) {
     70         Calendar calendar = Calendar.getInstance(Locale.CHINESE);
     71         calendar.setTime(baseDate);
     72         calendar.add(Calendar.MINUTE, increaseMonths);
     73         return calendar.getTime();
     74     }
     75 
     76     public static Date monthAfter(Date baseDate, int increaseMonths) {
     77         Calendar calendar = Calendar.getInstance(Locale.CHINESE);
     78         calendar.setTime(baseDate);
     79         calendar.add(Calendar.MONTH, increaseMonths);
     80         return calendar.getTime();
     81     }
     82 
     83     public static Date getInternalDateByDay(Date d, int days) {
     84         Calendar now = Calendar.getInstance(TimeZone.getDefault());
     85         now.setTime(d);
     86         now.add(Calendar.DATE, days);
     87         return now.getTime();
     88     }
     89 
     90     public static Date getInternalDateByMinute(Date d, int minutes) {
     91         Calendar now = Calendar.getInstance(TimeZone.getDefault());
     92         now.setTime(d);
     93         now.add(Calendar.MINUTE, minutes);
     94         return now.getTime();
     95     }
     96 
     97     /**
     98      * 将Date转换成字符串“yyyy-mm-dd hh:mm:ss”的字符串
     99      * 
    100      * @param date
    101      * @return
    102      */
    103     public static String dateToDateString(Date date) {
    104         return dateToDateString(date, DATATIMEF_STR);
    105     }
    106 
    107     /**
    108      * 将Date转换成字符串“yyyy-mm-dd hh:mm:ss”的字符串
    109      * 
    110      * @param date
    111      * @return
    112      */
    113     public static String dateToDateString2(Date date) {
    114         return dateToDateString(date, DATATIMEF_STR2);
    115     }
    116 
    117     /**
    118      * 将Date转换成formatStr格式的字符串
    119      * 
    120      * @param date
    121      * @param formatStr
    122      * @return
    123      */
    124     public static String dateToDateString(Date date, String formatStr) {
    125         if (date == null) {
    126             return null;
    127         }
    128         java.text.DateFormat df = getDateFormat(formatStr);
    129         return date != null ? df.format(date) : "";
    130     }
    131 
    132     /**
    133      * 按照默认formatStr的格式，转化dateTimeStr为Date类型 dateTimeStr必须是formatStr的形式
    134      * 
    135      * @param dateTimeStr
    136      * @param formatStr
    137      * @return
    138      */
    139     public static Date getDate(String dateTimeStr, String formatStr) {
    140         try {
    141             if (dateTimeStr == null || dateTimeStr.equals("")) {
    142                 return null;
    143             }
    144             java.text.DateFormat sdf = new SimpleDateFormat(formatStr);
    145             java.util.Date d = sdf.parse(dateTimeStr);
    146             return d;
    147         } catch (ParseException e) {
    148             throw new RuntimeException(e);
    149         }
    150     }
    151 
    152     public static String getCurDate() {
    153         return dateToDateString(Calendar.getInstance().getTime(),
    154                 DATAFORMAT_STR);
    155     }
    156 
    157     public static String getCurHour() {
    158         return dateToDateString(Calendar.getInstance().getTime(), HH_STR);
    159     }
    160 
    161     public static int getThisMonth() {
    162         Calendar c = Calendar.getInstance(Locale.CHINESE);
    163         int month = c.get(Calendar.MONTH) + 1;
    164         return month;
    165 
    166     }
    167 
    168     public static int getThisWeek() {
    169         Calendar c = Calendar.getInstance(Locale.CHINESE);
    170         c.setFirstDayOfWeek(Calendar.MONDAY);
    171         int week = c.get(Calendar.WEEK_OF_YEAR);
    172         return week;
    173 
    174     }
    175 
    176     public static SimpleDateFormat getDateFormat(final String formatStr) {
    177         return new SimpleDateFormat(formatStr);
    178     }
    179 
    180     @SuppressWarnings("deprecation")
    181     public static String getFirstDateOfMonth(Date now) {
    182         SimpleDateFormat df1 = new SimpleDateFormat(DATATIMEF_STR);
    183         Date da = new Date(now.getYear(), now.getMonth(), 01);
    184         return df1.format(da);
    185     }
    186 
    187     @SuppressWarnings("deprecation")
    188     public static String getLastDateOfMonth(Date now) {
    189         SimpleDateFormat df1 = new SimpleDateFormat(DATATIMEF_STR);
    190         Date da = new Date(now.getYear(), now.getMonth(), 31);
    191         return df1.format(da);
    192     }
    193 
    194     /**
    195      * 获取两个毫秒间隔的分钟
    196      * 
    197      * @param t1
    198      * @param t2
    199      * @return
    200      */
    201     public static int getMinutesBetweenMillis(long t1, long t2) {
    202         return (int) ((t1 - t2) / (60 * 1000));
    203     }
    204 
    205     /**
    206      * 判断目标时间是否处于某一时间段内
    207      * 
    208      * @param target
    209      * @param begin
    210      * @param end
    211      * @return
    212      */
    213     public static boolean compareTargetTime(Date target, String begin,
    214             String end) {
    215         // 格式化时间 暂时不考虑传入参数的判断，其他地方如果要调用，最好扩展判断一下入参问题
    216         String targetTime = dateToDateString(target, DATATIMEF_STR).substring(
    217                 11);// HH:mm:ss
    218         if (targetTime.compareTo(begin) >= 0 && end.compareTo(targetTime) >= 0) {
    219             return true;
    220         }
    221         return false;
    222     }
    223 
    224     /**
    225      * 
    226      * @param time1
    227      * @param timw2
    228      * @return time1 小于 time 2 返回 true
    229      */
    230     public static boolean compareTime(Date time1, Date time2) {
    231         long start = time1.getTime();
    232         long end = time2.getTime();
    233         if (start < end) {
    234             return true;
    235         }
    236 
    237         return false;
    238     }
    239 
    240     /**
    241      * 取得两个时间段的时间间隔 return t2 与t1的间隔天数 throws ParseException
    242      * 如果输入的日期格式不是0000-00-00 格式抛出异常
    243      */
    244     public static int getBetweenDays(String t1, String t2)
    245             throws ParseException {
    246         SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
    247         int betweenDays = 0;
    248         Date d1 = format.parse(t1);
    249         Date d2 = format.parse(t2);
    250         Calendar c1 = Calendar.getInstance();
    251         Calendar c2 = Calendar.getInstance();
    252         c1.setTime(d1);
    253         c2.setTime(d2);
    254         // 保证第二个时间一定大于第一个时间
    255         if (c1.after(c2)) {
    256             c1 = c2;
    257             c2.setTime(d1);
    258         }
    259         int betweenYears = c2.get(Calendar.YEAR) - c1.get(Calendar.YEAR);
    260         betweenDays = c2.get(Calendar.DAY_OF_YEAR)
    261                 - c1.get(Calendar.DAY_OF_YEAR);
    262         for (int i = 0; i < betweenYears; i++) {
    263             c1.set(Calendar.YEAR, (c1.get(Calendar.YEAR) + 1));
    264             betweenDays += c1.getMaximum(Calendar.DAY_OF_YEAR);
    265         }
    266         return betweenDays;
    267     }
    268 
    269     /**
    270      * 格式化时间 yyyy-MM-dd
    271      * 
    272      * @return
    273      */
    274     public static String getFormatDate(Date date) {
    275         return new SimpleDateFormat().format(date);
    276     }
    277 
    278     /**
    279      * 按照默认formatStr的格式，转化dateTimeStr为Date类型 dateTimeStr必须是formatStr的形式
    280      * 
    281      * @param dateTimeStr
    282      * @param formatStr
    283      * @return
    284      */
    285     public static Date getFormatDate(Date dateTimer, String formatStr) {
    286         try {
    287             if (dateTimer == null) {
    288                 return null;
    289             }
    290             java.text.DateFormat sdf = new SimpleDateFormat(formatStr);
    291             String timeStr = sdf.format(dateTimer);
    292             Date formateDate = sdf.parse(timeStr);
    293             return formateDate;
    294         } catch (ParseException e) {
    295             throw new RuntimeException(e);
    296         }
    297     }
    298 
    299     /**
    300      * 获取两个时间之间相差的天数
    301      * 
    302      * @param time1
    303      * @param time2
    304      * @return
    305      */
    306     public static long getQuot(String time1, String time2) {
    307         long quot = 0;
    308         SimpleDateFormat ft = new SimpleDateFormat("yyyy-MM-dd");
    309         try {
    310             Date date1 = ft.parse(time1);
    311             Date date2 = ft.parse(time2);
    312             quot = date1.getTime() - date2.getTime();
    313             quot = quot / 1000 / 60 / 60 / 24;
    314         } catch (ParseException e) {
    315             e.printStackTrace();
    316         }
    317         return quot;
    318     }
    319     
    320     public static long getQuot(Date time1, Date time2) {
    321         if(time1==null || time2==null)
    322             return -1;
    323         long quot = 0;
    324         quot = time1.getTime() - time2.getTime();
    325         quot = quot / 1000 / 60 / 60 / 24;
    326         return quot;
    327     }
    328 
    329     /**
    330      * 获取和当前时间相差的分钟数
    331      * 
    332      * @param begin
    333      * @return
    334      */
    335     public static long getDiffenceValue(Date begin) {
    336         long value = 0;
    337         Calendar cal = Calendar.getInstance();
    338         Date now = cal.getTime();
    339         value = (now.getTime() - begin.getTime()) / 1000 / 60;
    340         return value;
    341     }
    342     /**
    343      * 获取和当前时间相差的秒数
    344      * 
    345      * @param begin
    346      * @return
    347      */
    348     public static long getSecondsValue(Date begin) {
    349         long value = 0;
    350         Calendar cal = Calendar.getInstance();
    351         Date now = cal.getTime();
    352         value = (now.getTime() - begin.getTime()) / 1000;
    353         return value;
    354     }
    355 
    356     public static long getMillsBetweenTwoDate(Date date1, Date date2) {
    357         return date1.getTime() - date2.getTime();
    358     }
    359 
    360     /**
    361      * 求多少天前/后的日期
    362      * 
    363      * @param field
    364      *            单位：年，月，日
    365      * @param day
    366      *            多少天
    367      * @return
    368      */
    369     public static final Date addDate(int field, int day) {
    370         Calendar nowCalendar = Calendar.getInstance(Locale.CHINESE);
    371         nowCalendar.setTime(DateUtil.now());
    372         nowCalendar.add(field, day);
    373         return nowCalendar.getTime();
    374     }
    375     
    376     /**
    377      * 获取本月第一天
    378      * @return
    379      */
    380     public static final String getCurrFirstDay(){
    381         SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
    382         Calendar c = Calendar.getInstance();
    383         c.add(Calendar.MONTH, 0);
    384         c.set(Calendar.DAY_OF_MONTH, 1);// 设置为1号,当前日期既为本月第一天
    385         String first = format.format(c.getTime());
    386         return first;
    387     }
    388     
    389     /**
    390      * 获取本月第一天
    391      * @return
    392      */
    393     public static final String getCurrLastDay(){
    394         SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
    395         //获取当前月最后一天
    396         Calendar ca = Calendar.getInstance();   
    397         ca.set(Calendar.DAY_OF_MONTH, ca.getActualMaximum(Calendar.DAY_OF_MONTH)); 
    398         String last = format.format(ca.getTime());
    399         return last;
    400     }
    401 
    402     /**
    403      * date类型转timestamp类型
    404      * @return
    405      */
    406     public static final Timestamp dateToTimestamp(Date date){
    407         Timestamp time = new Timestamp(date.getTime());
    408         return time;
    409     }
    410     
    411     /**
    412      * timestamp类型转date类型
    413      * @return
    414      */
    415     public static final Date TimestampTodate(Timestamp date){
    416         Date d  = new Date(date.getTime());
    417         return d;
    418     }
    419     
    420     /**
    421      * String类型转date类型
    422      * @return
    423      */
    424     public static final Date StringTodate(String date){
    425         if(StringUtils.isNotBlank(date)){
    426             SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
    427             try {
    428                 return sdf.parse(date);
    429             } catch (ParseException e) {
    430                 return null;
    431             }
    432         }else{
    433             return null;
    434         }
    435     }
    436 }
    复制代码
