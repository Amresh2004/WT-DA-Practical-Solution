<html>
    <body>
        <script>
            function Display()
            {
                var x=new XMLHttpRequest();
                var n=document.getElementById("n").value;
                x.open("GET","slip14_1.php?n="+n,true);
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
        Teacher Name:<input type="text" name="n" id="n">
        <br>
        <button onclick="Display()">Display</button>
        <br>
        <h1 id="i"></h1>
    </body>
</html>

<?php
$tname = $_GET['n'];
$con = pg_connect("host=localhost dbname=amresh user=postgres password=8624807723") or die("Could not connect to server");

$q = "SELECT * FROM Teacher WHERE tname = '$tname'";
$rs = pg_query($con, $q) or die("Could not execute query");

if (pg_num_rows($rs) > 0) 
{
    echo "<table border=1>";
    echo "<tr><td>Teacher Number</td><td>Teacher Name</td><td>Qualification</td><td>Salary</td></tr>";

    while ($row = pg_fetch_row($rs)) 
    {
        echo "<tr>";
        foreach ($row as $r) 
        {
            echo "<td>$r</td>";
        }
        echo "</tr>"; 
    }
    echo "</table>";
} 
else 
{
    echo "No such teacher found";
}

pg_close($con);
?>