<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <link rel="canonical" href="https://blog.csdn.net/misswuxl/article/details/78198489"/>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit"/>
    <meta name="force-rendering" content="webkit"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="referrer" content="always">
    <meta http-equiv="Cache-Control" content="no-siteapp" /><link rel="alternate" media="handheld" href="#" />
    <meta name="shenma-site-verification" content="5a59773ab8077d4a62bf469ab966a63b_1497598848">
        <meta name="csdn-baidu-search"  content='{"autorun":true,"install":true,"keyword":"github：提交本地html到github - misswuxl的博客"}'>

    <link href="https://csdnimg.cn/public/favicon.ico" rel="SHORTCUT ICON">
    <title>github：提交本地html到github - misswuxl的博客 - CSDN博客</title>

                    <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/detail-7fc618a1d6.min.css">

            <script type="application/ld+json">{"@context":"https:\/\/ziyuan.baidu.com\/contexts\/cambrian.jsonld","@id":"https:\/\/blog.csdn.net\/misswuxl\/article\/details\/78198489","appid":"1563894916825412","title":"github\uff1a\u63d0\u4ea4\u672c\u5730html\u5230github - misswuxl\u7684\u535a\u5ba2","images":["https:\/\/img-blog.csdn.net\/20171010223639207?watermark\/2\/text\/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=\/font\/5a6L5L2T\/fontsize\/400\/fill\/I0JBQkFCMA==\/dissolve\/70\/gravity\/Center","https:\/\/img-blog.csdn.net\/20171010224019887?watermark\/2\/text\/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=\/font\/5a6L5L2T\/fontsize\/400\/fill\/I0JBQkFCMA==\/dissolve\/70\/gravity\/Center","https:\/\/img-blog.csdn.net\/20171010225057594?watermark\/2\/text\/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=\/font\/5a6L5L2T\/fontsize\/400\/fill\/I0JBQkFCMA==\/dissolve\/70\/gravity\/Center"],"pubDate":"2019-06-04T04:03:02"}</script>

            <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/themes/skin-yellow/skin-yellow-2eefd34acf.min.css">
        <script type="text/javascript">
        var username = "misswuxl";
        var blog_address = "https://blog.csdn.net/misswuxl";
        var static_host = "https://csdnimg.cn/release/phoenix/";
        var currentUserName = "weixin_44094314";
        var isShowAds = true;
        var isOwner = false;
        var loginUrl = "http://passport.csdn.net/account/login?from=https://blog.csdn.net/misswuxl/article/details/78198489"
        var blogUrl = "https://blog.csdn.net/";

        var curSkin = "skin-yellow";
        // 第四范式所需数据
        var articleTitles = "github：提交本地html到github - misswuxl的博客";

        var nickName = "脖子有点儿疼";
        var isCorporate = false;
        var subDomainBlogUrl = "https://blog.csdn.net/"
        var digg_base_url = "https://blog.csdn.net/misswuxl/phoenix/comment";
        var articleDetailUrl = "https://blog.csdn.net/misswuxl/article/details/78198489";
    </script>
    <script src="https://csdnimg.cn/public/common/libs/jquery/jquery-1.9.1.min.js" type="text/javascript"></script>
    <script src="https://csdnimg.cn/rabbit/exposure-click/main-1.0.6.js"></script>
    <script src="//g.csdnimg.cn/??fixed-sidebar/1.1.3/fixed-sidebar.js,track/1.2.6/track.js" type="text/javascript"></script>
    <link rel="stylesheet" href="https://csdnimg.cn/public/sandalstrap/1.4/css/sandalstrap.min.css">
    <style>
        .MathJax, .MathJax_Message, .MathJax_Preview{
            display: none
        }
    </style>
</head>
<body class="nodata " > 
    <link rel="stylesheet" href="https://csdnimg.cn/public/common/toolbar/content_toolbar_css/content_toolbar.css">
    <script id="toolbar-tpl-scriptId" src="https://csdnimg.cn/public/common/toolbar/js/content_toolbar.js" type="text/javascript" domain="https://blog.csdn.net/"></script>
<div id="kp_box_476" data-pid="476" data-track-view='{"mod":"kp_popu_476-845","con":",,"}' data-track-click='{"mod":"kp_popu_476-845","con":",,"}'><script src="//csdnimg.cn/public/common/indexSuperise/1.0.7/indexSuperise.js?20190508180304"></script>
<script>
window.csdn.indexSuperise({
zIndex:11000,
      smallMoveImg: '//img-ads.csdn.net/2019/201905051104247931.png',
      bigMoveImg: '//img-ads.csdn.net/2019/201905051104104645.png',
     link:'//edu.csdn.net/topic/python115?utm_source=blogpopup',
boxStyle:140,
trackSuperId:476,
smallMove:'notMove',  
trackSId:845
    });
</script></div><link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/blog_code-c3a0c33d5c.css">
<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/vendor/pagination/paging.css">
<script type="text/javascript">
	var NEWS_FEED = function(){}
</script>

<link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/chart-3456820cac.css" />
<div class="container clearfix" id="mainBox">
			<div class="recommend-right">

</div>	    <main>
        <div class="blog-content-box">
  <div class="article-header-box">
    <div class="article-header">
      <div class="article-title-box">
        <span class="article-type type-4 float-left">译</span>        

