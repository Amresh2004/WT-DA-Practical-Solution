<html>
    <body>
        <script>
            function Display()
            {
                var x=new XMLHttpRequest();
                var n=document.getElementById("n").value;
                x.open("GET","slip13_1.php?n="+n,true);
                x.send();
                x.onreadystatechange=function()
                {
                    if(x.readyState==4 && x.status==200)
                    {
                        document.getElementById("i").innerHTML=x.responseText;
                    }
                }
            }
        </script>
        Enter your name:<input type="text" id="n" name="n" onfocus="Display()" onkeyup="Display()">
        <br>
        <h1 id="i"></h1>
    </body>
</html>

<?php
$nm=$_GET['n'];
$nm_arr=array("Amresh","Shubham","Mitesh");
if($nm==NULL)
     echo "Stranger please tell me your name";
foreach($nm_arr as $n)
{
    if($n==$nm)
    {
        echo "Welcome ".$n;
        exit();
    }
}
echo"$nm, I don't know you";
?>