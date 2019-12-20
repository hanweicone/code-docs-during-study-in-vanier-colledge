<?php
  include '../../../public/common/conn.php';
  include '../../public/session.php';

  $user_id = $_SESSION['home_userid'];
  $sql = "select * from user where id = {$user_id}";
  $rst = mysql_query($sql);
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
                             <li><a href="userlist.php">|--check info</a></li>
                             <li>contact</li>
                             <li><a href="../touch/touchlist.php">|--check contact</a></li>
                             <li><a href="../touch/touchadd.php">|--add contact</a></li>
                             <li>my sellings</li>
                             <li><a href="../book/salelist.php">|--check sellings</a></li>
                             <li><a href="<?php echo $root?>/home/saleadd.php">|--add sellings</a></li>
                             <li>orders</li>
                             <li><a href="../order/myorder.php">|--my orders</a></li>
                             <li><a href="../order/gukeorder.php">|--customer orders</a></li>
						</ul>
					</div>

					<div class='floorFooter2Right'>
                    		<table width='100%'>
                    			<tr>
                    				<th>name</th>
                    				<th>actual name</th>
                    				<th>avatar</th>
                    				<th>gender</th>
                    				<th>edit</th>
                    			</tr>

                    			<?php
                    			   while($row=mysql_fetch_assoc($rst)){
										echo "<tr>";
										echo "<td>{$row['username']}</td>";
										echo "<td>{$row['realname']}</td>";
										echo "<td><img src='../../../public/upusers/thumb_{$row['img']}' width='50px'></td>";
										if($row['sex']){
										   echo "<td>female</td>";
										}else{
										   echo "<td>male</td>";
										}
										echo "<td><a href='userchange.php?id={$row['id']}'>edit</a></td>";
										echo "</tr>";
                    			}
                                ?>
                    		</table>
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