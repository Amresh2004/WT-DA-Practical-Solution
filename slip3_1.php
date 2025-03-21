<html>
    <body>
        <form action="slip3_1.php" method="get">
            Enter username:<input type="text" name="n">
            <br>
            Enter password:<input type="password" name="p">
            <br>
            <input type="submit" value="submit">
        </form>
    </body>
</html>
<?php
session_start();
$nm=$_GET['n'];
$ps=$_GET['p'];
if($nm == $ps)
   echo "Coreect <br> Login Sucessfull <br> Welcome $nm";
else if(isset($_SESSION['cnt']))
{
    echo $_SESSION['cnt']. " Chnaces used invalid login";
    $_SESSION['cnt']=$_SESSION['cnt']+1;
    if($_SESSION['cnt'] > 3)
    {
        echo "Attempt failed";
    }
    else
    {
        $_SESSION['cnt']=1;
        echo "1 chance used Invalid login";
    }
}    