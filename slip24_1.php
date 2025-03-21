<?php
// Define student details (added Amresh, Shubham, Mitesh)
$students = array(
    array("rollno" => 1, "name" => "Amresh", "address" => "pune", "college" => "RMC College", "course" => "Data Science"),
    array("rollno" => 2, "name" => "Shubham", "address" => "pune", "college" => "RMC College", "course" => "Computer Science"),
    array("rollno" => 3, "name" => "Mitesh", "address" => "pune", "college" => "RMC College", "course" => "Information Technology")
);

// Create a SimpleXMLElement object
$xml = new SimpleXMLElement('<students></students>');

// Add student elements to the XML object
foreach ($students as $student) {
    $student_element = $xml->addChild('student');
    $student_element->addChild('rollno', $student['rollno']);
    $student_element->addChild('name', $student['name']);
    $student_element->addChild('address', $student['address']);
    $student_element->addChild('college', $student['college']);
    $student_element->addChild('course', $student['course']);
}

// Save the XML data to a file
$xml->asXML('student.xml');

// Get course input from user (using a form)
$course = isset($_POST['course']) ? trim($_POST['course']) : '';

// Display the input form
echo '<form method="POST">
        <label>Enter Course: </label>
        <input type="text" name="course" required>
        <input type="submit" value="Search">
      </form>';

// If a course is entered, load the XML file and filter students by course
if (!empty($course)) {
    $xml = simplexml_load_file('student.xml');

    // Find students with the matching course
    $filtered_students = $xml->xpath("//student[course='$course']");

    // Print table of matching students
    echo "<h2>Students enrolled in $course</h2>";
    echo "<table border='1' cellpadding='5' cellspacing='0'>
            <tr>
                <th>Roll No</th>
                <th>Name</th>
                <th>Address</th>
                <th>College</th>
                <th>Course</th>
            </tr>";

    if ($filtered_students) {
        foreach ($filtered_students as $student) {
            echo "<tr>
                    <td>{$student->rollno}</td>
                    <td>{$student->name}</td>
                    <td>{$student->address}</td>
                    <td>{$student->college}</td>
                    <td>{$student->course}</td>
                  </tr>";
        }
    } else {
        echo "<tr><td colspan='5'>No students found for this course.</td></tr>";
    }

    echo "</table>";
}
?>
