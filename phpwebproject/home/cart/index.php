<?php
  session_start();
  include '../../public/common/conn.php';

?>
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Shopping Cart</title>
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
						<span>My cart:</span>	
					</div>
					<div class="right">
					    <a href="../index.php">continue>></a>
					</div>
				</div>

				<div class="floorFooter2">
					<table width='100%'>
						<tr>
							<th>Title</th>
							<th>Img</th>
							<th>Price</th>
							<th>Stock</th>
							<th>Quantiy</th>
							<th>Total</th>
							<th>Delete</th>
						</tr>
                        <?php
                          $tot = 0;
                          if(!@$_SESSION['books']){
                            echo "you have not buy any book&nbsp;<a href='../index.php' class='cartNum'>go shopping</a>";
                          }else{
                            foreach($_SESSION['books'] as $book){
                              $tot += $book['nowprice']*$book['num'];
                        ?>
						<!--购物车数据块开始-->
						<tr>
							<td><?php echo $book['name']?></td>
							<td>
								<img src="../../public/uploads/thumb_<?php echo $book['img']?>" width='100px'>
							</td>
							<td><?php echo $book['nowprice']?>$</td>
							<td><?php echo $book['stock']?>pics</td>
							<td>
								<a href="cut.php?id=<?php echo $book['id']?>" class='cartNum'>-</a>
								<span><?php echo $book['num']?></span>
								<a href="add.php?id=<?php echo $book['id']?>" class='cartNum'>+</a>
							</td>
							<td><?php echo $book['nowprice']*$book['num']?>$</td>
							<td>
								<a href="delete.php?id=<?php echo $book['id']?>" class='cartDel'>dekete</a>
							</td>
						</tr>
                        <!--购物车数据块结束-->
                        <?php
                           }
                        ?>
                        <tr class="cartTot">
                           <td colspan="4">
                              <a href="clear.php" class='cartNum'>empty cart</a>
                           <td>
                           <td>
                              <span>Total：</span>
                           </td>
                           <td>
                              <span><?php echo $tot?>$</span>
                           </td>
                        </tr>
                    <?php
                         }
                    ?>
				  </table>
				</div>
			</div>


            <div class="nav"></div>
			<div class="floor">
				<div class="floorHeader">
					<div class="left">
						<span>My contact info:</span>	
					</div>
					
				</div>

				<div class="floorFooter2">
				<!--判断用户是否登录 session-->
				<?php
                   if(@$_SESSION['home_userid']){
				?>
				  <form action="commit.php" method='post'>
					<table width='100%' class='touch'>
						<tr>
							<th>choice</th>
							<th>name</th>
							<th>address</th>
							<th>code</th>
							<th>phone</th>
						</tr>

                        <?php
                           $user_id = $_SESSION['home_userid'];
                           $sql = "select * from touch where user_id = {$user_id}";
                           $rst = mysql_query($sql);
                           $i = 0;
                           while($row=mysql_fetch_assoc($rst)){
							//联系方式数据块开始
							if($i == 0){
                               echo "<tr>
                         			    <td>
                         				    <input type='radio' name='touch_id' value='{$row['id']}' checked>
                         			    </td>
                         			    <td>{$row['name']}</td>
                         			    <td>{$row['addr']}</td>
                         			    <td>{$row['postcode']}</td>
                         			    <td>{$row['tel']}</td>
                         			 </tr>";
							}else{
							   echo "<tr>
                               			<td>
                               				<input type='radio' name='touch_id' value='{$row['id']}'>
                               			</td>
                               			<td>{$row['name']}</td>
                               			<td>{$row['addr']}</td>
                               			<td>{$row['postcode']}</td>
                               			<td>{$row['tel']}</td>
                               		</tr>";
							}
						    $i++;
							//联系方式数据块结束
                           }
                    }else{
                       echo "please log in! <a href='../login.php' class='cartNum'>登录</a>";
                    }
                        ?>
					</table>
				 </div>
			  </div>

			  <div class="floor">
              	 <div class="floorHeader">
              		 <div class="left">
              			  <span>calculate my order:</span>
              	     </div>
                 </div>

                 <div class="floorFooter2">
                         <select name="paytype">
                             <option value='1' selected>pay at shipping</option>
                             <option value='2'>by wechat</option>
                             <option value='3'>by credit</option>
                         </select>
                         <select name="posttype">
                             <option value='1' selected>normal express</option>
                             <option value='2'>EMS</option>
                             <option value='3'>Canada Post</option>
                         </select>
              	         <input type="submit" value="place order" class="commit">
                 </div>
              </div>
           </form>
		</div>	

		<?php 
			include '../footer.php';
		?>
	</div>	
</body>
</html>