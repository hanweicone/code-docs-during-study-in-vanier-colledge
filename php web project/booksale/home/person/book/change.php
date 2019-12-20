<?php
  include '../../../public/common/conn.php';
  include '../../public/session.php';

  $id = $_GET['id'];
  $sqlBook = "select * from book where id = {$id}";

  $rstBook = mysql_query($sqlBook);
  $rowBook = mysql_fetch_assoc($rstBook);
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>add sellings</title>
	<link rel="stylesheet" href="../../public/css/index.css">
</head>
<body>
	<div class="main">
		<?php
			include '../../header.php';
		?>
		<div class="nav"></div>
		<div class="content">
			<div class="floor">
				<div class="floorHeader">
					<div class="left">
						<span>user center:</span>
					</div>
				</div>

				<div class="floorFooter2">
					<div class='floorFooter2Left'>
						<ul>
							<li>user info</li>
                            <li><a href="../user/userlist.php">|--check info</a></li>
                            <li>contact</li>
                            <li><a href="../touch/touchlist.php">|--check contact</a></li>
                            <li><a href="../touch/touchadd.php">|--add contact</a></li>
                            <li>my sellings</li>
                            <li><a href="salelist.php">|--check sellings</a></li>
                            <li><a href="<?php echo $root?>/home/saleadd.php">|--add sellings</a></li>
                            <li>orders</li>
                            <li><a href="../order/myorder.php">|--check my orders</a></li>
                            <li><a href="../order/gukeorder.php">|--check customer orders</a></li>
						</ul>
					</div>

					<div class='floorFooter2Right'>
							<form action="update.php" method='post' enctype='multipart/form-data'>
                            	<p>Title:</p>
                                <p><input type="text" name='name' class="input-k" value='<?php echo $rowBook['name']?>'></p>

                                <p>Author:</p>
                                <p><input type="text" name='writer' class="input-k" value='<?php echo $rowBook['writer']?>'></p>

                                <p>Price:</p>
                                <p><input type="text" name='oldprice'  class="input-k" value='<?php echo $rowBook['oldprice']?>'></p>

                                <p>Price now:</p>
                                <p><input type="text" name='nowprice'  class="input-k" value='<?php echo $rowBook['nowprice']?>'></p>

                            	<p>Stock:</p>
                                <p><input type="text" name='stock' class="input-k" value='<?php echo $rowBook['stock']?>'></p>

                                <p>Sales:</p>
                                <p><input type="text" name='sales' class="input-k" value='<?php echo $rowBook['sales']?>'></p>

                            	<p>Avialiable:</p>
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

                            	<p>Catagory:</p>
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
                                <p>Original Image:</p>
                                <p><img src="../../../public/uploads/<?php echo $rowBook['img']?>" width="100px"></p>

                                <p>Img:</p>
                                <p><input type="file" name="img"></p>

                                <p>Description:</p>
                                <p>
                                  <textarea name='info' cols="30" rows="5" style="margin-left:10px;"><?php echo $rowBook['info']?></textarea>
                                </p>

                                <input type="hidden" name="id" value='<?php echo $rowBook['id']?>'>
                                <input type="hidden" name="imgsrc" value='<?php echo $rowBook['img']?>'>

                                <p><input type="submit" class="input-k" value="edit"></p>
                            </form>
					</div>
					<div class='clear'></div>
				</div>
			</div>
		</div>

		<?php
			include '../../footer.php';
		?>
	</div>
</body>
</html>