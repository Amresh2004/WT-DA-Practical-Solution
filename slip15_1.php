<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Search Suggestions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        #suggestions {
            border: 1px solid #ccc;
            width: 200px;
            margin: 0 auto;
            text-align: left;
        }
        .suggestion-item {
            padding: 5px;
            cursor: pointer;
        }
        .suggestion-item:hover {
            background-color: #f0f0f0;
        }
    </style>
    <script>
        function showSuggestions(str) {
            if (str.length === 0) {
                document.getElementById("suggestions").innerHTML = "";
                return;
            }

            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    document.getElementById("suggestions").innerHTML = xhr.responseText;
                }
            };
            xhr.open("GET", "slip15_1s.php?q=" + str, true);
            xhr.send();
        }

        function selectSuggestion(value) {
            document.getElementById("searchBox").value = value;
            document.getElementById("suggestions").innerHTML = "";
        }
    </script>
</head>
<body>

    <h2>Live Search Suggestions</h2>
    <input type="text" id="searchBox" onkeyup="showSuggestions(this.value)" placeholder="Type a name..." />
    <div id="suggestions"></div>

</body>
</html>

<?php
// Predefined array of suggestions
$suggestions = ["Rohit", "Virat", "Dhoni", "Ashwin", "Harbhajan", "Sachin", "Rahul", "Jadeja", "Pant", "Bumrah"];

$query = isset($_GET['q']) ? strtolower($_GET['q']) : '';

$response = "";

if ($query !== "") {
    foreach ($suggestions as $name) {
        if (stripos($name, $query) !== false) {
            $response .= "<div class='suggestion-item' onclick='selectSuggestion(\"$name\")'>$name</div>";
        }
    }
}

echo $response === "" ? "<div>No suggestions</div>" : $response;
?>