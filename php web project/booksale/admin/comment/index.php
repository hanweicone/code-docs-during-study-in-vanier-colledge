<?php
     include '../../public/common/conn.php';
     include '../public/session.php';

     $sql="select comment.*,user.username,book.name from comment,user,book where comment.user_id=user.id and comment.book_id=book.id";
     $rst=mysql_query($sql);

     $size = 4;
     $hangnum = mysql_num_rows($rst);
     if($hangnum == 0){
        echo "no comment";
     }else{
        $page_num = ceil($hangnum/$size);
        if(@$_GET['page_id']){
           $page_id = $_GET['page_id'];
           $start = ($page_id-1)*$size;
        }else{
           $page_id = 1;
           $start = 0;
        }

        $fenye_sel = "select comment.*,user.username,book.name from comment,user,book where comment.user_id=user.id and comment.book_id=book.id limit $start,$size";
        $fenye_add = mysql_query($fenye_sel);
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
		<table>
			<tr>
				<th>NO.</th>
				<th>User</th>
				<th>Book</th>
				<th>Comment</th>
				<th>Times</th>
				<th>Delete</th>
			</tr>
			<?php
				while($row=mysql_fetch_assoc($fenye_add)){
					echo "<tr>";
					echo "<td>{$row['id']}</td>";
					echo "<td>{$row['username']}</td>";
					echo "<td>{$row['name']}</td>";
					echo "<td>{$row['content']}</td>";
					echo "<td>".date('Y-m-d',$row['time'])."</td>";
					echo "<td><a href='delete.php?id={$row['id']}'>删除</a></td>";
					echo "</tr>";
				}
			?>
			<tr>
            	<td colspan="6">
            	<?php
            		echo "Total comment&nbsp;".$hangnum."&nbsp;&nbsp;";
            		echo "Comment per page&nbsp;".$size."&nbsp;&nbsp;";
            		echo "page&nbsp;".$page_id."&nbsp;/total&nbsp;".$page_num."&nbsp;页&nbsp;";
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
            			echo "<a href=?page_id=".$page_num.">end</a>";
            		}
            		echo "</td>";
                    echo "</tr>";
                   }
                ?>
		</table>
	</div>

</body>
</html>