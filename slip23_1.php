CREATE DATABASE student_db;

CREATE TABLE student (
    rollno INT PRIMARY KEY,
    name VARCHAR(50),
    class VARCHAR(20)
);

INSERT INTO student (rollno, name, class) VALUES
(1, 'Amresh', '10A'),
(2, 'Shubham', '10B'),
(3, 'Mitesh', '10C'),

🎯 Step 2: Set up CodeIgniter
1️⃣ Download CodeIgniter from here.
2️⃣ Extract the files into your web server (htdocs for XAMPP or www for WAMP).
3️⃣ Rename the folder to student_app.

🎯 Step 3: Configure the Database Connection
Go to application/config/database.php and edit this:
$db['default'] = array(
    'dsn'   => '',
    'hostname' => 'localhost',
    'username' => 'root',
    'password' => '',
    'database' => 'student_db',
    'dbdriver' => 'mysqli',
    'dbprefix' => '',
    'pconnect' => FALSE,
    'db_debug' => (ENVIRONMENT !== 'production'),
    'cache_on' => FALSE,
    'cachedir' => '',
    'char_set' => 'utf8',
    'dbcollat' => 'utf8_general_ci',
);


🎯 Step 4: Create a Model
Create a model file: application/models/Student_model.php
<?php
class Student_model extends CI_Model {
    
    public function get_students() {
        $query = $this->db->get('student');
        return $query->result();
    }
}
?>


🎯 Step 5: Create a Controller
Create a controller file: application/controllers/Student.php
<?php
class Student extends CI_Controller {

    public function index() {
        $this->load->model('Student_model');
        $data['students'] = $this->Student_model->get_students();
        $this->load->view('student_view', $data);
    }
}
?>

🎯 Step 6: Create the View
Create a view file: application/views/student_view.php
<!DOCTYPE html>
<html>
<head>
    <title>Student Records</title>
</head>
<body>
    <h2>Student Records</h2>
    <table border="1" cellpadding="10">
        <thead>
            <tr>
                <th>Roll No</th>
                <th>Name</th>
                <th>Class</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($students as $student): ?>
                <tr>
                    <td><?= $student->rollno; ?></td>
                    <td><?= $student->name; ?></td>
                    <td><?= $student->class; ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>

🎯 Step 7: Set Up Routes
Go to application/config/routes.php:
$route['default_controller'] = 'student';

🎯 Step 8: Run the App
1️⃣ Start XAMPP/WAMP and ensure Apache & MySQL are running.
2️⃣ Open your browser and go to:
👉 http://localhost/student_app/

