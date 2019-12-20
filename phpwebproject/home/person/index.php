<?php
  session_start();

  $path = $_SERVER['PHP_SELF'];
  $arr = explode('/',$path);
  $root = '/'.$arr[1];

  if(!@$_SESSION['home_username']){
     echo "<script>location='{$root}/home/login.php'</script>";
     exit;
  }
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>user center</title>
	<link rel="stylesheet" href="../public/css/index.css">
</head>
<body>
	<div class="main">
		<?php 
			include '../header.php';
		?>
		<div class="nav"></div>
		<div class="content">
			<div class="floor">
				<div class="floorHeader">
					<div class="left">
						<span>user center:</span>	
					</div>
				</div>

				<div class="floorFooter2">
					<div class='floorFooter2Left'>
						<ul>
						    <li>user info</li>
						    <li><a href="user/userlist.php">|--check info</a></li>
						    <li>contact</li>
							<li><a href="touch/touchlist.php">|--check contact</a></li>
							<li><a href="touch/touchadd.php">|--add contact</a></li>
							<li>my books</li>
							<li><a href="book/salelist.php">|--check sellings</a></li>
							<li><a href="<?php echo $root?>/home/saleadd.php">|--add sellings</a></li>
							<li>my order</li>
							<li><a href="order/myorder.php">|--check my order</a></li>
							<li><a href="order/gukeorder.php">|--check customer order</a></li>
						</ul>
					</div>

					<div class='floorFooter2Right'>
						<div class='fenmu'>
							<img src="../public/img/wel.png" alt="">	
						</div>
					</div>
					<div class='clear'></div>
				</div>
			</div>
		</div>	

		<?php 
			include '../footer.php';
		?>
	</div>	
</body>
</html>