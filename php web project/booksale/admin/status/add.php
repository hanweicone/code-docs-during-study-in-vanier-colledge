<?php
  include '../public/session.php';
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
		<form action="insert.php" method='post'>
			<p>Statue name:</p>
			<p><input type="text" name='name'></p>

			<p><input type="submit" value="add"></p>
		</form>		
	</div>
	
</body>
</html>