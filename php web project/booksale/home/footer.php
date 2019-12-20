<?php
 $path = $_SERVER['PHP_SELF'];
 $arr = explode('/',$path);
 $root = '/'.$arr[1];
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>footer</title>
<!--		<link rel="stylesheet" href="public/css/index_1.css" />-->
		<link rel="stylesheet" href="<?php echo $root?>/home/public/css/foot.css" />
	</head>
	<body>  
		<div class="foot">
			<img src="<?php echo $root?>/home/public/img/导航背景.png" class="foot-bg" />
			<div class="foot1" >
			<p style="padding-left: 85px">
				Copyright © 2019 Wei Han. All rights reserved.
			</p>
			</div>
			<div class="foot2">
			<nav>
				
				<ul>
					<li><a href="#">Category</a>  |</li>
					<li><a href="#">Collection</a>  |</li>
					<li><a href="#">Sell</a>  |</li>
					<li><a href="#">Recomandation</a>  |</li>
					<li><a href="#">Message Center</a>  |</li>
					<li><a href="#">User Cente</a></li>
				</ul>
			</nav>
			</div>
		</div>
	</body>
</html>



