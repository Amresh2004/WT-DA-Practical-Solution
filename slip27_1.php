<!DOCTYPE html>
<html>
<head>
    <title>Voter Registration</title>
    <script>
        function validateForm() {
            let name = document.getElementById("name").value;
            let age = document.getElementById("age").value;
            let nationality = document.getElementById("nationality").value;

            if (name !== name.toUpperCase()) {
                alert("Name must be in uppercase letters!");
                return false;
            }
            if (isNaN(age) || age < 18) {
                alert("Age must be a number and not less than 18!");
                return false;
            }
            if (nationality.toLowerCase() !== "indian") {
                alert("Nationality must be Indian!");
                return false;
            }

            let xhr = new XMLHttpRequest();
            xhr.open("POST", "validate.php", true);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    document.getElementById("result").innerHTML = xhr.responseText;
                }
            };
            xhr.send(`name=${name}&age=${age}&nationality=${nationality}`);
            return false;
        }
    </script>
</head>
<body>
    <h2>Voter Registration Form</h2>
    <form onsubmit="return validateForm()">
        Name: <input type="text" id="name" name="name" required><br><br>
        Age: <input type="number" id="age" name="age" required><br><br>
        Nationality: <input type="text" id="nationality" name="nationality" required><br><br>
        <input type="submit" value="Submit">
    </form>

    <div id="result"></div>
</body>
</html>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $age = $_POST['age'];
    $nationality = $_POST['nationality'];

    if ($name === strtoupper($name) && $age >= 18 && strtolower($nationality) === "indian") {
        echo "✅ Voter Registration Successful!";
    } else {
        echo "❌ Invalid Details. Please check the requirements.";
    }
}
?>
