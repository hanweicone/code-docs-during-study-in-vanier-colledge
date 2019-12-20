<?php
	include '../../public/common/conn.php';
    include '../public/session.php';

	$sql="select * from class";
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
			<p>title:</p>
			<p><input type="text" name='name'></p>

            <p>author:</p>
            <p><input type="text" name='writer'></p>

			<p>price:</p>
			<p><input type="text" name='oldprice'></p>

            <p>price now:</p>
			<p><input type="text" name='nowprice'></p>

			<p>recommend or not:</p>
            <p>
                 <label>
                     <input type="radio" name="recommend" value='1' checked> yes
                 </label>
                 <label>
                     <input type="radio" name="recommend" value='0'> no
                 </label>
            </p>

			<p>in stock:</p>
			<p><input type="text" name='stock'></p>

			<p>sales:</p>
            <p><input type="text" name='sales'></p>

			<p>available:</p>
			<p>
				<label>
					<input type="radio" name="shelf" value='1' checked> in stock
				</label>
				<label>
					<input type="radio" name="shelf" value='0'> out stock
				</label>
			</p>

			<p>catagory:</p>
			<p>
				<select name="class_id">
					<?php
                        while($row=mysql_fetch_assoc($rst)){
                        	echo "<option value='{$row['id']}'>{$row['name']}</option>";
                        }
					?>	
				</select>
			</p>

			<p>img:</p>
			<p><input type="file" name="img"></p>

			<p>discription:</p>
            <p><textarea name='info' cols="30" rows="5"></textarea></p>

			<p><input type="submit" value="add"></p>
		</form>		
	</div>
	
</body>
</html>