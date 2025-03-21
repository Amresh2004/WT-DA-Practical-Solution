<!DOCTYPE html>
<html>
<head>
    <title>Number Operations</title>
</head>
<body>

<h2>Enter a Number</h2>

<form method="post" action="">
    Number: <input type="number" name="number" required>
    <input type="submit" name="submit" value="Calculate">
</form>

<?php
if (isset($_POST['submit'])) {
    $num = intval($_POST['number']);
    
    // Fibonacci Series Function
    function fibonacci($n) {
        $fib = [0, 1];
        for ($i = 2; $i < $n; $i++) {
            $fib[] = $fib[$i - 1] + $fib[$i - 2];
        }
        return $fib;
    }

    // Sum of Digits Function
    function sum_of_digits($n) {
        $sum = 0;
        while ($n != 0) {
            $sum += $n % 10;
            $n = (int)($n / 10);
        }
        return $sum;
    }

    // Display Results
    echo "<h3>Results:</h3>";

    // Fibonacci Series
    echo "<strong>Fibonacci Series up to $num terms:</strong><br>";
    $fib_series = fibonacci($num);
    echo implode(", ", $fib_series) . "<br><br>";

    // Sum of Digits
    echo "<strong>Sum of the digits of $num:</strong> " . sum_of_digits($num);
}
?>

</body>
</html>
