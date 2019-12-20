<?php
  include '../../public/common/conn.php';
  include '../public/session.php';

  $id = $_GET['id'];
  $sql = "select * from user where id = {$id}";

  $rst = mysql_query($sql);
  $row = mysql_fetch_assoc($rst);
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
		<form action="update.php" method='post' enctype='multipart/form-data'>
			<p>user name:</p>
			<p><input type="text" name='username' value='<?php echo $row['username']?>'></p>

			<p>password:</p>
			<p><input type="password" name='password'></p>

            <p>actual name:</p>
            <p><input type="text" name='realname' value='<?php echo $row['realname']?>'></p>

            <p>gender:</p>
            <p>
            	<?php
            		if($row['sex']){
            	?>
            		<label>
            			<input type="radio" name="sex" value='1' checked> female
            		</label>
            		<label>
            		    <input type="radio" name="sex" value='0'> male
            		</label>
            	<?php
            		}else{
            	?>
            		<label>
            			<input type="radio" name="sex" value='1'> female
            		</label>
            		<label>
            		    <input type="radio" name="sex" value='0' checked> male
            		</label>
            	<?php
            		}
            	?>
            </p>

            <p>previous avatar :</p>
            <p><img src="../../public/upusers/<?php echo $row['img']?>" width="50px"></p>

            <p>avatar:</p>
            <p><input type="file" name="img"></p>

			<input type="hidden" name="id" value='<?php echo $row['id']?>'>
			<input type="hidden" name="imgsrc" value='<?php echo $row['img']?>'>

			<p><input type="submit" value="change"></p>
		</form>
	</div>

</body>
</html>