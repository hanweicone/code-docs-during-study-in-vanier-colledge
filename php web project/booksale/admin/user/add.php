<?php
  include '../../public/common/conn.php';
  include '../public/session.php';

  $sql="select * from user";
  $rst=mysql_query($sql);
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>index</title>
	<link rel="stylesheet" href="../public/css/index.css">
</head>
<body>
	<div class="main">
		<form action="insert.php" method='post' enctype='multipart/form-data'>
			<p>user name:</p>
			<p><input type="text" name='username'></p>

			<p>password:</p>
			<p><input type="password" name='password'></p>

			<p>real name:</p>
            <p><input type="text" name='realname'></p>

            <p>gender:</p>
            <p>
            	<label>
            		<input type="radio" name="sex" value='1' checked> female
            	</label>
            	<label>
            		<input type="radio" name="sex" value='0'> male
            	</label>
            </p>

            <p>avatar:</p>
            <p><input type="file" name="img"></p>

			<p><input type="submit" value="add"></p>
		</form>		
	</div>
	
</body>
</html>