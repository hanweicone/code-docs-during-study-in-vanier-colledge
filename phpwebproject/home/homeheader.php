<?php
 $path = $_SERVER['PHP_SELF'];
 $arr = explode('/',$path);
 $root = '/'.$arr[1];
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>Main</title>
		<script src="https://cdn.bootcss.com/vue/2.4.2/vue.min.js"></script>
		<link rel="stylesheet" href="public/css/index_1.css" />
		<link rel="stylesheet" href="<?php echo $root?>/home/public/css/bootstrap.css"> 
		<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
		<script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>

	</head>
	<body>
		<div>
			<div id="head">
			<span>
				<img src="public/img/新logo.png" class="logo"/>
				<div id="text">
					<?php
                     if(!@$_SESSION['home_userid']){
                       echo "<a href='{$root}/home/login.php'>Login</a>";
                     }else{
                       echo "&nbsp;&nbsp;<a href='{$root}/home/person/index.php'>
                       Welcome {$_SESSION['home_username']} login</a>&nbsp;&nbsp;
                       <a href='{$root}/home/logout.php'>logout</a>";
                     }
		            ?>
                    <a href="<?php echo $root?>/home/register.php">register</a>
				</div>				
			</span>	
			</div>
			
			<div id="search">
				<span>
					<form action="hotsearch.php" method="post">
					   <input name="keyword" type="text" placeholder="   Please Enter Keyword" class="kuang" style="box-shadow:0 0 8px rgba(0,0,0,0.2) ;"/>
                       <input name="ok" type="submit" value="" class="sbtn"/>
					</form>
				</span>		
			</div>
			</div>
	</body>
</html>
