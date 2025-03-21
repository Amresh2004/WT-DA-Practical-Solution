<html>
 <body>
<?php
  session_start();
  if(isset($_SESSION['count']))
  {
    $_SESSION['count']=$_SESSION['count']+1;
  }
  else
  {
    $_SESSION['count']=1;
  }
  echo "<h3> This Page is Accessed By Amresh </h3>" . $_SESSION['count'] . "Times";
?>
</body>
</html>