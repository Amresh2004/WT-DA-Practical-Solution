<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Details AJAX</title>
    <script>
        function showBookDetails(bookName) {
            if (bookName === "") {
                document.getElementById("details").innerHTML = "Please select a book!";
                return;
            }

            const xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    document.getElementById("details").innerHTML = xhr.responseText;
                }
            };
            xhr.open("GET", "slip16_1.php?title=" + bookName, true);
            xhr.send();
        }
    </script>
</head>
<body>

    <h2>Select a Book to Get Details</h2>
    <select onchange="showBookDetails(this.value)">
        <option value="">--Select a Book--</option>
        <option value="Harry Potter">Harry Potter</option>
        <option value="The Hobbit">The Hobbit</option>
        <option value="1984">1984</option>
        <option value="To Kill a Mockingbird">To Kill a Mockingbird</option>
    </select>

    <h3>Book Details:</h3>
    <div id="details">Please select a book.</div>

</body>
</html>

<?php
header("Content-Type: text/html");

if (!isset($_GET['title'])) {
    echo "No book selected!";
    exit;
}

$selectedTitle = $_GET['title'];
$xml = simplexml_load_file("book.xml") or die("Error loading XML file!");

$found = false;
foreach ($xml->book as $book) {
    if (strcasecmp($book->title, $selectedTitle) == 0) {
        echo "<strong>Title:</strong> " . $book->title . "<br>";
        echo "<strong>Author:</strong> " . $book->author . "<br>";
        echo "<strong>Year:</strong> " . $book->year . "<br>";
        echo "<strong>Price:</strong> $" . $book->price . "<br>";
        $found = true;
        break;
    }
}

if (!$found) {
    echo "Book not found!";
}
?>

<!-- book.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<books>
    <book>
        <title>Harry Potter</title>
        <author>J.K. Rowling</author>
        <year>1997</year>
        <price>15.99</price>
    </book>
    <book>
        <title>The Hobbit</title>
        <author>J.R.R. Tolkien</author>
        <year>1937</year>
        <price>12.50</price>
    </book>
    <book>
        <title>1984</title>
        <author>George Orwell</author>
        <year>1949</year>
        <price>10.99</price>
    </book>
    <book>
        <title>To Kill a Mockingbird</title>
        <author>Harper Lee</author>
        <year>1960</year>
        <price>14.50</price>
    </book>
</books>