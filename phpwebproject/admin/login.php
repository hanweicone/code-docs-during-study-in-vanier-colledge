<!doctype html>
<html>
<head>
    <title>admin login</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="public/css/login.css" />
</head>

<body >	
	<h1 class="text">admin center</h1>
	<div id=userlogin_body>
	<form action="check.php" method='post'>
	    <div class="top">
	        <p class="user">admin account： </p>
	        <input class="txtusernamecssclass" id=txtusername 
	          maxlength=20 name=username placeholder="please enter account name"><br />
	        <p class="pas">password： </p>
	        <input class="txtpasswordcssclass" id=txtpassword 
	          type=password name=password placeholder="please enter password">
	    </div>
	      
	    <div class="foot">
	      <input class="ibtnentercssclass" id=ibtnenter type=image  name=ibtnenter>	
	    </div>

	  <ul>
	</form>
	</div>
</body>
</html>
