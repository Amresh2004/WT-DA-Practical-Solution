<!DOCTYPE html>
<html>
<head>
    <title>Login System with AJAX and PHP</title>
    <script>
        function validateLogin() {
            let username = document.getElementById("username").value;
            let password = document.getElementById("password").value;

            let xhr = new XMLHttpRequest();
            xhr.open("POST", "validate.php", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    document.getElementById("result").innerHTML = xhr.responseText;
                }
            };

            xhr.send("username=" + username + "&password=" + password);
        }
    </script>
</head>
<body>
    <h2>Login Form</h2>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>

    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>

    <button type="button" onclick="validateLogin()">Login</button>

    <div id="result"></div>
</body>
</html>

<?php
// Database connection to PostgreSQL
$host = "localhost";
$dbname = "amresh";
$user = "postgres";
$password = "8624807723";

$conn = pg_connect("host=$host dbname=$dbname user=$user password=$password");

// Check connection
if (!$conn) {
    die("Connection failed: " . pg_last_error());
}

// Get input from AJAX request
$username = $_POST['username'];
$password = $_POST['password'];

// Protect from SQL injection
$username = pg_escape_string($conn, $username);
$password = pg_escape_string($conn, $password);

// Query to check username and password
$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = pg_query($conn, $sql);

if (pg_num_rows($result) > 0) {
    echo "<span style='color:green;'>✅ Valid login!</span>";
} else {
    echo "<span style='color:red;'>❌ Invalid username or password.</span>";
}

// Close connection
pg_close($conn);
?>
