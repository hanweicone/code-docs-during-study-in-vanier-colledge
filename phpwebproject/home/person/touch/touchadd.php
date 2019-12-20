<?php
  include '../../public/session.php';
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>add contact</title>
	<link rel="stylesheet" href="../../public/css/index.css">
</head>
<body>
	<div class="main">
		<?php 
			include '../../header.php';
		?>
		<div class="nav"></div>
		<div class="content">
			<div class="floor">
				<div class="floorHeader">
					<div class="left">
						<span>个人中心:</span>	
					</div>
				</div>

				<div class="floorFooter2">
					<div class='floorFooter2Left'>
						<ul>
							 <li>user info</li>
                             <li><a href="../user/userlist.php">|--check info</a></li>
                             <li>contact</li>
                             <li><a href="touchlist.php">|--check contact</a></li>
                             <li><a href="touchadd.php">|--add contact</a></li>
                             <li>my sellings</li>
                             <li><a href="../book/salelist.php">|--check sellings</a></li>
                             <li><a href="<?php echo $root?>/home/saleadd.php">|--add sellings</a></li>
                             <li>order</li>
                             <li><a href="../order/myorder.php">|--check my order</a></li>
                             <li><a href="../order/gukeorder.php">|--check customer order</a></li>
						</ul>
					</div>

					<div class='floorFooter2Right'>
						<div class='personUseradd'>
						  <form action='touchinsert.php' method='post'>
								<p>shipping name:</p>
								<p><input type="text" name='name' class="input-k"></p>
								<p>address:</p>
								<p><input type="text" name='addr' class="input-k"></p>
								<p>postal:</p>
								<p><input type="text" name='postcode' class="input-k"></p>
								<p>phone:</p>
								<p><input type="text" name='tel' class="input-k"></p>

								<p><input type="submit" value="提交" class="input-k"></p>
					      </form>
						</div>
					</div>
					<div class='clear'></div>
				</div>
			</div>
		</div>	

		<?php 
			include '../../footer.php';
		?>
	</div>	
</body>
</html>