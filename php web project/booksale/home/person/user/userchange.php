<?php
  include '../../../public/common/conn.php';
  include '../../public/session.php';

  $id = $_GET['id'];
  $sql = "select * from user where id = {$id}";

  $rst = mysql_query($sql);
  $row = mysql_fetch_assoc($rst);
?>

<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>user info</title>
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
                             <li>user info</li>
                             <li><a href="../user/userlist.php">|--check info</a></li>
                             <li>contact</li>
                             <li><a href="touchlist.php">|--check contact</a></li>
                             <li><a href="touchadd.php">|--add contact</a></li>
                             <li>my sellings</li>
                             <li><a href="../book/salelist.php">|--check sellings</a></li>
                             <li><a href="<?php echo $root?>/home/saleadd.php">|--add sellings</a></li>
                             <li>order</li>
                             <li><a href="../order/myorder.php">|--check my order</a></li>
                             <li><a href="../order/gukeorder.php">|--check customer order</a></li>
						</ul>
					</div>

					<div class='floorFooter2Right'>
                      <div class='personUseradd'>
                        <form action='userupdate.php' method='post' enctype='multipart/form-data'>
                            <p>user name:</p>
                            <p><input type="text" class="input-k" name='username' value='<?php echo $row['username']?>'></p>

                            <p>password:</p>
                            <p><input type="password"  class="input-k" name='password'></p>

                            <p>actual name:</p>
                            <p><input type="text"  class="input-k" name='realname' value='<?php echo $row['realname']?>'></p>

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

                            <p>Original image:</p>
                            <p><img src="../../../public/upusers/<?php echo $row['img']?>" width="50px"></p>

                            <p>avatar:</p>
                            <p><input type="file" name="img"></p>

                            <input type="hidden" name="id" value='<?php echo $row['id']?>'>
                            <input type="hidden" name="imgsrc" value='<?php echo $row['img']?>'>

                            <p><input type="submit" value="edit" class="input-k"></p>
                    	</form>
                      </div>
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