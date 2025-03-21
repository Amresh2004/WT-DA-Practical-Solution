<html>
    <body>
        <script>
            function display() {
            var x=new XMLHttpRequest();
            var n= document.getElementById("n").value;
            x.open("GET","slip26_1.php?n="+n,true);
            x.send();
            x.onreadystatechange=function(){
                if(x.readyState==4 && x.status==200){
                    document.getElementById("i").innerHTML=x.responseText;
                }
            }
        }
        </script>
        Customer Name:<input type="text" name="n" id="n">
        <br>
        <button onclick="display()">Display</button>
        <h1 id="i"></h1>
    </body>
</html>

<?php
$name=$_GET['n'];
$con=pg_connect("host=localhost dbname=amresh user=postgres password=8624807723") or die("Could not connect to server");
$q="select * from order1 where cno in(select cno from customer where cname='$name')";
$rs=pg_query($con,$q) or die("Could not execute query");
if(pg_num_rows($rs)>0)
{
    echo "<table border=1>";
    echo "<tr><td>Order Number</td><td>Order Date</td><td>Shipping Address</td><td>Customer Number</td></tr>";
    while($row=pg_fetch_row($rs))
    {
        echo "<tr>";
        foreach($row as $r)
        {
            echo "<td>$r</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
}
else
{
    echo "No such customer found";
}