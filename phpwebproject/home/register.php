<?php
  session_start();
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>register</title>
	<link rel="stylesheet" href="public/css/登录注册.css" />
	<link rel="stylesheet" href="public/css/u_dlzc.css">
	<script src="public/js/jquery-1.11.3.js"></script>
    <script src="public/js/register.js"></script>
</head>
<body>
	<div class="main">
		<div class="bg">  
        <ul>
			<form id="register" action="#">
            <input id="regname" type="text" name="regname" placeholder="please enter user name"/>
            <div id="namediv"></div>

            <p><input id="regpwd1" type="password" name="regpwd1" placeholder="please enter password more than 5 numbers"/>
            <div id="pwddiv1"></div></p>

            <input id="regpwd2" type="password" name="regpwd2" placeholder="enter password again"/>
            <div id="pwddiv2"></div>

            <p><input id="realname" type="text" name="realname" placeholder="enter real name"/></p>
            <div id="rnamediv"></div>

            <p><input id="regbtn" type="button" value="注册" disabled="disabled"/></p>
          </form>
        </ul>  
       </div> 		
	</div>	
</body>
</html>