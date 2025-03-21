<html>
    <head>
        <script>
            function print()
            {
                var ob=false;
                ob=new XMLHttpRequest();
                ob.open("GET","slip12_1.php",true);
                ob.send();
                ob.onreadystatechange=function()
                {
                    if(ob.readyState==4 && ob.status==200)
                    {
                        document.getElementById("i").innerHTML=ob.responseText;
                    }
                }
            }
        </script>
    </head>
    <body>
        <center>
            <h3>Display The Contents of Contact.dat file</h3>
            <br>
            <input type="button" value="Display" onclick="print()">
            <br>
            <span id="i"></span>
        </center>
    </body>
</html>

<?php
$fp=fopen("Contact.dat","r");
echo "<table border=1>";
echo "<tr><th>Sr.No.</th><th>Name</th><th>Residence No.</th><th>Mob. No.</th><th>Adress</th></tr>";
while($row=fscanf($fp,"%s %s %s %s %s"))
{
    echo "<tr>";
    foreach($row as $r)
    {
        echo "<td>".$r."</td>";
    }
    echo "</tr>";
}
echo "</table>";
fclose($fp);
?>

<!-- Contact.dat -->

1 Amresh 12345 8766555 Pune
2 Shubham 33653 93898 Pune 
3 Mitesh 35735 777 Pune