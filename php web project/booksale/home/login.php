<?php
 session_start();
 $path = $_SERVER['PHP_SELF'];
 $arr = explode('/',$path);
 $root = '/'.$arr[1];
?>

<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>User Login</title>
	<link rel="stylesheet" href="public/css/登录注册.css" />
	<script src="public/js/jquery-1.11.3.js"></script>
  <script src="public/js/login.js"></script>
</head>
<body>
	<div class="main">
		<div class="denglubiaodan">  
        <ul>
            <form action="#"> 
                <input  id="lgname" type="text"  name='username' class="inputname"
                		v-model="inputtext.name" placeholder="please enter user name"> <br />
                <input  id="lgpwd" type="password" name='password' class="inputpas"
                		v-model="inputtext.password" placeholder="please enter password">             	
				<input id="lgbtn" type="button" value=" ">
			
				<div class="zhuce">
					<a href="<?php echo $root?>/home/register.php" class="bt-zhuce">register</a>
				</div>
           </form>
        </ul>  
        </div> 	
		</div>	
		<div class="nav"></div>
	</div>	
</body>
</html>