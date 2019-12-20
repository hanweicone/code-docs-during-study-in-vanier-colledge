<?php
     include '../../public/common/conn.php';
     include '../public/session.php';

     $sql = "select * from status";
     $rst = mysql_query($sql);

     $size = 7;
     $hangnum = mysql_num_rows($rst);
     if($hangnum == 0){
         echo "no status record";
     }else{
         $page_num = ceil($hangnum/$size);
         if(@$_GET['page_id']){
            $page_id = $_GET['page_id'];
            $start = ($page_id-1)*$size;
         }else{
            $page_id = 1;
            $start = 0;
         }

         $fenye_sel = "select * from status limit $start,$size";
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
				<th>Status</th>
				<th>Edit</th>
				<th>Delete</th>
			</tr>
			<?php
               while($row = mysql_fetch_assoc($fenye_add)){
                  echo "<tr>";
                     echo "<td>{$row['id']}</td>";
                     echo "<td>{$row["name"]}</td>";
                     echo "<td><a href='change.php?id={$row["id"]}'>edit</a></td>";
                     if($row['id']==1){
                        echo "<td><a href='javascript:' style='background:#888'>delete</a></td>";
                     }else{
                        echo "<td><a href='delete.php?id={$row["id"]}'>delete</a></td>";
                     }
                  echo "</tr>";
               }
			?>
			<tr>
              <td colspan="4">
            	<?php
            	    echo "total records&nbsp;".$hangnum."&nbsp;&nbsp;";
            		echo "records per page&nbsp;".$size."&nbsp;&nbsp;";
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

</body>
</html>