# github：提交本地html到github

      </div>
      <div class="article-info-box">
        <div class="article-bar-top">
                                                  <span class="time">2017年10月10日 22:33:59</span>
          [脖子有点儿疼](https://me.csdn.net/misswuxl)
          <span class="read-count">阅读数：156</span>

                          <span class="tags-box artic-tag-box">
                <span class="label">标签：</span>
                                  [github                                  ](https://so.csdn.net/so/search/s.do?q=github&t=blog)
              </span>
                                      <div class="tags-box space">
                <span class="label">个人分类：</span>
                                  [github                                  ](https://blog.csdn.net/misswuxl/article/category/7216804)
              </div>
                                          </div>
        <div class="operating">
                  </div>
      </div>
    </div>
  </div>
  <article class="baidu_pl">
    <div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod=popu_307 data-dsm="post">
            <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css" />
                              <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-f57960eb32.css" />
          <div class="htmledit_views" id="content_views">

前提：下载好github，注册好github账号

1.登录github账号，点击 +  

![](https://img-blog.csdn.net/20171010223639207?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

2.来自  http://www.cnblogs.com/lixiaolun/p/5048954.html

![](https://img-blog.csdn.net/20171010224019887?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

3.打开Git Bash  进行操作   来自 https://zhidao.baidu.com/question/1303468264429394659.html

![](https://img-blog.csdn.net/20171010225057594?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

4.复制id_rsa.pub的内容 (在windows当前用户目录下生成.ssh文件夹中)，打开github网页

![](https://img-blog.csdn.net/20171010225744883?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![](https://img-blog.csdn.net/20171010225845600?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

![](https://img-blog.csdn.net/20171010230145449?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)该图片来自  http://www.cnblogs.com/lixiaolun/p/5048954.html

5..来自  http://www.cnblogs.com/lixiaolun/p/5048954.html

格式：https;//github.com/用户名/**仓库名**.git

作用就是 在你的 .ssh文件夹下 创建一个  以**仓库名**为名称的文件夹，在这个仓库名文件夹中  放上你要上传的文件

![](https://img-blog.csdn.net/20171010230659674?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

以上就是第一次的配置过程

6.以后每次上传从这个步骤开始即可

![](https://img-blog.csdn.net/20171011201641024?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbWlzc3d1eGw=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

A.git add .

B.git commit  用来书写你本次提交的一个注释 方便以后的查找   ，这个注释必须要有 不能不写

如果直接git commit  ，那么会进入 注释的插入页面 ，你需要在光标所在的位置 进行注释的撰写；

写好之后，1.按esc  2.再按： 3.再按x

或者 直接 git commit -m "我是注释"

C.git push

然后线上就有了哦~~~

          </div>
                  </div>
  </article>
</div>

<div class="hide-article-box hide-article-pos text-center">
      <a class="" id="btn-readmore" data-track-view='{"mod":"popu_376","con":",https://blog.csdn.net/misswuxl/article/details/78198489,"}' data-track-click='{"mod":"popu_376","con":",https://blog.csdn.net/misswuxl/article/details/78198489,"}'>
    展开阅读全文
    <svg class="icon chevrondown" aria-hidden="true">
        <use xlink:href="#csdnc-chevrondown"></use>
      </svg>
    </a>
    </div>
<script>
  $(".MathJax").remove();
  if ($('div.markdown_views pre.prettyprint code.hljs').length > 0) {
    $('div.markdown_views')[0].className = 'markdown_views';
  }
</script>        <div id="dmp_ad_58"><div id="kp_box_58" data-pid="58" data-track-view='{"mod":"kp_popu_58-386","con":",,"}' data-track-click='{"mod":"kp_popu_58-386","con":",,"}'><div style="width:100%;background:#fff;">
<script type="text/javascript" src="//rabc1.iteye.com/production/resource/web/6xwm4l.js?lg=ydmpioh"></script>
</div></div></div>        <a id="commentBox"></a>
<div class="comment-box">

	<div class="comment-edit-box d-flex">
		<a id="commentsedit"></a>
		<div class="user-img">
			[
				![](https://avatar.csdn.net/6/F/7/3_weixin_44094314.jpg)
			](//me.csdn.net/weixin_44094314)
		</div>
		<form id="commentform">
			<input type="hidden" id="comment_replyId">
			<textarea class="comment-content" name="comment_content" id="comment_content" placeholder="想对作者说点什么"></textarea>
			<div class="opt-box"> <!-- d-flex -->
				<div id="ubbtools" class="add_code">
					[](#insertcode)
				</div>
				<input type="hidden" id="comment_replyId" name="comment_replyId">
				<input type="hidden" id="article_id" name="article_id" value="78198489">
				<input type="hidden" id="comment_userId" name="comment_userId" value="">
				<input type="hidden" id="commentId" name="commentId" value="">
				<div style="display: none;" class="csdn-tracking-statistics tracking-click" data-mod="popu_384">[发表评论](#)</div>
				<div class="dropdown" id="myDrap">
					<a class="dropdown-face d-flex align-items-center" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
					<div class="txt-selected text-truncate">添加代码片</div>
					<svg class="icon d-block" aria-hidden="true">
						<use xlink:href="#csdnc-triangledown"></use>
					</svg>
					</a>

*   <a data-code="html">HTML/XML</a>
*   <a data-code="objc">objective-c</a>
*   <a data-code="ruby">Ruby</a>
*   <a data-code="php">PHP</a>
*   <a data-code="csharp">C</a>
*   <a data-code="cpp">C++</a>
*   <a data-code="javascript">JavaScript</a>
*   <a data-code="python">Python</a>
*   <a data-code="java">Java</a>
*   <a data-code="css">CSS</a>
*   <a data-code="sql">SQL</a>
*   <a data-code="plain">其它</a>
				</div>  
				<div class="right-box">
					<span id="tip_comment" class="tip">还能输入_1000_个字符</span>
					<input type="submit" class="btn btn-sm btn-red btn-comment" value="发表评论">
				</div>
			</div>
		</form>
	</div>

		<div class="comment-list-container">
		<a id="comments"></a>
		<div class="comment-list-box">
		</div>
		<div id="commentPage" class="pagination-box d-none"></div>
		<div class="opt-box text-center">
			<div class="btn btn-sm btn-link-blue" id="btnMoreComment"></div>
		</div>
	</div>
</div>
        <div class="recommend-box">
                            <div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/dongguan_123/article/details/52812721,BlogCommendFromBaidu_2"}'>
	<div class="content">
		[

#### 
				在_github_上浏览_html_文件		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">10-14</span>
				<span class="read-num hover-hide">
					阅读数 
					1009</span>

			</div>
		](https://blog.csdn.net/dongguan_123/article/details/52812721 "在github上浏览html文件")

			[
				<span class="desc oneline">可以通过http://htmlpreview.github.io/这个网站，直接在线预览html页面。即在自己github仓库里html文件的网址前方粘贴http://htmlpreview.gith...</span>
			](https://blog.csdn.net/dongguan_123/article/details/52812721 "在github上浏览html文件")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> donggua_123的博客</span>](https://blog.csdn.net/dongguan_123)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u010832551/article/details/50747950,BlogCommendFromBaidu_0"}'>
	<div class="content">
		[

#### 
				_Github_上值得推荐的10个_HTML_5资源		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">02-26</span>
				<span class="read-num hover-hide">
					阅读数 
					5031</span>

			</div>
		](https://blog.csdn.net/u010832551/article/details/50747950 "Github上值得推荐的10个HTML5资源")

			[
				<span class="desc oneline">1H5FullscreenPagehttps://github.com/lvming6816077/H5FullscreenPage基于zepto.js或者jquery.js的构建滚动动画页面的框架，...</span>
			](https://blog.csdn.net/u010832551/article/details/50747950 "Github上值得推荐的10个HTML5资源")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 让我们荡起双桨的博客</span>](https://blog.csdn.net/u010832551)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yanhuuii/article/details/72793392,BlogCommendFromBaidu_1"}'>
	<div class="content">
		[

#### 
				上传_本地_项目 到_GitHub_然后显示_html_页面		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">05-28</span>
				<span class="read-num hover-hide">
					阅读数 
					4202</span>

			</div>
		](https://blog.csdn.net/yanhuuii/article/details/72793392 "上传本地项目 到GitHub然后显示html页面")

			[
				<span class="desc oneline">1.打开GitBash输入cd加空格然后把你要上传的目录拖拽到客户端里面然后按回车键2.gitinit回车键3.gitadd.回车键（gitadd.之后会出现一大堆的英文是你要上传的内容的）4.git...</span>
			](https://blog.csdn.net/yanhuuii/article/details/72793392 "上传本地项目 到GitHub然后显示html页面")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> yanhuuii的博客</span>](https://blog.csdn.net/yanhuuii)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Yujie_Yang/article/details/79092409,BlogCommendFromQuerySearch_3"}'>
	<div class="content">
		[

#### 
				Git敲门(注册、建库、git命令、上传_本地_静态_html_并展示在_GitHub_ Pages)		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">01-18</span>
				<span class="read-num hover-hide">
					阅读数 
					470</span>

			</div>
		](https://blog.csdn.net/Yujie_Yang/article/details/79092409 "Git敲门(注册、建库、git命令、上传本地静态html并展示在GitHub Pages)")

			[
				<span class="desc oneline">前言使用GitHub工作也有大段时间了，不过平时只是当做一个代码管理工具，在可视化界面完成克隆、分支、拉取、暂存、上传等事情，不过不得不承认有一个可视化工具会方便很多，特别是对比冲突代码的时候真的很方...</span>
			](https://blog.csdn.net/Yujie_Yang/article/details/79092409 "Git敲门(注册、建库、git命令、上传本地静态html并展示在GitHub Pages)")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Yujie_Yang的博客</span>](https://blog.csdn.net/Yujie_Yang)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_59" data-pid="59" data-track-view='{"mod":"kp_popu_59-860","con":",,html"}' data-track-click='{"mod":"kp_popu_59-860","con":",,html"}'><iframe src="https://kunpeng-sc.csdnimg.cn/#/preview/109?positionId=59&queryWord=html" frameborder="0" width= "100%"  height= "75px" scrolling="no" ></iframe></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/y13156556538/article/details/79297162,BlogCommendFromQuerySearch_4"}'>
	<div class="content">
		[

#### 
				_github__提交__本地_代码方法		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">02-09</span>
				<span class="read-num hover-hide">
					阅读数 
					1227</span>

			</div>
		](https://blog.csdn.net/y13156556538/article/details/79297162 "github提交本地代码方法")

			[
				<span class="desc oneline">首先你得先创建仓库为仓库取一个名字，然后点击创建就会有一个仓库了，github是服务端，要想在自己电脑上使用git我们还需要一个git客户端，windows用户请下载 http://msysgit.g...</span>
			](https://blog.csdn.net/y13156556538/article/details/79297162 "github提交本地代码方法")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> y13156556538的博客</span>](https://blog.csdn.net/y13156556538)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yzh785119509/article/details/82902583,BlogCommendFromQuerySearch_5"}'>
	<div class="content">
		[

#### 
				_本地_项目_提交_到_Github_远程仓库项目分支的全过程——贼详细		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">09-29</span>
				<span class="read-num hover-hide">
					阅读数 
					278</span>

			</div>
		](https://blog.csdn.net/yzh785119509/article/details/82902583 "本地项目提交到Github远程仓库项目分支的全过程——贼详细")

			[
				<span class="desc oneline">个人学习，指正可以，不喜勿喷！！！项目文件（不是真实项目，仅演示）：$lltest_project/total1-rw-r--r--1Y19712124九月2920:39READEM1.本地初始化gi...</span>
			](https://blog.csdn.net/yzh785119509/article/details/82902583 "本地项目提交到Github远程仓库项目分支的全过程——贼详细")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> yzh785119509的博客</span>](https://blog.csdn.net/yzh785119509)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/gang456789/article/details/81084403,BlogCommendFromQuerySearch_6"}'>
	<div class="content">
		[

#### 
				将_本地_的代码上传到_github_ ，_Github__提交_更改的代码，		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">07-17</span>
				<span class="read-num hover-hide">
					阅读数 
					1017</span>

			</div>
		](https://blog.csdn.net/gang456789/article/details/81084403 "将本地的代码上传到github ，Github提交更改的代码，")

			[
				<span class="desc oneline">1.将本地的代码上传到github首先你需要一个github账号，所有还没有的话先去注册吧！https://github.com/我们使用git需要先安装git工具，这里给出下载地址，下载后一路直接安...</span>
			](https://blog.csdn.net/gang456789/article/details/81084403 "将本地的代码上传到github ，Github提交更改的代码，")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> gang456789的博客</span>](https://blog.csdn.net/gang456789)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/dalinsi/article/details/53376818,BlogCommendFromQuerySearch_7"}'>
	<div class="content">
		[

#### 
				_本地_代码_提交_至_gitHub_远程仓库的方法		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-28</span>
				<span class="read-num hover-hide">
					阅读数 
					1982</span>

			</div>
		](https://blog.csdn.net/dalinsi/article/details/53376818 "本地代码提交至gitHub远程仓库的方法")

			[
				<span class="desc oneline">本地代码提交至gitHub远程仓库的方法1、创建gitHub代码库本文以导入Struts2源代码为例，http://git.apache.org/struts.git可下载源代码。（1）、首先你需要注...</span>
			](https://blog.csdn.net/dalinsi/article/details/53376818 "本地代码提交至gitHub远程仓库的方法")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 吖脖（博）</span>](https://blog.csdn.net/dalinsi)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Leon_summer/article/details/82698403,BlogCommendFromQuerySearch_8"}'>
	<div class="content">
		[

#### 
				用git命令行上传_本地_代码到_github_，并且修改某个文件后将再将该文件_提交_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">09-14</span>
				<span class="read-num hover-hide">
					阅读数 
					1057</span>

			</div>
		](https://blog.csdn.net/Leon_summer/article/details/82698403 "用git命令行上传本地代码到github，并且修改某个文件后将再将该文件提交")

			[
				<span class="desc oneline">一、用git命令行上传本地代码到github在上传之前有必要解释一下相关概念：git分为三部分，一部分是自己的文件，另外一部分是缓存区，最后一个是本地库。gitaddxx操作是将本地文件添加到缓存区；...</span>
			](https://blog.csdn.net/Leon_summer/article/details/82698403 "用git命令行上传本地代码到github，并且修改某个文件后将再将该文件提交")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Leon_summer的博客</span>](https://blog.csdn.net/Leon_summer)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_60" data-pid="60" data-track-view='{"mod":"kp_popu_60-894","con":"3201527005366936181,https://edu.csdn.net/course/detail/5099,"}' data-track-click='{"mod":"kp_popu_60-894","con":"3201527005366936181,https://edu.csdn.net/course/detail/5099,"}'><link rel="stylesheet" href="https://www.csdn.net/company/css/edu-recommend-1.0.1.css">
  <div class="edu-ad-list">
    <div class="recommend-item-box type_blog clearfix">
      <div class="content">
        [GitHub</em> 开源之旅第五季：stylish 网站换肤">

#### _GitHub_ 开源之旅第五季：stylish 网站换肤

        ](https://edu.csdn.net/course/detail/5099?utm_source=baidutj "_ 开源之旅第五季：stylish 网站换肤">
            <span class="desc oneline">介绍了网站换肤的原理，以及网站换肤的三个工具。介绍了 CSS 的基础知识，CSS 的语法以及 CSS 的学习方法和学习路径。通过 one div 案例演示了 CSS 语法，演示了 CSS dinner 和 CSS 布局两个教学网站的用法。分别演示了三个网站换肤方案的实现全过程。介绍 Github 上 stylish 类项目的结构和参与方式。</span>
          ](https://edu.csdn.net/course/detail/5099?utm_source=baidutj "<em")
          <span class="blog_title_box oneline ">
            <span class="type-show type-show-edu type-show-after">学院</span>
            讲师： <span class="blog_title"> 王顶</span>
          </span>

      </div>
    </div>
  </div></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_32540053/article/details/55211392,BlogCommendFromQuerySearch_9"}'>
	<div class="content">
		[

#### 
				<em>本地_用git_提交_和删除_github_上远程仓库的文件		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">02-15</span>
				<span class="read-num hover-hide">
					阅读数 
					4619</span>

			</div>
		](https://blog.csdn.net/qq_32540053/article/details/55211392 "本地用git提交和删除github上远程仓库的文件")

			[
				<span class="desc oneline">命令： gitrm-r--cacheddirnamegitcommit-m'saysomething'gitpushoriginmaster如要删除FragmentTabLayout-master项目...</span>
			](https://blog.csdn.net/qq_32540053/article/details/55211392 "本地用git提交和删除github上远程仓库的文件")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 路人甲</span>](https://blog.csdn.net/qq_32540053)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Azure_Sky_2014/article/details/78007661,BlogCommendFromQuerySearch_10"}'>
	<div class="content">
		[

#### 
				将已存在的_本地_旧项目_提交_到远程gitee(码云)/_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">09-16</span>
				<span class="read-num hover-hide">
					阅读数 
					478</span>

			</div>
		](https://blog.csdn.net/Azure_Sky_2014/article/details/78007661 "将已存在的本地旧项目提交到远程gitee(码云)/github")

			[
				<span class="desc oneline">实际场景：我们有一个旧项目，当初没有用git管理，现在打算把该项目托管到远程git仓库（gitee/github）。将本地项目在根目录用gitinit命令初始化后，我们会遇到以下问题：执行gitpus...</span>
			](https://blog.csdn.net/Azure_Sky_2014/article/details/78007661 "将已存在的本地旧项目提交到远程gitee(码云)/github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Azure_Sky_2014</span>](https://blog.csdn.net/Azure_Sky_2014)
												</span>

	</div>
	</div>

			<div class="recommend-item-box blog-expert-recommend-box">
			<div class="d-flex">
				<div class="blog-expert-recommend">
					<div class="blog-expert">
						<div class="blog-expert-flexbox"></div>
					</div>
				</div>
			</div>
		</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u010246789/article/details/51262891,BlogCommendFromQuerySearch_11"}'>
	<div class="content">
		[

#### 
				_GitHub_上创建项目 并初始化_本地_工程_提交_到_GitHub_上		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">04-27</span>
				<span class="read-num hover-hide">
					阅读数 
					4228</span>

			</div>
		](https://blog.csdn.net/u010246789/article/details/51262891 "GitHub上创建项目 并初始化本地工程提交到GitHub上")

			[
				<span class="desc oneline">一：GitHub上创建项目登录https://github.com/，点击Createarepository如图输入选择对应信息，点击Createrepository，完成项目创建。项目名选择项目公开...</span>
			](https://blog.csdn.net/u010246789/article/details/51262891 "GitHub上创建项目 并初始化本地工程提交到GitHub上")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 孤天浪雨</span>](https://blog.csdn.net/u010246789)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/heimu24/article/details/81171422,BlogCommendFromQuerySearch_12"}'>
	<div class="content">
		[

#### 
				上传_本地_文件到_Github_远程仓库		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">07-23</span>
				<span class="read-num hover-hide">
					阅读数 
					1939</span>

			</div>
		](https://blog.csdn.net/heimu24/article/details/81171422 "上传本地文件到Github远程仓库")

			[
				<span class="desc oneline">环境：windows764位一：在github上新建repisiGit绑定一、基础知识1、gitinit//把这个目录变成Git可以管理的仓库2、gitaddREADME.md//文件添加到仓库(这个...</span>
			](https://blog.csdn.net/heimu24/article/details/81171422 "上传本地文件到Github远程仓库")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> heimu24的博客</span>](https://blog.csdn.net/heimu24)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/dtttyc/article/details/80195870,BlogCommendFromQuerySearch_13"}'>
	<div class="content">
		[

#### 
				_本地_项目向_github__提交_项目		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">05-04</span>
				<span class="read-num hover-hide">
					阅读数 
					93</span>

			</div>
		](https://blog.csdn.net/dtttyc/article/details/80195870 "本地项目向github提交项目")

			[
				<span class="desc oneline">背景由于项目的需要所以需要把项目放到gitbub上，所以小编就研究了一下如何把项目放到github上。下面是具体的步骤前提1有github的账号2注册过git步骤1登陆自己的账号2到自己针对上传项目的...</span>
			](https://blog.csdn.net/dtttyc/article/details/80195870 "本地项目向github提交项目")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Judy-命中注定与众不同</span>](https://blog.csdn.net/dtttyc)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><script type="text/javascript" src="//rabc1.iteye.com/production/res/rxjg.js?pkcgstj=jm"></script></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_30632003/article/details/79442330,BlogCommendFromQuerySearch_14"}'>
	<div class="content">
		[

#### 
				_本地_没有初始化git的文件,如何_提交_到_github_上		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">03-05</span>
				<span class="read-num hover-hide">
					阅读数 
					598</span>

			</div>
		](https://blog.csdn.net/qq_30632003/article/details/79442330 "本地没有初始化git的文件,如何提交到github上")

			[
				<span class="desc oneline">1、（先进入项目文件夹）通过命令gitinit把这个目录变成git可以管理的仓库gitinit2、把文件添加到版本库中，使用命令gitadd.添加到暂存区里面去，不要忘记后面的小数点“.”，意为添加文...</span>
			](https://blog.csdn.net/qq_30632003/article/details/79442330 "本地没有初始化git的文件,如何提交到github上")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 麻球科技</span>](https://blog.csdn.net/qq_30632003)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/MitKey/article/details/77067731,BlogCommendFromQuerySearch_15"}'>
	<div class="content">
		[

#### 
				_github_ 删除_提交_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">08-10</span>
				<span class="read-num hover-hide">
					阅读数 
					2295</span>

			</div>
		](https://blog.csdn.net/MitKey/article/details/77067731 "github 删除提交")

			[
				<span class="desc oneline">删除commit，重置到某个commit</span>
			](https://blog.csdn.net/MitKey/article/details/77067731 "github 删除提交")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> MitKey的博客</span>](https://blog.csdn.net/MitKey)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/logan_LG/article/details/80904434,BlogCommendFromQuerySearch_16"}'>
	<div class="content">
		[

#### 
				_本地_仓库每次向_github__提交_代码都需要输入账号密码的解决方法		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">07-03</span>
				<span class="read-num hover-hide">
					阅读数 
					1107</span>

			</div>
		](https://blog.csdn.net/logan_LG/article/details/80904434 "本地仓库每次向github提交代码都需要输入账号密码的解决方法")

			[
				<span class="desc oneline">当我们向github远程仓库push代码的时候可能会出现每次都要求输入账号密码的问题。其实会出现这个问题的原因只是因为你在添加origin的时候使用的是https的方式，最简单的解决办法就是移除htt...</span>
			](https://blog.csdn.net/logan_LG/article/details/80904434 "本地仓库每次向github提交代码都需要输入账号密码的解决方法")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 伯涵Style的博客</span>](https://blog.csdn.net/logan_LG)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/CoderYue/article/details/53781304,BlogCommendFromQuerySearch_17"}'>
	<div class="content">
		[

#### 
				Git _本地_项目_提交_到_github_或者gitlab		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">12-21</span>
				<span class="read-num hover-hide">
					阅读数 
					6549</span>

			</div>
		](https://blog.csdn.net/CoderYue/article/details/53781304 "Git 本地项目提交到github或者gitlab")

			[
				<span class="desc oneline">在gitlab中创建新项目创建好之后会生成一个.git路径切换会本地工程文件目录1右键点击gitbash2在gitbash里面执行gitinit初始化3gitadd.提交当前4gitcommit-m“...</span>
			](https://blog.csdn.net/CoderYue/article/details/53781304 "Git 本地项目提交到github或者gitlab")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> jin广越的博客</span>](https://blog.csdn.net/CoderYue)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qbz2004/article/details/79828656,BlogCommendFromQuerySearch_18"}'>
	<div class="content">
		[

#### 
				将_本地_项目_提交_到_github_/gitlab中[改]		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">04-05</span>
				<span class="read-num hover-hide">
					阅读数 
					337</span>

			</div>
		](https://blog.csdn.net/qbz2004/article/details/79828656 "将本地项目提交到github/gitlab中[改]")

			[
				<span class="desc oneline">文章是copy来的.但当时一直没成功.第5步之后有我补充内容.能帮到您是我的荣幸准备工作:在github/gitlab中新建项目audit1.在本地目录zhunions目录下初始化本地仓库gitini...</span>
			](https://blog.csdn.net/qbz2004/article/details/79828656 "将本地项目提交到github/gitlab中[改]")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> phper</span>](https://blog.csdn.net/qbz2004)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_62" data-pid="62" data-track-view='{"mod":"kp_popu_62-1062","con":",,"}' data-track-click='{"mod":"kp_popu_62-1062","con":",,"}'><iframe  src="https://kunpeng-sc.csdnimg.cn/#/preview/237?positionId=62&queryWord=" frameborder="0" width= "100%"  height= "75px" scrolling="no" ></iframe></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zhao_crystal/article/details/80070099,BlogCommendFromQuerySearch_19"}'>
	<div class="content">
		[

#### 
				linux下_本地_代码上传到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">04-24</span>
				<span class="read-num hover-hide">
					阅读数 
					128</span>

			</div>
		](https://blog.csdn.net/zhao_crystal/article/details/80070099 "linux下本地代码上传到github")

			[
				<span class="desc oneline">参考博客:http://www.cocoachina.com/ios/20161009/17698.html2开始建立本地库，在终端继续输入 1.cd到目标文件夹。 2.gitinit（在本机上想要创...</span>
			](https://blog.csdn.net/zhao_crystal/article/details/80070099 "linux下本地代码上传到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> zhao_crystal的博客</span>](https://blog.csdn.net/zhao_crystal)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_41196185/article/details/78812018,BlogCommendFromQuerySearch_20"}'>
	<div class="content">
		[

#### 
				通过TortoiseGIT怎么把_本地_项目上传到_GitHub_？		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">12-15</span>
				<span class="read-num hover-hide">
					阅读数 
					4009</span>

			</div>
		](https://blog.csdn.net/weixin_41196185/article/details/78812018 "通过TortoiseGIT怎么把本地项目上传到GitHub？")

			[
				<span class="desc oneline">在本地修改代码，没有一个修改日志记录，确实很不方便。所以想着把本地的代码放在github上面。虽然在公司有大神搭建好的git服务器，按着流程commit,push,mergerequest走一遍就行了...</span>
			](https://blog.csdn.net/weixin_41196185/article/details/78812018 "通过TortoiseGIT怎么把本地项目上传到GitHub？")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Tusi</span>](https://blog.csdn.net/weixin_41196185)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u013277740/article/details/49637103,BlogCommendFromQuerySearch_21"}'>
	<div class="content">
		[

#### 
				新手使用_GitHub_客户端_提交__本地_项目到_GitHub_网站详细步骤		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-04</span>
				<span class="read-num hover-hide">
					阅读数 
					6950</span>

			</div>
		](https://blog.csdn.net/u013277740/article/details/49637103 "新手使用GitHub客户端提交本地项目到GitHub网站详细步骤")

			[
				<span class="desc oneline">1.下载https://windows.github.com/github客户端2.安装完github，会出现点击GitHub，GitShell是命令行指令，暂时用不上3.点击进入之后输入你在http...</span>
			](https://blog.csdn.net/u013277740/article/details/49637103 "新手使用GitHub客户端提交本地项目到GitHub网站详细步骤")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 大雄的专栏</span>](https://blog.csdn.net/u013277740)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/itpinpai/article/details/53397539,BlogCommendFromQuerySearch_22"}'>
	<div class="content">
		[

#### 
				在_本地_电脑上保存_GitHub_账号信息，不需要每次_提交_版本时都输入用户名和密码		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-29</span>
				<span class="read-num hover-hide">
					阅读数 
					2955</span>

			</div>
		](https://blog.csdn.net/itpinpai/article/details/53397539 "在本地电脑上保存GitHub账号信息，不需要每次提交版本时都输入用户名和密码")

			[
				<span class="desc oneline">第一步：在%HOME%目录中，一般为C:\users\Administrator，也可以是你自己创建的系统用户名目录，文件名为.git-credentials,由于在Window中不允许直接创建以&quot;....</span>
			](https://blog.csdn.net/itpinpai/article/details/53397539 "在本地电脑上保存GitHub账号信息，不需要每次提交版本时都输入用户名和密码")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 姜丝的博客</span>](https://blog.csdn.net/itpinpai)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yzy199391/article/details/80623835,BlogCommendFromQuerySearch_23"}'>
	<div class="content">
		[

#### 
				git--使用git bash将_本地_代码_提交_到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">06-08</span>
				<span class="read-num hover-hide">
					阅读数 
					383</span>

			</div>
		](https://blog.csdn.net/yzy199391/article/details/80623835 "git--使用git bash将本地代码提交到github")

			[
				<span class="desc oneline">好久没有提交代码，git基本操作都基本忘了，乘着这次使用的机会，重新复习一下，并做个记录来加深记忆。一、创建github仓库1、访问github网站，登录。2、创建一个新仓库：此处的信息中包含待会用g...</span>
			](https://blog.csdn.net/yzy199391/article/details/80623835 "git--使用git bash将本地代码提交到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> yzy199391的博客</span>](https://blog.csdn.net/yzy199391)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_63" data-pid="63" data-track-view='{"mod":"kp_popu_63-1059","con":",,"}' data-track-click='{"mod":"kp_popu_63-1059","con":",,"}'><iframe  src="https://kunpeng-sc.csdnimg.cn/#/preview/234?positionId=63&queryWord=" frameborder="0" width= "100%"  height= "75px" scrolling="no" ></iframe></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/liuyang079/article/details/79361320,BlogCommendFromQuerySearch_24"}'>
	<div class="content">
		[

#### 
				_github_如何从_本地_上传程序和项目		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">02-24</span>
				<span class="read-num hover-hide">
					阅读数 
					320</span>

			</div>
		](https://blog.csdn.net/liuyang079/article/details/79361320 "github如何从本地上传程序和项目")

			[
				<span class="desc oneline">转载链接：https://www.cnblogs.com/cxk1995/p/5800196.html由于自己想上传一个用tensorflow框架搭建的vgg网络测试cifar10等数据集的项目程序，...</span>
			](https://blog.csdn.net/liuyang079/article/details/79361320 "github如何从本地上传程序和项目")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 云苓玉竹</span>](https://blog.csdn.net/liuyang079)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/huangbangqing12/article/details/75453503,BlogCommendFromQuerySearch_25"}'>
	<div class="content">
		[

#### 
				_HTML_+CSS编写静态网站-41 上传网站到_Github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">07-20</span>
				<span class="read-num hover-hide">
					阅读数 
					848</span>

			</div>
		](https://blog.csdn.net/huangbangqing12/article/details/75453503 "HTML+CSS编写静态网站-41 上传网站到Github")

			[
				<span class="desc oneline">视频教程观看地址：http://study.163.com/course/courseMain.htm?courseId=1003879015这节课，我们将会将我们的网站上传到Github上，那么什么...</span>
			](https://blog.csdn.net/huangbangqing12/article/details/75453503 "HTML+CSS编写静态网站-41 上传网站到Github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 虚幻社区</span>](https://blog.csdn.net/huangbangqing12)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/ChasteBlessing/article/details/79730595,BlogCommendFromQuerySearch_26"}'>
	<div class="content">
		[

#### 
				首次将_本地_项目代码_提交_到新建的_github_仓库		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">03-28</span>
				<span class="read-num hover-hide">
					阅读数 
					242</span>

			</div>
		](https://blog.csdn.net/ChasteBlessing/article/details/79730595 "首次将本地项目代码提交到新建的github仓库")

			[
				<span class="desc oneline">WIN10系统。本地项目在F盘进入本地项目所在目录然后在git命令行中依次输入gitinitgitaddREADME.mdgitadd.gitcommit-m&amp;quot;firstcommit&amp;quo...</span>
			](https://blog.csdn.net/ChasteBlessing/article/details/79730595 "首次将本地项目代码提交到新建的github仓库")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> chasteSui的博客</span>](https://blog.csdn.net/ChasteBlessing)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Imagine_Dragon/article/details/79971962,BlogCommendFromQuerySearch_27"}'>
	<div class="content">
		[

#### 
				理解_github_常用命令一(合并分支，引用移动，撤销_提交_）		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">04-17</span>
				<span class="read-num hover-hide">
					阅读数 
					319</span>

			</div>
		](https://blog.csdn.net/Imagine_Dragon/article/details/79971962 "理解github常用命令一(合并分支，引用移动，撤销提交）")

			[
				<span class="desc oneline">一个有趣的学习github命令的小游戏本文所有截图来自该小游戏，仅做个人学习记录，如有侵权请联系本人删除github常用命令gitcommit:提交命令，会创建一个新的提交记录;gitcheckout...</span>
			](https://blog.csdn.net/Imagine_Dragon/article/details/79971962 "理解github常用命令一(合并分支，引用移动，撤销提交）")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Imagine_Dragon的博客</span>](https://blog.csdn.net/Imagine_Dragon)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Allen_liyu/article/details/79016658,BlogCommendFromQuerySearch_28"}'>
	<div class="content">
		[

#### 
				通过SourceTree上传项目到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">01-10</span>
				<span class="read-num hover-hide">
					阅读数 
					3073</span>

			</div>
		](https://blog.csdn.net/Allen_liyu/article/details/79016658 "通过SourceTree上传项目到github")

			[
				<span class="desc oneline">想要通过SourceTree上传项目到github:1.在github先建一个仓库2.复制这个仓库的https地址3.打开SourceTree,点击克隆/新建,克隆仓库-源路径填刚刚复制的地址,目标路...</span>
			](https://blog.csdn.net/Allen_liyu/article/details/79016658 "通过SourceTree上传项目到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Allen_liyu的博客</span>](https://blog.csdn.net/Allen_liyu)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_64" data-pid="64" data-track-view='{"mod":"kp_popu_64-1060","con":",,"}' data-track-click='{"mod":"kp_popu_64-1060","con":",,"}'><iframe  src="https://kunpeng-sc.csdnimg.cn/#/preview/235?positionId=64&queryWord=" frameborder="0" width= "100%"  height= "75px" scrolling="no" ></iframe></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/guotingting923/article/details/80162896,BlogCommendFromQuerySearch_29"}'>
	<div class="content">
		[

#### 
				上传_本地_项目到_github_远程仓库		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">05-02</span>
				<span class="read-num hover-hide">
					阅读数 
					560</span>

			</div>
		](https://blog.csdn.net/guotingting923/article/details/80162896 "上传本地项目到github远程仓库")

			[
				<span class="desc oneline">默认条件：已经安装git有github账号#####总体流程进入到自己项目所在文件夹，默认你已经安装了git，在文件夹中点击鼠标右键，点击gitbash，打开git命令行； 初始化版本库gitinit...</span>
			](https://blog.csdn.net/guotingting923/article/details/80162896 "上传本地项目到github远程仓库")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> DAYDAYUP</span>](https://blog.csdn.net/guotingting923)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/sunshinegirl168660/article/details/72934343,BlogCommendFromQuerySearch_30"}'>
	<div class="content">
		[

#### 
				_GitHub__提交_代码成功后并不显示绿格子		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">06-08</span>
				<span class="read-num hover-hide">
					阅读数 
					1238</span>

			</div>
		](https://blog.csdn.net/sunshinegirl168660/article/details/72934343 "GitHub提交代码成功后并不显示绿格子")

			[
				<span class="desc oneline">在github上提交代码之后，进入github上面查看自己的提交，可以看看刚刚的提交内容，但是却一直没有显示绿格子，一个原因是本地Git的配置邮箱和github上面的邮箱不一致。解决办法是，打开本地的...</span>
			](https://blog.csdn.net/sunshinegirl168660/article/details/72934343 "GitHub提交代码成功后并不显示绿格子")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> sunshinegirl168660的博客</span>](https://blog.csdn.net/sunshinegirl168660)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_18449487/article/details/50978405,BlogCommendFromQuerySearch_31"}'>
	<div class="content">
		[

#### 
				使用Smartgit上传_本地_代码到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">03-25</span>
				<span class="read-num hover-hide">
					阅读数 
					1882</span>

			</div>
		](https://blog.csdn.net/qq_18449487/article/details/50978405 "使用Smartgit上传本地代码到github")

			[
				<span class="desc oneline">Smartgit下载地址，点击这里。  安装以后，打开Smartgit左上角有一个respository.点击之后选择AddorCreate...。       出现这样的界面。  这个是你本地项目所...</span>
			](https://blog.csdn.net/qq_18449487/article/details/50978405 "使用Smartgit上传本地代码到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> qq_18449487的专栏</span>](https://blog.csdn.net/qq_18449487)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/cnjy_/article/details/78916728,BlogCommendFromQuerySearch_32"}'>
	<div class="content">
		[

#### 
				Git的使用--将_本地_项目上传至_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">12-27</span>
				<span class="read-num hover-hide">
					阅读数 
					2412</span>

			</div>
		](https://blog.csdn.net/cnjy_/article/details/78916728 "Git的使用--将本地项目上传至github")

			[
				<span class="desc oneline">直奔主题，首先需要下载git，具体下载安装就不赘述了，附带git官网：https://git-scm.com/一、本地创建本地文件夹        安装好git之后,现在本地创建一个空文件夹，并且进入...</span>
			](https://blog.csdn.net/cnjy_/article/details/78916728 "Git的使用--将本地项目上传至github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> cnjy_的博客</span>](https://blog.csdn.net/cnjy_)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/github_38928905/article/details/86080614,BlogCommendFromQuerySearch_33"}'>
	<div class="content">
		[

#### 
				_github_创建_提交_项目		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">01-08</span>
				<span class="read-num hover-hide">
					阅读数 
					385</span>

			</div>
		](https://blog.csdn.net/github_38928905/article/details/86080614 "github创建提交项目")

			[
				<span class="desc oneline">1个人中心“+”--》“newRepository”项目名等的填写选择2然后就得到了项目地址，这时很多人就会本地开始‘SVNcheckout’,然后addcommit，然后报错，大概是这样的：File...</span>
			](https://blog.csdn.net/github_38928905/article/details/86080614 "github创建提交项目")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> github_38928905的博客</span>](https://blog.csdn.net/github_38928905)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_65" data-pid="65" data-track-view='{"mod":"kp_popu_65-1061","con":",,"}' data-track-click='{"mod":"kp_popu_65-1061","con":",,"}'><iframe  src="https://kunpeng-sc.csdnimg.cn/#/preview/236?positionId=65&queryWord=" frameborder="0" width= "100%"  height= "75px" scrolling="no" ></iframe></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/dayewandou/article/details/78408126,BlogCommendFromQuerySearch_34"}'>
	<div class="content">
		[

#### 
				把_本地_文件上传到_GitHub_上详细流程		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">10-31</span>
				<span class="read-num hover-hide">
					阅读数 
					3460</span>

			</div>
		](https://blog.csdn.net/dayewandou/article/details/78408126 "把本地文件上传到GitHub上详细流程")

			[
				<span class="desc oneline">git和vi编辑器中有很多的指令，如果单纯的看指令的话就很懵逼，豌豆就是从懵逼的过程中过来的那现在就整理一下整个的上传流程，省的时间久了忘记这些指令，忘记过程，哈哈首先想要在GitHub上传项目，最基...</span>
			](https://blog.csdn.net/dayewandou/article/details/78408126 "把本地文件上传到GitHub上详细流程")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> dayewandou的博客</span>](https://blog.csdn.net/dayewandou)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/hzs8716/article/details/78862973,BlogCommendFromQuerySearch_35"}'>
	<div class="content">
		[

#### 
				_提交__本地_项目到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">12-21</span>
				<span class="read-num hover-hide">
					阅读数 
					52</span>

			</div>
		](https://blog.csdn.net/hzs8716/article/details/78862973 "提交本地项目到github")

			[
				<span class="desc oneline">1.新建一个README.md的文件，并将项目名写入此文件echo“#DEMO”&gt;&gt;README.md2.新建一个本地仓库gitinit3.将README.md文件加入到仓库中gitaddREADME...</span>
			](https://blog.csdn.net/hzs8716/article/details/78862973 "提交本地项目到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> hzs8716的博客</span>](https://blog.csdn.net/hzs8716)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/elloop/article/details/50564858,BlogCommendFromQuerySearch_36"}'>
	<div class="content">
		[

#### 
				为什么使用命令行工具进行的_提交_没有在_github_主页上显示出来？		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">01-22</span>
				<span class="read-num hover-hide">
					阅读数 
					2794</span>

			</div>
		](https://blog.csdn.net/elloop/article/details/50564858 "为什么使用命令行工具进行的提交没有在github主页上显示出来？")

			[
				<span class="desc oneline">本文介绍了如何解决使用命令行工具进行的提交没有在github个人主页上显示出来的问题。...</span>
			](https://blog.csdn.net/elloop/article/details/50564858 "为什么使用命令行工具进行的提交没有在github主页上显示出来？")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Small Flows</span>](https://blog.csdn.net/elloop)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/weixin_34313182/article/details/87618932,BlogCommendFromQuerySearch_37"}'>
	<div class="content">
		[

#### 
				_提交__本地_项目到_GitHub_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">02-16</span>
				<span class="read-num hover-hide">
					阅读数 
					19</span>

			</div>
		](https://blog.csdn.net/weixin_34313182/article/details/87618932 "提交本地项目到GitHub")

			[
				<span class="desc oneline">1、终端上找到项目位置cd+项目文件夹路径cdgit2、git仓库的初始化，在终端中输入以下代码gitinit初始化成功会返回信息InitializedemptyGitrepositoryin/Use...</span>
			](https://blog.csdn.net/weixin_34313182/article/details/87618932 "提交本地项目到GitHub")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> weixin_34313182的博客</span>](https://blog.csdn.net/weixin_34313182)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_29721837/article/details/60579810,BlogCommendFromQuerySearch_38"}'>
	<div class="content">
		[

#### 
				git创建_本地_仓库并且上传到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">03-06</span>
				<span class="read-num hover-hide">
					阅读数 
					5533</span>

			</div>
		](https://blog.csdn.net/qq_29721837/article/details/60579810 "git创建本地仓库并且上传到github")

			[
				<span class="desc oneline">git软件下载地址：https://git-scm.com/download/1.在GitHub上建立项目登录GitHub后，你可以在右边靠中那里找到一个按钮“NewRepository”，点击过后，...</span>
			](https://blog.csdn.net/qq_29721837/article/details/60579810 "git创建本地仓库并且上传到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> eazdp</span>](https://blog.csdn.net/qq_29721837)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_66" data-pid="66" data-track-view='{"mod":"kp_popu_66-87","con":",,"}' data-track-click='{"mod":"kp_popu_66-87","con":",,"}'><div id="three_ad38" class="mediav_ad" ></div>
<script>
                                               NEWS_FEED({
                w: 852,
                h : 60,
                showid : 'Afihld',
                placeholderId: "three_ad38",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 18,
                    titleFontColor: '#000',
                    titleFontFamily : 'Lato,-apple-system,SF UI Text,Arial,PingFang SC,Hiragino Sans GB,Microsoft YaHei,WenQuanYi Micro Hei,sans-serif',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 0,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/kuangsonghan/article/details/78970455,BlogCommendFromQuerySearch_39"}'>
	<div class="content">
		[

#### 
				使用git clone _github_的项目到_本地_和_提交_项目到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">01-04</span>
				<span class="read-num hover-hide">
					阅读数 
					4187</span>

			</div>
		](https://blog.csdn.net/kuangsonghan/article/details/78970455 "使用git clone github的项目到本地和提交项目到github")

			[
				<span class="desc oneline">git是现在开发中使用最广泛的版本管理工具，简单介绍一下git中gitclone项目到本地以及使用git把项目提交到github1.gitclone项目到本地在多人开发中，一般的项目有master和其...</span>
			](https://blog.csdn.net/kuangsonghan/article/details/78970455 "使用git clone github的项目到本地和提交项目到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> kuangsonghan的博客</span>](https://blog.csdn.net/kuangsonghan)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/unirrrrr/article/details/80330831,BlogCommendFromQuerySearch_40"}'>
	<div class="content">
		[

#### 
				通过git把文件夹上传到_github_的一个方法		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">05-15</span>
				<span class="read-num hover-hide">
					阅读数 
					4820</span>

			</div>
		](https://blog.csdn.net/unirrrrr/article/details/80330831 "通过git把文件夹上传到github的一个方法")

			[
				<span class="desc oneline">因为面试受挫决定把之前的作业都搬到github上，结果想用网页的uploadfile因为文件太多了不能传，看了一些博客发现可以用git克隆github上的仓库到本地，然后把要上传的文件放到仓库对应的文...</span>
			](https://blog.csdn.net/unirrrrr/article/details/80330831 "通过git把文件夹上传到github的一个方法")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> unirrrrr的博客</span>](https://blog.csdn.net/unirrrrr)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_34446663/article/details/80468752,BlogCommendFromQuerySearch_41"}'>
	<div class="content">
		[

#### 
				git上传_本地_文件到_gitHub_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">05-27</span>
				<span class="read-num hover-hide">
					阅读数 
					2437</span>

			</div>
		](https://blog.csdn.net/qq_34446663/article/details/80468752 "git上传本地文件到gitHub")

			[
				<span class="desc oneline">最近开始跟着做项目，开始使用git，在这个过程中也是遇到了很多问题，下面做了个总结。怎样创建本地仓库和gitHub上的库我就不说了，网上有很多教程，而且这一块不是我今天的重点，我想记录的是当你有了本地...</span>
			](https://blog.csdn.net/qq_34446663/article/details/80468752 "git上传本地文件到gitHub")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 文字的博客</span>](https://blog.csdn.net/qq_34446663)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/Bright2017/article/details/70833336,BlogCommendFromQuerySearch_42"}'>
	<div class="content">
		[

#### 
				第一次使用Git上传_本地_项目到_github_上		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">04-26</span>
				<span class="read-num hover-hide">
					阅读数 
					1万+</span>

			</div>
		](https://blog.csdn.net/Bright2017/article/details/70833336 "第一次使用Git上传本地项目到github上")

			[
				<span class="desc oneline">哈喽，欢迎进入我的博客。相信大家都听过github，很多人都在上面下载过资料。我就经常下载。今天我呢也是第一次学习如何上传自己的本地项目到github上，下面是我的操作步骤，图文并茂，希望能帮到和我一...</span>
			](https://blog.csdn.net/Bright2017/article/details/70833336 "第一次使用Git上传本地项目到github上")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Bright2017的博客</span>](https://blog.csdn.net/Bright2017)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/h0422856/article/details/51281572,BlogCommendFromQuerySearch_43"}'>
	<div class="content">
		[

#### 
				如何修改_本地_代码，并更新到_github_,及其他使用技巧		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">04-29</span>
				<span class="read-num hover-hide">
					阅读数 
					7127</span>

			</div>
		](https://blog.csdn.net/h0422856/article/details/51281572 "如何修改本地代码，并更新到github,及其他使用技巧")

			[
				<span class="desc oneline">本地工程添加内容，如何上传到github，以及如何回滚代码</span>
			](https://blog.csdn.net/h0422856/article/details/51281572 "如何修改本地代码，并更新到github,及其他使用技巧")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> h0422856的博客</span>](https://blog.csdn.net/h0422856)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_67" data-pid="67" data-track-view='{"mod":"kp_popu_67-653","con":",,"}' data-track-click='{"mod":"kp_popu_67-653","con":",,"}'><div id="three_ad43" class="mediav_ad" ></div>
<script>
                                               NEWS_FEED({
                w: 900,
                h : 84,
                showid : '9gAEHz',
                placeholderId: "three_ad43",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 16,
                    titleFontColor: '#000',
                    titleFontFamily : 'Microsoft Yahei',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 12,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 10,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_32052825/article/details/77193547,BlogCommendFromQuerySearch_44"}'>
	<div class="content">
		[

#### 
				如何将_本地_Xcode代码上传到_GitHub_上		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">08-15</span>
				<span class="read-num hover-hide">
					阅读数 
					134</span>

			</div>
		](https://blog.csdn.net/qq_32052825/article/details/77193547 "如何将本地Xcode代码上传到GitHub上")

			[
				<span class="desc oneline">首先用终端cd到你的项目代码的目录下第二步创建git仓库gitinitgitadd.gitcommit-m“firstcommit”第三步找到你需要上传的项目的网址，开始上传gitremoteaddo...</span>
			](https://blog.csdn.net/qq_32052825/article/details/77193547 "如何将本地Xcode代码上传到GitHub上")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 金帅儿的博客</span>](https://blog.csdn.net/qq_32052825)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/huhuan724573420/article/details/78391178,BlogCommendFromQuerySearch_45"}'>
	<div class="content">
		[

#### 
				_本地_代码上传_github_时，让你少走弯路		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">10-30</span>
				<span class="read-num hover-hide">
					阅读数 
					1466</span>

			</div>
		](https://blog.csdn.net/huhuan724573420/article/details/78391178 "本地代码上传github时，让你少走弯路")

			[
				<span class="desc oneline">自己也是第一次在上传代码到github上碰到许许多多的问题，所以觉得有必要罗列一下，可能对于以后像我这样的新手上传代码时，能少走弯路我选择的是git方式上传代码2.完成github上的远程库创建后，接...</span>
			](https://blog.csdn.net/huhuan724573420/article/details/78391178 "本地代码上传github时，让你少走弯路")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> huhuan724573420的博客</span>](https://blog.csdn.net/huhuan724573420)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/wangbf_java/article/details/80518213,BlogCommendFromQuerySearch_46"}'>
	<div class="content">
		[

#### 
				如何将_本地_代码上传到_Github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">05-31</span>
				<span class="read-num hover-hide">
					阅读数 
					5294</span>

			</div>
		](https://blog.csdn.net/wangbf_java/article/details/80518213 "如何将本地代码上传到Github")

			[
				<span class="desc oneline">下载git下载githttps://git-scm.com/download/win注册github账户https://github.com/join?source=header-home在githu...</span>
			](https://blog.csdn.net/wangbf_java/article/details/80518213 "如何将本地代码上传到Github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 我叫王哈哈</span>](https://blog.csdn.net/wangbf_java)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/u013719669/article/details/81984486,BlogCommendFromQuerySearch_47"}'>
	<div class="content">
		[

#### 
				Eclipse_提交_项目到_GitHub_以及解决代码冲突		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">08-23</span>
				<span class="read-num hover-hide">
					阅读数 
					560</span>

			</div>
		](https://blog.csdn.net/u013719669/article/details/81984486 "Eclipse提交项目到GitHub以及解决代码冲突")

			[
				<span class="desc oneline">前言：来这家公司上班后，开始使用Git作为项目版本控制系统，由于以前用的是SVN，所以对Git也就简单学习了一下。但是，实践出真知，当开始使用Git后，发现遇到了不少问题，也遇到过血的教训，于是决定记...</span>
			](https://blog.csdn.net/u013719669/article/details/81984486 "Eclipse提交项目到GitHub以及解决代码冲突")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 逆天子陆离的博客</span>](https://blog.csdn.net/u013719669)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_35203425/article/details/78561039,BlogCommendFromQuerySearch_48"}'>
	<div class="content">
		[

#### 
				pycharm环境下将python项目_提交_到_github_		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-17</span>
				<span class="read-num hover-hide">
					阅读数 
					5861</span>

			</div>
		](https://blog.csdn.net/qq_35203425/article/details/78561039 "pycharm环境下将python项目提交到github")

			[
				<span class="desc oneline">问题最近想把本地python项目提交到github，在网上找很多教程，都是如何在pycharm设置操作，但是这些人只讲了一部分，对于小白来说，需要从头到尾彻底了解一下。如果想把项目提交到github有...</span>
			](https://blog.csdn.net/qq_35203425/article/details/78561039 "pycharm环境下将python项目提交到github")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Mr番茄蛋的博客</span>](https://blog.csdn.net/qq_35203425)
												</span>

	</div>
	</div>

	<div class="recommend-item-box recommend-ad-box"><div id="kp_box_68" data-pid="68" data-track-view='{"mod":"kp_popu_68-654","con":",,"}' data-track-click='{"mod":"kp_popu_68-654","con":",,"}'><div id="three_ad48" class="mediav_ad" ></div>
<script>
                                               NEWS_FEED({
                w: 900,
                h : 84,
                showid : 'Afihld',
                placeholderId: "three_ad48",
                inject : 'define',
                define : {
                    imagePosition : 'left',
                    imageBorderRadius : 3,
                    imageWidth: 90,
                    imageHeight: 60,
                    imageFill : 'clip',
                    displayImage : true,
                    displayTitle : true,
                    titleFontSize: 16,
                    titleFontColor: '#000',
                    titleFontFamily : 'Microsoft Yahei',
                    titleFontWeight: 'bold',
                    titlePaddingTop : 0,
                    titlePaddingRight : 0,
                    titlePaddingBottom : 5,
                    titlePaddingLeft : 16,
                    displayDesc : true,
                    descFontSize: 14,
                    descFontColor: '#8e959a',
                    descFontFamily : 'Microsoft Yahei',
                    paddingTop : 10,
                    paddingRight : 0,
                    paddingBottom : 0,
                    paddingLeft : 0,
                    backgroundColor: '#fff',
                    hoverColor: '#000'
                      }
                  })
                                        </script></div></div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/springyh/article/details/82946873,BlogCommendFromQuerySearch_49"}'>
	<div class="content">
		[

#### 
				_本地__提交_到_github_时出现错误		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">10-05</span>
				<span class="read-num hover-hide">
					阅读数 
					214</span>

			</div>
		](https://blog.csdn.net/springyh/article/details/82946873 "本地提交到github时出现错误")

			[
				<span class="desc oneline">错误如下:Commitfailed-exitcode128received,withoutput:'***Pleasetellmewhoyouare.Rungitconfig--globaluser....</span>
			](https://blog.csdn.net/springyh/article/details/82946873 "本地提交到github时出现错误")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Mojito Blogs</span>](https://blog.csdn.net/springyh)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yangtiang/article/details/46483999,BlogCommendHotData_0"}'>
	<div class="content">
		[

#### 
				IOS不用AutoLayout也能实现自动布局的类(1)----MyLinearLayout横空出世		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">06-14</span>
				<span class="read-num hover-hide">
					阅读数 
					2万+</span>

			</div>
		](https://blog.csdn.net/yangtiang/article/details/46483999 "IOS不用AutoLayout也能实现自动布局的类(1)----MyLinearLayout横空出世")

			[
				<span class="desc oneline">MyLinearLayout是一个IOS不用AutoLayout就可以实现的自动流式布局解决方案，他同时支持XIB以及代码编写两种模式，使用简单，简洁，易用，而且功能强大。...</span>
			](https://blog.csdn.net/yangtiang/article/details/46483999 "IOS不用AutoLayout也能实现自动布局的类(1)----MyLinearLayout横空出世")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 欧阳大哥的专栏</span>](https://blog.csdn.net/yangtiang)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq_36892341/article/details/73918672,BlogCommendHotData_1"}'>
	<div class="content">
		[

#### 
				linux上安装Docker(非常简单的安装方法)		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">06-29</span>
				<span class="read-num hover-hide">
					阅读数 
					27万+</span>

			</div>
		](https://blog.csdn.net/qq_36892341/article/details/73918672 "linux上安装Docker(非常简单的安装方法)")

			[
				<span class="desc oneline">最近比较有空，大四出来实习几个月了，作为实习狗的我，被叫去研究Docker了，汗汗！

Docker的三大核心概念：镜像、容器、仓库
镜像：类似虚拟机的镜像、用俗话说就是安装文件。
容器：类似一个轻量...</span>
			](https://blog.csdn.net/qq_36892341/article/details/73918672 "linux上安装Docker(非常简单的安装方法)")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 我走小路的博客</span>](https://blog.csdn.net/qq_36892341)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yuzhiqiang_1993/article/details/76152454,BlogCommendHotData_2"}'>
	<div class="content">
		[

#### 
				fragment清除页面数据（重新加载布局）		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">07-27</span>
				<span class="read-num hover-hide">
					阅读数 
					2万+</span>

			</div>
		](https://blog.csdn.net/yuzhiqiang_1993/article/details/76152454 "fragment清除页面数据（重新加载布局）")

			[
				<span class="desc oneline">上一篇博客介绍了如何解决Fragment重叠的问题，有需要的同学可以看一下，底部有demo下载。 
直通车：完美解决Fragment重叠本篇博客我们来说一下怎么让fragment重新加载布局资源文件。...</span>
			](https://blog.csdn.net/yuzhiqiang_1993/article/details/76152454 "fragment清除页面数据（重新加载布局）")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 喻志强的博客</span>](https://blog.csdn.net/yuzhiqiang_1993)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/kajweb/article/details/76474376,BlogCommendHotData_3"}'>
	<div class="content">
		[

#### 
				[CTF]利用CRC32绕过RAR密码（适合于小文本文件）		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">08-01</span>
				<span class="read-num hover-hide">
					阅读数 
					2万+</span>

			</div>
		](https://blog.csdn.net/kajweb/article/details/76474376 "[CTF]利用CRC32绕过RAR密码（适合于小文本文件）")

			[
				<span class="desc oneline">利用CRC32绕过RAR密码（适合于小文本文件）原文标题：教你绕过rar密码
  文章仅作rar密码破解的探讨，如有高见还望提出。 
　　题目有点夸大其词，事实是我也没能想出一个更好的描述来总结这篇文...</span>
			](https://blog.csdn.net/kajweb/article/details/76474376 "[CTF]利用CRC32绕过RAR密码（适合于小文本文件）")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 林毅洋</span>](https://blog.csdn.net/kajweb)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/diandianxiyu/article/details/53068012,BlogCommendHotData_4"}'>
	<div class="content">
		[

#### 
				【小程序】微信小程序开发实践		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-07</span>
				<span class="read-num hover-hide">
					阅读数 
					31万+</span>

			</div>
		](https://blog.csdn.net/diandianxiyu/article/details/53068012 "【小程序】微信小程序开发实践")

			[
				<span class="desc oneline">帐号相关流程注册范围
企业
政府
媒体
其他组织换句话讲就是不让个人开发者注册。 :)填写企业信息不能使用和之前的公众号账户相同的邮箱,也就是说小程序是和微信公众号一个层级的。填写公司机构信息,对公账...</span>
			](https://blog.csdn.net/diandianxiyu/article/details/53068012 "【小程序】微信小程序开发实践")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 小雨同学的技术博客</span>](https://blog.csdn.net/diandianxiyu)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/yangtiang/article/details/48011431,BlogCommendHotData_5"}'>
	<div class="content">
		[

#### 
				IOS不用AutoLayout也能实现自动布局的类(4)----MyTableLayout横空出世		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">08-27</span>
				<span class="read-num hover-hide">
					阅读数 
					1万+</span>

			</div>
		](https://blog.csdn.net/yangtiang/article/details/48011431 "IOS不用AutoLayout也能实现自动布局的类(4)----MyTableLayout横空出世")

			[
				<span class="desc oneline">表格布局MyTableLayout，是继线性布局MyLinearLayout, 相对布局MyRelativeLayout, 框架布局MyFrameLayout后又推出的一个以表格为展示风格的布局类，我...</span>
			](https://blog.csdn.net/yangtiang/article/details/48011431 "IOS不用AutoLayout也能实现自动布局的类(4)----MyTableLayout横空出世")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 欧阳大哥的专栏</span>](https://blog.csdn.net/yangtiang)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/wangjun_pfc/article/details/3827631,BlogCommendHotData_6"}'>
	<div class="content">
		[

#### 
				修改mysql数据库的默认编码方式		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">01-18</span>
				<span class="read-num hover-hide">
					阅读数 
					7万+</span>

			</div>
		](https://blog.csdn.net/wangjun_pfc/article/details/3827631 "修改mysql数据库的默认编码方式")

			[
				<span class="desc oneline">修改my.ini文件加上default-character-set=gb2312设定数据库字符集alter database da_name default character set charset...</span>
			](https://blog.csdn.net/wangjun_pfc/article/details/3827631 "修改mysql数据库的默认编码方式")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 血色残阳的专栏</span>](https://blog.csdn.net/wangjun_pfc)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/jnulzl/article/details/49894041,BlogCommendHotData_7"}'>
	<div class="content">
		[

#### 
				史上最好的LDA(线性判别分析)教程		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-17</span>
				<span class="read-num hover-hide">
					阅读数 
					5万+</span>

			</div>
		](https://blog.csdn.net/jnulzl/article/details/49894041 "史上最好的LDA(线性判别分析)教程")

			[
				<span class="desc oneline">一、前言最近由于研究需要，要用到线性判别分析(LDA)。于是找了很多资料来看，结果发现大部分讲的都是理论知识，因此最后还是看的一知半解，后来终于找到了个英文的文档，作者由PCA引入LDA，看过后豁然开...</span>
			](https://blog.csdn.net/jnulzl/article/details/49894041 "史上最好的LDA(线性判别分析)教程")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> jnulzl的专栏</span>](https://blog.csdn.net/jnulzl)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/themagickeyjianan/article/details/52386981,BlogCommendHotData_8"}'>
	<div class="content">
		[

#### 
				python图片处理类之~PIL.Image模块(ios android icon图标自动生成处理)		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">08-31</span>
				<span class="read-num hover-hide">
					阅读数 
					11万+</span>

			</div>
		](https://blog.csdn.net/themagickeyjianan/article/details/52386981 "python图片处理类之~PIL.Image模块(ios android icon图标自动生成处理)")

			[
				<span class="desc oneline">1.从pyCharm提示下载PIL包

 http://www.pythonware.com/products/pil/

2.解压后，进入到目录下

cd /Users/jianan/Dow...</span>
			](https://blog.csdn.net/themagickeyjianan/article/details/52386981 "python图片处理类之~PIL.Image模块(ios android icon图标自动生成处理)")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 专注于cocos+unity+服务器全栈</span>](https://blog.csdn.net/themagickeyjianan)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/wuchengzeng/article/details/50037611,BlogCommendHotData_9"}'>
	<div class="content">
		[

#### 
				jquery/js实现一个网页同时调用多个倒计时(最新的)		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-25</span>
				<span class="read-num hover-hide">
					阅读数 
					53万+</span>

			</div>
		](https://blog.csdn.net/wuchengzeng/article/details/50037611 "jquery/js实现一个网页同时调用多个倒计时(最新的)")

			[
				<span class="desc oneline">jquery/js实现一个网页同时调用多个倒计时(最新的)

最近需要网页添加多个倒计时. 查阅网络,基本上都是千遍一律的不好用. 自己按需写了个.希望对大家有用. 有用请赞一个哦!

//js
...</span>
			](https://blog.csdn.net/wuchengzeng/article/details/50037611 "jquery/js实现一个网页同时调用多个倒计时(最新的)")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> Websites</span>](https://blog.csdn.net/wuchengzeng)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/haitao111313/article/details/7875392,BlogCommendHotData_10"}'>
	<div class="content">
		[

#### 
				基于PCA的人脸检测（Matlab版代码）		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">08-16</span>
				<span class="read-num hover-hide">
					阅读数 
					3万+</span>

			</div>
		](https://blog.csdn.net/haitao111313/article/details/7875392 "基于PCA的人脸检测（Matlab版代码）")

			[
				<span class="desc oneline">花了几天，终于把matlab版的人脸检测运行成功了，虽然正确率不是很高，看着各种论文上的人脸检测正确率都出奇的高，我是不怎么相信的，有的论文连基于平均脸的人脸检测正确率都能达到98%，汗啊～～  也许...</span>
			](https://blog.csdn.net/haitao111313/article/details/7875392 "基于PCA的人脸检测（Matlab版代码）")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 海海人生</span>](https://blog.csdn.net/haitao111313)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/lsx991947534/article/details/45499205,BlogCommendHotData_11"}'>
	<div class="content">
		[

#### 
				servlet+jsp实现过滤器，防止用户未登录访问		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">05-05</span>
				<span class="read-num hover-hide">
					阅读数 
					4万+</span>

			</div>
		](https://blog.csdn.net/lsx991947534/article/details/45499205 "servlet+jsp实现过滤器，防止用户未登录访问")

			[
				<span class="desc oneline">我们可能经常会用到这一功能，比如有时，我们不希望用户没有进行登录访问后台的操作页面，而且这样的非法访问会让系统极为的不安全，所以我们常常需要进行登录才授权访问其它页面，否则只会出现登录页面，当然我的思...</span>
			](https://blog.csdn.net/lsx991947534/article/details/45499205 "servlet+jsp实现过滤器，防止用户未登录访问")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 沉默的鲨鱼的专栏</span>](https://blog.csdn.net/lsx991947534)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/qq574857122/article/details/16361033,BlogCommendHotData_12"}'>
	<div class="content">
		[

#### 
				强连通分量及缩点tarjan算法解析		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">11-16</span>
				<span class="read-num hover-hide">
					阅读数 
					65万+</span>

			</div>
		](https://blog.csdn.net/qq574857122/article/details/16361033 "强连通分量及缩点tarjan算法解析")

			[
				<span class="desc oneline">强连通分量：
简言之 就是找环（每条边只走一次，两两可达）
孤立的一个点也是一个连通分量 

使用tarjan算法 在嵌套的多个环中优先得到最大环( 最小环就是每个孤立点）

定义：
int Ti...</span>
			](https://blog.csdn.net/qq574857122/article/details/16361033 "强连通分量及缩点tarjan算法解析")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 九野的博客</span>](https://blog.csdn.net/qq574857122)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/gefangshuai/article/details/50328451,BlogCommendHotData_13"}'>
	<div class="content">
		[

#### 
				关于SpringBoot bean无法注入的问题（与文件包位置有关）		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">12-16</span>
				<span class="read-num hover-hide">
					阅读数 
					25万+</span>

			</div>
		](https://blog.csdn.net/gefangshuai/article/details/50328451 "关于SpringBoot bean无法注入的问题（与文件包位置有关）")

			[
				<span class="desc oneline">问题场景描述整个项目通过Maven构建，大致结构如下：
核心Spring框架一个module spring-boot-base
service和dao一个module server-core
提供系统...</span>
			](https://blog.csdn.net/gefangshuai/article/details/50328451 "关于SpringBoot bean无法注入的问题（与文件包位置有关）")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 开发随笔</span>](https://blog.csdn.net/gefangshuai)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/chunqiuwei/article/details/48765007,BlogCommendHotData_14"}'>
	<div class="content">
		[

#### 
				ListView乱谈之ListView中View重用的简单解析		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">10-10</span>
				<span class="read-num hover-hide">
					阅读数 
					3793</span>

			</div>
		](https://blog.csdn.net/chunqiuwei/article/details/48765007 "ListView乱谈之ListView中View重用的简单解析")

			[
				<span class="desc oneline">简单分析ListView的回收机制</span>
			](https://blog.csdn.net/chunqiuwei/article/details/48765007 "ListView乱谈之ListView中View重用的简单解析")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 菜鸟博客</span>](https://blog.csdn.net/chunqiuwei)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zml_2015/article/details/46662809,BlogCommendHotData_15"}'>
	<div class="content">
		[

#### 
				Linux虚拟机与外面系统ping不通，或者连不上网		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">06-27</span>
				<span class="read-num hover-hide">
					阅读数 
					1万+</span>

			</div>
		](https://blog.csdn.net/zml_2015/article/details/46662809 "Linux虚拟机与外面系统ping不通，或者连不上网")

			[
				<span class="desc oneline">很多人在做linux课程设计的时候，用的linux虚拟机与外面的系统ping不通，或者虚拟机里面上不了网，这个主要是与系统的默认设置有关，下面让我帮你们解决这个问题吧
1.首先打开虚拟机的    “编...</span>
			](https://blog.csdn.net/zml_2015/article/details/46662809 "Linux虚拟机与外面系统ping不通，或者连不上网")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 云淡风轻的博客</span>](https://blog.csdn.net/zml_2015)
												</span>

	</div>
	</div>

<div class="recommend-item-box type_blog clearfix"  data-track-click='{"mod":"popu_614","con":",https://blog.csdn.net/zd0303/article/details/7058457,BlogCommendHotData_16"}'>
	<div class="content">
		[

#### 
				MATLAB中注释一段程序		

		<div class="info-box d-flex align-content-center">

				<span class="date hover-show">12-09</span>
				<span class="read-num hover-hide">
					阅读数 
					4万+</span>

			</div>
		](https://blog.csdn.net/zd0303/article/details/7058457 "MATLAB中注释一段程序")

			[
				<span class="desc oneline">在MATLAB中，可以注释一段程序。
使用“%{”和“%}”。
例如
%{
。。。
%}
即可。
经典方法是用 if 0，但缺点是不够直观，注释掉的内容仍然保持代码的颜色。现在可以用
...</span>
			](https://blog.csdn.net/zd0303/article/details/7058457 "MATLAB中注释一段程序")
			<span class="blog_title_box oneline ">
									<span class="type-show type-show-blog type-show-after">博文</span>
											[来自：	<span class="blog_title"> 知识小屋</span>](https://blog.csdn.net/zd0303)
												</span>

	</div>
	</div>

                <div class="recommend-item-box type_hot_word">
                                <div class="content clearfix">
                    <div class="word float-left">
                                                            <span>
                        [
                        设计制作学习                    ](https://edu.csdn.net/combos/o363_l0_t )</span>
                                                                                <span>
                        [
                        机器学习教程                    ](https://edu.csdn.net/courses/o5329_s5330_k )</span>
                                                                                <span>
                        [
                        Objective-C培训                    ](https://edu.csdn.net/courses/o280_s351_k )</span>
                                                                                <span>
                        [
                        交互设计视频教程                    ](https://edu.csdn.net/combos/o7115_s388_l0_t )</span>
                                                                                <span>
                        [
                        颜色模型                    ](https://edu.csdn.net/course/play/5599/104252 )</span>
                                                            </div>
                </div>
                                                <div class="content clearfix">
                    <div class="float-left">
                                        <span>
                        [
                        mysql关联查询两次本表](https://www.csdn.net/gather_24/MtTaEg3sMDM5MS1ibG9n.html)
                    </span>
                                        <span>
                        [
                        native底部 react](https://www.csdn.net/gather_10/MtjaIg3sMTUzMy1kb3dubG9hZAO0O0OO0O0O.html)
                    </span>
                                        <span>
                        [
                        extjs glyph 图标](https://www.csdn.net/gather_1b/Ntzagg1sOTU3LWRvd25sb2Fk.html)
                    </span>
                                        <span>
                        [
                        python教程github](https://www.csdn.net/gather_4a/MtjaUg5sMy1lZHUO0O0O.html)
                    </span>
                                        <span>
                        [
                        java学习github](https://www.csdn.net/gather_4a/NtjaQg0sNzAtZWR1.html)
                    </span>
                                        </div>
                </div>
                                </div>
                            <div class="recommend-loading-box">
                ![](https://csdnimg.cn/release/phoenix/images/feedLoading.gif)
            </div>
            <div class="recommend-end-box">

没有更多推荐了，[返回首页](https://blog.csdn.net/)

            </div>
        </div>
    </main>

    <aside>
	<div id="asideProfile" class="aside-box">
    <!-- 

### 个人资料
 -->
    <div class="profile-intro d-flex">
        <div class="avatar-box d-flex justify-content-center flex-column">
            [
              ![](https://avatar.csdn.net/4/1/9/3_misswuxl.jpg)
                              ![](https://g.csdnimg.cn/static/user-reg-year/1x/2.png)
                          ](https://blog.csdn.net/misswuxl)

        </div>
        <div class="user-info d-flex justify-content-center flex-column">

                [脖子有点儿疼](https://blog.csdn.net/misswuxl)

                    </div>
                <div class="opt-box d-flex justify-content-center flex-column">
            <span  class="csdn-tracking-statistics tracking-click" data-mod="popu_379">
                <a class="btn btn-sm btn-red-hollow attention" id="btnAttent">关注</a>
            </span>
        </div>
            </div>
    <div class="data-info d-flex item-tiling">
                <dl class="text-center" title="0">
                        <dt>原创</dt>
            <dd><span class="count">0</span></dd>
                    </dl>
        <dl class="text-center" id="fanBox" title="0">
            <dt>粉丝</dt>
            <dd><span class="count" id="fan">0</span></dd>
        </dl>
        <dl class="text-center" title="2">
            <dt>喜欢</dt>
            <dd><span class="count">2</span></dd>
        </dl>
        <dl class="text-center" title="0">
            <dt>评论</dt>
            <dd><span class="count">0</span></dd>
        </dl>
    </div>
    <div class="grade-box clearfix">
        <dl>
            <dt>等级：</dt>
            <dd>
                [
                    <svg class="icon icon-level" aria-hidden="true">
                        <use xlink:href="#csdnc-bloglevel-1"></use>
                    </svg>
                ](https://blog.csdn.net/home/help.html#level "1级,点击查看等级说明")
            </dd>
        </dl>
        <dl>
            <dt>访问：</dt>
            <dd title="2875">
                2875            </dd>
        </dl>
        <dl>
            <dt>积分：</dt>
            <dd title="63">
                63            </dd>
        </dl>
        <dl title="1759075">
            <dt>排名：</dt>
            <dd>175万+</dd>
        </dl>
    </div>
    </div>
<div class="csdn-tracking-statistics mb8 box-shadow" data-pid="blog" data-mod="popu_4" style="height:250px;">
    <div class="aside-content text-center" id="cpro_u2734133">
      <div id="kp_box_56" data-pid="56" data-track-view='{"mod":"kp_popu_56-703","con":",,"}' data-track-click='{"mod":"kp_popu_56-703","con":",,"}'><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 博客内页左上视窗-20181120 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:250px"
     data-ad-client="ca-pub-1076724771190722"
     data-ad-slot="7700527946"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div>    </div>
</div>
<div id="asideNewArticle" class="aside-box">

### 最新文章

    <div class="aside-content">

*   [超简单的获取某图片上的某种颜色对应的css颜色值：不需要photoshop](https://blog.csdn.net/misswuxl/article/details/78220537)
*   [github上的html查看效果](https://blog.csdn.net/misswuxl/article/details/78219649)
*   [小薇学院任务一：零基础HTML编码（笔记）](https://blog.csdn.net/misswuxl/article/details/78137777)
*   [Phalon框架:将复选框所有选择的值从View视图层(.volt)传输到控制层(.php)](https://blog.csdn.net/misswuxl/article/details/77935918)
    </div>
</div>
<div id="asideCategory" class="aside-box">

### 个人分类

    <div class="aside-content">

*   [
                    <span class="title oneline">phalcon</span>
                    <span class="count float-right">1篇</span>
                ](https://blog.csdn.net/misswuxl/article/category/7165764)
*   [
                    <span class="title oneline">baidu_web_xiaowei</span>
                    <span class="count float-right">1篇</span>
                ](https://blog.csdn.net/misswuxl/article/category/7203399)
*   [
                    <span class="title oneline">github</span>
                    <span class="count float-right">2篇</span>
                ](https://blog.csdn.net/misswuxl/article/category/7216804)
*   [
                    <span class="title oneline">html+css</span>
                    <span class="count float-right">1篇</span>
                ](https://blog.csdn.net/misswuxl/article/category/7221727)
    </div>
    </div>
<div id="asideArchive" class="aside-box">

### 归档

    <div class="aside-content">

                        <!--归档统计-->*   [
                    2017年10月                    <span class="count float-right">3篇</span>
                ](https://blog.csdn.net/misswuxl/article/month/2017/10)

                        <!--归档统计-->*   [
                    2017年9月                    <span class="count float-right">2篇</span>
                ](https://blog.csdn.net/misswuxl/article/month/2017/09)
    </div>
    </div>
<div id="asideHotArticle" class="aside-box">

### 热门文章

	<div class="aside-content">

*   [超简单的获取某图片上的某种颜色对应的css颜色值：不需要photoshop](https://blog.csdn.net/misswuxl/article/details/78220537)

    阅读数 <span>1681</span>

*   [Phalon框架:将复选框所有选择的值从View视图层(.volt)传输到控制层(.php)](https://blog.csdn.net/misswuxl/article/details/77935918)

    阅读数 <span>396</span>

*   [github上的html查看效果](https://blog.csdn.net/misswuxl/article/details/78219649)

    阅读数 <span>327</span>

*   [小薇学院任务一：零基础HTML编码（笔记）](https://blog.csdn.net/misswuxl/article/details/78137777)

    阅读数 <span>317</span>

*   [github：提交本地html到github](https://blog.csdn.net/misswuxl/article/details/78198489)

    阅读数 <span>153</span>
	</div>
</div>
	<div id="asideFooter">

		<div class="aside-box">
			<div id="kp_box_57" data-pid="57" data-track-view='{"mod":"kp_popu_57-1158","con":",,"}' data-track-click='{"mod":"kp_popu_57-1158","con":",,"}'><!-- 广告位：PC-博客内页左下视窗 -->
<script>
(function() {
    var s = "_" + Math.random().toString(36).slice(2);
    document.write('<div id="' + s + '"></div>');
    (window.slotbydup=window.slotbydup || []).push({
        id: '6272567',
        container: s,
        size: '300,250',
        display: 'inlay-fix'
    });
})();
</script>
<script src="http://dup.baidustatic.com/js/os.js"></script></div>		</div>
				<div class="aside-box">
			<div class="persion_article">
			</div>
		</div>
	</div>
</aside>
<script src="https://csdnimg.cn/pubfooter/js/publib_footer-1.0.3.js" data-isfootertrack="false" type="text/javascript"></script>
<script>
	$("a.flexible-btn").click(function(){
		$(this).parents('div.aside-box').removeClass('flexible-box');
		$(this).remove();
	})
</script>
</div>
<div class="mask-dark"></div>
<div class="tool-box">

*   <button class=" low-height hover-box btn-like " title="点赞">
				<svg class="icon active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-thumbsup-ok"></use>
				</svg>
				<svg class="icon no-active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-thumbsup"></use>
				</svg>
				<span class="hover-show text-box text">
					<span class="no-active">点赞</span>
					<span class="active">取消点赞</span>
				</span>

    0

    			</button>
*   [
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-comments"></use>
				</svg>
				<span class="hover-show text">评论</span>

    			](#commentBox "写评论")
*   <button class="btn-toc low-height hover-box" title="目录">
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-contents"></use>
				</svg>
				<span class="hover-show text">目录</span>
			</button>
			<div class="toc-container">
				<div class="pos-box">
					<div class="icon-arrow"></div>
					<div class="scroll-box">
						<div class="toc-box"></div>
					</div>
				</div>
				<div class="opt-box">
					<button class="btn-opt prev nomore" title="向上">
						<svg class="icon" aria-hidden="true">
							<use xlink:href="#csdnc-chevronup"></use>
						</svg>
					</button>
					<button class="btn-opt next">
						<svg class="icon" aria-hidden="true">
							<use xlink:href="#csdnc-chevrondown"></use>
						</svg>
					</button>
				</div>
			</div>
*   <button class="btn-bookmark low-height hover-box" title="收藏">
				<svg class="icon active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-bookmark-ok"></use>
				</svg>
				<svg class="icon no-active hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-bookmark"></use>
				</svg>
					<span class="hover-show text">收藏</span>
				<!-- <span class="hover-show text-box text">
					<span class="no-active">收藏</span>
					<span class="active">取消收藏</span>
				</span> -->
			</button>
*   <div class="weixin-qr btn-comments low-height hover-box" >
        [](# "手机看")
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-usephone"></use>
				</svg>
				<span class="hover-show text text3">
					手机看
				</span>
			</div>
*   [
					<svg class="icon hover-hide" aria-hidden="true">
						<use xlink:href="#csdnc-chevronleft"></use>
					</svg>
					<span class="hover-show text text3">上一篇</span>
				](https://blog.csdn.net/misswuxl/article/details/78137777 "小薇学院任务一：零基础HTML编码（笔记）")
*   [
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-chevronright"></use>
				</svg>
				<span class="hover-show text text3">下一篇</span>
			](https://blog.csdn.net/misswuxl/article/details/78219649 "github上的html查看效果")

						<!-- 宽屏更多按钮 -->*   [
				<svg class="icon hover-hide" aria-hidden="true">
					<use xlink:href="#csdnc-more"></use>
				</svg>
				<span class="hover-show text">更多</span>
			](#chatqa "快问")

        *   [
							<svg class="icon hover-hide" aria-hidden="true">
								<use xlink:href="#csdnc-chevronleft"></use>
							</svg>
							<span class="hover-show text text3">上一篇</span>
						](https://blog.csdn.net/misswuxl/article/details/78137777 "小薇学院任务一：零基础HTML编码（笔记）")
    *   [
						<svg class="icon hover-hide" aria-hidden="true">
							<use xlink:href="#csdnc-chevronright"></use>
						</svg>
						<span class="hover-show text text3">下一篇</span>
					](https://blog.csdn.net/misswuxl/article/details/78219649 "github上的html查看效果")
</div>
<script>window._bd_share_config = { "common": { "bdSnsKey": {}, "bdText": "", "bdMini": "1", "bdMiniList": false, "bdPic": "", "bdStyle": "0", "bdSize": "16" }, "share": {} }; with (document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = 'https://csdnimg.cn/static/api/js/share.js?v=89860594'];</script>
<script>
    var recommendCount = 67;
    recommendCount = recommendCount > 1 ? (recommendCount + (recommendCount>6 ? 2 : 1)) : recommendCount;
    var ChannelId = 14;
    var articleId = "78198489";
    var commentscount = 0;
    var islock = false;
    var curentUrl = "https://blog.csdn.net/misswuxl/article/details/78198489";
    var myUrl = "https://my.csdn.net/";
    //1禁止评论，2正常
    var commentAuth = 2;
    //百度搜索
    var baiduKey = "github：提交本地html到github - misswuxl的博客";
    var needInsertBaidu = true;
    // 代码段样式
    var codeStyle = '';
	var highlight = ["github","\u63d0\u4ea4","\u672c\u5730","html","github"];//高亮数组

    var RecommendBlogExpertList = [{"user_name":"itpinpai","nick_name":"itpinpai","avatar":"https:\/\/avatar.csdn.net\/F\/7\/7\/3_itpinpai.jpg","is_expert":true,"article_count":383,"rank":"1000+"},{"user_name":"Yujie_Yang","nick_name":"Yujie_Yang","avatar":"https:\/\/avatar.csdn.net\/3\/9\/F\/3_yujie_yang.jpg","is_expert":false,"article_count":8,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"y13156556538","nick_name":"y13156556538","avatar":"https:\/\/avatar.csdn.net\/F\/6\/D\/3_y13156556538.jpg","is_expert":false,"article_count":280,"rank":"8000+"},{"user_name":"yzh785119509","nick_name":"Passingyan","avatar":"https:\/\/avatar.csdn.net\/4\/2\/C\/3_yzh785119509.jpg","is_expert":false,"article_count":1,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"gang456789","nick_name":"gang456789","avatar":"https:\/\/avatar.csdn.net\/3\/C\/3\/3_gang456789.jpg","is_expert":false,"article_count":60,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"dalinsi","nick_name":"\u82f1\u6770\u738b","avatar":"https:\/\/avatar.csdn.net\/F\/F\/6\/3_dalinsi.jpg","is_expert":false,"article_count":235,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"Leon_summer","nick_name":"Leon_summer","avatar":"https:\/\/avatar.csdn.net\/B\/D\/6\/3_leon_summer.jpg","is_expert":false,"article_count":12,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"qq_32540053","nick_name":"OKXLIN","avatar":"https:\/\/avatar.csdn.net\/3\/6\/C\/3_qq_32540053.jpg","is_expert":false,"article_count":37,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"Azure_Sky_2014","nick_name":"mysealer","avatar":"https:\/\/avatar.csdn.net\/4\/D\/E\/3_azure_sky_2014.jpg","is_expert":false,"article_count":19,"rank":"\u5343\u91cc\u4e4b\u5916"},{"user_name":"u010246789","nick_name":"\u5b64\u5929\u6d6a\u96e8","avatar":"https:\/\/avatar.csdn.net\/F\/4\/D\/3_u010246789.jpg","is_expert":false,"article_count":143,"rank":"6000+"}];
	var articleType = 4;
	var CopyrightContent = '';
</script>
<script src="https://csdnimg.cn/public/sandalstrap/1.4/js/sandalstrap.min.js"></script>
<script src="https://csdnimg.cn/release/phoenix/vendor/pagination/paging.js"></script>

<div style="display:none;">
	![]()
</div>
</body>

<!-- 高亮未与 markdown兼容  -->
	<link rel="stylesheet" href="https://csdnimg.cn/release/blog_editor_html/release1.3.9/ckeditor/plugins/chart/chart.css" />
	<script type="text/javascript" src="https://csdnimg.cn/release/blog_editor_html/release1.3.9/ckeditor/plugins/chart/lib/chart.min.js"></script>
	<script type="text/javascript" src="https://csdnimg.cn/release/blog_editor_html/release1.3.9/ckeditor/plugins/chart/widget2chart.js"></script>
	<link rel="stylesheet" href="https://csdnimg.cn/release/blog_editor_html/release1.3.9/ckeditor/plugins/codesnippet/lib/highlight/styles/atom-one-light.css">
	<script type="text/javascript" src="https://csdnimg.cn/release/phoenix/production/pc_wap_common-45af74a22e.js" /></script>

	<script type="text/javascript">

	</script>

<script src="https://csdnimg.cn/release/phoenix/template/js/common-0100d9c3da.min.js"></script>
<script src="https://csdnimg.cn/release/phoenix/template/js/detail-a8a55c8dd3.min.js"></script>

	<script src="https://csdnimg.cn/release/phoenix/themes/skin-yellow/skin-yellow-fc7383b956.min.js"></script>

<script src="https://csdnimg.cn/public/common/gotop/js/goTop-v1.0.min.js?v201904241615"></script><script>
    GoTop({
        right: 8,
        hasReport: true,
        reportFun: function() {
            showReport(false,articleTitles);
        }
    })
</script>

    <script src="//g.csdnimg.cn/??login-box/1.0.5/login-box.js,login-box/1.0.5/login-auto.js,copyright/1.0.3/copyright.js,baidu-search/1.0.0/baidu-search.js?t=20190307095522"  type="text/javascript"></script>

<script type="text/javascript" src="https://csdnimg.cn/release/blog_mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
            "HTML-CSS": {
                    linebreaks: { automatic: true, width: "94%container" },
                    imageFont: null
            },
            tex2jax: {
                preview: "none"
            },
            mml2jax: {
                preview: 'none'
            }
    });
</script>
<script type="text/javascript">
    </script>
<script src="https://gh.bdstatic.com/static/gh/js/sdk/bword.min.js"></script>
</html>
