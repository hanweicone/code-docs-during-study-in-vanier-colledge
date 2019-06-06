<div class="blog-content-box">
	<div class="article-header-box">
		<div class="article-header">
			<div class="article-title-box">
				<span class="article-type type-1 float-left">原</span>				<h1 class="title-article">Java工作利器之常用工具类（一）——数字工具类-数字转汉字</h1>
			</div>
			<div class="article-info-box">
				<div class="article-bar-top">
																				<span class="time">2015年11月16日 10:44:59</span>
					<a class="follow-nickName" href="https://me.csdn.net/xiaoxian8023" target="_blank">龙轩</a>
						<span class="read-count">阅读数：7886</span>
						
																															</div>
				<div class="operating">
									</div>
			</div>
		</div>
	</div>
	<article class="baidu_pl">
		<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post">
								<div class="article-copyright">
                  					<svg class="icon" title="CSDN认证原创" aria-hidden="true" style="width:53px; height: 18px; vertical-align: -4px;">
							<use xlink:href="#CSDN_Cert"></use>
					</svg>
                  					
					版权声明：本文为博主原创文章，未经博主允许不得转载。如需转载请声明：【转自 http://blog.csdn.net/xiaoxian8023 】					https://blog.csdn.net/xiaoxian8023/article/details/49834589				</div>
								<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">
								            <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">
						<div class="htmledit_views" id="content_views">
                <p>本人是从事互联网金融行业的，所以会接触到一些金融类的问题，常见的一种就是数字转汉字大小写的问题。所以抽空就写了一个小小的工具类，实现了数字转汉字、大数相加、相减、相乘的工具类，希望能帮助有需求的同行们。本篇就分享一下数字转化为汉字的思路吧。</p>

<p>&nbsp;</p>

<p>数字转汉字的原理：</p>

<ol><li>拆分：由于整数部分要加权值，而小数部分直接转换即可，所以首先要将数字拆分成整数+小数；</li>
	<li>整数处理：按照我们的中国人的习惯，把数字格式化成4位一组，不足4位前面补0。每次处理4位，按位匹配数组中的汉字+权值。即按照数值找数字数组（num_lower 、num_upper&nbsp;）中对应位置的汉字，按照在4位中的偏移量在单位权值数组（unit_lower 、unit_upper&nbsp;）中找。比如21，转化4位为0021，前面的0不用管，2对应数字“二”，权值是“十”，1对应数字“一”，权值是“（个）”用空字符串代替。即得到“二十一”。每4位处理完后，还要整体对应一个权值，比如“万、亿、兆”等；</li>
	<li>小数处理：小数部分直接按位对应汉字数组和权值即可。</li>
</ol><p>废话了这么多，可能云里雾里的，看看具体代码吧：</p>

<pre class="has"><code class="language-java">    //num 表示数字，lower表示小写，upper表示大写
    private static final String[] num_lower = { "零", "一", "二", "三", "四", "五", "六", "七", "八", "九" };
    private static final String[] num_upper = { "零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖" };

    //unit 表示单位权值，lower表示小写，upper表示大写
    private static final String[] unit_lower = { "", "十", "百", "千" };
    private static final String[] unit_upper = { "", "拾", "佰", "仟"};
    private static final String[] unit_common = {"","万", "亿","兆","京","垓","秭","穰","沟","涧","正","载"};

    //允许的格式
    private static final List&lt;String&gt; promissTypes = Arrays.asList("INTEGER","INT","LONG","DECIMAL","FLOAT","DOUBLE","STRING","BYTE","TYPE","SHORT");

    /**
     * 数字转化为小写的汉字
     * 
     * @param num 将要转化的数字
     * @return
     */
    public static String toChineseLower(Object num){
        return format(num, num_lower, unit_lower);
    }

    /**
     *  数字转化为大写的汉字
     *  
     * @param num 将要转化的数字
     * @return
     */
    public static String toChineseUpper(Object num){
        return format(num, num_upper, unit_upper);
    }

    /**
     * 格式化数字
     * 
     * @param num            原数字
     * @param numArray     数字大小写数组
     * @param unit            单位权值
     * @return
     */
    private static String format(Object num,String[] numArray,String[] unit){
        if(!promissTypes.contains(num.getClass().getSimpleName().toUpperCase())){
            throw new RuntimeException("不支持的格式类型");
        }
        //获取整数部分
        String intnum = getInt(String.valueOf(num));
        //获取小数部分
        String decimal = getFraction(String.valueOf(num));
        //格式化整数部分
        String result = formatIntPart(intnum,numArray,unit);
        if(!"".equals(decimal)){//小数部分不为空
            //格式化小数
            result += "点"+formatFractionalPart(decimal, numArray);
        }
        return result;
    }

    /**
     * 格式化整数部分
     * 
     * @param num    整数部分
     * @param numArray 数字大小写数组
     * @return
     */
    private static String formatIntPart(String num,String[] numArray,String[] unit){

        //按4位分割成不同的组（不足四位的前面补0）
        Integer[] intnums = split2IntArray(num);

        boolean zero = false;
        StringBuffer sb = new StringBuffer();
        for(int i=0;i&lt;intnums.length;i++){
            //格式化当前4位
            String r = formatInt(intnums[i], numArray,unit);
            if("".equals(r)){//
                if((i+1)==intnums.length){
                    sb.append(numArray[0]);//结果中追加“零”
                }else{
                    zero=true;
                }
            }else{//当前4位格式化结果不为空（即不为0）
                if(zero || (i&gt;0 &amp;&amp; intnums[i]&lt;1000)){//如果前4位为0，当前4位不为0
                    sb.append(numArray[0]);//结果中追加“零”
                }
                sb.append(r);
                sb.append(unit_common[intnums.length-1-i]);//在结果中添加权值
                zero=false;
            }
        }
        return sb.toString();
    }

    /**
     * 格式化小数部分
     * 
     * @param decimal 小数部分
     * @param numArray 数字大小写数组
     * @return
     */
    private static String formatFractionalPart(String decimal,String[] numArray) {
        char[] val = String.valueOf(decimal).toCharArray();
        int len = val.length;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i &lt; len; i++) {
            int n = Integer.valueOf(val[i] + "");
            sb.append(numArray[n]);
        }
        return sb.toString();
    }
