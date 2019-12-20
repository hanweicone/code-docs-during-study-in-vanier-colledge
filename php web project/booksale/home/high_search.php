<?php
 include '../public/common/conn.php';
?>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" /> 
		<link rel="stylesheet" href="public/css/high_search.css" />
		<title></title>
	</head>
	<body>
		<div id="search">				
			<form action="matchsearch.php" method="post">
			    <input placeholder=" Please enter book name" type="text" name="name" >
			    <input placeholder=" Please enter autor name" type="text" name="writer">
				<input name="search" type="submit" value="Advance Search" class="btn-search"/>
			</form>			
		</div>
	</body>
	
	
	
</html>