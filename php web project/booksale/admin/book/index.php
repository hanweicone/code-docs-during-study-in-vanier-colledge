<?php
     include '../../public/common/conn.php';
     include '../public/session.php';

     $sql="select book.*,class.name cname from book,class where book.class_id=class.id and book.supplier=0 order by book.id";
     $rst=mysql_query($sql);

     $size = 4;
     $hangnum = mysql_num_rows($rst);
     if($hangnum == 0){
        echo "no books now";
     }else{
        $page_num = ceil($hangnum/$size);
        if(@$_GET['page_id']){
            $page_id = $_GET['page_id'];
            $start = ($page_id-1)*$size;
        }else{
            $page_id = 1;
            $start = 0;
        }

        $fenye_sel = "select book.*,class.name cname from book,class where book.class_id=class.id and book.supplier=0 order by book.id limit $start,$size";
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
				<th>Title</th>
				<th>Author</th>
				<th>Img</th>
				<th>Price</th>
				<th>Price now</th>
				<th>In stock</th>
				<th>sales</th>
				<th>Avialiable</th>
				<th>Recommend</th>
				<th>Catagory</th>
				<th>Edit</th>
				<th>Delete</th>
			</tr>
			<?php
				while($row=mysql_fetch_assoc($fenye_add)){
					echo "<tr>";
					echo "<td>{$row['id']}</td>";
					echo "<td>{$row['name']}</td>";
					echo "<td>{$row['writer']}</td>";
					echo "<td><img src='../../public/uploads/thumb_{$row['img']}' width='50px'></td>";
					echo "<td>{$row['oldprice']}</td>";
					echo "<td>{$row['nowprice']}</td>";
					echo "<td>{$row['stock']}</td>";
					echo "<td>{$row['sales']}</td>";
					if($row['shelf']){
						echo "<td>in stock</td>";
					}else{
						echo "<td>out stock</td>";
					}
					if($row['recommend']){
                    	echo "<td>yes</td>";
                    }else{
                    	echo "<td>no</td>";
                    }
					echo "<td>{$row['cname']}</td>";
					echo "<td><a href='change.php?id={$row['id']}'>edit</a></td>";
					echo "<td><a href='delete.php?id={$row['id']}&img={$row['img']}'>delete</a></td>";
					echo "</tr>";
				}
			?>
			<tr>
              <td colspan="13">
              <?php
            	echo "total books &nbsp;".$hangnum."&nbsp;&nbsp;";
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

</body>
</html>