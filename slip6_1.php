<?php
$xml = simplexml_load_file("book.xml") or die("Error: Cannot load XML file");
foreach ($xml->book as $book) 
{
    echo "<b>Book Details:</b><br>";
    echo "Book No: " . $book->bookno . "<br>";
    echo "Title: " . $book->bookname . "<br>";
    echo "Author: " . $book->authorname . "<br>";
    echo "Price: $" . $book->price . "<br>";
    echo "Year: " . $book->year . "<br><br>";
}
?>

<!-- book.xml -->

<?xml version="1.0" encoding="UTF-8"?>
<BookInfo>
    <book>
        <bookno>1</bookno>
        <bookname>JAVA</bookname>
        <authorname>Balguru Swami</authorname>
        <price>250</price>
        <year>2006</year>
    </book>
    <book>
        <bookno>2</bookno>
        <bookname>PHP</bookname>
        <authorname>S.Kadam</authorname>
        <price>350</price>
        <year>2009</year>
    </book>
    <book>
        <bookno>3</bookno>
        <bookname>C</bookname>
        <authorname>Denis Ritchie</authorname>
        <price>500</price>
        <year>1971</year>
    </book>
    <book>
        <bookno>4</bookno>
        <bookname>C++</bookname>
        <authorname>Bjarne Straustrup</authorname>
        <price>400</price>
        <year>1994</year>
    </book>
    <book>
        <bookno>5</bookno>
        <bookname>DATABASE</bookname>
        <authorname>Rogers Presman</authorname>
        <price>700</price>
        <year>2001</year>
    </book>
</BookInfo>