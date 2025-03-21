<?php
session_start();
?>
<html>
<body>
    <h2>Enter Employee Details</h2>
    <form method="post" action="setb2(1).php">
        <label for="eno">Employee Number:</label>
        <input type="text" id="eno" name="eno" required><br><br>
        <label for="ename">Employee Name:</label>
        <input type="text" id="ename" name="ename" required><br><br>
        <label for="address">Address:</label>
        <input type="text" id="address" name="address" required><br><br>
        <button type="submit">Next</button>
    </form>
</body>
</html>

<!-- setb2(1).php -->

<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['eno'] = $_POST['eno'];
    $_SESSION['ename'] = $_POST['ename'];
    $_SESSION['address'] = $_POST['address'];
}
?>
<html>
<body>
    <h2>Enter Employee Earnings</h2>
    <form method="post" action="setb2(2).php">
        <label for="basic">Basic:</label>
        <input type="number" id="basic" name="basic" required><br><br>
        <label for="da">DA:</label>
        <input type="number" id="da" name="da" required><br><br>
        <label for="hra">HRA:</label>
        <input type="number" id="hra" name="hra" required><br><br>
        <button type="submit">Next</button>
    </form>
</body>
</html>

<!-- setb2(2).php -->

<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['basic'] = $_POST['basic'];
    $_SESSION['da'] = $_POST['da'];
    $_SESSION['hra'] = $_POST['hra'];
}

$total = $_SESSION['basic'] + $_SESSION['da'] + $_SESSION['hra'];
?>

<html>
<body>
    <h2>Employee Information</h2>
    <p><strong>Employee Number:</strong> <?php echo $_SESSION['eno']; ?></p>
    <p><strong>Employee Name:</strong> <?php echo $_SESSION['ename']; ?></p>
    <p><strong>Address:</strong> <?php echo $_SESSION['address']; ?></p>
    <p><strong>Basic:</strong> <?php echo $_SESSION['basic']; ?></p>
    <p><strong>DA:</strong> <?php echo $_SESSION['da']; ?></p>
    <p><strong>HRA:</strong> <?php echo $_SESSION['hra']; ?></p>
    <h3><strong>Total Earnings:</strong> <?php echo $total; ?></h3>
</body>
</html>