<?php
  include 'public/session.php';
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>left</title>
	<style>
		*{
			font-family: 黑体;
			text-decoration:none;
		}
		h4{
			cursor: pointer;/*光标形状是手指*/
			background:url(public/img/leader-bg.jpg) no-repeat center;
			width: auto;
			height: 25px;
			text-align: center;
			color:#fff;
			font-size: 14px;
			margin-top: 20px;
			padding-top: 6px;
		}

		h4:hover{
			color:#01afbe;
			background: #fff;
		}

		div{
			display: none;
		}

		p{
			padding-left:15px;
			text-align: center;
		}

		p a{
			color:#01afbe;
			font-size: 14px;
		}
	</style>
	<script src='public/js/jquery.js'></script>
</head>
<body>
	<h4>admin</h4>
    <div>
    	<p><a href='webmaster/index.php' target='right'>|-admin list</a></p>
    	<p><a href='webmaster/add.php' target='right'>|-add admin</a></p>
    </div>
	<h4>user</h4>
	<div>
		<p><a href='user/index.php' target='right'>|-user list</a></p>
		<p><a href='user/add.php' target='right'>|-add user</a></p>
	</div>
	<h4>catagory</h4>
	<div>
		<p><a href='class/index.php' target='right'>|-catagory</a></p>
		<p><a href='class/add.php' target='right'>|-add class</a></p>
	</div>
	<h4>book</h4>
	<div>
		<p><a href='book/index.php' target='right'>|-books</a></p>
		<p><a href='book/useroffer.php' target='right'>|-user books</a></p>
		<p><a href='book/putaway.php' target='right'>|-in stock book</a></p>
		<p><a href='book/soldout.php' target='right'>|-out stock book</a></p>
		<p><a href='book/add.php' target='right'>|-add sellings           </a></p>
	</div>
	<h4>comment</h4>
	<div>
		<p><a href='comment/index.php' target='right'>|-check comment</a></p>
	</div>
	<h4>order</h4>
	<div>
		<p><a href='status/index.php' target='right'>|-statues</a></p>
		<p><a href='status/add.php' target='right'>|-add statues</a></p>
	</div>
	<h4>orders</h4>
	<div>
		<p><a href='indent/index.php' target='right'>|-check order</a></p>
	</div>

	<h4>system</h4>
	<div>
		<p><a href="logout.php" target='_top' onclick="return confirm('do you want to quit？')">|-Quit</a></p>
		<p><a href="../index.html" target='_blank'>|-main</a></p>
	</div>
</body>
<script>
$('h4').click(function(){
	$(this).next().toggle();   //toggle()方法：切换<p>元素的显示与隐藏
	$('div').not($(this).next()).hide();
});
</script>
</html>