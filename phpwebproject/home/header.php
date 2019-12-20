<?php
 $path = $_SERVER['PHP_SELF'];
 $arr = explode('/',$path);
 $root = '/'.$arr[1];
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" href="<?php echo $root?>/home/public/css/页头.css" />
		<link rel="stylesheet" href="<?php echo $root?>/home/public/css/bootstrap.css"> 
		<script src="<?php echo $root?>/home/public/js/bootstrap.min.js"></script>
		<title>页头</title>
	</head>
	<body>
		<div>
		<div class="header">
		<div class="headerinner">
			<ul class="headernav">
				<li class="logo">
					<a href="<?php echo $root?>/home/index.php" target="_blank">
						<img src="<?php echo $root?>/home/public/img/无底logo.png" alt="首页"/>
					</a>					
				</li>				
				<li><a href="<?php echo $root?>/home/class.php">Category</a></li>
				<li><a href="<?php echo $root?>/home/bookshelf/index.php">Collection</a></li>
				<li><a href="<?php echo $root?>/home/saleadd.php">Sell </a></li>
				<li><a href="<?php echo $root?>/home/demo.html" >Recomandation</a></li>
				<li><a href="<?php echo $root?>/home/cart/index.php" >Shopping Cart</a></li>
				<li><a href="<?php echo $root?>/home/person/index.php" >User Center</a></li>		
			</ul>

			<!--<div class="geren">
				<a href="<?php echo $root?>/home/person/index.php">
					<img src="<?php echo $root?>/home/public/img/list.png" />
				</a>
			</div>-->
		</div>
		</div>
						
		</div>		
	</body>
</html>
