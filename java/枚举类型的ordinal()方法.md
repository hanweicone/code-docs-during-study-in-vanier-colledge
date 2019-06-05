<div class="blog-content-box">

<div class="article-header-box">

<div class="article-header">

<div class="article-title-box"><span class="article-type type-1 float-left">原</span>

# 从枚举类型的ordinal()方法说起

</div>

<div class="article-info-box">

<div class="article-bar-top" style="height: 26px;"><span class="time">2015年03月26日 15:59:01</span> [庭然](https://me.csdn.net/lili625) <span class="read-count">阅读数：12486</span> <span class="tags-box artic-tag-box"><span class="label">标签：</span> [枚举类型](https://so.csdn.net/so/search/s.do?q=枚举类型&t=blog) [开发](https://so.csdn.net/so/search/s.do?q=开发&t=blog) [代码分析](https://so.csdn.net/so/search/s.do?q=代码分析&t=blog) [java](https://so.csdn.net/so/search/s.do?q=java&t=blog) <span class="article_info_click">更多</span></span>

<div class="tags-box space"><span class="label">个人分类：</span> [代码分析](https://blog.csdn.net/lili625/article/category/3055455) [java](https://blog.csdn.net/lili625/article/category/3055453)</div>

</div>

</div>

</div>

</div>

<article class="baidu_pl">

<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post" style="height: 3126px; overflow: hidden;">

<div class="article-copyright">版权声明：本文为博主原创文章，未经博主允许不得转载。 https://blog.csdn.net/lili625/article/details/44651113</div>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css">

<div id="content_views" class="markdown_views">

## <a name="t0"></a>文章背景

本周有一个开发任务涉及到了枚举类型的修改，需要对枚举类型新增一项。在新增的时候我没有加在已有项的最后面，而是在中间随便找了个位置(其实也不是很随便，我是根据语义关联性觉得放在某一项后面比较合适)。没想到的是，我的无心之举经造成了大”**混乱**“，相关联的业务在使用该枚举类型时几乎都错位了。查了查，原来是ordinal()在作怪。写Java代码时间也不算短了，但用到枚举类型的次数不多，ordinal()方法就更少用了。趁着这次机会对枚举类型及ordinal()方法稍稍做了下研究，于是就有了这篇文章。

## <a name="t1"></a>Java枚举类型

> 枚举就是要让某个类型的变量的取值只能为若干个固定值中的一个，否则，编译器就会报错。枚举可以让编译器在编译时就可以控制源程序中填写的非法值，普通变量的方式在开发阶段无法实现这一目标。 —— [[ Java的枚举类型 ]](http://blog.sina.com.cn/s/blog_8c8c9be701012345.html)

### <a name="t2"></a>例子

参考了[java枚举类型enum的使用](http://blog.csdn.net/wgw335363240/article/details/6359614)这篇文章

    public enum Light {
           /**
            * 红灯
            */        
           RED , 
           /**
            * 绿灯
            */  
           GREEN , 
           /**
            * 黄灯
            */  
           YELLOW ;
    }

        public static void main(String[] args) {
            System.out.println(Light.GREEN.ordinal());
        }

输出结果是：1

### <a name="t3"></a>小结

我想，ordinal()方法在设计之初，仅仅只是像每一个javabean的get方法一样，返回枚举项在枚举类中出现的序号而已(从0开始的，所以这里的绿灯序号是1)。但是，**聪明**的我们，却**发掘**出了它的其他作用。聪明反被聪明误，说的就是我们吧。下面就将项目中的使用方式列出来，作为一个不成功的反例展示给大家。

## <a name="t4"></a>反例解析

### <a name="t5"></a>现场还原

服务端对图片枚举类型的定义：

    public enum ImageEnum {

        other("其它"),

        logo("_游戏logo"),

        split("_游戏截图"),

        banner("游戏大图"),

        advert("广告"),

        information("资讯"),

        column("栏目"),

        imgs("图集"),

        videopreview("视频预览");

        private final String value;

        /**
         * @param value
         */
        private ImageEnum(String value) {
            this.value = value;
        }

        /**
         * 定义获取游戏图片alt值
         * @param enumValue
         * @return
         */
        public static String getImageEnumValue(ImageEnum enumValue) {
            String val;
            switch (enumValue) {
            case other:
                val = ImageEnum.other.value;
                break;
            case logo:
                val = ImageEnum.logo.value;
                break;
            ……
            ……
            case imgs:
                val = ImageEnum.imgs.value;
                break;
            default:
                val = "";
            }
            return val;
        }
    }

action中声明一个枚举类：

        //设置图标类型
        ImageEnum banner = ImageEnum.banner;

前端页面拿到这个枚举类：

        gameImgBannerType = ${banner.ordinal()}

js中使用了枚举类的序号并作为参数传给服务端处理：

        jQuery('#file_upload').uploadify({
            'swf'     : '/public/include/uploadify/uploadify.swf',
            'uploader'  : '/Games/uploadImg?Id='+gameImgBannerType+'&gameId='+tmpGameId,
            'fileObjName' : 'file',
            'method'    : 'POST',
            'fileTypeExts'   : '*.*',      
            'formData'      : {},
             ……
                });

回到action层，看看action层拿到这个枚举类的序号干嘛用：

        public static void uploadImg(@Required @Valid File file, Boolean img2jpgs) throws IOException {
            response.setContentTypeIfNotSet("text/html"); 
            String imgType = RequestHelper.getParam("Id", 0);//拿到前端传过来的枚举类的序号
            String gameId = RequestHelper.getParam("gameId", 0);
            ……
            //图标类型,写入保存时值要加1(Note:注意这句话，为什么要加1？)
            int enumValue = Integer.valueOf(imgType);
            //获取图标类型
            ImageEnum imageEnum = ImageEnum.values()[enumValue];
            //游戏图片alt值
            String typeStr = ImageEnum.getImageEnumValue(imageEnum);
            ……
            //省去中间部分的处理逻辑
            try {
                if (imgImage.getId() == null) {
                    imgImage.setCreateTime(new Date());
                    imgImage.setModifyTime(new Date());
                    //设置上传文件类型(Note:果然在这里加了1，但是为什么要这么做呢？)
                    imgImage.setTypeId(enumValue + 1);
                    ……
                    ……
                    ImgImageDao.insert(imgImage, true);
                    ……
                } else {
                    ……
                }
                ……
            } catch (DuplicateNamesException e) {
                ……
            }
        }

OK，让我们串起来看看到底是怎么一回事

<div class="sequence-diagram"><svg height="377" version="1.1" width="891" xmlns="http://www.w3.org/2000/svg" style="overflow: hidden; position: relative; top: -0.34375px;"><desc style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);">Created with Raphaël 2.1.0</desc><text x="41.4609375" y="40.5" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">action</tspan></text><text x="41.4609375" y="336.5" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">action</tspan></text><text x="521.8046875" y="40.5" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">front page</tspan></text><text x="521.8046875" y="336.5" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">front page</tspan></text><text x="281.6328125" y="86" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">给，这个是banner的图片类型</tspan></text><text x="668.171875" y="137.5" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">好的，用户确实要上传一张banner图</tspan></text><text x="281.6328125" y="178" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">这是类型id、banner图对应的游戏id及图片本身</tspan></text><text x="182.3828125" y="229.5" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">OK，我会把这张图片处理后存下来</tspan></text><text x="281.6328125" y="280.5" text-anchor="middle" font="10px &quot;Arial&quot;" stroke="none" fill="#000000" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); text-anchor: middle; font-style: normal; font-variant: normal; font-weight: normal; font-stretch: normal; font-size: 16px; line-height: normal; font-family: &quot;Andale Mono&quot;, monospace;" font-size="16px" font-family="Andale Mono, monospace"><tspan style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);" dy="5.5">处理完毕，图片存在表里了，对应的图片类型id是你传过来的id+1</tspan></text></svg></div>

最后，让我们来揭开这神秘的面纱，为毛存的时候id要加1，且看这张表img_type:

<div class="table-box">

<table>

<thead>

<tr>

<th>id</th>

<th>name</th>

<th>create_time</th>

<th>modify_time</th>

</tr>

</thead>

<tbody>

<tr>

<td>1</td>

<td>其他</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>2</td>

<td>图标</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>3</td>

<td>截图</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>4</td>

<td>网游banner</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>5</td>

<td>广告</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>6</td>

<td>资讯</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>7</td>

<td>栏目</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>8</td>

<td>图集</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>9</td>

<td>视频预览</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

</tbody>

</table>

</div>

* * *

还记得ImageEnum类的各个项的顺序吗？对比一下，我想你跟我一样，露出了会心的微笑，终于知道这神秘的加1是怎么回事了。兜了好大的圈子，穿越了整个时空，却发现，**“其实就是二锅头，兑的那个白开水”**。

来，让我们试着用最简单的语言总结一下吧。前端有各种图片要上传，后端有一个通用的上传方式，后端存储的图片类型必须是img_type表里的9个数字之一。前后端于是约定了以ImageEnum中各个枚举项的序号作为标记。ImageEnum中枚举项的顺序和img_type表中各项的顺序一致，而序号是从0开始，表id却是从1开始的，因此服务端存储的时候要加1再存。Over。

### <a name="t6"></a>为啥不好

首先必须肯定的是，整个代码是完成了预设的功能的(废话，不完成能让上线么)。如果图片类型就这么多，以后再也不会新增，那么这样的代码其实也没啥好吐槽的。**但问题是**，图片类型真的会新增。甚至后台都开放了新增入口给运营同学，运营同学可以随意在img_type表里面加数据。试想一下吧，新业务来了，图片类型新增了，你在ImageEnum这个类中添加了一个新的枚举项，写了sql往img_type表里插数据。你小心翼翼地维持着ImageEnum枚举项和img_type表数据之间的对应关系，但运营后台开放的新增入口，却极有可能打破这一平衡。又或者像我一样，新接手这些代码，并不清楚枚举类和数据表之间的关系，在ImageEnum类中随意找了位置添加了一个枚举项，那么，旧有的数据就都乱套了。再或者，即使本地环境和测试环境都OK，可是线上环境多了一些图片类型，上线后才发现有问题。ordinal()只是个序号，我们却把它当做一个枚举项的唯一标识，让它承担了本不该承担的责任，那么，增加出错的可能性就不可避免了。

## <a name="t7"></a>修正之道(一)

改造ImageEnum

    public enum ImageEnum {

        other(1, "其它"),

        ……

        videopreview(9, "视频预览");

        private final Integer id;
        private final String value;

        /**
         * @param id
         * @param value
         */
        private ImageEnum(Integer id, String value) {
            this.id = id;
            this.value = value;
        }

        /**
         * 定义获取游戏图片alt值
         * @param enumValue
         * @return 图片alt值
         */
        public static String getImageEnumValue(ImageEnum enumValue) {
            String val;
            switch (enumValue) {
            case other:
                val = ImageEnum.other.value;
                break;
                ……
            case imgs:
                val = ImageEnum.imgs.value;
                break;
            }
            return val;
        }

        /**
         * 获取图片类型对应的id
         * @param enumValue
         * @return id
         */
        public static Integer getImageEnumId(ImageEnum enumValue) {
            Integer id;
            switch (enumValue) {
            case other:
                id = ImageEnum.other.id;
                break;
                ……
            case imgs:
                id = ImageEnum.imgs.id;
                break;
            }
            return id;
        }

        /**
         * 根据id获取图片类型
         * @param id
         * @return
         */
        public static ImageEnum getImageEnum(Integer id) {
            ImageEnum val = null;
            switch (id) {
            case 1:
                val = ImageEnum.other;
                break;
            ……
            case 9:
                val = ImageEnum.imgs;
                break;
            }
            return val;
        }

    }

action中声明枚举类的代码不变，前端页面拿到这个枚举类之后不再拿ordinal()而是id：

        gameImgBannerType = ${banner.id}

js部分也不改变，回到action层，这里也有变化：

        public static void uploadImg(@Required @Valid File file, Boolean img2jpgs) throws IOException {
            response.setContentTypeIfNotSet("text/html"); 
            String imgTypeId = RequestHelper.getParam("Id", 0);//拿到前端传过来是枚举类型的id而不是序号
            String gameId = RequestHelper.getParam("gameId", 0);
            ……
            //获取图标类型
            ImageEnum imageEnum = ImageEnum.getImageEnum(imgTypeId);
            //游戏图片alt值
            String typeStr = ImageEnum.getImageEnumValue(imageEnum);
            ……
            //省去中间部分的处理逻辑
            try {
                if (imgImage.getId() == null) {
                    imgImage.setCreateTime(new Date());
                    imgImage.setModifyTime(new Date());
                    //设置上传文件类型，这里不用再加1了
                    imgImage.setTypeId(imgTypeId);
                    ……
                    ……
                    ImgImageDao.insert(imgImage, true);
                    ……
                } else {
                    ……
                }
                ……
            } catch (DuplicateNamesException e) {
                ……
            }
        }

经过改造之后，至少我们已经摆脱了ordinal()这个我们不太熟悉的方法，另外一个大大的好处就是，ImageEnum类里的枚举项，可以不用限定顺序了，新增类型的时候，我爱在哪行加都行。  
但是，**还不够好**。因为ImageEnum里的id还是要和img_type中的id保持一致，代码耦合依然严重。因此，**继续优化**！

## <a name="t8"></a>修正之道(二)

为什么一定要用枚举类呢？不用不可以吗？答案是，可以。接下来我们尝试抛弃枚举类型来实现业务功能。  
首先我们回头看一下Java枚举类的定义，枚举类是对取值范围的一个限定，比如说交通灯的颜色，一定是红黄绿三种，那我们创建一个交通灯的枚举类是合乎情景合乎常理的。接下来再看我们的业务场景。(与游戏相关的)图片类型明显不是像交通灯颜色那样是基本固定的，尤其是后台给出了新增入口，就更加肯定地告诉我们，图片类型是可以新增而且有经常新增的可能性。既然如此，我们为何要维护两套图片类型呢？假设说我们从头开始做这个功能，这样设计是不是会好一些？  
先设计表结构，其中id是primary key：

<div class="table-box">

<table>

<thead>

<tr>

<th>id</th>

<th>name</th>

<th>alt</th>

<th>create_time</th>

<th>modify_time</th>

</tr>

</thead>

<tbody>

<tr>

<td>other</td>

<td>其他</td>

<td>其他</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>logo</td>

<td>图标</td>

<td>_游戏logo</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>split</td>

<td>截图</td>

<td>_游戏截图</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>banner</td>

<td>网游banner</td>

<td>游戏大图</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>advert</td>

<td>广告</td>

<td>广告</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>information</td>

<td>资讯</td>

<td>资讯</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>column</td>

<td>栏目</td>

<td>栏目</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>imgs</td>

<td>图集</td>

<td>图集</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

<tr>

<td>videopreview</td>

<td>视频预览</td>

<td>视频预览</td>

<td>2000-01-01</td>

<td>2013-09-25</td>

</tr>

</tbody>

</table>

</div>

* * *

然后在ImgType(即与数据表对应的实体)中添加一些静态变量(之所以是一些而不是全部，是因为并不是所有的图片类型都在后台有用到，也许后台只需要用到banner和videopreiview的上传，因此只声明需要用到的)

    public class ImgType {
        public static final String IMG_TYPE_OTHER = "other";
        ……
        public static final String IMG_TYPE_VIDEOPREVIEW = "videopreview";
        //其他逻辑省略
        ……
    }

ImgTypeDao提供根据主键查询的功能:

    public class ImgTypeDao {

        ……
        /**
         * 根据主键获取数据对象
         * @param name
         * @return 图片类型
         */
        public static ImgType getByPrimaryKey(String id){
            //省略具体逻辑
        }
        ……
    }

action中直接声明banner图片类型：

        //设置图标类型
        String gameImgBannerType= ImgType.IMG_TYPE_BANNER;

前端页面拿到banner图片类型：

        gameImgBannerType = ${gameImgBannerType}

js部分不变，回到action层，这里变化如下：

        public static void uploadImg(@Required @Valid File file, Boolean img2jpgs) throws IOException {
            response.setContentTypeIfNotSet("text/html"); 
            String imgTypeId = RequestHelper.getParam("Id", 0);//拿到前端传过来是图片类型的id
            String gameId = RequestHelper.getParam("gameId", 0);
            ……
            //获取图标类型
            ImgType imgType = ImgTypeDao.getByPrimaryKey(imgTypeName);
            //游戏图片alt值
            String typeStr = imgType.getAlt();
            ……
            //省去中间部分的处理逻辑
            try {
                if (imgImage.getId() == null) {
                    imgImage.setCreateTime(new Date());
                    imgImage.setModifyTime(new Date());
                    //设置上传文件类型，这里的id是字符串类型
                    imgImage.setTypeId(imgTypeId);
                    ……
                    ……
                    ImgImageDao.insert(imgImage, true);
                    ……
                } else {
                    ……
                }
                ……
            } catch (DuplicateNamesException e) {
                ……
            }
        }

调整完的代码有以下优点：

*   少了一个枚举类(有人要说了，你类是少了，但是多了几个常量的声明啊，确实，但是两相比较，代码量还是变少的)
*   前后端约定的图片类型标识不再是数字id而是更加表意的字符串
*   即使运营同学在线上添加了图片类型(在开发不知情的情况下)，也几乎不会对开发代码及上线造成任何影响。因为字符串是表意的，不同事物的表意字符串一般不会相同
*   流程清晰顺畅无怪异的地方，新同学接手后，在不了解整体流程的情况下新增图片类型，也不会出错。

## <a name="t9"></a>总结

本文从枚举类型的ordinal()方法说起，最后却弃枚举类型而去，是枚举类型不好吗？肯定不是。事实上，[java 枚举类型enum的使用](http://blog.csdn.net/wgw335363240/article/details/6359614)这篇文档刚好和我走了一条相反的道路，他的观点是枚举类强于静态常量，具体理由有兴趣可以看原文。虽然路是相反的，但我想观点并不冲突。在我看来，枚举类型和静态常量都有自己更适合的场景。在决定使用枚举类型还是静态常量的时候，多思考一下代码的扩展性和可维护性，就知道到底应该选择哪一个了。这里不再赘述，文章到这里就结束吧。

* * *

</div>

<link href="https://csdnimg.cn/release/phoenix/mdeditor/markdown_views-258a4616f7.css" rel="stylesheet"></div>

</article>

</div>
