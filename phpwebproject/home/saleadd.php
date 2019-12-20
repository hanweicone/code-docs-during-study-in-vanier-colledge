<?php
  include '../public/common/conn.php';
  include 'public/session.php';

  $sql="select * from class";
  $rst=mysql_query($sql);
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Sell book</title>
	<link rel="stylesheet" href="public/css/发布旧书.css">
	<link rel="stylesheet" href="public/css/animate.min.css">
</head>
<body>
	<div class="main">
		<?php
			include 'header.php';
		?>
		<div id="fabu" class="animated bounceInRight">
      <div class="fabu">
				<form   action="<?php echo $root?>/home/person/book/insert.php" method='post' enctype='multipart/form-data'>
            <p class="left-name">Title:</p>
            <p><input type="text" name='name' class="right-name"></p>
          
            <p class="left-writer">Author:</p>
            <p><input type="text" name='writer'  class="right-writer"></p>

            <p class="left-oprice">prePrice:</p>
            <p><input type="text" name='oldprice'  class="right-oprice"></p>

            <p class="left-nprice">Price:</p>
            <p><input type="text" name='nowprice'  class="right-nprice"></p>

            <p class="left-stock">stock:</p>
            <p><input type="text" name='stock'  class="right-stock"></p>

            <p class="left-num">Sales:</p>
            <p><input type="text" name='sales'  class="right-num"></p>

            <p class="left-huojia">Avialiable:</p>
            <p class="right-huojia">
            <label>
            	<input type="radio" name="shelf" value='1' checked> in stock
            </label>
            <label>
            	<input type="radio" name="shelf" value='0'> out stock
            </label>
            </p>

            <p class="left-leibie">Catagory:</p>
            <p class="right-leibie">
              <select name="class_id">
                <?php
                   while($row=mysql_fetch_assoc($rst)){
                    echo "<option value='{$row['id']}'>{$row['name']}</option>";}
                ?>
              </select>
            </p>

            <p class="left-img">Img:</p>
            <p><input type="file" name="img"  class="right-img"></p>

            <p class="left-jianjie">Discription:</p>
            <p><textarea name='info' cols="30" rows="5"  class="right-jianjie"></textarea></p>

            <p><input type="submit" value="put" class="commit"></p>
            </form>
			    </div>
        </div>

		<?php
			include 'footer.php';
		?>
	</div>
</body>
</html>