</code></pre>

<p>拆分整数和小数的方法在这里：</p>

<pre class="has"><code class="language-java">    /**
     * 获取整数部分
     * 
     * @param num
     * @return
     */
    private static String getInt(String num){
        //检查格式
        checkNum(num);

        char[] val = String.valueOf(num).toCharArray();
        StringBuffer sb = new StringBuffer();
        int t , s = 0;
        for (int i = 0; i &lt; val.length; i++) {
            if(val[i]=='.') {
                break;
            }
            t = Integer.parseInt(val[i]+"",16);
            if(s+t==0){
                continue;
            }
            sb.append(t);
            s+=t;
        }
        return (sb.length()==0? "0":sb.toString());
    }

    /**
     * 获取小数部分
     * 
     * @param num
     * @return
     */
    private static String getFraction(String num){
        int i = num.lastIndexOf(".");
        if(num.indexOf(".") != i){
            throw new RuntimeException("数字格式不正确，最多只能有一位小数点！");
        }
        String fraction =""; 
        if(i&gt;=0){
            fraction = getInt(new StringBuffer(num).reverse().toString());
            if(fraction.equals("0")){
                return "";
            }
        }
        return new StringBuffer(fraction).reverse().toString();
    }

    /**
     * 检查数字格式
     * 
     * @param num
     */
    private static void checkNum(String num) {
        if(num.indexOf(".") != num.lastIndexOf(".")){
            throw new RuntimeException("数字["+num+"]格式不正确!");
        }
        if(num.indexOf("-") != num.lastIndexOf("-") || num.lastIndexOf("-")&gt;0){
            throw new RuntimeException("数字["+num+"]格式不正确！");
        }
        if(num.indexOf("+") != num.lastIndexOf("+")){
            throw new RuntimeException("数字["+num+"]格式不正确！");
        }
        if(num.indexOf("+") != num.lastIndexOf("+")){
            throw new RuntimeException("数字["+num+"]格式不正确！");
        }
        if(num.replaceAll("[\\d|\\.|\\-|\\+]", "").length()&gt;0){
            throw new RuntimeException("数字["+num+"]格式不正确！");
        }
    }
</code></pre>

<p>通过这种分而治之的思路，处理起来就简单多了。写个main函数调用一下：</p>

<pre class="has"><code class="language-java">    public static void main(String[] args) {
        short s = 10;
        byte b=10;
        char c='A';
        Object[] nums = {s, b, c, 0, 1001, 100100001L, 21., 205.23F, 205.23D, "01000010", "1000000100105.0123", ".142", "20.00", "1..2", true};
        System.out.println("将任意数字转化为汉字(包括整数、小数以及各种类型的数字)");
        System.out.println("--------------------------------------------");
        for(Object num :nums){
            try{
                System.out.print("["+num.getClass().getSimpleName()+"]"+num);
                for(int i=0;i&lt;25-String.valueOf(num+num.getClass().getSimpleName()).length();i+=4){
                    System.out.print("\t");
                }
                //调用转化为小写和大写
                System.out.print(" format:"+toChineseLower(num));
                System.out.println("【"+toChineseUpper(num)+"】");
            }catch(Exception e){
                System.out.println(" 错误信息："+e.getMessage());
            }
        }
    }
</code></pre>

<p><br>
看看结果吧：</p>

<p><img alt="" class="has" src="https://img-blog.csdn.net/20151114113812178?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center"></p>

<p>&nbsp;</p>

<p>从上述代码和运行结果中，我们可以看到该功能支持多种数据类型的转换、支持转化为一般汉字和财务专用大写汉字。还可以智能处理非正常逻辑的数字。比如“20”会转化为“二十”而非“二十零”；“1 0000 0001”&nbsp;转换成“一亿零一”而非“一亿零万零一”。</p>

<p>工具类包代码已分享到github上：<a href="https://github.com/Arronlong/commonutils" rel="nofollow">https://github.com/Arronlong/commonutils</a></p>

<p>当前工具类代码（可能博文中的代码略有出入）：<a href="https://github.com/Arronlong/commonutils/blob/master/src/main/java/com/arronlong/common/util/num/NumUtils.java" rel="nofollow">https://github.com/Arronlong/commonutils/blob/master/src/main/java/com/arronlong/common/util/num/NumUtils.java</a></p>

<p>这里只分享了一个转换汉字的功能，下篇将分享一下大数相乘、相加、相减的方法。支持小数和负数的运算，敬请期待。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>            </div>
                      </div>
	</article>
</div>
