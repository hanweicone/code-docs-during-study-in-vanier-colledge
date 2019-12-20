<?php
  session_start();
  include '../../public/common/conn.php';
?>

<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>My library</title>
	<link rel="stylesheet" href="../public/css/index.css">
</head>
<body>
	<div class="main">
		<?php
			include '../header.php';
		?>
		<div class="nav"></div>
		<div class="content">
			<div class="floor">
				<div class="floorHeader">
					<div class="left">
						<span><a href='../index.php'>main</a> &raquo; shelf</span>
					</div>

				</div>

				<div class="floorFooter2">
					<table width='100%'>
						<tr>
							<th>Img</th>
							<th>Title</th>
							<th>Author</th>
							<th>Price</th>
							<th>New Price</th>
							<th>In stock</th>
							<th>Sales</th>
							<th>Read</th>
							<th>Delete</th>
							<th>Cart</th>
						</tr>
					<!--判断用户是否登录 session-->
                        <?php
                           if(@!$_SESSION['home_userid']){
                               echo "please login! <a href='../login.php' class='cartNum'>登录</a>";
                           }else{
                                     $user_id = $_SESSION['home_userid'];
                                     $sqlShelf = "select * from bookshelf where user_id = {$user_id}";
                                     $rstShelf = mysql_query($sqlShelf);

                                     $size = 4;
                                     @$hangnum = mysql_num_rows($rstShelf);
                                     if($hangnum == 0){
                                        echo "you don't have any book in collection&nbsp;<a href='../index.php' class='cartNum'>go to collection</a>";
                                     }else{
                                        if($rowShelf=mysql_fetch_assoc($rstShelf)){
                                             $page_num = ceil($hangnum/$size);
                                             if(@$_GET['page_id']){
                                                 $page_id = $_GET['page_id'];
                                                 $start = ($page_id-1)*$size;
                                             }else{
                                                 $page_id = 1;
                                                 $start = 0;
                                             }

                                             $fenye_sel = "select * from bookshelf where user_id = {$user_id} limit $start,$size";
                                             $fenye_add = mysql_query($fenye_sel);

                                             while($rowShelf=mysql_fetch_assoc($fenye_add)){

                                                $sqlBook = "select * from book where id = {$rowShelf['book_id']}";
                                                $rstBook= mysql_query($sqlBook);
                                                $rowBook=mysql_fetch_assoc($rstBook);

                        ?>
						<tr>
							<td>
								<img src="../../public/uploads/thumb_<?php echo $rowBook['img']?>" width='50px'>
							</td>
							<td><?php echo $rowBook['name']?></td>
							<td><?php echo $rowBook['writer']?></td>
							<td><?php echo $rowBook['oldprice']?>$</td>
							<td><?php echo $rowBook['nowprice']?>$</td>
							<td><?php echo $rowBook['stock']?></td>
							<td><?php echo $rowBook['sales']?></td>
							<td><a href="../book.html">|Trials|</a></td>
							<td><a href="delete.php?id=<?php echo $rowBook['id']?>">|Delete From Collection|</a></td>
							<td>
								<a href="../cart/insert.php?id=<?php echo $rowBook['id']?>">
									<img src="../public/img/cart.jpg" alt="">
								</a>
							</td>
						</tr>
						<?php
                              }
						     }
						    }
                        ?>
                        <tr>
                            <td colspan="9">
                        <?php
							echo "total records &nbsp;".$hangnum."&nbsp;&nbsp;";
							echo "display per page &nbsp;".$size."&nbsp;&nbsp;";
							echo "page &nbsp;".$page_id."&nbsp;/total &nbsp;".$page_num."&nbsp;&nbsp;";
							if($page_id>=1 && $page_num>1){
								echo "<a href=?page_id=1>first&nbsp;&nbsp;</a>";
							}
							if($page_id>1 && $page_num>1){
								echo "<a href=?page_id=".($page_id-1).">previous&nbsp;&nbsp;</a>";
							}
							if($page_id>=1 && $page_num>$page_id){
								echo "<a href=?page_id=".($page_id+1).">next&nbsp;&nbsp;</a>";
							}
							if($page_id>=1 && $page_num>1){
								echo "<a href=?page_id=".$page_num.">end</a>";
							}
							echo "</td>";
							echo "</tr>";
						}
                        ?>
					</table>
				</div>
			</div>

		</div>

		<?php
			include '../footer.php';
		?>
	</div>
</body>
</html>