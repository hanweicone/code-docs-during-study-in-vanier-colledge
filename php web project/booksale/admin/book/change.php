<?php
  include '../../public/common/conn.php';
  include '../public/session.php';

  $id = $_GET['id'];
  $sqlBook = "select * from book where id = {$id}";

  $rstBook = mysql_query($sqlBook);
  $rowBook = mysql_fetch_assoc($rstBook);
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
			<p>title:</p>
			<p><input type="text" name='name' value='<?php echo $rowBook['name']?>'></p>

            <p>author:</p>
            <p><input type="text" name='writer' value='<?php echo $rowBook['writer']?>'></p>

			<p>price:</p>
			<p><input type="text" name='oldprice' value='<?php echo $rowBook['oldprice']?>'></p>

            <p>price now:</p>
			<p><input type="text" name='nowprice' value='<?php echo $rowBook['nowprice']?>'></p>

			<p>recommend or not:</p>
            <p>
            <?php
               if($rowBook['recommend']){
            ?>
                 <label>
                     <input type="radio" name="recommend" value='1' checked> yes
                 </label>
                 <label>
                     <input type="radio" name="recommend" value='0'> no
                 </label>
            <?php
              }else{
            ?>
                 <label>
                     <input type="radio" name="recommend" value='1'> yes
                 </label>
                 <label>
                     <input type="radio" name="recommend" value='0' checked> no
                  </label>
            <?php
              }
            ?>
            </p>

			<p>in stock:</p>
			<p><input type="text" name='stock' value='<?php echo $rowBook['stock']?>'></p>

			<p>sales:</p>
            <p><input type="text" name='sales' value='<?php echo $rowBook['sales']?>'></p>

			<p>avialible:</p>
			<p>
				<?php
					if($rowBook['shelf']){
				?>
						<label>
							<input type="radio" name="shelf" value='1' checked> in stock
						</label>
						<label>
							<input type="radio" name="shelf" value='0'> out stock
						</label>
				<?php
					}else{
				?>
						<label>
							<input type="radio" name="shelf" value='1'> in stock
						</label>
						<label>
							<input type="radio" name="shelf" value='0' checked> out stock
						</label>
				<?php
					}
				?>
			</p>

			<p>catagory:</p>
			<p>
				<select name="class_id">
                	<?php
                	    $sqlClass="select * from class";
                        $rstClass=mysql_query($sqlClass);
                        while($rowClass=mysql_fetch_assoc($rstClass)){
                           if($rowClass['id'] == $rowBook['class_id']){
                              echo "<option value='{$rowClass['id']}' selected>{$rowClass['name']}</option>";
                           }else{
                              echo "<option value='{$rowClass['id']}'>{$rowClass['name']}</option>";
                           }
                        }
                	?>
                </select>
			</p>
			<p>original img:</p>
			<p><img src="../../public/uploads/<?php echo $rowBook['img']?>" width="100px"></p>

			<p>img:</p>
			<p><input type="file" name="img"></p>

			<p>discription:</p>
            <p>
              <textarea name='info' cols="30" rows="5" style="margin-left:10px;"><?php echo $rowBook['info']?></textarea>
            </p>

			<input type="hidden" name="id" value='<?php echo $rowBook['id']?>'>
			<input type="hidden" name="imgsrc" value='<?php echo $rowBook['img']?>'>

			<p><input type="submit" value="edit"></p>
		</form>
	</div>

</body>
</html>