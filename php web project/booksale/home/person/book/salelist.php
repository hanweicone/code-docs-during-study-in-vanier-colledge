<?php
  include '../../../public/common/conn.php';
  include '../../public/session.php';
?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Check Sellings</title>
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
                             <li>order</li>
                             <li><a href="../order/myorder.php">|--check my order</a></li>
                             <li><a href="../order/gukeorder.php">|--check customer order</a></li>
						</ul>
					</div>

					<div class='floorFooter2Right'>
						<table width='100%'>
							<tr>
                            	<th>Title</th>
                            	<th>Author</th>
                            	<th>Img</th>
                            	<th>Price</th>
                            	<th>Price now</th>
                            	<th>stock</th>
                            	<th>sales</th>
                            	<th>Avialiable</th>
                            	<th>Catagory</th>
                            	<th>edit</th>
                            	<th>delete</th>
                            </tr>
                        <?php
                            $user_id = $_SESSION['home_userid'];
                            $sql = "select book.*,class.name cname from book,class where book.class_id=class.id and book.supplier = {$user_id}";
                            $rst = mysql_query($sql);

                            $size = 6;
                            $hangnum = mysql_num_rows($rst);
                            if($hangnum == 0){
                                echo "no sellings";
                            }else{
                                $page_num = ceil($hangnum/$size);
                                if(@$_GET['page_id']){
                                   $page_id = $_GET['page_id'];
                                   $start = ($page_id-1)*$size;
                                }else{
                                   $page_id = 1;
                                   $start = 0;
                                }

                                $fenye_sel = "select book.*,class.name cname from book,class where book.class_id=class.id and book.supplier = {$user_id} limit $start,$size";
                                $fenye_add = mysql_query($fenye_sel);

                                while($row=mysql_fetch_assoc($fenye_add)){
							           echo "<tr>";
                            		   echo "<td>{$row['name']}</td>";
                            		   echo "<td>{$row['writer']}</td>";
                            		   echo "<td><img src='../../../public/uploads/thumb_{$row['img']}' width='50px'></td>";
                            		   echo "<td>{$row['oldprice']}</td>";
                            		   echo "<td>{$row['nowprice']}</td>";
                            		   echo "<td>{$row['stock']}</td>";
                            		   echo "<td>{$row['sales']}</td>";
                            		   if($row['shelf']){
                            			   echo "<td>in stock</td>";
                            		   }else{
                            			   echo "<td>out stock</td>";
                            		   }
                            		   echo "<td>{$row['cname']}</td>";
                            		   echo "<td><a href='change.php?id={$row['id']}'>edit</a></td>";
                            		   echo "<td><a href='delete.php?id={$row['id']}&img={$row['img']}'>delete</a></td>";
                            		   echo "</tr>";
                            	   }
                            ?>
                         	<tr>
                               <td colspan="11">
                            <?php
                                echo "total records&nbsp;".$hangnum."&nbsp;&nbsp;";
                                echo "display per page&nbsp;".$size."&nbsp;&nbsp;";
                                echo "page&nbsp;".$page_id."&nbsp;/total&nbsp;".$page_num."&nbsp;&nbsp;";
                                if($page_id>=1 && $page_num>1){
                                  echo "<a href=?page_id=1>first&nbsp;&nbsp;</a>";
                                }
                                if($page_id>1 && $page_num>1){
                                  echo "<a href=?page_id=".($page_id-1).">pre&nbsp;&nbsp;</a>";
                                }
                                if($page_id>=1 && $page_num>$page_id){
                                  echo "<a href=?page_id=".($page_id+1).">next&nbsp;&nbsp;</a>";
                                }
                                if($page_id>=1 && $page_num>1){
                                  echo "<a href=?page_id=".$page_num.">last</a>";
                                }
                                echo "</td>";
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